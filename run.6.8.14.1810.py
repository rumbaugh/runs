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

date = '6.8.14'

try:
    runs
except NameError:
    runs = 10

execfile("/home/rumbaugh/LoadEVLA_2011.py")

for lens in ['1938']:
    crS = LoadEVLA_2011('B1938',normalize=True)
    crS['day'] -= crS['day'][0]
    ltime = crS['day']
    rms = crS['rms']
    fluxratio_err = 0.0048

    imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
    errnames = ['errC1','errC2','errB','errA']
    fluxC1 = crS[imgnames[0]]
    C1err = crS[errnames[0]]
    fluxC2 = crS[imgnames[1]]
    C2err = crS[errnames[1]]
    fluxC = fluxC1+fluxC2
    Cerr = np.sqrt(C1err**2+C2err**2)
    fluxB = crS[imgnames[2]]
    Berr = crS[errnames[2]]
    Cflux,Bflux=fluxC,fluxB
    g = np.where((fluxC1 > 0) & (fluxC2 > 0) & (Bflux > 0) & (Cerr > 0) & (Berr > 0))[0]

    st = time.time()#/86400
#find time delays
    #g = np.arange(len(ltime))[:len(ltime)-10]
    #gsb = np.where(ltime[1:]-ltime[:-1] > 30)[0]
    #gsb = np.sort(np.append(gsb,gsb+1))
    #seasonbounds = np.append(0,np.append(gsb,len(ltime)-1))
    #seasonlengths = ltime[seasonbounds[2*np.arange(len(seasonbounds)/2)+1]]-ltime[seasonbounds[2*np.arange(len(seasonbounds)/2)]]
    maxtime = int(0.75*np.max(ltime))
    mintime = -1*maxtime
    tau_init,mu_init = 0.,np.mean(Cflux[g])/np.mean(Bflux[g])
    ndim,nwalkers = 2,10
    if lens == '1938':
        maxtimestep = 60.
    else:
        maxtimestep = 105.
    maxtime,mintime = 60.,-60.
    p0 = np.zeros((nwalkers,ndim))
    p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
    sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[Cflux[g],Bflux[g],Cerr[g],Berr[g],ltime[g],mu_init,mintime,maxtime,False,True,True,'interp',10.,0.5,None])
    print maxtime,mintime
    pos,prob,state=sampler.run_mcmc(p0,100)
    sampler.reset()
    pos,prob,state=sampler.run_mcmc(pos,runs)
    if runs < 50: 
        FILE = open('/home/rumbaugh/EVLA/light_curves/Dispersions/test.%s.emcee_output_full_chain_interp_bs.%s.dat'%(lens,date),'w')
    else:
        FILE = open('/home/rumbaugh/EVLA/light_curves/Dispersions/%s.emcee_output_full_chain_interp_bs.%s.dat'%(lens,date),'w')
    for i in range(0,runs):
        for j in range(0,nwalkers):
            FILE.write('%f %f\n'%(sampler.chain[j,i,0],sampler.chain[j,i,1]))
    FILE.close()
    print '\n\nAll Done! Elapsed time: %.0f seconds\n'%(time.time()-st)

