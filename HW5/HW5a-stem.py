import numpy as np
import scipy as sp
import math
from scipy.optimize import fsolve


def GetNodeFlowRates(Q, seg_names):
    '''
    There are 8 nodes in this network and mass conservation should be true at each node.
    That is, sum of all mass flow rates at a node should equal zero.
    :param Q: List of flow rates for the pipe segments.
    :param seg_names: Dictionary of pipe names and indices
    :return: the list of node equation results
    '''
    # I can retrieve the flow in a pipe from Q by Q[seg_names['a-b']] for example
    # Be sure to remember a positive flow moves in direction from lowest letter to highest letter for a pipe segment
    Sum_a = Q[seg_names['a-b']] + Q[seg_names['a-c']]  # sum all flows at node a
    Sum_b = Q[seg_names['b-e']]  # sum all flows at node b
    Sum_c = Q[seg_names['c-d']] + Q[seg_names['c-f']]  # sum all flows at node c
    Sum_d = Q[seg_names['c-d']] + Q[seg_names['d-e']] + Q[seg_names['d-g']]  # sum all flows at node d
    Sum_e = Q[seg_names['b-e']] + Q[seg_names['d-e']] + Q[seg_names['e-h']]  # sum all flows at node e
    Sum_f = Q[seg_names['c-f']] + Q[seg_names['f-g']]  # sum all flows at node f
    Sum_g = Q[seg_names['f-g']] + Q[seg_names['d-g']] + Q[seg_names['g-h']]  # sum all flows at node g
    Sum_h = Q[seg_names['e-h']] + Q[seg_names['g-h']]  # sum all flows at node h
    return [Sum_a, Sum_b, Sum_c, Sum_d, Sum_e, Sum_f, Sum_g, Sum_h]


def GetLoopHeadLoss(Q, *args):
    '''
    This calculates the head loss in the three loops of the pipe network.
    :param Q: the list of flow rates
    :param args: an unspecified number of positional arguments.
    :return: the list of head losses for the loops.
    '''
    # unpack *args
    seg_names, seg_lengths, seg_diams, viscosity, roughness = args

    def Scalar(q): return 1.0 if q > 0 else -1.0  # using this to determine which direction flow is going to determine pressure drop or rise through pipe.

    # head loss in loop A is net zero around the loop
    # note:  the head loss calculate by the Darcy-Weisbach equation is always positive.  Need keep trac of which way I am traversing
    # the loop (pipe segment) and if it counts as a pressure loss or increase.  Hence, the Scalar calculation
    # multiple lines missing.  need to sum the head losses around the loop A as HLA
    for i in range(10):
        Q[i] = HeadLoss(seg_lengths[i], seg_diams[i], viscosity, roughness, Q[i])

    HLA = Q[seg_names['a-b']] + Q[seg_names['b-e']] + Q[seg_names['d-e']] + Q[seg_names['c-d']] + Q[seg_names['a-c']]
    # head loss in loop B is net zero around the loop
    # multiple lines missing.  need to sum the head losses around the loop B as HLB
    HLB = Q[seg_names['c-d']] + Q[seg_names['d-g']] + Q[seg_names['f-g']] + Q[seg_names['c-f']]
    # head loss in loop C is net zero around the loop
    # multiple lines missing.  need to sum the head losses around the loop C as HLC
    HLC = Q[seg_names['d-e']] + Q[seg_names['e-h']] + Q[seg_names['g-h']] + Q[seg_names['d-g']]

    return [HLA, HLB, HLC]


def Find_FlowRates(Q, *args):
    '''
    Finds the flow rates that satisfy the constraints of the pipe network (i.e., node and loop equations)
    :param Q: numpy array with 11 elements for the flow rates needed.
    :param args: arguments used in calculation.  note: *args means an unspecified number of positional arguments.  It could be a tuple, list or simple numbers
    :return:
    '''
    # unpack *args into recognizable names
    density = args[0]
    viscosity = args[1]
    roughness = args[2]
    seg_names = args[3]
    seg_lengths = args[4]
    seg_diams = args[5]

    # Assume incompressible fluids and apply continuity at nodes.
    # Also, the pressure drop around loops A, B, and C has to equal zero.

    # continuity equations (sum of volumetric flows at node = 0)
    NF = GetNodeFlowRates(Q, seg_names)  # returned result is list of 8 node equation results, when correct set of flow rates guessed, the should all be zero
    # head loss around each loop should be zero
    LHL = GetLoopHeadLoss(Q, seg_names, seg_lengths, seg_diams, viscosity, roughness)  # returned result is list of 3 loop equation results

    result = (NF + LHL)
    return result


def Reynolds(V, nu, dia):
    '''
    Calculates the reynolds number
    :param V: velocity in m/s
    :param nu: kinematic viscosity in m^2/s
    :param dia: pipe diameter in m
    :return:
    '''
    return V * dia / nu


