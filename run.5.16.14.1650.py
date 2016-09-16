import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
execfile('/home/rumbaugh/LoadEVLA_2011.py')
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

date = '5.16.14'

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

for source in ['B1938','B0712']:
    crS = LoadEVLA_2011(source,normalize=True)
    crS['day'] -= crS['day'][0]
    rms = crS['rms']
    fluxratio_err = 0.0043
    if source == 'B1938':
        fluxratio_err = 0.0048
        imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
    if source == 'B0712':
        imgnames = ['fluxA','fluxB','fluxC','fluxD']
    fluxA1 = crS[imgnames[0]]
    A1err = np.sqrt(rms**2+(fluxratio_err*A1)**2)
    fluxA2 = crS[imgnames[1]]
    A2err = np.sqrt(rms**2+(fluxratio_err*A2)**2)
    fluxA = fluxA1+fluxA2
    Aerr = np.sqrt(A1err**2+A2err**2)
    fluxB = crS[imgnames[2]]
    Berr = np.sqrt(rms**2+(fluxratio_err*B)**2)
    
    g = np.where((fluxA > 0)&(fluxB>0))[0]


#find time delays
    dispmatrixAB = calc_disp_delay(fluxB[g],fluxA[g],crS['day'][g],crS['day'][g],Berr[g],Aerr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2,dispmatrix=True,outfile='/mnt/data2/rumbaugh/EVLA/11A-138/disp_results/disp_out.%s.D_2.%s.dat'%(source,date))
#now use D_4_2 with range of deltas
    delta_arr = np.arange(19)+3.5
    BA_delay_d42,BAmud42,BAdispd42,BC_delay_d42,BCmud42,BCdispd42,BD_delay_d42,BDmud42,BDdispd42 = np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr))
    for i in range(0,len(delta_arr)):
        BA_delay_d42[i],BAmud42[i],BAdispd42[i] = calc_disp_delay(fluxB[g],fluxA[g],crS['day'][g],crS['day'][g],Berr[g],Aerr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta=delta_arr[i],output=2,outfile='/mnt/data2/rumbaugh/EVLA/11A-138/disp_results/disp_out.%s.D_4_2.delta_%.1f.%s.dat'%(source,delta_arr[i],date))
