import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

execfile("/home/rumbaugh/radmon_var_chisq_test.py")

FILE = open('/home/rumbaugh/B1608_files/chisq_results_1608.4.8.13.dat','w')
FILE.write("# lens img1 chisq1 P1 img2 chisq2 P2 img3 chisq3 P3 img4 chisq4 P4")

try:
    trials
except NameError:
    trials = 1000000

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
    maxtimestep = 60
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

#execfile("/home/rumbaugh/Load1608.py")
#ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1608()

#Cflux = C1flux+C2flux
#Cerr = np.zeros(len(Cflux))
#for i in range(0,len(Cerr)): Cerr[i] = m.sqrt((C1err[i])**2+(C2err[i])**2)

cr = np.loadtxt('/home/rumbaugh/B1608_files/1608_season1.dat')
ltime,Aflux,Bflux,Cflux,Dflux,Aerr,Berr,Cerr,Derr = cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4],cr[:,5],cr[:,6],cr[:,7],cr[:,8]

st = time.time()
ltime = (ltime-ltime[0])#/86400

fluxdict = {0: Cflux, 1: Bflux, 2: Aflux, 3: Dflux}
errdict = {0: Cerr, 1: Berr, 2: Aerr, 3: Derr}
imgname = {0: 'C', 1: 'B', 2: 'A', 3: 'D'}

FILE.write("\n1608 ")
chisq_arr,prob_arr = np.zeros(4),np.zeros(4)
for img in range(0,4):
    S,Serr = fluxdict[img].copy(),errdict[img].copy()
    S,Serr = S/np.mean(S),Serr/np.mean(S)
    chisq_arr[img],prob_arr[img] = calc_chi_sqrd(S,Serr,calcprob=True,trials=trials)
for img in range(0,4):
    FILE.write("%2s %6.2f %6.4f "%(imgname[img],chisq_arr[img],prob_arr[img]))
FILE.write("NA      0     0")
FILE.close()

print 'All Done!\nTime elapsed: %f seconds'%(time.time()-st)
