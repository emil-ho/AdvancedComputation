'This file contains the functions for force calculations'
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from src_neighbors import *

# vectorized force calculation
def calc_forces(positions, sigma, epsilon):
    pos = np.copy(positions[:,1:])
    N = len(pos)
    forces = np.zeros_like(pos)

    for i in range(N):
        # Increase dimension of r to allow vector operations
        r_inv = 1 / np.linalg.norm(pos[i] - pos[i + 1:], axis=1)[:, np.newaxis]
        r_norm = (pos[i] - pos[i + 1:]) * r_inv

        # multiply vectors with scalar force
        r6_inv = r_inv**6
        # Lennard-Jones force
        force = 24 * epsilon * sigma**6 * r_inv * r6_inv * (2 * sigma**6 * r6_inv - 1) * r_norm
        forces[i] += np.sum(force, axis=0)
        forces[i + 1:] -= force

    total_forces = np.copy(positions)
    total_forces[:,1:] = forces

    return total_forces


def calc_red_forces(pos1, positions, sigma, epsilon):
    total_forces = np.zeros((len(positions)+1,4))
    total_forces[0] = pos1
    total_forces[1:] = positions
    total_forces[:,1:] *= 0

    for j in range(len(positions)):
        vec_r = pos1[1:] - positions[j, 1:]  # relative position
        mod_r = np.sqrt(vec_r[0]**2+vec_r[1]**2+vec_r[2]**2)  # distance
        mod_force = - 4 * epsilon * (12 * ((sigma**12) / (mod_r)**13) - 6 * ((sigma**6) / (mod_r)**7))  # mod of the force
        vec_force = mod_force * vec_r / mod_r  # force from atom pos1 on atom j
        total_forces[1+j,1:] += vec_force  # add this force to the total force arr
        vec_force_rev = - vec_force # force from atom j on atom pos1
        total_forces[0,1:] += vec_force_rev  # add this force to the total force arr
    return total_forces


def calc_forces_nb(positions, nblist, nbpoint, sigma, epsilon):
    total_force = np.zeros_like(positions)

    for j in range(len(positions)-1):
        nbbs = get_nb_pos(positions, nblist, nbpoint, j)
        forces = calc_red_forces(positions[j], nbbs, sigma, epsilon)

        total_force[j] += forces[0]
        kk = 1
        for k in nbbs[:,0]:
            total_force[int(k),1:] += forces[kk,1:]
            kk += 1
    
    return total_force

