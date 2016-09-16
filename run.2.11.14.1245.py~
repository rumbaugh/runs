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

execfile("/home/rumbaugh/chi_squared_min.py")
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

try:
    date
except NameError:
    date = '2.10.14'

try:
    runs
except NameError:
    runs = 10

if lens != '1938':
    execfile("/home/rumbaugh/LoadVLA_2001.py")
    ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)

    Aflux,Bflux = flux_arr[0],flux_arr[1]
    Aerr,Berr = flux_err_arr[0],flux_err_arr[1]

    if lens == '0712': 
        Aflux += Bflux
        Aerr = np.sqrt(Aerr**2+Berr**2)
        Bflux,Berr = flux_arr[2],flux_err_arr[2]

    ltime = (ltime-ltime[0])#/86400
    g = np.arange(len(ltime))[:len(ltime)-10]
    tau_init,mu_init = 0.,np.mean(Bflux[g])/np.mean(Aflux[g])

else:
    execfile("/home/rumbaugh/Load1938.py")
    ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()

    Cflux = C1flux+C2flux
    Cerr = np.zeros(len(Cflux))
    for i in range(0,len(Cerr)): Cerr[i] = m.sqrt((C1err[i])**2+(C2err[i])**2)
    ltime = (ltime-ltime[0])/86400
    tau_init,mu_init = 45.,np.mean(Bflux)/np.mean(Cflux)

st = time.time()

#find time delays
#maxtime = int(0.75*np.max(ltime[g]))
#mintime = -1*maxtime
ndim,nwalkers = 2,10
if lens == '1938':
    maxtimestep = 60.
else:
    maxtimestep = 105.
#maxtime,mintime = 105.,-105.
maxtime,mintime = maxtimestep,-1*maxtimestep
p0 = np.zeros((nwalkers,ndim))
p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
if lens != '1938': 
    sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[Bflux[g],Aflux[g],Berr[g],Aerr[g],ltime[g],mu_init,mintime,maxtime,True,True,True,'interpolate'])
else:
    sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[Bflux,Cflux,Berr,Cerr,ltime,mu_init,mintime,maxtime,True,True,True,'interpolate'])
pos,prob,state=sampler.run_mcmc(p0,100)
sampler.reset()
pos,prob,state=sampler.run_mcmc(pos,runs)
FILE = open('/home/rumbaugh/EVLA/light_curves/Dispersions/%s.emcee_output_full_chain_interp.%s.dat'%(lens,date),'w')
for i in range(0,runs):
    for j in range(0,nwalkers):
        FILE.write('%f %f\n'%(sampler.chain[j,i,0],sampler.chain[j,i,1]))
FILE.close()
print '\n\nAll Done! Elapsed time: %.0f seconds\n'%(time.time()-st)

