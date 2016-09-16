import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm
import time

st = time.time()

try:
    runs
except NameError:
    runs = 10

try:
    date
except NameError:
    date = '1.30.13'

try:
    maxmuratio
except NameError:
    maxmuratio = 0.5

try:
    nwalkers
except NameError:
    nwalkers = 10

execfile('/home/rumbaugh/MCMC_delaylnprob.py')

cr = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/tdc1_rung0_quad_pair6A.txt')
ltime,A,B,Aerr,Berr = cr[:,0],cr[:,1],cr[:,3],cr[:,2],cr[:,4]
#crl = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/emcee/tdc1_rung0_quad_pair6A.emcee_output_hist_tau.%s.dat'%date)
tau_init,mu_init = 15.,np.mean(B)/np.mean(A)

ndim,nwalkers = 2,nwalkers#phil made me do this
#p0 = crl[np.shape(crl)-10:,:]
p0 = np.zeros((nwalkers,ndim))
p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[B,A,Berr,Aerr,ltime,mu_init,0,30])
pos,prob,state=sampler.run_mcmc(p0,runs)
#pos,prob,state=sampler.run_mcmc(p0,100)
#sampler.reset()
#pos,prob,state=sampler.run_mcmc(pos,runs)
tau_sort = np.sort(sampler.flatchain[:,0])
FILE = open('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/emcee/tdc1_rung0_quad_pair6A.emcee_output_hist_tau.%s.dat'%date,'w')
#for i in range(0,len(tau_sort)): FILE.write(str(sampler.flatchain[:,0][i]) + '\n')
for i in range(0,runs):
    for j in range(0,nwalkers):
        FILE.write('%f %f\n'%(sampler.chain[j,i,0],sampler.chain[j,i,1]))
FILE.close()

print '\n\nAll Done! Elapsed time: %.0f seconds\n'%(time.time()-st)
exit
