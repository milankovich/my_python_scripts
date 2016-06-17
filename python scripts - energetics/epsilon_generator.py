# -*- coding: utf-8 -*-
"""
Created on Tue Nov 03 10:57:07 2015

@author: Shipeng
"""

# this is for pair interaction input generation
# stick to first nearest neighbors

W_FeCu =  0.0;     W_FeMn =  0.094;   W_FeNi = 0.007;   W_FeSi = -1.542;
W_CuMn =  0.0;     W_CuNi =  0.0;     W_CuSi = 0.0; 
W_MnNi = -0.207;   W_MnSi = -0.907; 
W_NiSi =  0.002; 

Coh_Fe = -4.28
Coh_Cu = -3.49
Coh_Mn = -2.92
Coh_Ni = -4.34
Coh_Si = -4.03

V_f_Fe = 2.0
V_f_Cu = 1.6
V_f_Mn = 1.4
V_f_Ni = 1.48
V_f_Si = -0.21

Z = 8.0

eps_FeFe = Coh_Fe/(Z/2.0)
eps_CuCu = Coh_Cu/(Z/2.0)
eps_MnMn = Coh_Mn/(Z/2.0)
eps_NiNi = Coh_Ni/(Z/2.0)
eps_SiSi = Coh_Si/(Z/2.0)

eps_FeCu =  0.0;     eps_FeMn =  0.094;   eps_FeNi = 0.007;   eps_FeSi = -1.542;
eps_CuMn =  0.0;     eps_CuNi =  0.0;     eps_CuSi = 0.0; 
eps_MnNi = -0.207;   eps_MnSi = -0.907; 
eps_NiSi =  0.002; 