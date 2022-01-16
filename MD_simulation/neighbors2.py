# this file contains the neighborlist initialization and update method
import numpy as np
from datetime import datetime
from fake_inputs import *  # just for testing

# positions = np.load('MD_simulation/files/positions_ini.npy')

# status: not working properly? Less neighbors than Javier
# Problems:
# periodic boundary condition is not implemented

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

def initialize_neighbor_list(positions, cutoff_distance, savedir=None):
    '''
    This function initializes the neighbor list from a given array of positions

    positions: array of shape (N, 4)
        N is the number of Atoms
        positions[:,0] corresponds the index of the atom
        positions[:,1] corresponds to the x coordinate
        positions[:,1] corresponds to the y coordinate
        positions[:,1] corresponds to the z coordinate
    cutoff_distance: float
        cutoff distance in units of sigma
    savedir: string
        The location of the directory where the files should be saved
    returns: 1d-array, 1d-array
        The neighbor list and the neighborpoint, indicating the position of the next atom in the neighborlist
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
    if savedir != True:
        with open(savedir + '/nblist_ini.dat', 'w') as f:
            STAMP = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            now = datetime.now()
            local_now = now.astimezone()
            local_tz = local_now.tzinfo
            local_tzname = local_tz.tzname(local_now)
            space = ' '
            HEADER = f'Neighbors of the atoms after initialization \
            \nTime of initialization: {STAMP + space + local_tzname}\n\n'
            f.write(HEADER)

        for i in range(len(nbpoint) - 1):
            nn = nbpoint[i+1] - nbpoint[i]
            with open(savedir + '/nblist_ini.dat', 'a') as f:
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
        
        # the loop ignores the last atom, but it can't have any neighbors
        # without double counting anyways

    return nblist, nbpoint
