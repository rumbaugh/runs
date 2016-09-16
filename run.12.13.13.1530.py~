import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

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
    maxtimestep = 60
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

execfile("/home/rumbaugh/Load1938.py")
ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()

Cflux = C1flux+C2flux
Cerr = np.zeros(len(Cflux))
for i in range(0,len(Cerr)): Cerr[i] = m.sqrt((C1err[i])**2+(C2err[i])**2)

st = time.time()
ltime = (ltime-ltime[0])/86400
#find time delays
BA_disp_mat = np.zeros(ntrials)
delta = 17.5
BC_disp_mat = np.zeros(ntrials)
FILE = open('/home/rumbaugh/output.disp_sim.1938_BC.8.22.13.dat','w')
for i in range(0,ntrials):
    g = np.arange(len(Cflux))
    rC = np.random.normal(0,1.,len(g))*Cerr
    np.random.shuffle(g)
    g2 = np.arange(len(Bflux))
    rB = np.random.normal(0,1.,len(g2))*Berr
    np.random.shuffle(g2)
    ttmp,mtmp,BC_disp_mat[i] = calc_disp_delay(Cflux[g]+rC[g],Bflux[g2]+rB[g2],ltime,ltime,Cerr[g],Berr[g2],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True)
    FILE.write('%E\n'%(BC_disp_mat[i]))
FILE.close()
