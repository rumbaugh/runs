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
execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')

oneminussigma = 0.317310507863
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

date = '12.15.14'

try:
    runs
except NameError:
    runs = 10

try:
    ntrials
except NameError:
    ntrials=10

execfile("/home/rumbaugh/LoadVLA_2001.py")

for lens in ['0712','1030']:
    mu_trials,tau_trials,mu_err_trials,tau_err_trials = np.zeros(ntrials),np.zeros(ntrials),np.zeros(ntrials),np.zeros(ntrials)

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
        maxtimestep = 155.
    maxtime,mintime = 155.,-155.
    if lens == '0712':  maxtime,mintime = 105.,-105.
    cadence=ltime[g[1:]]-ltime[g[:-1]]
    A_avg,B_avg,Aerr_avg,Berr_avg=np.average(Aflux[g]),np.average(Bflux[g]),np.average(Aerr[g]),np.average(Berr[g])
    rtime = np.copy(ltime[g])
    rfluxA,rfluxB = np.copy(Aflux[g]),np.copy(Bflux[g])
    rerrA,rerrB = np.copy(Aerr[g]),np.copy(Berr[g])
    if lens == '0712':
        mu_true = np.random.random()*(4.475-4.425)+4.425
    else:
        mu_true = np.random.random()*(12.585-12.25)+12.25            
    for k in range(0,2):
        rcadence = np.copy(cadence)
        np.random.shuffle(rcadence)
        for j in range(1,len(rcadence)): rcadence[j] += rcadence[j-1]
        rtime = np.append(rtime,rtime[-1*len(g)]+np.random.normal(365.25,10.)+np.append(0.,rcadence))
        taavg = 0.
        while taavg < 0.1*A_avg: taavg = np.random.normal(A_avg,0.1*A_avg)
        tfluxA,tfluxB = np.ones(len(g))*taavg+np.random.normal(0.,Aerr_avg*taavg/A_avg),np.ones(len(g))*taavg/mu_true+np.random.normal(0.,Berr_avg*taavg/A_avg/mu_true)
        rfluxA,rfluxB = np.append(rfluxA,tfluxA),np.append(rfluxB,tfluxB)
        terrA,terrB = np.copy(Aerr[g]),np.copy(Berr[g])
        np.random.shuffle(terrA),np.random.shuffle(terrB)
        rerrA,rerrB = np.append(rerrA,terrA),np.append(rerrB,terrB)
    p0 = np.zeros((nwalkers,ndim))
    p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
    sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[rfluxB,rfluxA,rerrB,rerrA,rtime,mu_init,mintime,maxtime,False,True,True,'interp',10.,0.5,None])
    pos,prob,state=sampler.run_mcmc(p0,100)
    sampler.reset()
    pos,prob,state=sampler.run_mcmc(pos,runs)
    tmp_srt_chain_tau,tmp_srt_chain_mu = np.sort(sampler.flatchain[:,0]),np.sort(sampler.flatchain[:,1])
    tau_trials,tau_err_trials,mu_trials,mu_err_trials = np.median(tmp_srt_chain_tau),0.5*(tmp_srt_chain_tau[int(runs*10*(1-oneminussigma/2))]-tmp_srt_chain_tau[int(oneminussigma/2*runs*10)]),np.median(tmp_srt_chain_mu),0.5*(tmp_srt_chain_mu[int(runs*10*(1-oneminussigma/2))]-tmp_srt_chain_mu[int(oneminussigma/2*runs*10)])
    tau,mu = sampler.flatchain[:,0],sampler.flatchain[:,1]
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    hist2d(tau,1./mu,V=np.array([0.682689,0.9545,0.9973]))#, extent=[extents[j], extents[i]],
    plt.xlabel('Time Delay (days)',fontsize=14)
    plt.ylabel('Magnification',fontsize=14)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/simulations/flatsim.onetrial.%s.chisq_conplot.interp.triangle_mod_plot.%s.png'%(lens,date))
