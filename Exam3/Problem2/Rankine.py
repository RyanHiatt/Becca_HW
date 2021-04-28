from Steam import *
from matplotlib import pyplot as plt


class StateDataForPlotting:
    """
    I'm making this class for easy storage of data for plotting.
    """
    def __init__(self):
        self.T = []
        self.P = []
        self.h = []
        self.s = []
        self.v = []

    def clear(self):
        self.T.clear()
        self.P.clear()
        self.h.clear()
        self.s.clear()
        self.v.clear()

    def add(self, vals):
        T, P, h, s, v = vals
        self.T.append(T)
        self.P.append(P)
        self.h.append(h)
        self.s.append(s)
        self.v.append(v)

    def getAxisLabel(self, W='T'):
        w=W.lower()
        if w == 't':
            return r'T $\left(^oC\right)$'
        if w == 'h':
            return r'h $\left(\frac{kJ}{kg}\right)$'
        if w == 's':
            return r'S $\left(\frac{kJ}{kg\cdot K}\right)$'
        if w == 'v':
            return r'v $\left(\frac{m^3}{kg}\right)$'
        if w == 'p':
            return r'P $\left(kPa\right)$'

    def getDataCol(self, W='T'):
        w=W.lower()
        if w=='t':
            return self.T
        if w=='h':
            return self.h
        if w=='s':
            return self.s
        if w=='v':
            return self.v
        if w=='p':
            return self.P


class rankine():
    def __init__(self, p_low=8, p_high=8000, t_high=None, eff_turbine=1.0, name='Rankine Cycle'):
        '''
        Constructor for rankine power cycle.  If t_high is not specified, the State 1
        is assigned x=1 (saturated steam @ p_high).  Otherwise, use t_high to find State 1.
        :param p_low: the low pressure isobar for the cycle in kPa
        :param p_high: the high pressure isobar for the cycle in kPa
        :param t_high: optional temperature for State1 (turbine inlet) in degrees C
        :param eff_turbine: the turbine efficiency eta=(h1-h2)/(h1-h2s)<=1.0
        :param name: a convenient name
        '''
        self.steam = steam(8000)
        self.scl = subcooled()
        # These are for storing the state data for plotting later
        self.satLiqPlotData = StateDataForPlotting()
        self.satVapPlotData = StateDataForPlotting()
        self.upperCurve = StateDataForPlotting()
        self.lowerCurve = StateDataForPlotting()


