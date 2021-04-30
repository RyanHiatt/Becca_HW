import numpy as np


class Pump:
    def __init__(self):
        self.pump_name = None
        self.flow_units = None
        self.head_units = None

        self.flow = []
        self.head = []
        self.efficiency = []

    def read_file(self, filename):
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
                self.flow.append(l[0])
                self.head.append(l[1])
                self.efficiency.append(l[2].strip())
                i += 1

    def list_to_string(self, list):
        string = ''
        for element in list:
            string += element
            string += ', '
        return string

    def plot_data(self, ax1, ax2):

        ax1.plot(100, 100)
        ax2.plot(50, 50)



if __name__ == '__main__':
    p = Pump()
    p.read_file('pump1.txt')
    print(p.pump_name)
    print(p.flow_units)
    print(p.head_units)
    print(p.flow)
    print(p.head)
    print(p.efficiency)
