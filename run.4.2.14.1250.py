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
    runs
except NameError:
    runs = 1000

burnins = 100
if runs < 100: burnins = 1

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
    maxtimestep = 200
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9
try:
    date
except NameError:
    date = '4.2.14'

try:
    use_cov_matrix
except NameError:
    use_cov_matrix = False

try:
    delbuffer
except NameError:
    delbuffer = 30.

kernel = 'boxcar'

st = time.time()

pairs = np.array([6,26,51,101,151])

true_delays = {6: np.array([0,8.87,7.8,7.8+18.13]),\
26:    np.array([0, 11.75, 11.7, 11.7+63.08]),\
51:    np.array([48.9,  48.9+10.93,0,54.84]),\
101:   np.array([0, 19.8,  12.68,12.68+7.12]),\
151:   np.array([0, 6.56,  3.2,  3.2+20.95])}

FILE = open('/mnt/data2/rumbaugh/TDC/quadsample.4.1.14/quadtest_results_append.4.2.14.dat','w')
FILE.write('# lens imagepair delay dealy_lb delay_ub\n')
FILE.close()

for rung in range(0,1):
#for rung in range(0,5):
    pair = pairs[rung]
    crA = np.loadtxt('/mnt/data2/rumbaugh/TDC/quadsample.4.1.14/tdc1_rung%i_quad_pair%iA.txt'%(rung,pair))
    crB = np.loadtxt('/mnt/data2/rumbaugh/TDC/quadsample.4.1.14/tdc1_rung%i_quad_pair%iB.txt'%(rung,pair))
    ltime,A1,A1err,A2,A2err = crA[:,0],crA[:,1],crA[:,2],crA[:,3],crA[:,4]
    ltime,B1,B1err,B2,B2err = crB[:,0],crB[:,1],crB[:,2],crB[:,3],crB[:,4]
    ltime -= ltime[0]
    fluxdict = {'A1': A1, 'A2': A2, 'B1': B1, 'B2': B2}
    errdict = {'A1': A1err, 'A2': A2err, 'B1': B1err, 'B2': B2err}
    for img,img_i in zip(['A2','B1','B2'],np.arange(3)+1):
    #for img,img_i in zip(['A2'],np.arange(3)+1):
        tdel = true_delays[pair][img_i]-true_delays[pair][0]
        maxtime,mintime = tdel+delbuffer,tdel-delbuffer
        tau_init,mu_init = tdel,np.mean(fluxdict[img])/np.mean(A1)
        ndim,nwalkers = 2,10
        gsb = np.where(ltime[1:]-ltime[:-1] > 30)[0]
        gsb = np.sort(np.append(gsb,gsb+1))
        seasonbounds = np.append(0,np.append(gsb,len(ltime)-1))
        p0 = np.zeros((nwalkers,ndim))
        p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
        sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[A1,fluxdict[img],A1err,errdict[img],ltime,mu_init,mintime,maxtime,use_cov_matrix,True,True,kernel,10.,0.5,seasonbounds])
        pos,prob,state=sampler.run_mcmc(p0,burnins)
        sampler.reset()
        pos,prob,state=sampler.run_mcmc(pos,runs)
        if img == 'A2': print time.time()-st
        tau_sort = np.sort(sampler.flatchain[:,0])
        tau_med,tau_lb,tau_ub = np.median(tau_sort),tau_sort[int(0.31731*0.5*len(tau_sort))],tau_sort[int((1-0.31731*0.5)*len(tau_sort))]
        FILE = open('/mnt/data2/rumbaugh/TDC/quadsample.4.1.14/quadtest_results.4.2.14.dat','a')
        FILE.write('%3i A1-%2s %9.5f %9.5f %9.5f\n'%(pair,img,tau_med,tau_lb,tau_ub))
        FILE.close()
