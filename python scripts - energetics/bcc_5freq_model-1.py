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
import sys, math

freq = 6E12
temp = 0.06

eaa1 = -0.611
eaa2 = -0.611
ebb1 = -0.271
ebb2 = -0.611
eav1 = -0.163
eav2 = -0.163
ebv1 = -0.038
ebv2 = -0.203
eab1 = -0.430
eab2 = -0.609

Ea_0 = 0.62
Eb_0 = 1.03

#calculate Eact, Eact = Ea_0 + (E_f - E_i)/2
E2  = Eb_0
E3  = Ea_0 + ( (7*eaa1 + 1*eab1 + 6*eaa2 + 8*eav1 + 5*eav2 + 1*ebv2) - (7*eav1 + 1*ebv1 + 6*eav2 + 1*eav1 + 7*eaa1 + 5*eaa2 + 1*eab2) )/2.0
E3p = Ea_0 + ( (7*eaa1 + 1*eab1 + 6*eaa2 + 8*eav1 + 6*eav2) - (7*eav1 + 1*ebv1 + 6*eav2 + 7*eaa1 + 1*eav1 + 6*eaa2) )/2.0
E4  = Ea_0 + ( (7*eav1 + 1*ebv1 + 6*eav2 + 1*eav1 + 7*eaa1 + 5*eaa2 + 1*eab2) - (7*eaa1 + 1*eab1 + 6*eaa2 + 8*eav1 + 5*eav2 + 1*ebv2) )/2.0
E5  = Ea_0 + ( (7*eaa1 + 1*eav1 + 5*eaa2 + 1*eab2 + 8*eav1 + 6*eav2) - (8*eav1 + 1*ebv1 + 5*eav2 + 1*eav1 + 7*eaa1 + 6*eaa2) )/2.0

print "The five energies are:"

w2  = freq*math.exp(-E2/temp)
w3  = freq*math.exp(-E3/temp)
w3p = freq*math.exp(-E3p/temp)
w4  = freq*math.exp(-E4/temp)
w5  = freq*math.exp(-E5/temp)
ratio=w4/w5
r2=ratio**2
r1=ratio
Ffactor=1.0/7.0*((331.14*r2 + 857.93*r1+409.95)/(165.57*r1+134.21))
ffactor=(7*Ffactor*w3p)/(2*w2 + 7*Ffactor*w3p)
D=w2*w4/w3*ffactor*(1/32.0/32.0/32.0)

print "The five frequencies are:"
print "w2 : ", w2
print "w3 : ", w3
print "w3p: ", w3p
print "w4 : ", w4
print "w5 : ", w5
print "The relative diffusivity is: ",D
print "The diffusivity is: ",D*math.exp(-1.995/temp)/(1/32.0/32.0/32.0)

