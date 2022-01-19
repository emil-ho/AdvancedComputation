'Execute this file to start the program'
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from tqdm import tqdm

from src_inputs import *
from src_coordinates import *
from src_neighbors import *
from src_verlet import *
from src_verlet_slow import *
from src_energies import *
# from expl_fake_inputs import *


mainbutton()

N_FCC,RED_D,RED_T,SIGMA,EPSILON,CO_POT,CO_LIST,N_STEPS,RED_TS,wh,sigma1,epsilon1,SVDIR = return_values()

delete_values()

positions_ini, box, boxl = initialize_positions(number_fcc_units=int(N_FCC), reduced_density=RED_D, see_atoms=True, savedir=SVDIR)
velocities_ini = initialize_velocities(positions_ini, reduced_temperature=RED_T, savedir=SVDIR)
nblist, nbpoint = initialize_neighbor_list(positions_ini, CUTOFF_DISTANCE, savedir=SAVEDIR)
plot_velocity_hist(velocities_ini, 40, True)

res = do_md_nb_pbc(positions_ini, velocities_ini, RED_TS, int(N_STEPS), nblist, nbpoint, box, boxl, SIGMA, EPSILON)

x_traj, v_traj, pot, kin, forc, ptosb = res

save_traj(x_traj, SVDIR)
save_energies(pot, kin, SVDIR)

print('Simulation done')
