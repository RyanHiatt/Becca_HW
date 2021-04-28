import numpy as np
import scipy as sp
import scipy.optimize as opt
import numpy.random as random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def SSE(xvals, yvals, fnX): #calculate sum of squared error between yvals and f(x)
    sse=0 #initialize sum squared errors to 0
    for i in range(len(xvals)):
        sse += (yvals[i]-fnX(xvals[i]))**2
    return sse

def randf(fmin=0.0,fmax=1.0): #generate a random floating point number
    r=fmax-fmin
    return fmin+random.randint(0,1000)/1000.0*r

class point3d():
    """
    I made this position for holding a position in 3D space (i.e., a point).  I've given it some ability to do
    vector arithmitic and vector algebra (i.e., a dot product).  I could have used a numpy array, but I wanted
    to create my own.  This class uses operator overloading as explained in the class.
    """
    def __init__(self, pos=None, x=None, y=None, z=None):
        """
        x, y, and z have the expected meanings
        :param pos: a tuple (x,y,z)
        :param x: float
        :param y: float
        :param z: float
        """
        #set default values
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        #unpack position from a tuple if given
        if pos is not None:
            self.x, self.y, self.z = pos
        #override the x,y,z defaults if they are given as arguments
        self.x=x if x is not None else self.x
        self.y=y if y is not None else self.y
        self.z=z if z is not None else self.z

    #region operator overloads $NEW$ 4/7/21
    def __eq__(self, other):
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        if self.z != other.z:
            return False
        return True

    # this is overloading the addition operator.  Allows me to add point3d objects with simple math: c=a+b, where
    # a, b, and c are all position objects.
    def __add__(self, other):
        return point3d((self.x+other.x, self.y+other.y,self.z+other.z))

    #this overloads the iterative add operator
    def __iadd__(self, other):
        if other in (float, int):
            self.x += other
            self.y += other
            self.z += other
            return self
        if type(other) == point3d:
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self

    # this is overloading the subtract operator.  Allows me to subtract point3ds. (i.e., c=b-a)
    def __sub__(self, other):
        return point3d((self.x-other.x, self.y-other.y,self.z-other.z))

    #this overloads the iterative subtraction operator
    def __isub__(self, other):
        if other in (float, int):
            self.x -= other
            self.y -= other
            self.z -= other
            return self
        if type(other) == point3d:
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self

    # this is overloading the multiply operator.  Allows me to multiply a scalar or do a dot product (i.e., b=s*a or c=b*a)
    def __mul__(self, other):
        if type(other) in (float, int):
            return point3d((self.x*other, self.y*other, self.z*other))
        if type(other) is point3d:
            return point3d((self.x*other.x, self.y*other.y, self.z*other.z))

    # this is overloading the __rmul__ operator so that s*Pt works.
    def __rmul__(self,other):
        return self*other

    # this is overloading the *= operator.  Same as a = point3d((a.x*other, a.y*other, a.z*other))
    def __imul__(self, other):
        if type(other) in (float, int):
            self.x *= other
            self.y *= other
            self.z *= other
            return self

    # this is overloading the division operator.  Allows me to divide by a scalar (i.e., b=a/s)
    def __truediv__(self, other):
        if type(other) in (float, int):
            return point3d((self.x/other, self.y/other, self.z/other))

    # this is overloading the /= operator.  Same as a = point3d((a.x/other, a.y/other, a.z/other))
    def __idiv__(self, other):
        if type(other) in (float,int):
            self.x/=other
            self.y/=other
            self.z/=other
            return self
    #endregion

    def set(self,strXYZ=None, tupXYZ=None):
        #set position by string or tuple
        if strXYZ is not None:
            cells=strXYZ.replace('(','').replace(')','').strip().split(',')
            x, y, z = float(cells[0]), float(cells[1]), float(cells[2])
            self.x=float(x)
            self.y=float(y)
            self.z=float(z)
        elif tupXYZ is not None:
            x, y, z = tupXYZ #[0], strXYZ[1],strXYZ[2]
            self.x=float(x)
            self.y=float(y)
            self.z=float(z)

    def getTup(self): #return (x,y,z) as a tuple
        return (self.x, self.y, self.z)

    def getStr(self, nPlaces=3):
        return '{}, {}, {}'.format(round(self.x, nPlaces), round(self.y,nPlaces), round(self.z, nPlaces))

    def mag(self):  # normal way to calculate magnitude of a vector
        return (self.x**2+self.y**2+self.z**2)**0.5

    def midPt(self,p):
        return (self+p)/2.0

    def normalize(self):  # typical way to normalize to a unit vector
        l=self.mag()
        if l<=0.0:
            return
        self.__idiv__(l)

    def getAngleRad(self):
        """
        Gets angle of position relative to an origin (0,0) in the x-y plane
        :return: angle in x-y plane in radians
        """
        l=self.mag()
        if l<=0.0:
            return 0
        if self.y>=0.0:
            return math.acos(self.x/l)
        return 2.0*math.pi-math.acos(self.x/l)

    def getAngleDeg(self):
        """
        Gets angle of position relative to an origin (0,0) in the x-y plane
        :return: angle in x-y plane in degrees
        """
        return 180.0/math.pi*self.getAngleRad()

