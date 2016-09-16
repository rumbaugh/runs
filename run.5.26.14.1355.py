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

date = '5.26.14'

try:
    ntrials
except NameError:
    ntrials = 10000
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
lens = 'B0712'
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
    g = np.where((fluxA > 0)&(fluxB>0)&(Aerr > 0)&(Berr>0))[0]
    gEVLA = np.arange(len(g))
    
    if source == 'B0712':
        days,flux_arr,flux_err_arr = LoadVLA_2001(lens='0712')
        tfluxA1,tfluxA2,tfluxB = flux_arr[0],flux_arr[1],flux_arr[2]
        tAerr1,tAerr2,tBerr = flux_err_arr[0],flux_err_arr[1],flux_err_arr[2]
        ltime = np.append(days,ltime+1000)
        fluxA,fluxB = np.append(tfluxA1+tfluxA2,fluxA),np.append(tfluxB,fluxB)
        Aerr,Berr = np.append(np.sqrt(tAerr1**2+tAerr2**2),Aerr),np.append(tBerr,Berr)

    g = np.where((fluxA > 0)&(fluxB>0)&(Aerr > 0)&(Berr>0))[0]
    gVLA = np.arange(len(g)-len(gEVLA))+len(gEVLA)
    fluxA,fluxB,Aerr,Berr,ltime = fluxA[g],fluxB[g],Aerr[g],Berr[g],ltime[g]
    #print np.mean(fluxA[g])/np.mean(fluxB[g])
    #print np.mean(fluxA[g[2:8]])/np.mean(fluxB[g[2:8]])
delta=10.5
FILE = open('/home/rumbaugh/output.disp_sim.%s_jointfit.%s.dat'%(lens,date),'w')
st = time.time()
for i in range(0,ntrials):
    g_R_VLA = np.arange(len(gVLA))
    rAVLA = np.random.normal(0,1.,len(g_R_VLA))*Aerr[gVLA]
    np.random.shuffle(g_R_VLA)
    g2_R_VLA = np.arange(len(gVLA))
    rBVLA = np.random.normal(0,1.,len(g2_R_VLA))*Berr[gVLA]
    np.random.shuffle(g2_R_VLA)
    g_R_EVLA = np.arange(len(gEVLA))
    rAEVLA = np.random.normal(0,1.,len(g_R_EVLA))*Aerr[gEVLA]
    np.random.shuffle(g_R_EVLA)
    g2_R_EVLA = np.arange(len(gEVLA))
    rBEVLA = np.random.normal(0,1.,len(g2_R_EVLA))*Berr[gEVLA]
    np.random.shuffle(g2_R_EVLA)
    randfluxA,randfluxB = np.append(fluxA[gEVLA[g_R_EVLA]]+rAEVLA[g_R_EVLA],fluxA[gVLA[g_R_VLA]]+rAVLA[g_R_VLA]),np.append(fluxB[gEVLA[g2_R_EVLA]]+rBEVLA[g2_R_EVLA],fluxB[gVLA[g2_R_VLA]]+rBVLA[g2_R_VLA])
    randerrA,randerrB = np.append(Aerr[gEVLA[g_R_EVLA]],Aerr[gVLA[g_R_VLA]]),np.append(Berr[gEVLA[g_R_EVLA]],Berr[gVLA[g_R_VLA]])
    ttmp,mtmp,BA_disp = calc_disp_delay(randfluxB,randfluxA,ltime,ltime,randerrB,randerrA,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2a',delta,output=2,verbose=False)
    FILE.write('%E %f\n'%(BA_disp,mtmp))
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
