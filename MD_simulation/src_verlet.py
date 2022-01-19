'''This file contains the verlet algorithm and what is needed for it'''
from turtle import position
import numpy as np
from tqdm import tqdm

from src_neighbors import *
from src_forces import *
from src_energies import *

# using only vectorized calculations, no pbc or neighbor list
def do_md(x_init, v_init, dt, n_steps):
    '''
    execute a md simulation

    x_init: array of shape (N, 4)
        current positions
        x_init[:,0] corresponds the index of the atom
        x_init[:,1] corresponds to the x coordinate
        x_init[:,2] corresponds to the y coordinate
        x_init[:,3] corresponds to the z coordinate
    v_init: array of shape (N, 4)
        current positions
        v_init[:,0] corresponds the index of the atom
        v_init[:,1] corresponds to the x coordinate
        v_init[:,2] corresponds to the y coordinate
        v_init[:,3] corresponds to the z coordinate
    returns:
        positions: array of shape (n_steps, N, 4)
        velocities: array of shape (n_steps, N, 4)
        pot: array of shape (n_steps)
        kin: array of shape (n_steps)
    '''
    # Initialize energy arrays
    pot = np.zeros(n_steps)
    kin = np.zeros(n_steps)

    # Initialize trajectory arrays
    x = np.zeros([n_steps, len(x_init), 4])
    v = np.zeros_like(x)
    forces = np.zeros_like(x)

    x[0], v[0] = x_init, v_init
    forces[0] = calc_forces(x[0])
    pot[0], kin[0] = calc_energies(x[0], v[0])

    for i in tqdm(range(1, n_steps)):
        x[i,:,1:] = x[i-1,:,1:] + v[i-1,:,1:] * dt + 0.5 * dt**2 * forces[i-1,:,1:]
        forces[i] = calc_forces(x[i])
        v[i,:,1:] = v[i-1,:,1:] + 0.5 * dt * (forces[i,:,1:] + forces[i-1,:,1:])
        pot[i], kin[i] = calc_energies(x[i], v[i])
        
    return x, v, pot, kin, forces


# using only vectorized calculations and pbc, no neighbor list
def do_md_pbc(x_init, v_init, dt, n_steps, box, boxl):
    # Initialize energy arrays
    pot = np.zeros(n_steps)
    kin = np.zeros(n_steps)

    # Initialize trajectory arrays
    x = np.zeros([n_steps, len(x_init), 4])
    v = np.zeros_like(x)
    forces = np.zeros_like(x)

    x[0], v[0] = x_init, v_init
    forces[0] = calc_forces(x[0])
    pot[0], kin[0] = calc_energies(x[0], v[0])

    box0 = box[0]  # a bottom corner of the box
    box00 = box[0] + boxl * np.ones(3)  # the corner furthest away from the former
    ptosb = np.zeros((n_steps, 1))  # array to count particles that went "outside"

    for i in tqdm(range(1, n_steps)):
        # calculate new positions
        x[i,:,1:] = x[i-1,:,1:] + v[i-1,:,1:] * dt + 0.5 * dt**2 * forces[i-1,:,1:]
        
        # check if atoms 'escaped'
        for j in range(len(x_init)):
            if (x[i,j,1:] > box0).all() and (x[i,j,1:] < box00).all():
                pass
            else:
                ptosb[i] += 1
                # find the value that's too big
                for k in range(3):
                    if x[i,j,1+k] < box0[k]:
                        x[i,j,1+k] += boxl
                    elif x[i,j,1+k] > box00[k]:
                        x[i,j,1+k] -= boxl
                    else:
                        pass
        
        # calculate new forces and velocities
        forces[i] = calc_forces(x[i])
        v[i,:,1:] = v[i-1,:,1:] + 0.5 * dt * (forces[i,:,1:] + forces[i-1,:,1:])
        pot[i], kin[i] = calc_energies(x[i], v[i])
        
    return x, v, pot, kin, forces, ptosb


