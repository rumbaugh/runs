import numpy as np
import smoothing_1d as sm

for pair in range (1,101):
    cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nickrung0/Nickrung0_pair%i.txt'%pair)
    ltime = cr[:,0]
    A,Aerr,B,Berr = cr[:,1],cr[:,2],cr[:,3],cr[:,4]
    smB,smB_var = sm.boxcar(ltime+10,B,ltime[10:len(A)-10],10.,y_var=Berr**2,calc_cov_matrix=False)
