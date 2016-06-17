# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:00:15 2016

@author: Shipeng
"""
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

Omega = 1.18E-2


fig = plt.figure()
ax = fig.gca(projection='3d')

N_MNS = np.arange(100,3000,5)
r_Cu = np.arange(0.3,2,0.1)
N_MNS, r_Cu = np.meshgrid(N_MNS,r_Cu)


#N_MNS = 100

r_MNS = pow(3.0*N_MNS/pi/4.0*Omega,1.0/3.0)

#r_Cu = 1.5 #nm
N_Cu = 3*pi*pow(r_Cu,3.0)/3.0/Omega
gamma_Cu_Fe = 0.05725
gamma_MNS_Fe = 0.014732162
gamma_MNS_Cu = 0.013983


#print "Effective radius of MNS cluster:", r_MNS

# Es1 is the scaled interfacial energy of two separate precipitates

Es1 = 4*pi*pow(r_MNS,2.0)*gamma_MNS_Fe + 4*pi*pow(r_Cu,2.0)*gamma_Cu_Fe 
#print "Es1", Es1 is the "appendage"

r_cs = pow(3.0*(N_MNS+N_Cu)/pi/4.0*Omega,1.0/3.0)

Es2 = 4*pi*pow(r_Cu,2.0)*gamma_MNS_Cu + 4*pi*pow(r_cs,2.0)*gamma_MNS_Fe
#print "Es2", Es2 is the "core-shell"

#print Es1/Es2

Z = Es1/Es2
surf = ax.plot_surface(N_MNS, r_Cu, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.xlabel('Number of atoms in MNS shell')
plt.ylabel('Radius of Cu core (nm)')



plt.show()