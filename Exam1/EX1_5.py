from math import *


def Whichmann_Hill_Algorithm(seeds, how_many):

    # Define initial seeds
    s1 = seeds[0]
    s2 = seeds[1]
    s3 = seeds[2]

    random_values = []

    while True:
        if len(random_values) < how_many:

            # Update seed values
            s1 = ((171 * s1) % 30269)
            s2 = ((172 * s2) % 30307)
            s3 = ((170 * s3) % 30323)

            # Calculate random number
            r = s1 / 30269 + s2 / 30307 + s3 / 30323
            r = (r % 1.0)

            # Append results to values list
            random_values.append(r)

        else:
            break

    return random_values


def get_mean(values):

    mean = sum(values) / len(values)
    return mean


def get_stdev(values):

    mean = get_mean(values)
    difference = 0
    for val in values:
        difference = difference + (val - mean) ** 2
    stdev = sqrt(difference / (len(values) - 1))
    return stdev


def Simspons_Method(f, a, b, N=50):  # Calculate Simpson Method

    if N % 2 == 1:
        raise ValueError("N must be an even integer.")

    dx = (b - a) / N
    estimate = f(a) + f(b)  # Coefficient Value

    for i in range(1, N, 2):
        estimate += 4 * f(a + (dx * i))  # Add the coefficient

    for i in range(2, N, 2):
        estimate += 2 * f(a + (dx * i))  # Add the coefficient

    return estimate * (dx / 3)  # Rule of Simpson's method


def Secant_Method(f, xold, xnew, N, xtol=1e-6):  # Calculate Secant Method

    i = 0

    for i in range(1, N + 1):
        if abs(xnew - xold) > xtol:  # Iterate value
            break
        else:
            xnew = xnew - f(xnew) * ((xnew - xold) / (f(xnew) - f(xold)))
            i += 1

    return xnew


def main():

    seed = [1234, 19857, 25000]
    amount = 1000

    values = Whichmann_Hill_Algorithm(seed, amount)
    mean = get_mean(values)
    stdev = get_stdev(values)

    def gauss(x): return (1 / (stdev * sqrt(2 * pi))) * exp(-0.5 * ((x - mean) ** 2) / stdev ** 2)

    a = mean - 5 * stdev
    b = mean + 5 * stdev

    print(a)
    print(b)

    print(Simspons_Method(gauss, a, b))

    print(Secant_Method(gauss, a, b, 50))


main()
