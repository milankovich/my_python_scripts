# -*- coding: utf-8 -*-
"""
Created on Fri May 27 14:12:57 2016

@author: Shipeng
"""
import math
from math import *

# This code will calculate the RED related vacancy concentration under
# neutron irradiation. See Odette Phil. Mag. in 2005

kT = (290.0 + 273.0) / 11604
print "\ntemperature: \t", kT, "\n"

rv = 0.57E-9 # SIA-vacancy recombination radius in m

xi = 0.4 # defect creation efficiency

sigma_dpa = 1.5E-25 # displacement-per-atom (dpa) cross-section

phi = 2.3E18 # dose rate  (m^-2s^-1) ATR1

print "\nflux: \t\t",phi, "\n"

Omega_a = 1.18E-29 # atomic volume

Dv = pow(Omega_a,2.0/3.0) * 6E12 * exp(-0.7/kT)

St = 2E14

eta = 16.0 * pi * rv * xi * phi * sigma_dpa / Omega_a / Dv / St / St

print eta

phi_ratio = pow(3E15/phi,0.25)

gs = 2.0 / eta * (sqrt(1.0 + eta) - 1.0) * phi_ratio

print gs

Xv = gs * xi * sigma_dpa * phi / Dv / St

print "RED Xv: \t\t", Xv

thermoXv = exp(-1.6/kT)
print "thermo Xv: \t", thermoXv

ratio =  thermoXv / (Xv + thermoXv)
print "ratio: \t\t",ratio



#myXv = 1.0 / pow(128,3)
#print myXv

print "\n", ratio/phi

print "\nscaling factor: ", 1.0 / (Xv + thermoXv) * phi