class rankineCycleController():
    def __init__(self):
        self.model = rankine()
        self.view = rankineCycleView()

    def set(self, p_low=8, p_high=8000, t_high=None, eff_turbine=1.0, name='Rankine Cycle'):
        self.p_low = p_low
        self.p_high = p_high
        self.t_high = t_high
        self.name = name
        self.efficiency = None
        self.eff_turbine = eff_turbine
        self.turbine_work = 0
        self.pump_work = 0
        self.heat_added = 0
        # these will be thermodynamic state objects
        self.state1 = None
        self.state2s = None
        self.state2 = None
        self.state3 = None
        self.state4 = None
        self.satPLow = self.model.steam.getSatProp(P_KPa=self.p_low)
        self.satPHigh = self.model.steam.getSatProp(P_KPa=self.p_high)

    def calc_efficiency(self):
        # calculate the 4 states
        # state 1: turbine inlet (p_high, t_high) superheated or saturated vapor
        if self.t_high is None:
            self.state1 = self.model.steam.set(self.p_high, x=1.0, name='Turbine Inlet')
        else:
            self.state1 = self.model.steam.set(self.p_high, T=self.t_high, name='Turbine Inlet')
        # state 2: turbine exit (p_low, s=s_turbine inlet) two-phase
        # create state 2s for 100% efficient turbine
        self.state2s = self.model.steam.set(self.p_low, s=self.state1.s, name="Turbine Exit")
        # use turbine efficiency to calculate h2
        h2 = self.state1.h - (self.state1.h - self.state2s.h) * self.eff_turbine
        # finally, find state 2
        self.state2 = self.model.steam.set(self.p_low, h=h2, name="Turbine Exit")
        # state 3: pump inlet (p_low, x=0) saturated liquid
        self.state3 = self.model.steam.set(self.p_low, x=0, name='Pump Inlet')
        # state 4: pump exit (p_high,s=s_pump_inlet) typically sub-cooled, but estimate as saturated liquid
        self.state4 = self.model.scl.getState(PLowSat=self.satPLow, PHighSat=self.satPHigh, P=self.p_high,
                                        T=self.satPLow.Tsat)
        self.state4.name = 'Pump Exit'

        self.turbine_work = self.state1.h - self.state2.h
        self.pump_work = self.state4.h - self.state3.h
        self.heat_added = self.state1.h - self.state4.h
        self.efficiency = 100.0 * (self.turbine_work - self.pump_work) / self.heat_added

        self.buildDataForPlotting()
        return self.efficiency

    def buildVaporDomeData(self, nPoints=200):
        SS=self.model.steam.SatSteam
        for row in range(len(self.model.steam.SatSteam.TCol)):
            T=SS.TCol[row]
            P=SS.PCol[row]*100 #kPa
            self.model.satLiqPlotData.add((T,P, SS.hfCol[row], SS.sfCol[row], SS.vfCol[row]))
            self.model.satVapPlotData.add((T,P, SS.hgCol[row], SS.sgCol[row], SS.vgCol[row]))

    def buildDataForPlotting(self):
        """
        I want to create h, s, v, p, T data between states 1-2, 2-3, 3-4, 4-1
        I'll piece together an upperCurve data set from 3-4 + 4-1 + 1-2
        The lowerCurve data set is 2-3
        :return:
        """
        # clear out any old data
        self.model.upperCurve.clear()
        self.model.lowerCurve.clear()

        #region build upperCurve
        # region states from 3-4
        nPts = 15
        for n in range(nPts):
            z = n * 1.0 / (nPts - 1)
            DeltaP = (self.satPHigh.Psat - self.satPLow.Psat)
            state = self.model.scl.getState(self.satPLow, self.satPHigh, P=(self.satPLow.Psat + z * DeltaP), T=self.satPLow.Tsat)
            self.model.upperCurve.add((state.T, state.P, state.h, state.s, state.v))
        # endregion

        # region states from 4-1
        #first from T4 to T5
        T4 = self.satPLow.Tsat
        T5 = self.satPHigh.Tsat
        DeltaT = (T5 - T4)
        nPts = 20
        for n in range(nPts):
            z = n * 1.0 / (nPts - 1)
            P = self.satPHigh.Psat
            T = T4 + z * DeltaT
            state = self.model.scl.getState(self.satPLow, self.satPHigh, P, T)
            self.model.upperCurve.add((state.T, state.P, state.h, state.s, state.v))
        for n in range(nPts):
            z = n * 1.0 / (nPts - 1)
            state = self.model.steam.getState(self.satPHigh.Psat,x=z)
            self.model.upperCurve.add((state.T, state.P, state.h, state.s, state.v))
        if self.state1.T>(self.satPHigh.Tsat+1):
            T6 = self.satPHigh.Tsat
            DeltaT = self.state1.T - T6
            for n in range(nPts):
                z = n * 1.0 / (nPts - 1)
                state = self.model.steam.getState(self.satPHigh.Psat, T=T6+z*DeltaT)
                self.model.upperCurve.add((state.T, state.P, state.h, state.s, state.v))
        # endregion

        #region states between 1 and 2
        #I'm assuming a linear change in Pressure from P1 to P2, along with linear change in s,
        #but not sure of details inside the turbine, so this is just a guess.
        s1=self.state1.s
        s2=self.state2.s
        P1=self.state1.P
        P2=self.state2.P
        Deltas=s2-s1
        DeltaP=P2-P1
        for n in range(nPts):
            z = n * 1.0 / (nPts - 1)
            state = self.model.steam.getState(P1+z*DeltaP, s=s1+z*Deltas)
            self.model.upperCurve.add((state.T, state.P, state.h, state.s, state.v))
        #endregion
        #endregion

        #region build lowerCurve
        x2=self.state2.x
        nPts= len(self.model.upperCurve.T)
        for n in range(nPts):
            z = n * 1.0 / (nPts - 1)
            state=self.model.steam.getState(self.satPLow.Psat, x=(1.0-z)*x2)
            self.model.lowerCurve.add((state.T, state.P, state.h, state.s, state.v))
        #endregion

    def plot_cycle_XY(self, X='s', Y='T', ax=None, logx=False, logy=False):
        """
        I want to plot any two thermodynaimc properties on X and Y
        :param X: letter for which variable to plot on X axis
        :param Y: letter for which variable to plot on Y axis
        :return:
        """
        if X==Y:
            return
        QTPlotting = True  # assumes we are plotting onto a QT GUI form
        if ax == None:
            ax = plt.subplot()
            QTPlotting = False  # actually, we are just using CLI and showing the plot

        ax.set_xscale('log' if logx else 'linear')
        ax.set_yscale('log' if logy else 'linear')
        YF= self.model.satLiqPlotData.getDataCol(Y)
        YG= self.model.satVapPlotData.getDataCol(Y)
        XF = self.model.satLiqPlotData.getDataCol(X)
        XG = self.model.satVapPlotData.getDataCol(X)
        # plot the vapor dome
        ax.plot(XF, YF, color='b')
        ax.plot(XG, YG, color='r')
        # plot the upper and lower curves
        ax.plot(self.model.lowerCurve.getDataCol(X), self.model.lowerCurve.getDataCol(Y), color='k')
        ax.plot(self.model.upperCurve.getDataCol(X), self.model.upperCurve.getDataCol(Y), color='g')
        #ax.fill_between(self.upperCurve.getDataCol(X), self.upperCurve.getDataCol(Y), self.lowerCurve.getDataCol(Y), color='grey', alpha=0.2)

        # add axis labels
        ax.set_ylabel(self.model.lowerCurve.getAxisLabel(Y), fontsize='large' if QTPlotting else 'medium')
        ax.set_xlabel(self.model.lowerCurve.getAxisLabel(X), fontsize='large' if QTPlotting else 'medium')
        # put a title on the plot
        self.name = 'Rankine Cycle - ' + self.state1.region + ' at Turbine Inlet'
        ax.set_title(self.name, fontsize='large' if QTPlotting else 'medium')

        # modify the tick marks
        ax.tick_params(axis='both', which='both', direction='in', top=True, right=True,
                       labelsize='large' if QTPlotting else 'medium')  # format tick marks

        # plot the circles for states 1, 2, 3, and 4
        ax.plot(self.state1.getVal(X), self.state1.getVal(Y), marker='o', markerfacecolor='w', markeredgecolor='k')
        ax.plot(self.state2.getVal(X), self.state2.getVal(Y), marker='o', markerfacecolor='w', markeredgecolor='k')
        ax.plot(self.state3.getVal(X), self.state3.getVal(Y), marker='o', markerfacecolor='w', markeredgecolor='k')
        ax.plot(self.state4.getVal(X), self.state3.getVal(Y), marker='o', markerfacecolor='w', markeredgecolor='k')
        # set limits on x and y
        xmin = min(min(XF), min(XG), min(self.model.upperCurve.getDataCol(X)), max(self.model.lowerCurve.getDataCol(X)))
        xmax = max(max(XF), max(XG), max(self.model.upperCurve.getDataCol(X)), max(self.model.lowerCurve.getDataCol(X)))
        ymin=min(min(YF), min(YG), min(self.model.upperCurve.getDataCol(Y)), max(self.model.lowerCurve.getDataCol(Y)))
        ymax=max(max(YF), max(YG), max(self.model.upperCurve.getDataCol(Y)), max(self.model.lowerCurve.getDataCol(Y)))*1.1
        ax.set_xlim(xmin,xmax)
        ax.set_ylim(ymin,ymax)
        deltax=xmax-xmin
        deltay=ymax-ymin
        # add the summary text to the plot
        ax.text(xmin+0.05*deltax, ymin+0.7*deltay, self.view.get_summary(self.efficiency, self.calc_efficiency(), self.eff_turbine, self.turbine_work, self.pump_work, self.heat_added))

        # show the plot
        if QTPlotting == False:
            plt.show()