def sortSimplex(s): #order the vertices of the simples according to z component.
    sNew=s
    sNew.sort(key=lambda v:v.z)
    return sNew

def NelderMeadForSSEFit(xdata, ynoisy, guess, tol=0.00000001):
    '''
    My implementation of the Nelder-Mead method is for a sum of squared error minimization for
    fitting y=b*exp(x/lam) to some noisy data.  I'm treating this as an unconstrained problem with
    the objective function = SSE(xdata, ynoisy, lambda x: b*exp(x/lam)).
    To find the inital simplex, I guess a random lam and b between the limits.  Then find two more
    vertices.  Then I follow the Nelder-Mead rules for expansion and contraction of the simplex
    until the area of the simplex is < 0.01
    '''
    lamGuess,bGuess=guess  # unpack guess tuple

    #simplex transformations
        #reflect
        #expand
        #contract inside
        #contract outside
        #shrink

    # region build initial simplex
    lam1 = lamGuess
    b1 = bGuess
    fx1=lambda x:b1*math.exp(x/lam1)
    SSE1 = SSE(xdata, ynoisy, fx1)
    v1 = point3d(x=lam1,y=b1,z=SSE1)

    lam2 = lam1*1.1
    fx2=lambda x:b1*math.exp(x/lam2)
    SSE2 = SSE(xdata, ynoisy, fx2)
    v2 = point3d(x=lam2, y=b1, z=SSE2)

    b3 = b1*1.1
    fx3=lambda x:b3*math.exp(x/lam1)
    SSE3 = SSE(xdata, ynoisy, fx3)
    v3 = point3d(x=lam1,y=b3,z=SSE3)

    s1 = [v1,v2,v3]  # simplex 1 vertices
    s1 = sortSimplex(s1)
    #endregion

    alpha = 1.0
    beta = 0.5
    delta = 0.1
    gamma = 1.5
    nIter = 0
    dZ = 1.0
    zWorst = s1[2].z
    while math.fabs(dZ) > 1E-6 and nIter < 1000: # keep looking for lower value of Z
        # centroid between lowest and second highest simplex point
        midPt = (s1[0]+s1[1])/2.0
        acceptPt = False
        # reflect transformation
        reflectPt = (midPt-s1[2])*alpha+midPt
        reflectPt.z = SSE(xdata,ynoisy,lambda x: reflectPt.y*math.exp(x/reflectPt.x))
        if reflectPt.x >= s1[0].z and reflectPt.z < s1[1].z:
            acceptPt = True
            s1[2] = reflectPt
            s1 = sortSimplex(s1)
            dZ = zWorst-s1[2].z
            zWorst = s1[2].z

        #reflect unsuccessful, so try expand
        if acceptPt == False and reflectPt.z < s1[0].z:
            acceptPt = True
            expandPt = midPt+(midPt-s1[2])*gamma
            expandPt.z = SSE(xdata, ynoisy, lambda x: expandPt.y * math.exp(x / expandPt.x))
            if expandPt.z < reflectPt.z:
                s1[2] = expandPt
            else:
                s1[2] = reflectPt
            s1 = sortSimplex(s1)
            dZ = zWorst-s1[2].z
            zWorst = s1[2].z

        # try external contraction
        if acceptPt == False and reflectPt.z < s1[2].z:
            contractPt = midPt+(midPt-s1[2])*beta
            contractPt.z = SSE(xdata, ynoisy, lambda x: contractPt.y * math.exp(x / contractPt.x))
            if contractPt.z < reflectPt.z:
               acceptPt = True
               s1[2]=contractPt
               s1 = sortSimplex(s1)
               dZ = zWorst - s1[2].z
               zWorst = s1[2].z

        # try internal contraction
        if acceptPt == False and reflectPt.z > s1[2].z:
            contractPt = midPt-(midPt-s1[2])
            contractPt.z = SSE(xdata, ynoisy, lambda x: contractPt.y * math.exp(x / contractPt.x))
            if contractPt.z < s1[2].z:
               acceptPt = True
               s1[2]=contractPt
               s1 = sortSimplex(s1)
               dZ = zWorst - s1[2].z
               zWorst = s1[2].z

        #expansion and contraction failed, so shrink
        if acceptPt == False:
            s1[2]= s1[2]+(s1[0]-s1[2])*delta #s1[2].add((s1[0].subtract(s1[2]).scalarMult(delta)))
            s1[2].z=SSE(xdata,ynoisy, lambda x: s1[2].y*math.exp(x/s1[2].x))

            s1[1] = s1[1]+(s1[0]-s1[1])*delta  #s1[1].add((s1[0].subtract(s1[1]).scalarMult(delta)))
            s1[1].z = SSE(xdata, ynoisy, lambda x: s1[1].y * math.exp(x / s1[1].x))
            s1 = sortSimplex(s1)
            dZ = zWorst - s1[2].z
            zWorst = s1[2].z

        nIter+=1

    return s1[0].x,s1[0].y, s1[0].z, nIter

