'This module executes a simulation. User input is skipped for testing purposes'
from coordinates import *
# from neighbours import *
from verlet import *

from fake_inputs import *


positions = initialize_positions(NUMBER_FCC_UNITS, REDUCED_DENSITY, True)
velocities = initialize_velocities(positions, REDUCED_TEMPERATURE, False)
plot_velocity_hist(velocities, False)

print(np.shape(positions))