# using partly vectorized calculations and neighbor list, no pbc
def do_md_nb(x_init, v_init, dt, n_steps, nblist, nbpoint, sigma, epsilon):
    '''
    execute a md simulation

    x_init: array of shape (N, 4)
        current positions
        x_init[:,0] corresponds the index of the atom
        x_init[:,1] corresponds to the x coordinate
        x_init[:,2] corresponds to the y coordinate
        x_init[:,3] corresponds to the z coordinate
    v_init: array of shape (N, 4)
        current positions
        v_init[:,0] corresponds the index of the atom
        v_init[:,1] corresponds to the x coordinate
        v_init[:,2] corresponds to the y coordinate
        v_init[:,3] corresponds to the z coordinate
    returns:
        positions: array of shape (n_steps, N, 4)
        velocities: array of shape (n_steps, N, 4)
        pot: array of shape (n_steps)
        kin: array of shape (n_steps)
    '''
    # Initialize energy arrays
    pot = np.zeros(n_steps)
    kin = np.zeros(n_steps)

    # Initialize trajectory arrays
    x = np.zeros([n_steps, len(x_init), 4])
    v = np.zeros_like(x)
    forces = np.zeros_like(x)

    x[0], v[0] = x_init, v_init
    forces[0] = calc_forces(x[0], sigma, epsilon)
    pot[0], kin[0] = calc_energies(x[0], v[0], sigma, epsilon)

    for i in tqdm(range(1, n_steps)):
        # calc new positions
        x[i,:,1:] = x[i-1,:,1:] + v[i-1,:,1:] * dt + 0.5 * dt**2 * forces[i-1,:,1:]

        # check if new nblist has to be computed
        vec = x[i,:,1:] - x[i-1,:,1:]
        dist_diff = (vec[0]**2 + vec[1]**2 + vec[2]**2)**0.5
        
        if max(dist_diff) > CUTOFF_LIST - CUTOFF_DISTANCE:
            nblist, nbpoint = initialize_neighbor_list(x[i], CUTOFF_DISTANCE)
        
        # calculate forces only in between neighbors
        forces[i] = calc_forces_nb(x[i], nblist, nbpoint, sigma, epsilon)

        # calculate new velocities
        v[i,:,1:] = v[i-1,:,1:] + 0.5 * dt * (forces[i,:,1:] + forces[i-1,:,1:])
        
        # calculate energies
        pot[i], kin[i] = calc_energies(x[i], v[i], sigma, epsilon)
        
    return x, v, pot, kin, forces


# using partly vectorized calculations and neighbor list and pbc
def do_md_nb_pbc(x_init, v_init, dt, n_steps, nblist, nbpoint, box, boxl, sigma, epsilon):
    '''
    execute a md simulation

    x_init: array of shape (N, 4)
        current positions
        x_init[:,0] corresponds the index of the atom
        x_init[:,1] corresponds to the x coordinate
        x_init[:,2] corresponds to the y coordinate
        x_init[:,3] corresponds to the z coordinate
    v_init: array of shape (N, 4)
        current positions
        v_init[:,0] corresponds the index of the atom
        v_init[:,1] corresponds to the x coordinate
        v_init[:,2] corresponds to the y coordinate
        v_init[:,3] corresponds to the z coordinate
    returns:
        positions: array of shape (n_steps, N, 4)
        velocities: array of shape (n_steps, N, 4)
        pot: array of shape (n_steps)
        kin: array of shape (n_steps)
    '''
    # Initialize energy arrays
    pot = np.zeros(n_steps)
    kin = np.zeros(n_steps)

    # Initialize trajectory arrays
    x = np.zeros([n_steps, len(x_init), 4])
    v = np.zeros_like(x)
    forces = np.zeros_like(x)

    x[0], v[0] = x_init, v_init
    forces[0] = calc_forces(x[0], sigma, epsilon)
    pot[0], kin[0] = calc_energies(x[0], v[0], sigma, epsilon)

    box0 = box[0]  # a bottom corner of the box
    box00 = box[0] + boxl * np.ones(3)  # the corner furthest away from the former
    ptosb = np.zeros((n_steps, 1))  # array to count particles that went "outside"

    for i in tqdm(range(1, n_steps)):
        # calc new positions
        x[i,:,1:] = x[i-1,:,1:] + v[i-1,:,1:] * dt + 0.5 * dt**2 * forces[i-1,:,1:]
        
        # check and apply PBC
        for j in range(len(x_init)):
            if (x[i,j,1:] > box0).all() and (x[i,j,1:] < box00).all():
                pass
            else:
                ptosb[i] += 1
                # find the value that's too big
                for k in range(3):
                    if x[i,j,1+k] < box0[k]:
                        x[i,j,1+k] += boxl
                    elif x[i,j,1+k] > box00[k]:
                        x[i,j,1+k] -= boxl
                    else:
                        pass

        # check if new nblist has to be computed
        vec = x[i,:,1:] - x[i-1,:,1:]
        dist_diff = (vec[0]**2 + vec[1]**2 + vec[2]**2)**0.5
        
        if max(dist_diff) > CUTOFF_LIST - CUTOFF_DISTANCE:
            nblist, nbpoint = initialize_neighbor_list(x[i], CUTOFF_DISTANCE)
        
        # calculate forces only in between neighbors
        forces[i] = calc_forces_nb(x[i], nblist, nbpoint, sigma, epsilon)

        # calculate new velocities
        v[i,:,1:] = v[i-1,:,1:] + 0.5 * dt * (forces[i,:,1:] + forces[i-1,:,1:])
        
        # calculate energies
        pot[i], kin[i] = calc_energies(x[i], v[i], sigma, epsilon)
    
    x[:,:,0] = x_init[:,0]

    return x, v, pot, kin, forces, ptosb
