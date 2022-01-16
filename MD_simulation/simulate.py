'This module executes a simulation. User input is skipped for testing purposes'
# from MD_simulation.animation import POSITIONS
from coordinates import *
# from neighbours import *
from verlet import *

from fake_inputs import *

positions_ini = initialize_positions(NUMBER_FCC_UNITS, REDUCED_DENSITY, SIGMA, SEE_ATOMS=False)
velocities_ini = initialize_velocities(positions_ini, REDUCED_TEMPERATURE, False)
# plot_velocity_hist(velocities, False)

DT = 0.0002
N_STEPS = 100

res = do_md(positions_ini, velocities_ini, dt=DT, n_steps=N_STEPS)

x_equil_traj = res[0]
v_equil_traj = res[1]
pot_equil = res[2]
kin_equil = res[3]

steparr = np.arange(N_STEPS)

# Plot energy
plt.plot(steparr, pot_equil, label="$E_\mathrm{pot}$")
plt.plot(steparr, kin_equil, label="$E_\mathrm{kin}$")
plt.plot(steparr, pot_equil + kin_equil, label="$E_\mathrm{pot} + E_\mathrm{kin}$")
plt.legend()
plt.xlabel("step")
plt.ylabel("Energy")
plt.show()