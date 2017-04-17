import numpy as np
import matplotlib.pyplot as plt

#-----------------some variable----------------#
L = 0.25
nx = 41
dx = L/nx
nt = 25
f = 50
dt = 1/f
R = 8.314
A = 

#--------------------------------#
P = np.ones((nt,nx))*2.0*10**3    #(kPa)
T = np.ones((nt,nx))*300    #(K)
u = np.ones((nt,nx))*0.001    #(m/s)

#---------------------------------#

