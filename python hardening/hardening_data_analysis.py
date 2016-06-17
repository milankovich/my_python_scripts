# -*- coding: utf-8 -*-
"""
Created on Mon May 30 13:46:28 2016

@author: Shipeng
"""
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.interpolate as interp
import math
from math import *

def extrap1d(interpolator):
    xs = interpolator.x
    ys = interpolator.y

    def pointwise(x):
        if x < xs[0]:
            return ys[0]+(x-xs[0])*(ys[1]-ys[0])/(xs[1]-xs[0])
        elif x > xs[-1]:
            return ys[-1]+(x-xs[-1])*(ys[-1]-ys[-2])/(xs[-1]-xs[-2])
        else:
            return interpolator(x)

    def ufunclike(xs):
        return array(map(pointwise, array(xs)))

    return ufunclike
    
def get_sigma(fv,r):
    myalpha = open('alpha.txt', 'r')
    tr = []
    tsigma = []
    sigma_ye = 200.0
    for line in myalpha:
        string = line.rstrip()
        myline = string.split()
        tr.append(float(myline[0]))
        tsigma.append(float(myline[1]))
    array_tr = np.asarray(tr)
    array_tsigma = np.asarray(tsigma)
    p = interp.interp1d(array_tr,array_tsigma,'cubic')
#    print "r",r
#    print "fv",fv,
#    print sqrt(max(fv,0.0))
    sigma_yp = p(r) * sqrt(max(fv,0.0))
    return sqrt(sigma_ye * sigma_ye + sigma_yp * sigma_yp) - sigma_ye

def red(flux):
# This code will calculate the RED related vacancy concentration under
# neutron irradiation. See Odette Phil. Mag. in 2005
    kT = (300.0 + 273.0) / 11604
    #print "\ntemperature: \t", kT, "\n"
    rv = 0.57E-9 # SIA-vacancy recombination radius in m
    xi = 0.4 # defect creation efficiency
    sigma_dpa = 1.5E-25 # displacement-per-atom (dpa) cross-section
    #phi = 2.3E18 # dose rate  (m^-2s^-1) ATR1
    phi = flux
#    print "\nflux: \t\t",phi, "\n"
    Omega_a = 1.18E-29 # atomic volume
    Dv = pow(Omega_a,2.0/3.0) * 6E12 * exp(-0.7/kT)
    St = 10E14
    eta = 16.0 * pi * rv * xi * phi * sigma_dpa / Omega_a / Dv / St / St    
#    print eta
    phi_ratio = pow(3E15/phi,0.25)
    gs = 2.0 / eta * (sqrt(1.0 + eta) - 1.0) * phi_ratio
#    print gs
    Xv = gs * xi * sigma_dpa * phi / Dv / St
#    print "RED Xv: \t\t", Xv
    thermoXv = exp(-1.6/kT)
#    print "thermo Xv: \t", thermoXv    
    ratio =  thermoXv / (Xv + thermoXv)
#    print "ratio: \t\t",ratio
#    print "\n", ratio/phi
#    print "\nscaling factor: ", 1.0 / (Xv + thermoXv) * phi
    return 1.0 / (Xv + thermoXv) * phi
    

#plt.plot(array_tr, array_tsigma, 'ro', markersize=10, clip_on=False, linewidth=0)
#plt.plot(xx, yy, 'g-', linewidth=2)
#plt.legend(('sampling point','5-point cubic spline interpolation'),loc='best')
#plt.show()

mydata = open('fvrdata.txt', 'r')

t_kmc = []
r = []
fv = []
dsigma = []

for line in mydata:
    string = line.rstrip()
    myline = string.split()
    t_kmc.append(float(myline[1]))
    r.append(float(myline[3]))
    fv.append(float(myline[5]))
    
array_t_kmc = np.asarray(t_kmc)
array_r = np.asarray(r)
array_fv = np.asarray(fv)

p_r = interp.interp1d(array_t_kmc,array_r,'slinear')
p_fv = interp.interp1d(array_t_kmc,array_fv,'slinear')
ep_fv = extrap1d(p_fv)
ep_r = extrap1d(p_r)

xxx = np.linspace(min(array_t_kmc), max(array_t_kmc)*1.5, 1000)
yyy = ep_fv(xxx)

plt.figure(0)
plt.semilogx(array_t_kmc, array_fv, 'ro', markersize=10, clip_on=False, linewidth=0)
plt.semilogx(xxx, yyy, 'g-', linewidth=2)
plt.legend(('sampling point','spline interpolation'),loc='best')
plt.show()



#for i in range(len(t_kmc)):
#    sigma_yp = p(r[i]) * sqrt(fv[i])
#    dsigma.append(sqrt(sigma_ye * sigma_ye + sigma_yp * sigma_yp) - sigma_ye)
    

ivar_ld = open('IVAR_LD.txt', 'r')

ivar_flux = []
ivar_fluence = []
ivar_sigma = []

for line in ivar_ld:
    string = line.rstrip()
    myline = string.split()
    if (int(myline[10]) == 290):
        ivar_flux.append(float(myline[9]))
        ivar_fluence.append(float(myline[8]))
        ivar_sigma.append(float(myline[11]))

plot_sigma_KMC = []

for i in range(len(ivar_flux)):
    target_fluence = ivar_fluence[i]
    time = ivar_fluence[i] / ivar_flux[i]

    KMC_output_to_fluence_factor = red(ivar_flux[i]*1E4)

    kmc_output_time = time / KMC_output_to_fluence_factor * (ivar_flux[i]*1E4)
    value_fv = ep_fv([kmc_output_time])
    value_r = ep_r([kmc_output_time])
    sigma_KMC = get_sigma(value_fv[0],value_r[0])
    print value_fv[0],value_r[0],kmc_output_time
    plot_sigma_KMC.append(sigma_KMC)
    #print ivar_fluence[i], sigma_KMC,ivar_sigma[i]

plt.figure(1)
fig1 = plt.semilogx(ivar_fluence, plot_sigma_KMC, 'ro', markersize=10, clip_on=False, linewidth=0)
fig2 = plt.semilogx(ivar_fluence, ivar_sigma, 'bs', markersize=12, clip_on=False, linewidth=0)
plt.legend(('KMC','IVAR '),loc='best')
plt.show()    



    
    
    