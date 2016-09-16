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
date = '5.22.14'

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
source = 'MG0414'
crS = LoadEVLA_2011(source,normalize=True)
crS['day'] -= crS['day'][0]
ltime = crS['day']
rms = crS['rms']
imgnames = ['fluxA1','fluxA2','fluxB','fluxC']
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
fluxC = crS[imgnames[3]]
Cerr = crS[errnames[3]]

for img,fluxA,Aerr in zip(['A1','A2','C'],[fluxA1,fluxA2,fluxC],[A1err,A2err,Cerr]):
    g = np.where((fluxA > 0)&(fluxB>0)&(Aerr > 0)&(Berr>0))[0]

    st = time.time()
#find time delays

    dispmatrixAB = calc_disp_delay(fluxA[g],fluxB[g],ltime[g],ltime[g],Aerr[g],Berr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2,dispmatrix=True,outfile='/mnt/data2/rumbaugh/EVLA/11A-138/disp_results/disp_out.%s_B%s.D_2.%s.dat'%(source,img,date))
    tauAB,muAB,dispAB = calc_disp_delay(fluxA[g],fluxB[g],ltime[g],ltime[g],Aerr[g],Berr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2,dispmatrix=False,outfile='/mnt/data2/rumbaugh/EVLA/11A-138/disp_results/disp_out.%s_B%s.D_2.%s.dat'%(source,img,date),verbose=False)
#now use D_4_2 with range of deltas
    delta_arr = np.arange(19)+3.5
    BA_delay_d42,BAmud42,BAdispd42,BC_delay_d42,BCmud42,BCdispd42,BD_delay_d42,BDmud42,BDdispd42 = np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr))
    print '%s B%s:\n\nD_2 - %f\n\nD_4_2\n'%(source,img,tauAB)
    for i in range(0,len(delta_arr)):
        BA_delay_d42[i],BAmud42[i],BAdispd42[i] = calc_disp_delay(fluxA[g],fluxB[g],ltime[g],ltime[g],Aerr[g],Berr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta=delta_arr[i],output=2,outfile='/mnt/data2/rumbaugh/EVLA/11A-138/disp_results/disp_out.%s_B%s.D_4_2.delta_%.1f.%s.dat'%(source,img,delta_arr[i],date),verbose=False)
        print '%.1f - tau: %5.1f  mu: %f\n'%(delta_arr[i],BA_delay_d42[i],BAmud42[i])
    print 'Medians- tau: %5.1f  mu: %f\n'%(np.median(BA_delay_d42),np.median(BAmud42))

