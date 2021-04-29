import numpy as np

class OttoCycle:
    def __init__(self):
        # Inputs
        self.cylinder_volume = None
        self.initial_pressure = None
        self.compression_ratio = None
        self.initial_temp = None
        self.max_temp = None

        # Air Constants
        self.R = 0.2870  # Gas Constant - kJ/kg*K
        self.mass = None
        self.cp = 1.005
        self.cv = 0.718
        self.k = 1.4

        # Outputs
        self.T = []
        self.P = []
        self.V = []
        self.s = []
        self.Q_in = None
        self.Q_out = None
        self.eff = None

    def plotting_data(self):
        pass


class Controller:
    def __init__(self):
        self.model = OttoCycle()
        self.view = View()

    def init_values(self, values):
        self.model.cylinder_volume = values[0]
        self.model.initial_pressure = values[1]
        self.model.compression_ratio = values[2]
        self.model.initial_temp = self.view.celsius_to_kelvin(values[3])
        self.model.max_temp = self.view.celsius_to_kelvin(values[4])

        self.model.T.clear()
        self.model.P.clear()
        self.model.V.clear()

        self.model.T.append(self.view.celsius_to_kelvin(values[3]))
        self.model.P.append(values[1])
        self.model.V.append(values[0])

    def run_cycle(self):
        self.calc_mass()
        self.process_1_2()
        self.process_2_3()
        self.process_3_4()
        self.process_4_1()
        self.calc_eff()

    def calc_mass(self):
        self.model.mass = (self.model.P[0] * self.model.V[0]) / (self.model.R * self.model.T[0])
        print(f'Air Mass = {self.model.mass:.2f}')

    def process_1_2(self):
        print(f'Point1: T={self.model.T[0]:.2f}, P={self.model.P[0]:.2f}, V={self.model.V[0]}')

        self.model.T.append(self.model.T[0] * self.model.compression_ratio ** (self.model.k - 1))
        self.model.P.append(self.model.compression_ratio * (self.model.T[1] / self.model.T[0]) * self.model.P[0])
        self.model.V.append((self.model.mass * self.model.R * self.model.T[1]) / self.model.P[1])
        print(f'Point2: T={self.model.T[1]:.2f}, P={self.model.P[1]:.2f}, V={self.model.V[1]}')

    def process_2_3(self):

        self.model.T.append(self.model.max_temp)
        self.model.P.append((self.model.T[2] / self.model.T[1]) * self.model.P[1])
        self.model.V.append((self.model.mass * self.model.R * self.model.T[2]) / self.model.P[2])
        print(f'Point3: T={self.model.T[2]:.2f}, P={self.model.P[2]:.2f}, V={self.model.V[2]}')

        self.model.Q_in = self.model.mass * self.model.cv * (self.model.T[2] - self.model.T[1])

    def process_3_4(self):

        self.model.T.append(self.model.T[2] * (1 / self.model.compression_ratio) ** (self.model.k - 1))
        self.model.P.append((1 / self.model.compression_ratio) * (self.model.T[3] / self.model.T[2]) * self.model.P[2])
        self.model.V.append((self.model.mass * self.model.R * self.model.T[3]) / self.model.P[3])
        print(f'Point4: T={self.model.T[3]:.2f}, P={self.model.P[3]:.2f}, V={self.model.V[3]}')

    def process_4_1(self):

        self.model.Q_out = self.model.mass * self.model.cv * (self.model.T[3] - self.model.T[0])
        print(f'Qin = {self.model.Q_in:.2f}, Qout = {self.model.Q_out:.2f}')

    def calc_eff(self):
        self.model.eff = (self.model.Q_in - self.model.Q_out) / self.model.Q_in
        print(f'Efficiency = {self.model.eff}')

    def plot_cycle_xy(self, type, ax=None):
        self.view.plot_cycle_xy(type=type, ax=ax, model=self.model)


class View:
    def __init__(self):
        pass

    def celsius_to_kelvin(self, c_temp):
        return c_temp + 273.15

    def kelvin_to_celsius(self, k_temp):
        return k_temp - 273.15

    def kelvin_to_fahrenheit(self, k_temp):
        return (k_temp - 273.15) * 9/5 + 32

    def plot_cycle_xy(self, type, ax=None, model=None):

        if type == 'P-V':  # P vs V
            # Plot Process 1_2
            ax.plot([model.V[0], model.V[1]], [model.P[0], model.P[1]], label='Process 1 -> 2')
            # Plot Process 2_3
            ax.plot([model.V[1], model.V[2]], [model.P[1], model.P[2]], label='Process 2 -> 3')
            # Plot Process 3_4
            ax.plot([model.V[2], model.V[3]], [model.P[2], model.P[3]], label='Process 3 -> 4')
            # Plot Process 4_1
            ax.plot([model.V[3], model.V[0]], [model.P[3], model.P[0]], label='Process 4 -> 1')
            ax.set(xlabel='Volume', ylabel='Pressure', title='P v Graph')
            ax.legend()

        elif type == 'T-S':  # T vs s
            # Plot Process 2_3
            ax.plot([model.Q_in / model.T[1], model.Q_in / model.T[2]], [model.T[1], model.T[2]], label='Process 2 -> 3')
            # Plot Process 4_1
            ax.plot([model.Q_out / model.T[3], model.Q_out / model.T[0]], [model.T[3], model.T[0]], label='Process 4 -> 1')
            ax.set(xlabel='Entropy', ylabel='Temperature', title='T S Graph')
            ax.legend()
