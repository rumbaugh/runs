import smoothing_1d as sm
import numpy as np
import matplotlib.pyplot as py
import emcee
import time

A = np.array([1,2,4,8,6,5])*1.
B = np.copy(A)*2+0.5
ltime = np.arange(len(A))*3+1.
Aerr,Berr = np.ones(len(A))*0.1,np.ones(len(B))*0.1
tau = 0.5
smooth_param = 10.
smB,smB_var,Bcovmat = sm.boxcar(ltime+tau,B,ltime,smooth_param,y_var=Berr*Berr,calc_cov_matrix=True)
