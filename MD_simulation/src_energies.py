'This file contains the function for calculating and saving the energies'
from re import I
import numpy as np
from datetime import datetime


# vectorized energy calculation
def calc_energies(positions, velocities, sigma, epsilon):
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


def save_energies(epot, ekin, savedir):
    STAMP = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    now = datetime.now()
    local_now = now.astimezone()
    local_tz = local_now.tzinfo
    local_tzname = local_tz.tzname(local_now)
    space = ' '

    energies = np.zeros((len(epot), 4))
    for i in range(len(epot)):
        energies[i,0] = i
        energies[i,1] = epot[i]
        energies[i,2] = ekin[i]
        energies[i,3] = epot[i] + ekin[i]

    HEADER = f'Energies of the system \
    \nTime of initialization: {STAMP + space + local_tzname}\
    \n Ts   Epot      Ekin      Eges'
    np.savetxt(savedir + '/energy.dat', energies, header=HEADER,
                fmt='%4g' + '% 10.4f' * 3)
    return None
