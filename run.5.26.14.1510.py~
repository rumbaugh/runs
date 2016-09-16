import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
execfile('/home/rumbaugh/LoadEVLA_2011.py')
execfile('/home/rumbaugh/LoadVLA_2001.py')
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

date = '5.20.14'

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

for source in ['B0712']:
    crS = LoadEVLA_2011(source,normalize=True)
    crS['day'] -= crS['day'][0]
    ltime = crS['day']
    rms = crS['rms']
    fluxratio_err = 0.0043
    if source == 'B1938':
        fluxratio_err = 0.0048
        imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
    if source == 'B0712':
        imgnames = ['fluxA','fluxB','fluxC','fluxD']
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
    
    if source == 'B0712':
        days,flux_arr,flux_err_arr = LoadVLA_2001(lens='0712')
        tfluxA1,tfluxA2,tfluxB = flux_arr[0],flux_arr[1],flux_arr[2]
        tAerr1,tAerr2,tBerr = flux_err_arr[0],flux_err_arr[1],flux_err_arr[2]
        ltime = np.append(days,ltime+1000)
        fluxA,fluxB = np.append(tfluxA1+tfluxA2,fluxA),np.append(tfluxB,fluxB)
        Aerr,Berr = np.append(np.sqrt(tAerr1**2+tAerr2**2),Aerr),np.append(tBerr,Berr)

    g = np.where((fluxA > 0)&(fluxB>0)&(Aerr > 0)&(Berr>0))[0]
    print np.mean(fluxA[g])/np.mean(fluxB[g])
    print np.mean(fluxA[g[2:8]])/np.mean(fluxB[g[2:8]])
