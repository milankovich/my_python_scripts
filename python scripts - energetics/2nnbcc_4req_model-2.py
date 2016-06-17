# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:32:49 2015

@author: Shipeng
"""

# This program calculates the five frequencies for solute diffusion at infinite
# dilution (BCC). This code uses the model I of Philibert. 
# The five frequencies are:
# w2:  the frequency of impurity-vacancy exchange;
# w3:  the frequency of solvent-vacancy exchange that dissociate the impurity-vacancy
#      pairfrom a nearest-neighbor position to a 2nd-nearest-neighbor position;
# w3p: the frequency of solvent-vacancy exchange that dissociate the impurity-vacancy
#      pairfrom a nearest-neighbor position to long distance (no interaction);
# w4:  the frequency of solvent-vacancy exchange that associate the impurity-vacancy
#      pair from a 2nd-nearest-neighbor position to nearest-neighbor position;
# w5:  the frequency of solvent-vacancy exchange that dissociate the impurity-vacancy
#      pair from a 2nd-nearest-neighbor position to long distance (no interaction).
import sys, math, numpy as np
x = []
y = []

#Fe-Fe

Eb_00 = 0.62
for n in range(1):
    Eb_0 = Eb_00 + n*0.01
    for i in range(5):
        temp = 0.04+i*0.01
        freq = 6E12

        eaa1 = -1.06925
        ebb1 = -1.06925
        eav1 = -0.28525
        ebv1 = -0.28525
        eab1 = -1.06925
        
        Ea_0 = Eb_0

#calculate Eact, Eact = Ea_0 + (E_f - E_i)/2
        E0 = Ea_0
        E2 = Eb_0
        E3 = Ea_0 + ( (1*eav1 + 6*eaa1 + 1*eab1 + 8*eav1) - (7*eav1 + 1*ebv1 + 1*eav1 + 7*eaa1) )/2.0
        E4 = Ea_0 + ( (7*eav1 + 1*ebv1 + 1*eav1 + 7*eaa1) - (8*eav1 + 1*eav1 + 6*eaa1 + 1*eab1) )/2.0
        
#    print "\nThe five energies are:"
        #print "E0 : ", E0
        #print "E2 : ", E2
        #print "E3 : ", E3
        #print "E4 : ", E4

        w0  = freq*math.exp(-E0/temp)
        w2  = freq*math.exp(-E2/temp)
        w3  = freq*math.exp(-E3/temp)
        w4  = freq*math.exp(-E4/temp)
        
        ratio=w4/w0
        r2=ratio**2
        r1=ratio
        r3=r1*r2
        Ffactor=1.0/7.0*((528.5+779.03*r1+267.5*r2+24*r3)/(75.5+146.83*r1+69.46*r2+8*r3))
        ffactor=(7*Ffactor*w3)/(2*w2 + 7*Ffactor*w3)
        D=0.287*0.287*w4/w3*ffactor*w2
        #print ratio, Ffactor
        #print ffactor

#    print "\nThe five frequencies are:"
#    print "w2 : ", w2
#    print "w3 : ", w3
#    print "w3p: ", w3p
#    print "w4 : ", w4
#    print "w5 : ", w5
#    print "The relative diffusivity is: ",D
#    print "The diffusivity is: ",D*math.exp(-1.995/temp)
#    print "\n"
        Evfor = 8*eav1 - 4*eaa1
        #print Evfor
        #print 1/temp, math.log(D*math.exp(-Evfor/temp))
        x.append(1/temp)
        y.append(math.log(D*math.exp(-Evfor/temp)))
    
    z = np.polyfit(x,y,1)
    print Eb_0, z[0]