class rankineCycleView():
    def __init__(self):
        pass

    def print_summary(self):
        if self.controller.efficiency == None:
            self.controller.calc_efficiency()
        print('Cycle Summary for: ', self.controller.name)
        print('\tEfficiency: {:0.3f}%'.format(self.controller.efficiency))
        print('\tTurbine Work: {:0.3f} kJ/kg'.format(self.controller.turbine_work))
        print('\tPump Work: {:0.3f} kJ/kg'.format(self.controller.pump_work))
        print('\tHeat Added: {:0.3f} kJ/kg'.format(self.controller.heat_added))
        self.controller.state1.print()
        self.controller.state2.print()
        self.controller.state3.print()
        self.controller.state4.print()

    def get_summary(self, efficiency, eq, eff_turbine, turbine_work, pump_work, heat_added):
        '''
        This returns a formatted string to put on the plot of the rankine cycle.
        :return:
        '''
        if efficiency == None:
            eq
        s = r'Summary:'
        s += '\n$\eta$: {:0.1f}% '.format(efficiency)
        s += '\n$\eta_{turbine}$: ' + '{:0.2f}'.format(eff_turbine) if eff_turbine < 1.0 else ''
        s += '\n$W_{turbine}$: ' + '{:0.1f} kJ/k'.format(turbine_work)
        s += '\n$W_{pump}$: ' + '{:0.1f} kJ/kg'.format(pump_work)
        s += '\n$Q_{boiler}$: ' + '{:0.1f} kJ/kg'.format(heat_added)
        return s


def main():
    rankine1 = rankine(8, 8000, t_high=500, eff_turbine=0.95, name='Rankine Cycle - Superheated at turbine inlet')
    # t_high is specified
    # if t_high were not specified, then x_high = 1 is assumed
    eff = rankine1.calc_efficiency()
    print(eff)
    rankine1.state3.print()
    rankine1.print_summary()
    rankine1.plot_cycle_XY(X='s', Y='T')
    # hf=rankine1.state1.hf
    # hg=rankine1.state1.hg
    rankine2 = rankine(8, 8000, eff_turbine=0.95, name='Rankine Cycle - Saturated at turbine inlet')
    eff2 = rankine2.calc_efficiency()
    rankine2.plot_cycle_XY(X='s', Y='T')
    print(eff2)

    rankine2.print_summary()

if __name__ == "__main__":
    main()
