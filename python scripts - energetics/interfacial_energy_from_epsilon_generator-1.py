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
W[0][2] =  0.094;        #Fe-Mn
W[0][3] =  0.007;        #Fe-Ni
W[0][4] = -1.542;        #Fe-Si
W[1][2] =  0.0;        #Cu-Mn
W[1][3] =  0.04353;      #Cu-Ni
W[1][4] = -1.47069;        #Cu-Si
W[2][3] = -2.5*0.207;   #Mn-Ni
W[2][4] = -1.094;        #Mn-Si
W[3][4] = -2.03;         #Ni-Si

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
V_f[1] =  0.9  #Cu
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
        eps[j][i] = eps[i][j]
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

# MNS-Fe
list1 = [0]
list2 = [2,3,4]      
list3 = list1 + list2
print list3    

x_MNS = np.zeros(5)
x_Fe = np.zeros(5)

x_MNS[2] = 0.37
x_MNS[3] = 0.52
x_MNS[4] = 1 - x_MNS[2] - x_MNS[3]

x_Fe[0] = 1.0

epsilon_star = 0.0

for i in list3:
    for j in list3:
#        print i,j,eps[i][j]
#        print i,j,x_MNS[i], x_MNS[j]
#        print i,j,x_Fe[i], x_Fe[j]
#        print "\n"
        epsilon_star += eps[i][j] * (x_MNS[i] * x_Fe[j] - x_MNS[i] * x_MNS[j] / 2.0 - x_Fe[i] * x_Fe[j] / 2.0)

print "Fe-MNS:", epsilon_star


print "\n"

#MNS-Cu
list1 = [1]
list2 = [2,3,4]  
list3 = list1 + list2
print list3    

x_MNS = np.zeros(5)
x_Cu = np.zeros(5)

x_MNS[2] = 0.4
x_MNS[3] = 0.5
x_MNS[4] = 1 - x_MNS[2] - x_MNS[3]

x_Cu[1] = 1.0

epsilon_star = 0.0

for i in list3:
    for j in list3:
        epsilon_star += eps[i][j] * (x_MNS[i] * x_Cu[j] - x_MNS[i] * x_MNS[j] / 2.0 - x_Cu[i] * x_Cu[j] / 2.0)

print "Cu-MNS:", epsilon_star

print "\n"

#Fe-Cu
list1 = [0]
list2 = [1]  
list3 = list1 + list2
print list3    

x_Fe = np.zeros(5)
x_Cu = np.zeros(5)

x_Fe[0] = 1.0
x_Cu[1] = 1.0

epsilon_star = 0.0

for i in list3:
    for j in list3:
#        print i,j,eps[i][j]
#        print i,j,x_Cu[i],x_Cu[j]
#        print i,j,x_Fe[i],x_Fe[j]
#        print "term1 = ", x_Cu[i] * x_Fe[j]
#        print "term2 = ", x_Cu[i] * x_Cu[j] / 2.0
#        print "term3 = ", x_Fe[i] * x_Fe[j] / 2.0
#        print "temp = ", eps[i][j] * (x_Cu[i] * x_Fe[j] - x_Cu[i] * x_Cu[j] / 2.0 - x_Fe[i] * x_Fe[j] / 2.0)
#        print "\n"
        epsilon_star += eps[i][j] * (x_Cu[i] * x_Fe[j] - x_Cu[i] * x_Cu[j] / 2.0 - x_Fe[i] * x_Fe[j] / 2.0)

print "Cu-Fe:", epsilon_star

   
           