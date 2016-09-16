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
execfile("/home/rumbaugh/LoadEVLA_2011.py")
try:
    ntrials
except NameError:
    ntrials = 10000
date = '5.26.14'

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
    lens
except NameError:
    lens = '1938'
source = 'B1938'
crS = LoadEVLA_2011(source,normalize=True)
crS['day'] -= crS['day'][0]
ltime = crS['day']
rms = crS['rms']
imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
errnames = np.copy(imgnames)
for n in np.arange(0,len(errnames)): errnames[n] = 'err%s'%errnames[n][4:]
fluxA1 = crS[imgnames[0]]
A1err = crS[errnames[0]]
fluxA2 = crS[imgnames[1]]
A2err = crS[errnames[1]]
fluxA = fluxA1+fluxA2
Aerr = np.sqrt(A1err**2+A2err**2)
fluxB = crS[imgnames[2]]
Berr = crS[errnames[2]]
g = np.where((fluxA > 0)&(fluxB>0)&(Aerr > 0)&(Berr>0))[0]

st = time.time()
#find time delays
BA_disp_mat = np.zeros(ntrials)
delta = 10.5
FILE = open('/home/rumbaugh/output.disp_sim.%s_BC.%s.dat'%(lens,date),'w')
st = time.time()
for i in range(0,ntrials):
    g = np.arange(len(fluxA))
    rA = np.random.normal(0,1.,len(g))*Aerr
    np.random.shuffle(g)
    g2 = np.arange(len(fluxB))
    rB = np.random.normal(0,1.,len(g2))*Berr
    np.random.shuffle(g2)
    ttmp,mtmp,BA_disp_mat[i] = calc_disp_delay(fluxB[g2]+rB[g2],fluxA[g]+rA[g],ltime,ltime,Berr[g2],Aerr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta,output=2,verbose=False)
    FILE.write('%E %f\n'%(BA_disp_mat[i],mtmp))
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
