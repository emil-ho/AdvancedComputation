# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 23:10:44 2022

@author: Pedro
"""

from inputs import *
from coordinates import *
from neighbors2 import *



mainbutton()

fcc,rd,rt,sig,eps,cop,col,ns,rs,wh,sigma1,epsilon1,savedir=return_values()


delete_values()

positions_ini=initialize_positions(int(fcc), rd,True)

velocities_ini=initialize_velocities(positions_ini, float(rt))

plot_velocity_hist(velocities_ini, 100, True)

initialize_neighbor_list(positions_ini, float(col),savedir)

