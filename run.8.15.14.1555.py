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

date = '8.15.14'
FILE = open('/home/rumbaugh/EVLA/light_curves/flux_ratios_EVLA.8.15.14.dat','w')


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
    maxtimes
except NameError:
    maxtime = 60
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

def iter_fluxratio(Aflux,Bflux,ltime,maxtime,timestep):
    steps = 2*(int(np.floor(maxtime/timestep)))+1
    BA_FR_arr = np.zeros(steps)
    for tau,i in zip((np.arange(steps)-steps/2)*timestep,np.arange(steps)):
        if tau > 0:
            overlapA,overlapB = np.where(ltime+tau<np.max(ltime))[0],np.where(ltime>tau+np.min(ltime))[0]
        elif tau < 0:
            overlapA,overlapB = np.where(ltime+tau>np.min(ltime))[0],np.where(ltime<np.max(ltime)+tau)[0]
        else:
            overlapA,overlapB = np.arange(len(ltime)),np.arange(len(ltime))
        BA_FR_arr[i] = np.mean(Aflux[overlapA])/np.mean(Bflux[overlapB])
    return BA_FR_arr

for source in ['MG0414','B0712','B1938']:
    crS = LoadEVLA_2011(source,normalize=True)
    crS['day'] -= crS['day'][0]
    ltime = crS['day']
    rms = crS['rms']
    fluxratio_err = 0.0043
    if source == 'MG0414':
        fluxratio_err = 0.0048
        imgnames = ['fluxA1','fluxA2','fluxB','fluxC']
        nimg = 4
    if source == 'B1938':
        fluxratio_err = 0.0048
        imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
        nimg = 3
    if source == 'B0712':
        imgnames = ['fluxA','fluxB','fluxC','fluxD']
        nimg = 3
    errnames,imgshnames = np.copy(imgnames),np.copy(imgnames)
    for n in np.arange(0,len(errnames)): 
        errnames[n] = 'err%s'%errnames[n][4:]
        imgshnames[n] = '%s'%imgshnames[n][4:]
    if source == 'B1938': imgshnames = np.append('C',imgshnames[2:])
    if source == 'B0712': imgshnames = np.append('(A+B)',imgshnames[2:])
    fluxA1 = crS[imgnames[0]]
    A1err = crS[errnames[0]]
    fluxA2 = crS[imgnames[1]]
    A2err = crS[errnames[1]]
    fluxA = fluxA1+fluxA2
    Aerr = np.sqrt(A1err**2+A2err**2)
    fluxB = crS[imgnames[2]]
    Berr = crS[errnames[2]]
    
    #if source == 'B0712':
    #    days,flux_arr,flux_err_arr = LoadVLA_2001(lens='0712')
    #    tfluxA1,tfluxA2,tfluxB,tfluxC = flux_arr[0],flux_arr[1],flux_arr[2],flux_arr[3]
    #    tAerr1,tAerr2,tBerr,tCerr = flux_err_arr[0],flux_err_arr[1],flux_err_arr[2],flux_err_arr[3]
    #    ltime = np.append(days,ltime+1000)
    #    fluxA,fluxB = np.append(tfluxA1+tfluxA2,fluxA),np.append(tfluxB,fluxB)
    #    Aerr,Berr = np.append(np.sqrt(tAerr1**2+tAerr2**2),Aerr),np.append(tBerr,Berr)
    if source == 'MG0414':
        fluxA,Aerr = fluxA1,A1err
    compimg = 'B'
    if source == 'B0712': compimg='C'
    g = np.where((fluxA > 0)&(fluxB>0)&(Aerr > 0)&(Berr>0))[0]
    print '%s\n\n%s%s: %f\n'%(source,compimg,imgshnames[0],np.mean(fluxA[g])/np.mean(fluxB[g]))
    BA_FR_arr = iter_fluxratio(fluxA[g],fluxB[g],ltime[g],maxtime,timestep)
    sarr = np.sort(BA_FR_arr)
    FILE.write('%6s %s%2s  %f %f\n'%(source,compimg,imgshnames[0],np.mean(fluxA[g])/np.mean(fluxB[g]),np.max(BA_FR_arr)-np.min(BA_FR_arr)))
    for img,imgname in zip(np.array(imgnames[5-nimg:])[imgshnames[1:]!=compimg],imgshnames[1:][imgshnames[1:]!=compimg]):
        fluxA = crS[img]
        Aerr = crS[img]
        #if source == 'B0712':
        #    fluxA = np.append(tfluxC,fluxA)
        #    Aerr = np.append(tCerr,Aerr)
        g = np.where((fluxA > 0)&(fluxB>0)&(Aerr > 0)&(Berr>0))[0]
        BA_FR_arr = iter_fluxratio(fluxA[g],fluxB[g],ltime[g],maxtime,timestep)
        sarr = np.sort(BA_FR_arr)
        FILE.write('%6s %s%2s  %f %f\n'%(source,compimg,imgname,np.mean(fluxA[g])/np.mean(fluxB[g]),np.max(BA_FR_arr)-np.min(BA_FR_arr)))
        print '%s%s: %f\n'%(compimg,imgname,np.mean(fluxA[g])/np.mean(fluxB[g]))
FILE.close()
