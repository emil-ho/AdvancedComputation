# this file contains the neighborlist initialization and update method
import numpy as np
from datetime import datetime
from fake_inputs import *  # just for testing

# positions = np.load('MD_simulation/files/positions_ini.npy')

# status: not working properly
# Problems:
# periodic boundary condition is not implemented

# this function might be unnecessary
import coordinates
def calc_distance(coord1, coord2):
    '''
    calculates distance between two atoms
    coord1: array of shape (1,4)
    coord2: array of shape (1,4)
    '''
    vec = coord1[1:] - coord2[1:]
    distance = np.sqrt((vec[0]**2 + vec[1]**2 + vec[2]**2))
    return distance

def initialize_neighbor_list(positions, cutoff_distance, output=True):
    '''
    This function initializes the neighbor list from a given array of positions
    positions: np.array with dims (n,4). arr[n,0] is the index of the atom, arr[n,1:] are the xzy coordinates
    cutoff_distance: float, in units of sigma
    output: bool, wether a output file of the neighbors should be generated or not
    '''
    natoms = len(positions)
    nblist = []
    nblist_dist = []
    nbpoint = []
    counter = 0

    for i in range(natoms):
        nbpoint.append(counter)
        for j in range(i+1, natoms):
            dist = calc_distance(positions[i], positions[j])
            if dist > cutoff_distance:
                pass
            else:
                nblist.append(j)
                nblist_dist.append(dist)
                counter += 1

    # this block is for the output file
    if output == True:
        with open('files/nblist_ini.txt', 'w') as f:
            STAMP = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            now = datetime.now()
            local_now = now.astimezone()
            local_tz = local_now.tzinfo
            local_tzname = local_tz.tzname(local_now)
            space = ' '
            HEADER = f'Neighbors of the atoms after initialization \
            \nTime of initialization: {STAMP + space + local_tzname}\n\n'
            f.write(HEADER)
            f.close()

        for i in range(len(nbpoint) - 1):
            nn = nbpoint[i+1] - nbpoint[i]
            with open('files/nblist_ini.txt', 'a') as f:
                f.write(f'Atom number: {int(positions[i,0])}\n')
                f.write(f'  Position of Atom: {positions[i, 1:]}\n')
                f.write(f'  Number of neighbors: {nn}\n')
                f.write(f'  Index           Position           Distance\n')
                for j in range(nbpoint[i] - 0, nbpoint[i] + nn):
                    f.write(f'{format(positions[nblist[j]][0], "4g")}     ')
                    f.write(f'{format(positions[nblist[j]][0], "4g")}     ')
                    f.write(f'{format(positions[nblist[j]][1], " .4f")}  ')
                    f.write(f'{format(positions[nblist[j]][2], " .4f")}  ')
                    f.write(f'{format(positions[nblist[j]][3], " .4f")}  ')
                    f.write(f'{format(nblist_dist[j], " .2f")}\n')
                f.write('\n')
                f.close()
        # the loop ignores the last atom, but it can't have any neighbors
        # without double counting anyways

    return nblist, nbpoint



POSITIONS = np.loadtxt('files/initial_positions.dat')
positions=coordinates.initialize_positions(3,0.8442,0.341)

NBlist, NBpoint = initialize_neighbor_list(positions, 2.7)

# print(NBpoint)

#print(POSITIONS)
#print(initialize_neighbor_list(POSITIONS, 2.7))