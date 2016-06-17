# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Shipeng\.spyder2\.temp.py
"""

#epsilon to omega

Z1=8.0
Z2=6.0

epsilon_X_X_1 = -1.07
epsilon_X_X_2 = 0.0

epsilon_Y_Y_1 = -0.73
epsilon_Y_Y_2 = 0.0

epsilon_X_Y_1 = -0.853
epsilon_X_Y_2 = 0.0

print 

Omega = Z1/2.0*(2.0*epsilon_X_Y_1-epsilon_X_X_1-epsilon_Y_Y_1) + Z2/2.0*(2.0*epsilon_X_Y_2-epsilon_X_X_2-epsilon_Y_Y_2)

print "Omega is", Omega
print "omega1 = ",(2.0*epsilon_X_Y_1-epsilon_X_X_1-epsilon_Y_Y_1)
print "omega2 = ",(2.0*epsilon_X_Y_2-epsilon_X_X_2-epsilon_Y_Y_2)

#omega to epsilon

omega = 0.094
lambda0 = 0.0

epsilon_xy1 = ( omega - Z1/2 * (-epsilon_X_X_1 - epsilon_Y_Y_1) - Z2/2 * (-epsilon_X_X_2 - epsilon_Y_Y_2) ) / (2.0) / (Z1/2 + Z2/2 * lambda0)
print "epsilon_xy1", epsilon_xy1
print "epsilon_xy2", epsilon_xy1 * lambda0

ordering1 = 2.0*epsilon_X_Y_1-epsilon_X_X_1-epsilon_Y_Y_1
ordering2 = 2.0*epsilon_X_Y_2-epsilon_X_X_2-epsilon_Y_Y_2

print ordering1, ordering2

cohesive_X = Z1/2*epsilon_X_X_1 + Z2/2*epsilon_X_X_2
cohesive_Y = Z1/2*epsilon_Y_Y_1 + Z2/2*epsilon_Y_Y_2
print cohesive_X, cohesive_Y
