################################################################################                                                                        #
# @author: spati164@asu.edu; updates by sdm                                    #
#                                                                              #
# Program to solve resister network with voltage and/or current sources        #
################################################################################

import numpy as np                     # needed for arrays
from numpy.linalg import solve         # needed for matrices
from read_netlist import read_netlist  # supplied function to read the netlist
import comp_constants as COMP          # needed for the common constants

# this is the list structure that we'll use to hold components:
# [ Type, Name, i, j, Value ]

################################################################################
# How large a matrix is needed for netlist? This could have been calculated    #
# at the same time as the netlist was read in but we'll do it here             #
# Input:                                                                       #
#   netlist: list of component lists                                           #
# Outputs:                                                                     #
#   node_cnt: number of nodes in the netlist                                   #
#   volt_cnt: number of voltage sources in the netlist                         #
################################################################################

def get_dimensions(netlist):           # pass in the netlist
    node_cnt = 0                       # initialize nodes count with 0
    volt_cnt = 0                       # initialize voltage count with 0
    for comp in netlist:
        # count the number of nodes
        # the count will always be the greatest number of i & j
        # since we're ignoring the ground node (0)
        if (comp[COMP.I] != comp[COMP.J]):
            node_cnt = max(comp[COMP.I], comp[COMP.J], node_cnt)
        else:
            print('Wrong node values, cannot move from node', comp[COMP.I], 'to node', comp[COMP.J])
        if comp[COMP.TYPE] == COMP.VS:         
            volt_cnt += 1
    return node_cnt, volt_cnt

################################################################################
# Function to stamp the components into the netlist                            #
# Input:                                                                       #
#   y_add:    the admittance matrix                                            #
#   netlist:  list of component lists                                          #
#   currents: the matrix of currents                                           #
#   node_cnt: the number of nodes in the netlist                               #
# Outputs:                                                                     #
#   node_cnt: the number of rows in the admittance matrix                      #
################################################################################

def stamper(y_add,netlist,currents,node_cnt):
    # return the total number of rows in the matrix for
    # error checking purposes
    # add 1 for each voltage source...

    for comp in netlist:                  # for each component...
        #print(' comp ', comp)            # which one are we handling...

        # extract the i,j and fill in the matrix...
        # subtract 1 since node 0 is GND and it isn't included in the matrix
        i = comp[COMP.I] - 1
        j = comp[COMP.J] - 1

        if ( comp[COMP.TYPE] == COMP.R ):           # a resistor
            if (i >= 0):                            # add on the diagonal
                y_add[i,i] += 1.0/comp[COMP.VAL]
            
            #EXTRA STUFF HERE!
            if (j >= 0):                            
                y_add[j, j] += 1.0 / comp[COMP.VAL]
            if (i >= 0 and j >= 0):                
                y_add[i, j] -= 1.0 / comp[COMP.VAL]
                y_add[j, i] -= 1.0 / comp[COMP.VAL]
        
        elif (comp[COMP.TYPE] == COMP.VS):          
            node_cnt += 1
            M = node_cnt                            
            if (i>= 0):                            
                y_add[M-1, i] = 1.0
                y_add[i, M-1] = 1.0
            if (j >= 0):                            
                y_add[M-1, j] = -1.0
                y_add[j, M-1] = -1.0

            currents[M-1] = comp[COMP.VAL]
            voltages[M-1] = 0

        elif (comp[COMP.TYPE] == COMP.IS):          
            if (i >= 0):                            
                if (comp[COMP.VAL] >= 0):
                    currents[i] -= 1.0 * comp[COMP.VAL]
                else:
                    currents[i] += 1.0 * comp[COMP.VAL]
            if (j >= 0):                            # Add I at entry [j] in the current matrix
                if(comp[COMP.VAL] >= 0):
                    currents[j] += 1.0 * comp[COMP.VAL]
                else:
                    currents[j] -= 1.0 * comp[COMP.VAL]

    print('Admittance Matrix =', y_add)
    print('Voltage Matrix =', voltages)
    print('Currents Matrix =', currents)
    return node_cnt  # should be same as number of rows!

################################################################################
# Start the main program now...                                                #
################################################################################

# Read the netlist!
netlist = read_netlist()

# Print the netlist so we can verify we've read it correctly
for index in range(len(netlist)):
    print(netlist[index])
print("\n")

#EXTRA STUFF HERE!

nodes_count, voltage_sources_count = get_dimensions(netlist)
total = nodes_count + voltage_sources_count

admittance = np.zeros((total, total), dtype=float)
currents = np.zeros(total, dtype=float)
voltages = np.zeros(total, dtype=float)

node_count = stamper(admittance, netlist, currents, nodes_count)

voltages = solve(admittance, currents)
print(voltages)
# print('Voltage Vector =', voltages)