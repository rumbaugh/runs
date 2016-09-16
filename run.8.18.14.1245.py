import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
import emcee
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

execfile('/home/rumbaugh/MCMC_delaylnprob.py')
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

date = '8.18.14'

try:
    runs
except NameError:
    runs = 10

execfile("/home/rumbaugh/LoadVLA_2001.py")

for lens in ['1030','0712']:
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
    g = np.arange(len(ltime))[:len(ltime)-10]
    #gsb = np.where(ltime[g][1:]-ltime[g][:-1] > 30)[0]
    #gsb = np.sort(np.append(gsb,gsb+1))
    #seasonbounds = np.append(0,np.append(gsb,len(ltime[g])-1))
    #seasonlengths = ltime[g][seasonbounds[2*np.arange(len(seasonbounds)/2)+1]]-ltime[g][seasonbounds[2*np.arange(len(seasonbounds)/2)]]
    maxtime = int(0.75*np.max(ltime[g]))
    mintime = -1*maxtime
    tau_init,mu_init = 50.,np.mean(Bflux[g])/np.mean(Aflux[g])
    ndim,nwalkers = 2,10
    if lens == '1938':
        maxtimestep = 60.
    else:
        maxtimestep = 105.
    maxtime,mintime = 105.,-105.
    p0 = np.zeros((nwalkers,ndim))
    p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
    sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[Bflux[g],Aflux[g],2*Berr[g],2*Aerr[g],ltime[g],mu_init,mintime,maxtime,False,True,True,'interp',10.,0.5,None])
    print maxtime,mintime
    pos,prob,state=sampler.run_mcmc(p0,100)
    sampler.reset()
    pos,prob,state=sampler.run_mcmc(pos,runs)
    if runs < 50: 
        FILE = open('/home/rumbaugh/EVLA/light_curves/Dispersions/test.%s.emcee_output_full_chain_interp_bs.2Xerr.%s.dat'%(lens,date),'w')
    else:
        FILE = open('/home/rumbaugh/EVLA/light_curves/Dispersions/%s.emcee_output_full_chain_interp_bs.2Xerr.%s.dat'%(lens,date),'w')
    for i in range(0,runs):
        for j in range(0,nwalkers):
            FILE.write('%f %f\n'%(sampler.chain[j,i,0],sampler.chain[j,i,1]))
    FILE.close()
    print '\n\nAll Done! Elapsed time: %.0f seconds\n'%(time.time()-st)

