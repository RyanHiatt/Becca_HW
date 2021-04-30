import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math


class Pump:
    def __init__(self, ax = None):
        self.pump_name = None
        self.flow_units = None
        self.head_units = None

        self.flow = []
        self.head = []
        self.efficiency = []
        self.ax = ax
        if ax:
            self.ax1 = self.ax.twinx()

    def read_file(self, filename='pump1.txt'):
        self.flow.clear()
        self.head.clear()
        self.efficiency.clear()

        file = open(filename, 'r')  # open the file
        data = file.readlines()  # read all the lines of the file into a list of strings

        i = 0
        while i < len(data):
            if i == 0:
                self.pump_name = data[i].strip()
                i += 1
            elif i == 1:
                i += 1
                continue
            elif i == 2:
                l = '' + data[i]
                l.strip()
                l = l.split()
                self.flow_units = l[0]
                self.head_units = l[1]
                i += 1
            else:
                l = '' + data[i]
                l.strip()
                l = l.split()
                self.flow.append(float(l[0]))
                self.head.append(float(l[1]))
                self.efficiency.append(float(l[2].strip()))
                i += 1

    def list_to_string(self, list):
        string = ''
        for element in list:
            string += str(element)
            string += ', '
        return string

    def plot_data(self):
        if self.ax:
            xnew = np.linspace(self.flow[0], self.flow[-1], 100)
            coeffs = poly.polyfit(self.flow, self.head, 3)
            ffit = poly.polyval(xnew, coeffs)
            self.ax.scatter(self.flow, self.head, marker='o', label='Head')
            self.ax.plot(xnew, ffit, linestyle='--', label='Head')
            self.ax.set(xlabel=f'Flow Rate ({self.flow_units})', ylabel=f'Head ({self.head_units})')
            self.ax.legend(loc='center left')

            coeffs = poly.polyfit(self.flow, self.efficiency, 3)
            ffit = poly.polyval(xnew, coeffs)
            self.ax1.scatter(self.flow, self.efficiency, color='red', marker='^', label='Efficiency')
            self.ax1.plot(xnew, ffit, color='red', linestyle='dotted', label='Efficiency')
            self.ax1.set(ylabel='Efficiency (%)')
            self.ax1.legend()
        else:
            ax = plt.subplot()
            ax1 = ax.twinx()

            xnew = np.linspace(self.flow[0], self.flow[-1], 100)
            coeffs = poly.polyfit(self.flow, self.head, 3)
            ffit = poly.polyval(xnew, coeffs)
            ax.scatter(self.flow, self.head)
            ax.plot(xnew, ffit)

            coeffs = poly.polyfit(self.flow, self.efficiency, 3)
            ffit = poly.polyval(xnew, coeffs)
            ax1.scatter(self.flow, self.efficiency)
            ax1.plot(xnew, ffit)
            plt.show()


if __name__ == '__main__':
    p = Pump()
    # p.read_file('pump1.txt')
    # print(p.pump_name)
    # print(p.flow_units)
    # print(p.head_units)
    # print(p.flow)
    # print(p.head)
    # print(p.efficiency)
    p.read_file()
    p.plot_data()
