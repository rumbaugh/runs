import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
import emcee
execfile("/home/rumbaugh/arrconv.py")

execfile("/home/rumbaugh/chi_squared_min.py")
execfile('/home/rumbaugh/MCMC_delaylnprob.py')

try:
    runs
except NameError:
    runs = 10

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

st = time.time()

for pair in range(1,2):
    cr = np.loadtxt('/home/rumbaugh/sim_ltcurve_testing/Nickrung0/Nickrung0_pair%i.txt'%pair)
    ltime,A,Aerr,B,Berr = cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]
    ltime -= ltime[0]
    maxtimestep = int(0.5*(ltime[-1]-ltime[0]))
    if maxtimestep < 60: maxtimestep = 60
    maxtime,mintime = maxtimestep,-1*maxtimestep
    tau_init,mu_init = 0.,np.mean(B)/np.mean(A)
    ndim,nwalkers = 2,10
    for kernel in ['interp','boxcar']:
        for use_cov_matrix in [True,False]:
            for use_Neff in [True,False]:
                p0 = np.zeros((nwalkers,ndim))
                p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
                sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[B,A,Berr,Aerr,ltime,mu_init,mintime,maxtime,use_cov_matrix,use_Neff,True,kernel])
                pos,prob,state=sampler.run_mcmc(p0,runs)
                if pair == 1: print time.time()-st
