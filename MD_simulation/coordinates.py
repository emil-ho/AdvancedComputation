"""This file is for inititalizing the coordinates and velocities of the atoms"""

import numpy as np
import matplotlib.pyplot as plt

# the parameters are only set like that for testing purposes, actually they will be imported
NUMBER_FCC_UNITS = 3  # Number of FCC unit cells in each direction in the supercell
REDUCED_DENSITY = 0.8442 # Reduced density (adimensional)
REDUCED_TEMPERATURE = 0.722 # Reduced temperature (adimensional)

NUMBER_HIST_BINS = 11
SEE_HISTOGRAM = 11  # has to be 1 for calculation of the velocity histogram

SIGMA = 0.341  # nm  # Parameter sigma   of the Lennard-Jones potential
EPSILON = 119.8  # K   # Parameter epsilon of the Lennard-Jones potential

#######################################
###### COORDINATES
#######################################

# calculate the lattice constant (for an fcc lattice)
A = (4 / REDUCED_DENSITY) ** (1/3)

# initialize the numpy arrays:
# first dim is number of atom, second dim is the cordinate (xyz)
positions = np.zeros([4*NUMBER_FCC_UNITS**3, 4])
for i in range(4*NUMBER_FCC_UNITS**3):
    positions[i,0] = i

# initialize the positions of the 4 atoms in the basis (atom 0 is at (0,0,0))
positions[1] = np.array([1, 0, 0, 0]) + A * np.array([0, 0.5, 0.5, 0])
positions[2] = np.array([2, 0, 0, 0]) + A * np.array([0, 0, 0.5, 0.5])
positions[3] = np.array([3, 0, 0, 0]) + A * np.array([0, 0.5, 0, 0.5])

for i in range(NUMBER_FCC_UNITS):
    for n in range(4*NUMBER_FCC_UNITS**0):
        positions[4 * i * NUMBER_FCC_UNITS**0 + n, 1:] = positions[n, 1:]  + i * np.array([A, 0, 0])

for i in range(NUMBER_FCC_UNITS):
    for n in range(4*NUMBER_FCC_UNITS**1):
        positions[4 * i * NUMBER_FCC_UNITS**1 + n, 1:] = positions[n, 1:]  + i * np.array([0, A, 0])

for i in range(NUMBER_FCC_UNITS):
    for n in range(4*NUMBER_FCC_UNITS**2):
        positions[4 * i * NUMBER_FCC_UNITS**2 + n, 1:] = positions[n, 1:]  + i * np.array([0, 0, A])

# determine the current center of the system
center_first = A * np.array([0.5, 0.5, 0.5])
center_last = NUMBER_FCC_UNITS * center_first
center = center_first + 0.5 * center_last

# shift everything so the center is on (0,0,0)
for i in range(4*NUMBER_FCC_UNITS**3):
    positions[i,1:] = positions[i,1:] - center

# switch to units where sigma=1
# ?????

np.save("MD_Simulation/files/positions_ini", positions)

HAVE_A_LOOK = 11
if HAVE_A_LOOK == 1:
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(positions[:,1],positions[:,2], positions[:,3])
    for i in range(0):
        ax.text(positions[i,1], positions[i,2], positions[i,3], positions[i,0])
    ax.scatter(center[0], center[1], center[2], c='r')
    ax.scatter(0,0,0,c='r')
    ax.text(center[0], center[1], center[2], 'center_old')
    ax.text(0,0,0, 'center_new')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

#######################################
###### VELOCITIES
#######################################

VARIANCE = REDUCED_TEMPERATURE**(-0.5)

# initialize the numpy arrays:
# first dim is number of atom, second dim is the cordinate (xyz)
velocities = np.zeros([4*NUMBER_FCC_UNITS**3, 4])
for i in range(4*NUMBER_FCC_UNITS**3):
    velocities[i,0] = int(i)

velocities[:,1:] = VARIANCE**2 * np.random.randn(4*NUMBER_FCC_UNITS**3, 3)

total_velocity = np.zeros(3)
for i in range(4 * NUMBER_FCC_UNITS**3):
    total_velocity += velocities[i, 1:]
total_velocity = total_velocity / (4 * NUMBER_FCC_UNITS**3)

# shift the velocities so that the center of mass is in rest
for i in range(4 * NUMBER_FCC_UNITS**3):
    velocities[i,1:] -= total_velocity

np.save("MD_simulation/files/velocities_ini", velocities)

if SEE_HISTOGRAM == 1:

    # calculate total velocity again
    total_velocity = np.zeros(3)
    for i in range(4 * NUMBER_FCC_UNITS**3):
        total_velocity += velocities[i, 1:]
    total_velocity = total_velocity / (4 * NUMBER_FCC_UNITS**3)
    print(f"total_velocity = {total_velocity}")


    # making the histogram
    vel_hist_x, bin_edges_x = np.histogram(velocities[:,1], NUMBER_HIST_BINS)
    vel_hist_y, bin_edges_y = np.histogram(velocities[:,2], NUMBER_HIST_BINS)
    vel_hist_z, bin_edges_z = np.histogram(velocities[:,3], NUMBER_HIST_BINS)

    max_counts = np.max(np.concatenate((vel_hist_x, vel_hist_y, vel_hist_z)))
    max_vel = np.max(np.abs(velocities[:,1:]))

    fig, ax1 = plt.subplots(1,3, squeeze=True)
    ax1[0].hist(bin_edges_x[:-1], NUMBER_HIST_BINS, weights=vel_hist_x)
    ax1[0].set_title('x direction')
    ax1[0].set_xlabel('v in unit/unit')
    ax1[0].set_ylabel('frequency')
    ax1[0].set_xlim(-1.1 * max_vel, 1.1 * max_vel)
    ax1[0].set_ylim(0, 1.1 * max_counts)
    ax1[1].hist(bin_edges_y[:-1], NUMBER_HIST_BINS, weights=vel_hist_y)
    ax1[1].set_title('y direction')
    ax1[1].set_xlabel('v in unit/unit')
    ax1[1].set_xlim(-1.1 * max_vel, 1.1 * max_vel)
    ax1[1].set_ylim(0, 1.1 * max_counts)
    ax1[2].hist(bin_edges_z[:-1], NUMBER_HIST_BINS, weights=vel_hist_z)
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
