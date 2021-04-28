import numpy as np
import math
from scipy.optimize import fsolve


class Fluid():
    def __init__(self, mu=0.00089, rho=1000):
        """
        default properties are for water
        :param mu: dynamic viscosity in Pa*s -> (kg*m/s^2)*(s/m^2) -> kg/(m*s)
        :param rho: density in kg/m^3
        """
        self.mu = mu
        self.rho = rho
        self.nu = self.mu / self.rho  # units of m^2/s


class Node():
    def __init__(self, Name='a', Pipes=[], ExtFlow=0):
        """
        A node in a pipe network.
        :param Name: name of the node
        :param Pipes: a list/array of pipes connected to this node
        :param ExtFlow: any external flow into (+) or out (-) of this node in L/s
        """
        self.name = Name
        self.pipes = Pipes
        self.extFlow = ExtFlow
        self.P = 0

    def getNetFlowRate(self):
        """
        Calculates the net flow rate into this node in L/s
        :return:
        """
        Qtot = self.extFlow  # count the external flow first
        for p in self.pipes:
            # retrieves the pipe flow rate (+) if into node (-) if out of node.  see class for pipe.
            Qtot += p.getFlowIntoNode(self.name)
        return Qtot


class SprinklerHead():
    def __init__(self, p=2, k=1):
        self.p = p
        self.k = k
        self.q = k * math.sqrt(p)

    def CalcK(self, Q, P):
        self.k = Q / math.sqrt(P)
        return self.k

    def CalQ(self, P):
        return self.k * math.sqrt(P)


class Loop():
    def __init__(self, Name='A', Pipes=[]):
        """
        Defines a loop in a pipe network.
        :param Name: name of the loop
        :param Pipes: a list/array of pipes in this loop
        """
        self.name = Name
        self.pipes = Pipes

    def getNodeByName(self, nodes, name):
        for i in nodes:
            if i.name==name:
                return i

    def getLoopHeadLoss(self, nodes):
        """
        Calculates the net head loss as I traverse around the loop, in m of fluid.
        :return:
        """
        deltaP = 0  # initialize to zero
        startNode = self.pipes[0].startNode  # begin at the start node of the first pipe
        n=self.getNodeByName(nodes, startNode)
        for p in self.pipes:
            # calculates the head loss in the pipe considering loop traversal and flow directions
            phl = p.getHeadLoss(startNode)
            deltaP += phl
            startNode = p.endNode if startNode != p.endNode else p.startNode  # move to the next node
            k = self.getNodeByName(nodes, startNode)
            k.P = n.P-phl
            n=k
        return deltaP


class Pipe():
    def __init__(self, Start='A', End='B', L=100, D=200, r=0.00025, fluid=Fluid()):
        """
        Defines a generic pipe with orientation from lowest letter to highest.
        :param Start: the start node
        :param End: the end node
        :param L: the pipe length in m
        :param D: the pipe diameter in mm
        :param r: the pipe roughness in m
        """
        self.startNode = min(Start, End)  # makes sure to use the lowest letter for startNode
        self.endNode = max(Start, End)  # makes sure to use the highest letter for the endNode
        self.length = L
        self.d = D / 1000.0
        self.r = r
        self.relrough = self.r / self.d  # calculate relative roughness for easy use later
        self.Q = 10  # working in units of L/s
        self.A = math.pi / 4.0 * self.d ** 2  # calculate pipe cross sectional area for easy use later
        self.fluid = fluid  # the fluid in the pipe
        self.vel = self.V()  # calculate the initial velocity of the fluid
        self.reynolds = self.Re()  # calculate the initial reynolds number

    def V(self):
        """
        Calculate average velocity for self.Q
        :return:
        """
        self.vel = (abs(self.Q) / 1000.0) / self.A
        return self.vel

    def Re(self):
        """
        Calculate the reynolds number under current conditions.
        :return:
        """
        self.reynolds = self.V() * self.d / self.fluid.nu
        return self.reynolds

    def FrictionFactor(self):
        """
        Use the Colebrook equation to find the friction factor.
        NOTE:  math.log is natural log, math.log10 is base 10 log
        """

        def ffc(ff):  # friction factor calculator
            LHS = 1 / (ff ** 0.5)
            RHS = -2.0 * math.log10(self.relrough / 3.7 + 2.51 / (self.Re() * ff ** 0.5))
            return LHS - RHS

        f = fsolve(ffc, 0.008)  # use fsolve to find friction factor
        return f[0]

    def HeadLoss(self):  # calculate headloss through a section of pipe in m of fluid
        """
        Use the Darcy-Weisbach equation to find the head loss through a section of pipe.
        """
        g = 9.81  # m/s^2
        ff = self.FrictionFactor()
        hl = ff * (self.length / self.d) * (self.V() ** 2) / (2 * g)  # m of water
        return hl

    def getHeadLoss(self, s):
        """
        Calculate the head loss for the pipe.
        :param s: the node i'm starting with in a traversal of the pipe
        :return: the signed headloss through the pipe in m of fluid
        """
        # while traversing a loop, if s = startNode I'm traversing in same direction as positive pipe
        nTraverse = 1 if s == self.startNode else -1
        # if flow is positive sense, scalar =1 else =-1
        nFlow = 1 if self.Q >= 0 else -1
        return nTraverse * nFlow * self.HeadLoss()

    def Name(self):
        """
        Gets the pipe name.
        :return:
        """
        return self.startNode + '-' + self.endNode

    def oContainsNode(self, node):
        # does the pipe connect to the node?
        return self.startNode == node or self.endNode == node

    def printPipeFlowRate(self):
        print('The flow in segment {} is {:0.2f} L/s'.format(self.Name(), self.Q))

    def getFlowIntoNode(self, n):
        """
        determines the flow rate into node n
        :param n: a node object
        :return: +/-Q
        """
        if n == self.startNode:
            return -self.Q
        return self.Q


