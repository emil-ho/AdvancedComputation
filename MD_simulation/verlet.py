'''This file contains the verlet algorithm and what is needed for it'''
import numpy as np
from tqdm import tqdm
from neighbors2 import get_nb_pos, initialize_neighbor_list
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


def calc_red_forces(pos1, positions, sigma=SIGMA, epsilon=EPSILON):
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


def calc_forces_nb(positions, nblist, nbpoint):
    total_force = np.zeros_like(positions)

    for j in range(len(positions)-1):
        nbbs = get_nb_pos(positions, nblist, nbpoint, j)
        forces = calc_red_forces(positions[j], nbbs)

        total_force[j] += forces[0]
        kk = 1
        for k in nbbs[:,0]:
            total_force[int(k),1:] += forces[kk,1:]
            kk += 1
    
    return total_force

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

def do_md_nb(x_init, v_init, dt, n_steps, nblist, nbpoint):
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
        # calc new positions
        x[i,:,1:] = x[i-1,:,1:] + v[i-1,:,1:] * dt + 0.5 * dt**2 * forces[i-1,:,1:]
        
        # check and apply PBC


        # check if new nblist has to be computed
        vec = x[i,:,1:] - x[i-1,:,1:]
        dist_diff = (vec[0]**2 + vec[1]**2 + vec[2]**2)**0.5
        
        if max(dist_diff) > CUTOFF_LIST - CUTOFF_DISTANCE:
            nblist, nbpoint = initialize_neighbor_list(x[i], CUTOFF_DISTANCE)
        
        # calculate forces only in between neighbors
        forces[i] = calc_forces_nb(x[i], nblist, nbpoint)

        # calculate new velocities
        v[i,:,1:] = v[i-1,:,1:] + 0.5 * dt * (forces[i,:,1:] + forces[i-1,:,1:])
        
        # calculate energies
        pot[i], kin[i] = calc_energies(x[i], v[i])
        
    return x, v, pot, kin, forces


def do_md_nb_pbc(x_init, v_init, dt, n_steps, nblist, nbpoint, box, boxl):
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
        forces[i] = calc_forces_nb(x[i], nblist, nbpoint)

        # calculate new velocities
        v[i,:,1:] = v[i-1,:,1:] + 0.5 * dt * (forces[i,:,1:] + forces[i-1,:,1:])
        
        # calculate energies
        pot[i], kin[i] = calc_energies(x[i], v[i])
        
    return x, v, pot, kin, forces, ptosb