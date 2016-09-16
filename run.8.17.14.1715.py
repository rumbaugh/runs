import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
import emcee
execfile('/home/rumbaugh/LoadEVLA_2011.py')
execfile('/home/rumbaugh/LoadVLA_2001.py')
execfile("/home/rumbaugh/arrconv.py")
execfile('/home/rumbaugh/MCMC_delaylnprob.py')

date = '8.17.14'

try:
    runs
except NameError:
    runs = 10000
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
        gB = np.arange(len(ltime))[:-9]
        tfluxA1,tfluxA2,tfluxB,tAerr1,tAerr2,tBerr,ltime = tfluxA1[gB],tfluxA2[gB],tfluxB[gB],tAerr1[gB],tAerr2[gB],tBerr[gB],ltime[gB]
        ltime = np.append(days,ltime+1000)
        fluxA,fluxB = np.append(tfluxA1+tfluxA2,fluxA),np.append(tfluxB,fluxB)
        Aerr,Berr = np.append(np.sqrt(tAerr1**2+tAerr2**2),Aerr),np.append(tBerr,Berr)

    g = np.where((fluxA > 0)&(fluxB>0)&(Aerr > 0)&(Berr>0))[0]
    gVLA = np.arange(len(g)-len(gEVLA))+len(gEVLA)
    gsb = np.where(ltime[g][1:]-ltime[g][:-1] > 30)[0]
    gsb = np.sort(np.append(gsb,gsb+1))
    seasonbounds = np.append(0,np.append(gsb,len(g)-1))
    slengths = np.average(ltime[g][seasonbounds[np.arange(len(seasonbounds)/2)*2+1]]-ltime[g][seasonbounds[np.arange(len(seasonbounds)/2)*2]])
    #print np.mean(fluxA[g])/np.mean(fluxB[g])
    #print np.mean(fluxA[g[2:8]])/np.mean(fluxB[g[2:8]])
    tau_init,mu_init = 0.,np.mean(fluxA[g])/np.mean(fluxB[g])
    ndim,nwalkers = 2,10
    maxtime,mintime = 60.,-60.
    p0 = np.zeros((nwalkers,ndim))
    p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
    sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[fluxA[g],fluxB[g],Aerr[g],Berr[g],ltime[g],mu_init,mintime,maxtime,False,True,True,'interp',10.,0.5,seasonbounds])
    pos,prob,state=sampler.run_mcmc(p0,100)
    sampler.reset()
    pos,prob,state=sampler.run_mcmc(pos,runs)
    if runs < 50: 
        FILE = open('/home/rumbaugh/EVLA/light_curves/Dispersions/test.%s_jointfit.emcee_output_full_chain_interp_bs.%s.dat'%(lens,date),'w')
    else:
        FILE = open('/home/rumbaugh/EVLA/light_curves/Dispersions/%s_jointfit.emcee_output_full_chain_interp_bs.%s.dat'%(lens,date),'w')
    for i in range(0,runs):
        for j in range(0,nwalkers):
            FILE.write('%f %f\n'%(sampler.chain[j,i,0],sampler.chain[j,i,1]))
    FILE.close()