def RSquared(xdata, ydata, fn):
        '''
        To calculate the R**2 value for a set of x,y data and a LeastSquares fit with polynomial having coefficients a
        :param x:
        :param y:
        :param a:
        :return:
        '''
        AvgY=np.mean(ydata) #calculates the average value of y
        SSTot=0
        SSRes=0
        for i in range(len(ydata)):
            SSTot+=(ydata[i]-AvgY)**2
            SSRes+=(ydata[i]-fn(xdata[i]))
        RSq=1-SSRes/SSTot
        return RSq

def main():
    '''
    Demo for using an equation y=b*exp(x/lam) to fit some noisy data using
    Nelder-Mead method to find best b and lam by minimizing Sum of Squared Errors
    First, solve using custom written NelderMeadForSSEFit
    Second, solve using scipy.optimize.minimize

    Finally, plot the results on one graph with important numbers
    and, plot a 3D graphic of the SSE surface as fn(lam,b)
    :return:
    '''
    #create some noisy data
    fNoiseLevel=2.5 #a level of noise to put in the data
    bActual=2.0
    lActual=25.0
    fn1X=lambda x: randf(-fNoiseLevel,fNoiseLevel)+bActual*math.exp(x/lActual) #function to create data that nearly fits the exponential, but with random noise
    xdata=np.linspace(0,50) #some x data
    ynoisy=np.array([fn1X(f) for f in xdata]) #list comprehension to create y data

    #create some data to plot showing the exponential function with no noise
    fn2X=lambda x: bActual*math.exp(x/lActual)
    yclean=np.array([fn2X(f) for f in xdata])
    RsqClean = RSquared(xdata, ynoisy, lambda x: bActual * math.exp(x / lActual))
    SSEClean = SSE(xdata, ynoisy, lambda x: bActual * math.exp(x / lActual))

    #build SSE surface for plotting
    lMin=lActual-1
    lMax=lActual+1
    bMin=bActual-0.5
    bMax=bActual+0.5
    lam=np.linspace(lMin,lMax) #a range for lam used later for plotting
    b=np.linspace(bMin,bMax) #a range for b used later for plotting
    sseSurface=np.zeros(shape=(len(b),len(lam))) #sse surface plotted later
    for r in range(len(b)):
        for c in range(len(lam)):
            sseSurface[r][c]=SSE(xdata,ynoisy,lambda x: b[r]*math.exp(x/lam[c]))

    #use my own NelderMead method to find best lam and b to minimize SSE
    lamBest, bBest, SSEFit,nIters=NelderMeadForSSEFit(xdata,ynoisy,(lActual+1.0,bActual+0.5))
    RsqFit=RSquared(xdata,ynoisy,lambda x: bBest*math.exp(x/lamBest))
    yfit=np.array([bBest*math.exp(x/lamBest) for x in xdata]) #for plotting later

    #buid an objective function for scipy.optimize.minimize
    def fnM(args):
        l,b=args
        return SSE(xdata,ynoisy,lambda x: b*math.exp(x/l)) #y=A+B*math.exp(C*x)

    #use scipy.optimize.minimize on objective function
    vals=opt.minimize(fnM, np.array([lActual+1, bActual+1]), method='Nelder-Mead')
    lOpt=vals.x[0]
    bOpt=vals.x[1]
    SSEOpt=vals.fun
    RSqOpt=RSquared(xdata,ynoisy,lambda x: bOpt*math.exp(x/lOpt))
    NOpt= vals.nit
    yopt=np.array([bOpt*math.exp(x/lOpt) for x in xdata]) #for plotting

    #plot the noisy, clean, and best fit data
    plt.plot(xdata,ynoisy, 'o', label="Noisy Data")
    lblClean="$%s\cdot\exp^{(x/%s)}, R^2$"%("{:0.3f}".format(bActual),"{:0.3f}".format(lActual))
    lblClean += "={rsq:0.3f}, SSE={sse:0.3f}".format(rsq=RsqClean, sse=SSEClean)
    plt.plot(xdata,yclean, label=lblClean, color='red')
    lblFit="Mine: $%s\cdot\exp^{(x/%s)}, R^2$"%("{:0.3f}".format(bBest),"{:0.3f}".format(lamBest))
    lblFit+="={rsq:0.3f}, SSE={sse:0.3f}, N={nitr:0d}".format( rsq=RsqFit, sse=SSEFit, nitr=nIters)
    plt.plot(xdata,yfit, label=lblFit, color='green')
    lblOpt="Opt: $%s\cdot\exp^{(x/%s)}, R^2$"%("{:0.3f}".format(bOpt),"{:0.3f}".format(lOpt))
    lblOpt+="={rsq:0.3f}, SSE={sse:0.3f}, N={nitr:0d}".format( rsq=RSqOpt, sse=SSEOpt, nitr=NOpt)
    plt.plot(xdata,yopt, label=lblOpt, color='blue')
    plt.legend()
    plt.show()

    #build a surface and projected contour plot of sse(lam,b)
    MGX,MGY=np.meshgrid(lam,b)
    fig=plt.figure()
    ax=plt.axes(projection='3d')
    ax.plot_surface(MGX,MGY,sseSurface, rstride=1, cstride=1, cmap='hsv', alpha=0.9)
    ax.set_xlabel('$\lambda$')
    ax.set_ylabel('b')
    ax.set_zlabel('sse($\lambda$, b)')
    ax.contour(MGX,MGY,sseSurface,levels=50, zdir='z',offset=0, cmap='magma')
    #ax.set_zlim(0,30)
    plt.show()

    print('MyMethod:  Lam = {:0.3f}, b = {:0.3f}'.format(lamBest,bBest))
    print('Minimize:  Lam = {:0.3f}, b = {:0.3f}'.format(vals.x[0],vals.x[1]))
    print(vals)

    '''
    MGX, MGY=np.meshgrid(np.linspace(0,2),np.linspace(0,2))
    fXY=lambda x,y:y**2-y+x**2-3*x
    Z=fXY(MGX,MGY)

    ax=plt.axes(projection='3d')
    ax.plot_surface(MGX,MGY,Z,cmap='hsv',alpha=0.5)
    ax.set_zlim(-3,2)
    ax.contourf(MGX, MGY, Z, offset=-3, zdir='z', cmap='hsv', levels=20)
    plt.show()
    '''

main()