class PipeNetwork():
    def __init__(self, Pipes=[], Loops=[], Nodes=[], fluid=Fluid()):
        """
        The pipe network is built from pipe, node, loop, and fluid objects.
        :param Pipes: a list of pipe objects
        :param Loops: a list of loop objects
        :param Nodes: a list of node objects
        :param fluid: a fluid object
        """
        self.loops = Loops
        self.nodes = Nodes
        self.Fluid = fluid
        self.pipes = Pipes
        self.sprinkler = SprinklerHead

    def findFlowRates(self):
        """
        a method to analyze the pipe network and find the flow rates in each pipe
        given the constraints of no net flow into a node and no net pressure drops in the loops.
        :return: a list of flow rates in the pipes
        """
        # see how many nodes and loops there are
        N = len(self.nodes) + len(self.loops)
        # build an initial guess for flow rates
        Q0 = np.full(N, 10)

        def fn(q):  # the callback for fsolve
            # update the flow rate in each pipe object
            for i in range(len(self.pipes)):
                self.pipes[i].Q = q[i]
            # calculate the net flow rate for the node objects
            L = self.getNodeFlowRates()
            # calculate the net head loss for the loop objects
            L += self.getLoopHeadLosses()
            return L

        # using fsolve to find the flow rates
        FR = fsolve(fn, Q0)
        return FR

    def getNodeFlowRates(self):
        # each node object is responsible for calculating its own net flow rate
        fr = [n.getNetFlowRate() for n in self.nodes]
        return fr

    def getLoopHeadLosses(self):
        # each loop object is responsible for calculating its own net head loss
        lhl = [l.getLoopHeadLoss(self.nodes) for l in self.loops]
        return lhl

    def getPipe(self, name):
        # returns a pipe object by its name
        for p in self.pipes:
            if name == p.Name():
                return p

    def getNodePipes(self, node):
        # returns a list of pipe objects that are connected to the node object
        l = []
        for p in self.pipes:
            if p.oContainsNode(node):
                l.append(p)
        return l

    def nodeBuilt(self, node):
        # determins if I have already constructed this node object (by name)
        for n in self.nodes:
            if n.name == node:
                return True
        return False

    def getNode(self, name):
        # returns one of the node objects by name
        for n in self.nodes:
            if n.name == name:
                return n

    def buildNodes(self):
        # automatically create the node objects by looking at the pipe ends
        for p in self.pipes:
            if self.nodeBuilt(p.startNode) == False:
                # instantiate a node object and append it to the list of nodes
                self.nodes.append(Node(p.startNode, self.getNodePipes(p.startNode)))
            if self.nodeBuilt(p.endNode) == False:
                # instantiate a node object and append it to the list of nodes
                self.nodes.append(Node(p.endNode, self.getNodePipes(p.endNode)))

    def printPipeFlowRates(self):
        for p in self.pipes:
            p.printPipeFlowRate()

    def printNetNodeFlows(self):
        for n in self.nodes:
            print('net flow into node {} is {:0.2f}'.format(n.name, n.getNetFlowRate()))

    def printLoopHeadLoss(self):
        for l in self.loops:
            print('head loss for loop {} is {:0.2f}'.format(l.name, l.getLoopHeadLoss(self.nodes)))

    def printPipeHeadloss(self):
        for p in self.pipes:
            print('head loss in pipe {} is {:0.2f}'.format(p.Name(), p.HeadLoss()))

    def printNodeK(self):
        for n in self.nodes:
            if n.name in ['b', 'd', 'f', 'h']:
                print('pressure head at sprinkler {} is {:0.2f}m of water'.format(n.name, n.P))
            else:
                print('pressure head at node {} is {:0.2f}m of water'.format(n.name, n.P))


