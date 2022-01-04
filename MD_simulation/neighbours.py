# this file contains the neighborlist initialization and update method
import numpy as np
from fake_inputs import *  # just for testing

positions = np.load('MD_simulation/files/positions_ini.npy')

# Problems:
# unfinished
# line 33 is unclear

# this function might be unnecessary
def calc_distance(coord1, coord2):
    '''
    calculates distance between two atoms
    coord1: array of shape (1,4)
    coord2: array of shape (1,4)
    '''
    vec = coord1[1:] - coord2[1:]
    distance = (vec[0]**2 + vec[1]**2 + vec[2]**2)**0.5
    return distance

def initialize_neighbor_list(positions, cutoff_distance, cutoff_list, box_length):
    '''
    This function initializes the neighbor list from a given array of positions
    '''
    point, list = [], []
    NLIST = 0  # initialize counter

    for i in range(len(positions)):  # loop over all atoms in supercell
        point[i] = NLIST + 1
        for j in range(i+1, len(positions)):  # loop over all remaining atoms in sc
            rel_pos = positions[j, 1:] - positions[i, 1:]
#            RXIJ = ANINT(RCIJ/BOXL) * BOXL  # float(round()) = ANINT()
            dist2 = rel_pos[0]**2 + rel_pos[1]**2 + rel_pos[2]**2
            if dist2 < cutoff_list**2:
                NLIST += 1
                list[NLIST] = j
            else:
                pass
    return point, list

def update_neighbor_list(positions, cutoff_distance, cutoff_list, neighbors):
    '''
    This function updates the neighbor list
    '''
    return neighbors

print(initialize_neighbor_list(positions, 2.5, 2.7, ))



print(float(round(0.49)))