'''This file contains older, slower versions of the calculating algorithms'''
import numpy as np
from tqdm import tqdm
from expl_fake_inputs import *

# first version of calculating energies
def calc_energies1(positions, velocities, sigma=SIGMA, epsilon=EPSILON):
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


# first version of calculating forces
def calc_forces1(positions, sigma=SIGMA, epsilon=EPSILON):
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
            if i != j:
                vec_r = positions[i, 1:] - positions[j, 1:]  # relative position
                mod_r = np.sqrt(vec_r[0]**2+vec_r[1]**2+vec_r[2]**2)  # distance
                mod_force = - 4 * epsilon * (12 * ((sigma**12) / (mod_r)**13) - 6 * ((sigma**6) / (mod_r)**7))  # mod of the force
                vec_force = mod_force * vec_r / mod_r  # force from atom i on atom j
                total_forces[j,1:] += vec_force  # add this force to the total force arr
            else: 
                pass
    return total_forces


# eliminated double counting and if statement
def calc_forces2(positions, sigma=SIGMA, epsilon=EPSILON):
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
    total_forces[:,0] = np.copy(positions[:,0])
    
    for i in range(N):
        forces = np.zeros_like(positions)  # initialize array
        forces[:,0] = np.copy(positions[:,0])  # initialize index in array
        for j in range(i+1, N): # atoms don't have force on themself and actio = reactio
            vec_r = positions[i, 1:] - positions[j, 1:]  # relative position
            mod_r = np.sqrt(vec_r[0]**2+vec_r[1]**2+vec_r[2]**2)  # distance
            mod_force = - 4 * epsilon * (12 * ((sigma**12) / (mod_r)**13) - 6 * ((sigma**6) / (mod_r)**7))  # mod of the force
            vec_force = mod_force * vec_r / mod_r  # force from atom i on atom j
            total_forces[j,1:] += vec_force  # add this force to the total force arr
            vec_force_rev = - vec_force # force from atom j on atom i
            total_forces[i,1:] += vec_force_rev  # add this force to the total force arr
    return total_forces


# first approach
def do_md1(x_init, v_init, dt, n_steps):
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
    forces[0] = calc_forces1(x[0])
    pot[0], kin[0] = calc_energies1(x[0], v[0])

    for i in tqdm(range(1, n_steps)):
        x[i,:,1:] = x[i-1,:,1:] + v[i-1,:,1:] * dt + 0.5 * dt**2 * forces[i-1,:,1:]
        forces[i] = calc_forces1(x[i])
        v[i,:,1:] = v[i-1,:,1:] + 0.5 * dt * (forces[i,:,1:] + forces[i-1,:,1:])
        pot[i], kin[i] = calc_energies1(x[i], v[i])
        
    return x, v, pot, kin, forces


# use calc_forces2
def do_md2(x_init, v_init, dt, n_steps):
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
    forces[0] = calc_forces2(x[0])
    pot[0], kin[0] = calc_energies1(x[0], v[0])

    for i in tqdm(range(1, n_steps)):
        x[i,:,1:] = x[i-1,:,1:] + v[i-1,:,1:] * dt + 0.5 * dt**2 * forces[i-1,:,1:]
        forces[i] = calc_forces2(x[i])
        v[i,:,1:] = v[i-1,:,1:] + 0.5 * dt * (forces[i,:,1:] + forces[i-1,:,1:])
        pot[i], kin[i] = calc_energies1(x[i], v[i])
       
    return x, v, pot, kin, forces

