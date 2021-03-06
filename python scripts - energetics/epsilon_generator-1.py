# -*- coding: utf-8 -*-
"""
Created on Tue Nov 03 11:41:32 2015

@author: Shipeng
"""

import numpy as np

W = np.zeros((5,5))

alpha = 1.0

Z = 8.0

W[0][1] =  0.458;        #Fe-Cu   
W[0][2] =  0.094;      #Fe-Mn
W[0][3] =  0.007;      #Fe-Ni
W[0][4] = -1.542;      #Fe-Si
W[1][2] =  0.090;        #Cu-Mn
W[1][3] =  0.106;        #Cu-Ni
W[1][4] = -0.344;        #Cu-Si
W[2][3] = -2.2*0.207;  #Mn-Ni
W[2][4] = -1.094;      #Mn-Si
W[3][4] = -2.03;      #Ni-Si

print W

W[:][:] = W[:][:]/(Z/2.0)*alpha

print W

Coh = np.zeros(5)

Coh[0] = -4.28
Coh[1] = -3.49
Coh[2] = -2.92
Coh[3] = -4.34
Coh[4] = -4.03

V_f = np.zeros(5)

V_f[0] =  1.6  #Fe
V_f[1] =  1.6  #Cu
V_f[2] =  1.4  #Mn
V_f[3] =  1.48 #Ni
V_f[4] = -0.21 #Si

eps = np.zeros((5,5))

for i in range(5):
    eps[i][i] = Coh[i] / (Z/2.0)
    print eps[i][i]

print "\n"
xv = np.zeros(5)
    
for i in range(5):
    xv[i] = (V_f[i] + Z/2.0*eps[i][i])/Z
    print xv[i]
    
print "\n"


for i in range(5):
    for j in range(i+1,5):
        eps[i][j] = (W[i][j] + eps[i][i] + eps[j][j])/2.0
        print i,j, eps[i][j]
print "\n"
print "%0.4f" % (0.126),"\t",
for i in range(5):
    print "%0.4f" % (xv[i]),"\t\t",
print "\n",        
for i in range(5):
    for j in range(5):
        print "\t ",
        if (j < i):
            print "\t ",
        else:
            if (j != 4):
                print "%0.6f" % (eps[i][j]),
            if (j == 4):
                print "%0.6f" % (eps[i][j]),"\n",
           
           
           
           