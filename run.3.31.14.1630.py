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
    delta
except NameError:
    delta = 17.5

date = '3.28.14'

lens = '0414'

execfile("/home/rumbaugh/LoadVLA_2001.py")
ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)
g = np.arange(len(ltime))[:len(ltime)-10]
ltime=ltime[g]
A1flux,A2flux,Bflux,Cflux = flux_arr[0][g],flux_arr[1][g],flux_arr[2][g],flux_arr[3][g]
A1err,A2err,Berr,Cerr = flux_err_arr[0][g],flux_err_arr[1][g],flux_err_arr[2][g],flux_err_arr[3][g]

st = time.time()
ltime = (ltime-ltime[0])#/86400
#find time delays


fluxdict = {'A1': A1flux, 'A2': A2flux, 'C': Cflux}
errdict = {'A1': A1err, 'A2': A2err, 'C': Cerr}
imgnames = ['A1','A2','C']

gAonly = np.where(ltime < 1946-1839)[0]

for imgname in imgnames:
    cr = np.loadtxt('/home/rumbaugh/output.disp_sim.%s_B%s.%s.dat'%(lens,imgname,date))
    ttmp,mtmp,BA_disp = calc_disp_delay(fluxdict[imgname][g],Bflux[g],ltime,ltime,errdict[imgname][g],Berr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2a',delta,output=2,verbose=False)
    perhi = len(cr[cr<BA_disp])*1./len(cr)
    print 'B%s time delay:\n%4.1f days\nDispersion greater than %4.1f%% of trials\n'%(imgname,ttmp,perhi)
    

for imgname in imgnames:
    cr = np.loadtxt('/home/rumbaugh/output.disp_sim.%s_VLA_A_only_B%s.%s.dat'%(lens,imgname,date))
    ttmp,mtmp,BA_disp = calc_disp_delay(fluxdict[imgname][g[gAonly]],Bflux[g[gAonly]],ltime[gAonly],ltime[gAonly],errdict[imgname][g[gAonly]],Berr[g[gAonly]],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2a',delta,output=2,verbose=False)
    perhi = len(cr[cr<BA_disp])*1./len(cr)
    print 'B%s time delay - A config only:\n%4.1f days\nDispersion greater than %4.1f%% of trials\n'%(imgname,ttmp,perhi)
