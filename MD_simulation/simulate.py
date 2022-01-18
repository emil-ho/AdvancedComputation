'This module executes a simulation. User input is skipped for testing purposes'
# from MD_simulation.animation import POSITIONS
from coordinates import *
from neighbors2 import *
from verlet import *
from verlet_slow import *
from fake_inputs import *
import os
from matplotlib.patches import Rectangle

SAVEDIR = os.getcwd() + '/MD_simulation/files'
NUMBER_FCC_UNITS = 1

positions_ini, BOX, BOXL = initialize_positions(NUMBER_FCC_UNITS, REDUCED_DENSITY, see_atoms=False, savedir=SAVEDIR)
velocities_ini = initialize_velocities(positions_ini, reduced_temperature=REDUCED_TEMPERATURE, savedir=SAVEDIR)
# plot_velocity_hist(velocities_ini, False)

TIMESTEP = 0.001
N_STEPS = 100

res = do_md_pbc(positions_ini, velocities_ini, dt=TIMESTEP, n_steps=N_STEPS, box=BOX, boxl=BOXL)

x_traj, v_traj, pot, kin, forc, ptosb = res


# plot trajectory
for a in range(len(positions_ini)):
    plt.plot(x_traj[0, a, 1], x_traj[0, a, 2], "x")
    plt.plot(x_traj[:, a, 1], x_traj[:, a, 2])
    plt.plot(x_traj[-1, a, 1], x_traj[-1, a, 2], ">")
rectangle = Rectangle((BOX[0,0], BOX[0,1]), BOXL, BOXL, fill=False, lw=2)
plt.gca().add_patch(rectangle)
plt.show()

steparr = np.arange(N_STEPS)

# Plot energy
#plt.plot(steparr, pot, label="$E_\mathrm{pot}$")
#plt.plot(steparr, kin, label="$E_\mathrm{kin}$")
#plt.plot(steparr, pot + kin, label="$E_\mathrm{pot} + E_\mathrm{kin}$")
plt.plot(steparr, ptosb)
plt.plot(steparr, len(positions_ini) - ptosb)
plt.legend()
plt.xlabel("step")
plt.ylabel("Number of particles")
#plt.show()

print(x_traj)