def main():
    """
    This program analyzes flows in a given pipe network based on the following:
    1. The pipe segments are named by their endpoint node names:  e.g., a-b, b-e, etc.
    2. Flow from the lower letter to the higher letter of a pipe is considered positive.
    3. Pressure decreases in the direction of flow through a pipe.
    4. At each node in the pipe network, mass is conserved.
    5. For any loop in the pipe network, the pressure loss is zero
    Approach to analyzing the pipe network:
    Step 1: build a pipe network object that contains pipe, node, loop and fluid objects
    Step 2: calculate the flow rates in each pipe using fsolve
    Step 3: output results
    Step 4: check results against expected properties of zero head loss around a loop and mass conservation at nodes.
    :return:
    """
    # instantiate a Fluid object to define the working fluid as water
    water = Fluid(mu=0.00089, rho=1000.0)
    roughness = 0.00025  # in m

    # instantiate a new PipeNetwork object
    PN = PipeNetwork()
    # add Pipe objects to the pipe network
    PN.pipes.append(Pipe('a', 'b', 250, 300, roughness, water))
    PN.pipes.append(Pipe('a', 'c', 100, 200, roughness, water))
    PN.pipes.append(Pipe('b', 'e', 100, 200, roughness, water))
    PN.pipes.append(Pipe('c', 'd', 125, 200, roughness, water))
    PN.pipes.append(Pipe('c', 'f', 100, 150, roughness, water))
    PN.pipes.append(Pipe('d', 'e', 125, 200, roughness, water))
    PN.pipes.append(Pipe('d', 'g', 100, 150, roughness, water))
    PN.pipes.append(Pipe('e', 'h', 100, 150, roughness, water))
    PN.pipes.append(Pipe('f', 'g', 125, 250, roughness, water))
    PN.pipes.append(Pipe('g', 'h', 125, 250, roughness, water))
    # add Node objects to the pipe network
    PN.buildNodes();
    # update the external flow of certain nodes
    PN.getNode('a').extFlow = 60
    PN.getNode('d').extFlow = -30
    PN.getNode('f').extFlow = -15
    PN.getNode('h').extFlow = -15;
    # add Loop objects to the pipe network
    PN.loops.append(
        Loop('A', [PN.getPipe('a-b'), PN.getPipe('b-e'), PN.getPipe('d-e'), PN.getPipe('c-d'), PN.getPipe('a-c')]))
    PN.loops.append(Loop('B', [PN.getPipe('c-d'), PN.getPipe('d-g'), PN.getPipe('f-g'), PN.getPipe('c-f')]))
    PN.loops.append(Loop('C', [PN.getPipe('d-e'), PN.getPipe('e-h'), PN.getPipe('g-h'), PN.getPipe('d-g')]))

    # call the findFlowRates method of the PN (a PipeNetwork object)
    PN.findFlowRates()

    # get output
    print('Pipe Flow Rates')
    PN.printPipeFlowRates()
    print()
    print('Check node flows:')
    PN.printNetNodeFlows()
    print()
    print('Check loop head loss:')
    PN.printLoopHeadLoss()
    print()
    print('Pipe head loss')
    PN.printPipeHeadloss()

    PN.printNodeK()


main()
