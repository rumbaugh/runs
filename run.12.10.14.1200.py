import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

date = '12.10.14'

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
    lens = '1030'

try:
    ntrials
except NameError:
    ntrials=10

delta=10.5

for lens in ['1030','0712']:

    execfile("/home/rumbaugh/LoadVLA_2001.py")
    ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)

    Aflux,Bflux = flux_arr[0],flux_arr[1]
    Aerr,Berr = flux_err_arr[0],flux_err_arr[1]

    if lens == '0712': 
        Aflux += Bflux
        Aerr = np.sqrt(Aerr**2+Berr**2)
        Bflux,Berr = flux_arr[2],flux_err_arr[2]

    st = time.time()
    ltime = (ltime-ltime[0])#/86400
#find time delays
    BA_disp_mat = np.zeros(1000)
    delta = 10.5
    g = np.arange(len(ltime))[:len(ltime)-10]
    if lens == '1938':
        maxtimestep = 60.
    elif lens == '0712':
        maxtimestep = 105.
    else:
        maxtimestep = 155.
    cadence=ltime[g[1:]]-ltime[g[:-1]]    
    ttmp,mtmp,BA_disp = calc_disp_delay(Aflux[g],Bflux[g],ltime[g],ltime[g],Aerr[g],Berr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta,output=2,outfile='/home/rumbaugh/EVLA/light_curves/Dispersions/Disp_grid_out.%s.delta_%.1f_%s.dat'%(lens,delta,date))
    for i in range(0,ntrials):
        rtime = np.copy(ltime[g])
        for k in range(0,2):
            rcadence = np.shuffle(np.copy(cadence))
            for j in range(1,len(rcadence)): rcadence[j] += rcadence[j-1]
            rtime = np.append(rtime,rtime[-1*len(g)]+np.random.normal(365.25,10.)+np.append(0.,rcadence))
        ttmp,mtmp,BA_disp = calc_disp_delay(Aflux[g],Bflux[g],ltime[g],ltime[g],Aerr[g],Berr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta,output=2,outfile='/home/rumbaugh/EVLA/light_curves/Dispersions/Disp_grid_out.%s.delta_%.1f_%s.dat'%(lens,delta,date))
        
