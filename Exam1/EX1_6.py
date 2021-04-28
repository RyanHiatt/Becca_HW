def Simspons_Method(fcn, a, b, points=50):  # Calculate Simpson Method
    points += 1 if points % 2 == 0 else 0  # Checking numbers to be even or odd

    s = (b - a) / (points - 1)  # Step Process
    estimate = fcn(a) + fcn(b)  # Coefficient Value

    for i in range(1, points, 2):
        estimate += 4 * fcn(a + (s * i))  # Add the coefficient

    for i in range(2, points - 1, 2):
        estimate += 2 * fcn(a + (s * i))  # Add the coefficient

    return estimate * s / 3  # Rule of Simpson's method

 # return value


def STO(Thrust):  # Calculate STO function
    Weight = 56000
    S = 1000
    CMax = 2.4
    Cd = 0.0279
    rho = 0.002377
    gc = 32.2

    A1 = gc * (Thrust / Weight)
    B1 = (gc / Weight) * (0.5 * S * rho * Cd)  # A1 and B1 calculate the STO function

    def fcn(v): return v / (A1 - B1 * v ** 2)  # Simpson's Method

    a1 = 0
    b1 = 1.2 * ((Weight) / (0.5 * rho * S * CMax)) ** (1 / 2)

    STO = Simspons_Method(fcn, a1, b1, points=1000)

    return STO


def ThrustNeededForTakeoff(distance):  # Calculate the thrust needed for take off

    def fcn(T): return STO(T) - distance
    xnew = 10e3
    xold = 30e3

    T = Secant_Method(fcn, xold, xnew)

    return T


def main():

    distance = STO(13000)
    print('The take off distance with a thrust of 13,000 pounds is {:.1f} feet.'.format(distance))

    thrust_needed = ThrustNeededForTakeoff(1500)
    print('The thrust needed to take-off within a distance of 1,500 feet is {:.2f} pounds.'.format(thrust_needed))

    thrust_needed = ThrustNeededForTakeoff(1000)
    print('The thrust needed to take-off within a distance of 1,000 feet is {:.2f} pounds.'.format(thrust_needed))


main()
