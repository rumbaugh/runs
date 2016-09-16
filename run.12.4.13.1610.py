import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")
execfile("/home/rumbaugh/LinReg.py")
try:
    ntrials
except NameError:
    ntrials = 10


try:
    ALAG
except NameError:
    ALAG = 31.5
try:
    CLAG
except NameError:
    CLAG = 36.5
try:
    DLAG
except NameError:
    DLAG = 80.5
try:
    justone
except NameError:
    justone = False
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
    maxtimestep = 105
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

try:
    lens
except NameError:
    lens = '1030'

execfile("/home/rumbaugh/LoadVLA_2001.py")
ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)
g = np.arange(len(ltime))[:len(ltime)-10]
ltime=ltime[g]
Aflux,Bflux = flux_arr[0][g],flux_arr[1][g]
Aerr,Berr = flux_err_arr[0][g],flux_err_arr[1][g]

if lens == '0712': 
    Aflux += Bflux
    Aerr = np.sqrt(Aerr**2+Berr**2)
    Bflux,Berr = flux_arr[2][g],flux_err_arr[2][g]

st = time.time()
ltime = (ltime-ltime[0])#/86400
#find time delays
BA_disp_mat = np.zeros(ntrials)
delta = 17.5
FILE = open('/home/rumbaugh/output.disp_sim.%s_BA.12.4.13.dat'%lens,'w')
lsA_A,lsB_A = LinReg(ltime,Aflux,wy=1./(Aerr**2))
lsA_B,lsB_B = LinReg(ltime,Bflux,wy=1./(Berr**2))
Aflux_diff,Bflux_diff = Aflux-(lsA_A+lsB_A*ltime),Bflux-(lsA_B+lsB_B*ltime)
st = time.time()
for i in range(0,ntrials):
    g = np.arange(len(Aflux_diff))
    rA = np.random.normal(0,1.,len(g))*Aerr
    np.random.shuffle(g)
    g2 = np.arange(len(Bflux_diff))
    rB = np.random.normal(0,1.,len(g2))*Berr
    np.random.shuffle(g2)
    ttmp,mtmp,BA_disp_mat[i] = calc_disp_delay(Aflux_diff[g]+rA[g]+lsA_A+lsB_A*ltime,Bflux_diff[g2]+rB[g2]+lsA_B+lsB_B*ltime,ltime,ltime,Aerr[g],Berr[g2],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,verbose=False)
    FILE.write('%E\n'%(BA_disp_mat[i]))
    if i == 0: 
        t0 = time.time()
        print 'Initial ETA: %i seconds'%((t0-st)*(ntrials-1))
    for ichk in range(1,10):
        if ((i >= ntrials*ichk/10.) & (i < ntrials*ichk/10.+1)):
            tchk = time.time()
            print '%i%% done. ETA: %i second'%(ichk*10,(tchk-st)*1./ichk*(10.-ichk))
tend = time.time()
print '\n\nTotal Time Elapsed: %.0f seconds\n\n'%(tend-st)
FILE.close()
