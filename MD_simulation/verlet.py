# this file contains the verlet algorithm
import numpy as np
from tqdm import tqdm

import matplotlib.pyplot as plt
from fake_inputs import *

# no idea if we even need this function
def potential_init(sigma, epsilon, r):
    """
    This function calculates a LJ-Potential and the corresponding forces for a given array of radii

    sigma: float
        Parameter of the LJ potential
    epsilon: float
        Parameter of the LJ potential
    r: int or float or 1d-array
        distance(s) for which the value(s) are calculated
    returns: float or 1d-array, float or 1d-array
        The potential and force for the given distance(s)
    """
    V_LJ = 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6)
    F_LJ = - 4 * epsilon * (12 * (sigma / r)**13 - 6 * (sigma / r)**7)
    return V_LJ, F_LJ

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
    v, x = velocities, positions

    for i in range(0, N): # loop over all atoms
        Ekin += (v[i,1]**2+v[i,2]**2 + v[i,3]**2) / 2 # calc Ekin of atom i
        for j in range(i+1, N): # loop over all "remaining" atoms for all interactions
            r = ( (x[i,1] - x[j,1])**2 + (x[i,2] - x[j,2])**2 + (x[i,3] - x[j,3])**2 )**(0.5)
            Epot += 4 * epsilon * ((sigma / r)**12 - (sigma / r)**6) 

    return Epot, Ekin


def calc_forces(positions, sigma=SIGMA, epsilon=EPSILON):
    """
    This function calculates the forces on all atoms with LJ-Pot
    positions: array of shape (N, 4)
        N is the number of Atoms
        positions[:,0] corresponds the index of the atom
        positions[:,1] corresponds to the x coordinate
        positions[:,2] corresponds to the y coordinate
        positions[:,3] corresponds to the z coordinate
    sigma: float
        Parameter of the LJ potential
    epsilon: float
        Parameter of the LJ potential
    returns: array of shape (N, 4)
        N is the number of Atoms
        forces[:,0] corresponds the index of the atom
        forces[:,1] corresponds to the x coordinate
        forces[:,2] corresponds to the y coordinate
        forces[:,3] corresponds to the z coordinate
    """ 
    N = len(positions)
    total_forces = np.zeros_like(positions)
    total_forces[:,0] = positions[:,0]
    
    for i in range(N):
        forces = np.zeros_like(positions)  # initialize array
        forces[:,0] = positions[:,0]
        for j in range(N):
            if i != j:  # atoms don't have force on themself
                vec_r = positions[i, 1:] - positions[j, 1:]
                mod_r = np.sqrt(vec_r[0]**2+vec_r[1]**2+vec_r[2]**2)
                mod_force = - 4 * epsilon * (12 * ((sigma**12) / (mod_r)**13) - 6 * ((sigma**6) / (mod_r)**7))
                vec_force = vec_r / mod_r
                forces[j, 1:] += mod_force * vec_force
            else:
                pass
        total_forces[:,1:] += forces[:,1:]
    return total_forces

def integrate(pos_cur, pos_prev, dt, forces):
    """
    Integrate the equation of motion using the Verlet algorithm.       
    pos_cur : array of shape (N, 4)
        current positions
        positions[:,0] corresponds the index of the atom
        positions[:,1] corresponds to the x coordinate
        positions[:,2] corresponds to the y coordinate
        positions[:,3] corresponds to the z coordinate
    pos_prev : array of shape (N, 4)
        previus positions
        positions[:,0] corresponds the index of the atom
        positions[:,1] corresponds to the x coordinate
        positions[:,2] corresponds to the y coordinate
        positions[:,3] corresponds to the z coordinate
    dt : float
        time step size
    forces : array of shape (N, 4)
        N is the number of Atoms
        forces[:,0] corresponds the index of the atom
        forces[:,1] corresponds to the x coordinate
        forces[:,2] corresponds to the y coordinate
        forces[:,3] corresponds to the z coordinate
    returns: array of shape (N, 4), array of shape (N, 4)
        new positions and velocities
    """
    pos_next, v = pos_cur, pos_cur  # initialize arrays
    pos_next[:,1:] = 2 * pos_cur[:,1:] - pos_prev[:,1:] + dt**2 * forces[:,1:]
    v[:,1:] = (pos_next[:,1:] - pos_prev[:,1:]) / (2 * dt)
    return pos_next, v

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
    v = np.zeros(x.shape)

    # Initialize values for positions and velocities
    x_prev, x_cur = x_init, x_init
    x_cur[:,1:] = x_init[:,1:] + dt * v_init[:,1:]

    for i in tqdm(range(n_steps)):
        forces = calc_forces(x_cur)
        x[i], v[i] = integrate(x_cur, x_prev, dt, forces)

        x_prev = x_cur
        x_cur = x[i]
#         print(np.shape(x), np.shape(v))
        pot[i], kin[i] = calc_energies(x[i], v[i])
        
    return x, v, pot, kin
