'''This file contains the verlet algorithm and what is needed for it'''
import numpy as np
from tqdm import tqdm
from fake_inputs import *

# vectorized energy calculation
def calc_energies(positions, velocities, sigma=SIGMA, epsilon=EPSILON):
    """
    This function calculates the potential and kinetic energy of a system
    positions: array of shape (N, 4)
        N is the number of Atoms
        positions[:,0] corresponds the index of the atom
        positions[:,1] corresponds to the x coordinate
        positions[:,2] corresponds to the y coordinate
        positions[:,3] corresponds to the z coordinate
    velocities: array of shape (N, 4)
        N is the number of Atoms
        velocities[:,0] corresponds the index of the atom
        velocities[:,1] corresponds to the x coordinate
        velocities[:,2] corresponds to the y coordinate
        velocities[:,3] corresponds to the z coordinate
    sigma: float
        Parameter of the LJ potential
    epsilon: float
        Parameter of the LJ potential
    returns: float, float
        Potential and kinetic energy of the system
    """
    N = len(positions)
    Ekin = 0
    Epot = 0
    v, x = np.copy(velocities[:,1:]), np.copy(positions[:,1:])

    for i in range(N): # loop over all atoms
        Ekin += (v[i,0]**2+v[i,1]**2 + v[i,2]**2) / 2 # calc Ekin of atom i
        
        r = np.linalg.norm(x[i] - x[i + 1:], axis=1)[:, np.newaxis]
        r6inv = (1 / r)**6
        Epot  += np.sum(4 * epsilon * sigma**6  * r6inv * (sigma**6 * r6inv - 1))

    return Epot, Ekin


# vectorized force calculation
def calc_forces(positions, sigma=SIGMA, epsilon=EPSILON):
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


# using only vectorized calculations
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


def do_md_pdb(x_init, v_init, dt, n_steps, box, boxl):
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

    ptosb = np.zeros((n_steps, 1))

    for i in tqdm(range(1, n_steps)):
        # calculate new positions
        x[i,:,1:] = x[i-1,:,1:] + v[i-1,:,1:] * dt + 0.5 * dt**2 * forces[i-1,:,1:]
        # check if atoms 'escaped'
        for j in range(len(x_init)):
            if (x[i,j,1:] > box[0]).all() and (x[i,j,1:] < box[0] + boxl * np.ones(3)).all():
                pass
            else:
                ptosb[i] += 1
            

        forces[i] = calc_forces(x[i])
        v[i,:,1:] = v[i-1,:,1:] + 0.5 * dt * (forces[i,:,1:] + forces[i-1,:,1:])
        pot[i], kin[i] = calc_energies(x[i], v[i])
        
    return x, v, pot, kin, forces, ptosb