def FrictionFactor(relrough, Re):
    '''
    Use the Colebrook equation to find the friction factor.
    NOTE:  math.log is natural log, math.log10 is base 10 log
    :param relrough: the relative roughness for the pipe
    :param Re: the reynolds number
    :return: the darcy friction factor
    '''
    def ffc(ff):  # implementing Colebrook equation for fsolve to find ff
        LHS = 1 / math.sqrt(ff)
        RHS = -2 * math.log10((relrough / 3.7) + (2.51 / (Re * math.sqrt(ff))))
        return LHS - RHS
    f = fsolve(ffc, 0.008)  # use fsolve to find friction factor
    return f[0]


def HeadLoss(L, d, nu, rough, Q):
    '''
    Use the Darcy-Weisbach equation to find the head loss through a section of pipe.
    :param L: pipe length in m
    :param d: pipe diameter in m
    :param nu: kinematic viscosity of water in m^2/s
    :param rough: pipe roughness in m
    :param Q: volumetric flow rate in L/s
    :return:
    '''
    A = math.pi * (d / 2) ** 2  # calculate pipe cross sectional area in m^2
    V = abs(Q)  # calculate absolute value of average water velocity in pipe
    g = 9.81  # gravity
    Re = Reynolds(V, nu, d)  # calculate the reynolds number
    relrough = rough / d  # calculate the relative roughness for the pipe
    ff = FrictionFactor(relrough, Re)  # calculate the Darcy friction factor
    hl = ff * (L / d) * ((1000 * nu ** 2) / 2)  # calculate the head loss in m
    return hl


def main():
    '''
    This program analyzes flows in a given pipe network based on the following:
    1. The pipe segments are named by their endpoint node names:  e.g., a-b, b-e, etc.
    2. Flow from the lower letter to the higher letter of a pipe is considered positive.
    3. Pressure decreases in the direction of flow through a pipe.
    4. At each node in the pipe network, mass is conserved.
    5. For any loop in the pipe network, the pressure loss is zero
    Approach to analyzing the pipe network:
    Step 1: assign convenient names to the pipes using a dictionary for indices
    Step 2: populate tuples with pipe diameters and lengths to correspond to the named pipes from step 1.
    Step 3: calculate the flow rates in each pipe using fsolve
    Step 4: output results
    Step 5: check results against expected properties of zero head loss around a loop and mass conservation at nodes.
    :return:
    '''
    # overall properties for the pipe fluid and pipe network
    density = 1000  # kg/m^3
    mu = 0.00089  # N*s/m^2 dynamic viscosity
    nu = mu / density  # m^2/s kinematic viscosity
    roughness = 0.00025  # in m

    # There are 10 segments of pipe, inconnveniently named.
    # step 1:  create a dictionary to refer to pipes by name
    seg_names = {'a-b': 0, 'b-e': 1, 'e-h': 2, 'g-h': 3, 'f-g': 4, 'c-f': 5, 'a-c': 6, 'c-d': 7, 'd-e': 8, 'd-g': 9}
    # step 2:  create tuples to contain pipe lengths and diameters (both in units of m)
    seg_lengths = (250, 100, 100, 125, 125, 100, 100, 125, 125, 100)
    seg_diams = (0.3, 0.2, 0.15, 0.25, 0.25, 0.15, 0.2, 0.2, 0.2, 0.15)
    # observation of the pipe network shows 8 node equations and 3 loop equations, so I need 11 variables
    # we could remove node b from the system since it is redundant (i.e., just an elbow rather than a tee or cross), but we leave it in for now.
    Q0 = np.full(11, 10)

    # passing arguments to fsolve as a tuple
    seg_flow_rates = fsolve(Find_FlowRates, Q0, (density, mu, roughness, seg_names, seg_lengths, seg_diams))  # density, viscosity, roughness, pipe names, pipe lengths, pipe diameters

    # output the flow rates for each pipe segment
    for Seg in seg_names:
        print('The flow in segment {:} is {:0.4f} L/s'.format(Seg, seg_flow_rates[seg_names[Seg]]))

    # verify no mass accumulation in nodes
    print(GetNodeFlowRates(seg_flow_rates, seg_names))
    # verify no net head loss for loops
    print(GetLoopHeadLoss(seg_flow_rates, seg_names, seg_lengths, seg_diams, nu, roughness))

    nI = 0
    # outputting head losses for the pipe segments for fun
    for seg in seg_names:
        HL = HeadLoss(seg_lengths[nI], seg_diams[nI], nu, roughness, seg_flow_rates[nI])
        tmpStr = "{:}".format(seg) + "\t{:5.3f}".format(HL)
        print(tmpStr)
        nI += 1


main()
