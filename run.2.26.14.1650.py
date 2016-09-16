import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
import emcee
execfile("/home/rumbaugh/arrconv.py")

execfile("/home/rumbaugh/chi_squared_min.py")

try:
    runs
except NameError:
    runs = 1000

burnins = 100
if runs < 100: burnins = 1

try:
    timestep
except NameError:
    timestep = 0.5
try:
    mustep
except NameError:
    mustep = 0.001
try:
    maxtimestep
except NameError:
    maxtimestep = 60
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9
try:
    date
except NameError:
    date = '2.26.14'

bwidth = 10.
maxseasonfrac = 0.75

progress_doc = '/home/rumbaugh/sim_ltcurve_testing/progress_run.2.26.14.1650.dat'

FILE = open('/home/rumbaugh/sim_ltcurve_testing/results/VLA_grid_interp_nocovmat_%s.dat'%date,'w')
FILE.write('#pair tau  ### maxseasonfrac = %4.2f\n'%maxseasonfrac)
FILE.close()
FILE = open('/home/rumbaugh/sim_ltcurve_testing/results/VLA_grid_interp_nocovmat_noNeff_%s.dat'%date,'w')
FILE.write('#pair tau  ### maxseasonfrac = %4.2f\n'%maxseasonfrac)
FILE.close()
FILE = open('/home/rumbaugh/sim_ltcurve_testing/results/VLA_grid_interp_wcovmat_Neff_%s.dat'%date,'w')
FILE.write('#pair tau  ### maxseasonfrac = %4.2f\n'%maxseasonfrac)
FILE.close()
FILE = open('/home/rumbaugh/sim_ltcurve_testing/results/VLA_grid_interp_wcovmat_noNeff_%s.dat'%date,'w')
FILE.write('#pair tau  ### maxseasonfrac = %4.2f\n'%maxseasonfrac)
FILE.close()
FILE = open(progress_doc,'w')
FILE.write('# Starting...\n')
FILE.close()

st = time.time()

for pair in range(1,101):
    cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nick/Nick_pair%i.txt'%pair)
    ltime,A,Aerr,B,Berr = cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]
    ltime -= ltime[0]
    maxtimestep = int(maxseasonfrac*(ltime[-1]-ltime[0]))
    if maxtimestep < 60: maxtimestep = 60
    maxtime,mintime = maxtimestep,-1*maxtimestep
    for kernel in ['interp']:
        for use_cov_matrix in [True,False]:
            if use_cov_matrix:
                cmstr = 'wcovmat'
            else:
                cmstr = 'nocovmat'
            for use_Neff in [True,False]:
                if use_Neff: 
                    Neffstr = '_Neff'
                else:
                    Neffstr = '_noNeff'
                ttmp,mtmp,BA_disp,neff = chi_squared_min_delays(A,B,ltime,ltime,Aerr,Berr,None,maxtimestep,timestep,minmu,maxmu,mustep,smooth_function=kernel,smooth_param=np.array([bwidth]),use_overlap_mean=False,dotime=False,use_cov_matrix=use_cov_matrix,use_Neff=use_Neff)
                FILE = open('/home/rumbaugh/sim_ltcurve_testing/results/VLA_grid_%s_%s%s_%s.dat'%(kernel,cmstr,Neffstr,date),'a')
                FILE.write('%3i %9.5f\n'%(pair,ttmp))
                FILE.close()
    if ((((pair/5)*5 == pair) & (pair < 100)) | (pair == 1)):
        tchk = time.time()-st
        ETA = tchk/pair*100-tchk
        FILE = open(progress_doc,'a')
        FILE.write('\n#%2i%% Done\n#%.1f seconds elapsed\n#ETA: %.1f seconds\n'%(pair,tchk,ETA))
        FILE.close()
FILE = open(progress_doc,'a')
FILE.write('\n#100%% Done\n#%.1f seconds elapsed'%(tchk))
FILE.close()
