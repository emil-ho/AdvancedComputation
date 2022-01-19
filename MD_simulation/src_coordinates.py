"""This file is for inititalizing the coordinates and velocities of the atoms"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from itertools import product, combinations

# Problems:
# number of bins makes problems, supposedly isn't an int?
# what is the unit of velocity?

#######################################
###### COORDINATES
#######################################

def initialize_positions(number_fcc_units, reduced_density, see_atoms=False, savedir=None):
    '''
    This function initializes the atom positions in an FCC lattice.

    number_fcc_units: int
        Number of unit cells in each direction
    reduced_density: float
        Density in reduced units
    see_atoms: BOOL
        If True, the atom configuration will be plotted
    savedir: string
        The location of the directory where the files should be saved
    returns: array of shape (N, 4), array of shape (4,3)
        N is the number of Atoms
        positions[:,0] corresponds the index of the atom
        positions[:,1] corresponds to the x coordinate
        positions[:,1] corresponds to the y coordinate
        positions[:,1] corresponds to the z coordinate

        First row is starting point of the box
        Other rows are xyz coord of one basis vector of the box
    '''
    # calculate number of atoms
    NATOMS = int(4 * number_fcc_units**3)

    # calculate the lattice constant (for an fcc lattice)
    A = (4 / reduced_density) ** (1/3)

    # initialize the numpy arrays:
    # first dim is number of atom, second dim is the cordinate (xyz)
    positions = np.zeros([NATOMS, 4])
    for i in range(NATOMS):
        positions[i,0] = i

    # initialize the positions of the 4 atoms in the basis (atom 0 is at (0,0,0))
    positions[1] = np.array([1, 0, 0, 0]) + A * np.array([0, 0.5, 0.5, 0])
    positions[2] = np.array([2, 0, 0, 0]) + A * np.array([0, 0, 0.5, 0.5])
    positions[3] = np.array([3, 0, 0, 0]) + A * np.array([0, 0.5, 0, 0.5])

    # initialize in x direction
    for i in range(number_fcc_units):
        for n in range(4*number_fcc_units**0):
            positions[4 * i * number_fcc_units**0 + n, 1:] = positions[n, 1:]  + i * np.array([A, 0, 0])

    # initialize in y direction
    for i in range(number_fcc_units):
        for n in range(4*number_fcc_units**1):
            positions[4 * i * number_fcc_units**1 + n, 1:] = positions[n, 1:]  + i * np.array([0, A, 0])

    # initialize in z direction
    for i in range(number_fcc_units):
        for n in range(4*number_fcc_units**2):
            positions[4 * i * number_fcc_units**2 + n, 1:] = positions[n, 1:]  + i * np.array([0, 0, A])

    
    # determine the current center of the system
    center_old = 0.5 * A * number_fcc_units * np.ones(3)
    center_new = np.zeros(3)

    # shift everything so the center is on (0,0,0)
    for i in range(NATOMS):
        positions[i,1:] = positions[i,1:] - 0.5 * number_fcc_units * A * np.ones(3)

    # compute coordinates of the simulation box
    boxl = number_fcc_units * A
    box = np.array([positions[0,1:],
                    positions[0,1:] + boxl * np.array([1,0,0]),
                    positions[0,1:] + boxl * np.array([0,1,0]),
                    positions[0,1:] + boxl * np.array([0,0,1])])

    if see_atoms == True:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(positions[:,1],positions[:,2], positions[:,3])
        
        for i in range(0):  # labels of the first ... atoms
            ax.text(positions[i,1], positions[i,2], positions[i,3], int(positions[i,0]))

        ax.scatter(center_old[0], center_old[1], center_old[2])
        ax.text(center_old[0], center_old[1], center_old[2], s="center_old")     

        ax.scatter(center_new[0], center_new[1], center_new[2], c='r')
        ax.text(center_new[0], center_new[1], center_new[2], 'center_new')
        
        r1 = [- 0.5 * number_fcc_units * A, 0.5 * number_fcc_units * A]
        for s, e in combinations(np.array(list(product(r1, r1, r1))), 2):
            if np.sum(np.abs(s-e)) == r1[1]-r1[0]:
                ax.plot3D(*zip(s, e), color="b")

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()

    if savedir != None:
        STAMP = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        now = datetime.now()
        local_now = now.astimezone()
        local_tz = local_now.tzinfo
        local_tzname = local_tz.tzname(local_now)
        space = ' '

        HEADER = f'Initial positions of the atoms in units of SIGMA \
        \nTime of initialization: {STAMP + space + local_tzname}\
        \nfirst column: Atom number, rest: x,y,z coordinate'
        np.savetxt(savedir + '/positions_ini.dat', positions, header=HEADER,
                    fmt='%4g' + '% 10.4f' * 3)

    return positions, box, boxl

def save_traj(positions, savedir):
    """
    This function saves the computed trajectory
    
    positions: array of dims (N_timesteps, N_atoms, 4)
        In last dimension the first value is the index, the others the xyz coordinates
    savedir: string
        The location where it should be saved
    """
    N_time = len(positions)
    N_atoms = len(positions[0])

    with open(savedir + '/trajectory.dat', 'w') as f:
            STAMP = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            now = datetime.now()
            local_now = now.astimezone()
            local_tz = local_now.tzinfo
            local_tzname = local_tz.tzname(local_now)
            space = ' '
            HEADER = f'Positions of the atoms at all timesteps \
            \nTime of initialization: {STAMP + space + local_tzname}\n\n'
            f.write(HEADER)

    for i in range(N_time):
        with open(savedir + '/trajectory.dat', 'a') as f:
            f.write(f'Timestep: {i}\n')
            f.write(f'Index           Position\n')
            for j in range(N_atoms):
                f.write(f'{format(positions[i,j,0], "4g")}     ')  # dirty fix
#                arr = np.array([j])
#                f.write(f'{format(arr, "4g")}     ')
                f.write(f'{format(positions[i,j,1], " .4f")}  ')
                f.write(f'{format(positions[i,j,2], " .4f")}  ')
                f.write(f'{format(positions[i,j,3], " .4f")}  \n')
            f.write('\n')
    return None

#######################################
###### VELOCITIES
#######################################

def initialize_velocities(positions, reduced_temperature, savedir=None):
    '''
    This function initialize Boltzmann distributed velocities for a given array of atoms.

    positions: array of shape (N, 4)
        N is the number of Atoms
        positions[:,0] corresponds the index of the atom
        positions[:,1] corresponds to the x coordinate
        positions[:,1] corresponds to the y coordinate
        positions[:,1] corresponds to the z coordinate
    reduced_temperature: float
        Temperature of the system in reduced units
    see_histogram: Bool
        If True, the histogram will be plotted and saved
    savedir: string
        The location of the directory where the files should be saved
    returns: array of shape (N, 4)
        N is the number of Atoms
        velocities[:,0] corresponds the index of the atom
        velocities[:,1] corresponds to the x coordinate
        velocities[:,2] corresponds to the y coordinate
        velocities[:,3] corresponds to the z coordinate
    '''

    VARIANCE = reduced_temperature**(-0.5)
    number_fcc_units = int((0.25 * len(positions))**(1/3))
    NATOMS = len(positions)
    # initialize the numpy arrays:
    # first dim is number of atom, second dim is the cordinate (xyz)
    velocities = np.zeros([NATOMS, 4])
    for i in range(NATOMS):
        velocities[i,0] = int(i)

    velocities[:,1:] = VARIANCE**2 * np.random.randn(NATOMS, 3)

    total_velocity = np.zeros(3)
    for i in range(4 * number_fcc_units**3):
        total_velocity += velocities[i, 1:]
    total_velocity = total_velocity / (4 * number_fcc_units**3)

    # shift the velocities so that the center of mass is in rest
    for i in range(4 * number_fcc_units**3):
        velocities[i,1:] -= total_velocity

    if savedir != None:
        STAMP = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        now = datetime.now()
        local_now = now.astimezone()
        local_tz = local_now.tzinfo
        local_tzname = local_tz.tzname(local_now)
        space = ' '

        HEADER = f'Initial velocities of the atoms in reduced units \
        \nTime of initialization: {STAMP + space + local_tzname}\
        \nfirst column: Atom number, rest: x,y,z component'
        np.savetxt(savedir + '/velocities_ini.dat', velocities, header=HEADER,
                    fmt='%4g' + '% 10.4f' * 3)

    return velocities

def plot_velocity_hist(velocities, number_hist_bins, see_histogram=False):
    '''
    This function calculates and plots a histogram of the velocitites in each direction.

    velocities: array of shape (N, 4)
        N is the number of Atoms.
        velocities[:,0] corresponds the index of the atom
        velocities[:,1] corresponds to the x coordinate
        velocities[:,2] corresponds to the y coordinate
        velocities[:,3] corresponds to the z coordinate
    number_hist_bins: int
        The number of bins the histogram should have
    see_histogram: Bool
        if True, the histogram is plotted
    returns: bunch of stuff
    '''
    
    # calculating the total velocity (to include in the plot)
    number_fcc_units = int((0.25 * len(velocities))**(1/3))
    total_velocity = np.zeros(3)
    for i in range(4 * number_fcc_units**3):
        total_velocity += velocities[i, 1:]
    total_velocity = total_velocity / (4 * number_fcc_units**3)

    # computing the histogram
    vel_hist_x, bin_edges_x = np.histogram(velocities[:,1], number_hist_bins)
    vel_hist_y, bin_edges_y = np.histogram(velocities[:,2], number_hist_bins)
    vel_hist_z, bin_edges_z = np.histogram(velocities[:,3], number_hist_bins)

    # Plotting of the histogram
    if see_histogram == True:

        max_counts = np.max(np.concatenate((vel_hist_x, vel_hist_y, vel_hist_z)))
        max_vel = np.max(np.abs(velocities[:,1:]))

        fig, ax1 = plt.subplots(1,3, squeeze=True)
        ax1[0].hist(bin_edges_x[:-1], number_hist_bins, weights=vel_hist_x)
        ax1[0].set_title('x direction')
        ax1[0].set_xlabel('v in unit/unit')
        ax1[0].set_ylabel('frequency')
        ax1[0].set_xlim(-1.1 * max_vel, 1.1 * max_vel)
        ax1[0].set_ylim(0, 1.1 * max_counts)
        ax1[1].hist(bin_edges_y[:-1], number_hist_bins, weights=vel_hist_y)
        ax1[1].set_title('y direction')
        ax1[1].set_xlabel('v in unit/unit')
        ax1[1].set_xlim(-1.1 * max_vel, 1.1 * max_vel)
        ax1[1].set_ylim(0, 1.1 * max_counts)
        ax1[2].hist(bin_edges_z[:-1], number_hist_bins, weights=vel_hist_z)
        ax1[2].set_title('z direction')
        ax1[2].set_xlabel('v in unit/unit')
        ax1[2].set_xlim(-1.1 * max_vel, 1.1 * max_vel)
        ax1[2].set_ylim(0, 1.1 * max_counts)

        yaxis_1 = ax1[1].get_yaxis()
        yaxis_1.set_visible(False)
        yaxis_2 = ax1[2].get_yaxis()
        yaxis_2.set_visible(False)

        fig.suptitle(f'total velocity: v = \
            {round(total_velocity[0], 18), round(total_velocity[1], 18), round(total_velocity[2], 18)} \
            unit', fontsize=10)
        plt.show()

    return vel_hist_x, bin_edges_x, vel_hist_y, bin_edges_y, vel_hist_z, bin_edges_z
