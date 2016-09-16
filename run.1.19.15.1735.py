import numpy as np
import matplotlib.pyplot as plt
import emcee
execfile('/home/rumbaugh/MCMC_delaylnprob.py')
execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')

oneminussigma = 0.317310507863

proot = '/home/rumbaugh/sim_ltcurve_testing/VLA/plots'
date = '1.19.15'

try:
    runs
except NameError:
    runs = 10

try:
    ntrials
except NameError:
    ntrials=10

#try:
#    mu,lag
#except NameError:
mu,lag = 0.817,234.4

try:
    dpts
except NameError:
    dpts = 1000

dt = np.random.uniform(1.,7.5,dpts)
ttmp=np.cumsum(dt)
t=ttmp-ttmp[0]
tmax = t[-1]
scaleF = 3./tmax
y,y2=((t-0.5*tmax)*scaleF)**3-(t-0.5*tmax)*scaleF+10,mu*(((t+lag-0.5*tmax)*scaleF)**3-(t+lag-0.5*tmax)*scaleF+10)
yerr = np.ones(len(t))*0.01
maxtime = int(0.75*tmax)
mintime = -1*maxtime
tau_init,mu_init = 200.,np.mean(y2)/np.mean(y)
ndim,nwalkers = 2,10
p0 = np.zeros((nwalkers,ndim))
p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[y2,y,yerr,yerr,t,mu_init,mintime,maxtime,False,True,True,'interp',10.,0.5,None])
pos,prob,state=sampler.run_mcmc(p0,100)
sampler.reset()
pos,prob,state=sampler.run_mcmc(pos,runs)
tmp_srt_chain_tau,tmp_srt_chain_mu = np.sort(sampler.flatchain[:,0]),np.sort(sampler.flatchain[:,1])
tau_trials,tau_err_trials,mu_trials,mu_err_trials = np.median(tmp_srt_chain_tau),0.5*(tmp_srt_chain_tau[int(runs*10*(1-oneminussigma/2))]-tmp_srt_chain_tau[int(oneminussigma/2*runs*10)]),np.median(tmp_srt_chain_mu),0.5*(tmp_srt_chain_mu[int(runs*10*(1-oneminussigma/2))]-tmp_srt_chain_mu[int(oneminussigma/2*runs*10)])
mu_true = mu

tau,mu = sampler.flatchain[:,0],sampler.flatchain[:,1]
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
hist2d(tau,1./mu,V=np.array([0.682689,0.9545,0.9973]))#, extent=[extents[j], extents[i]],
plt.axvline(lag)
plt.axhline(1./mu_true)
plt.xlabel('Time Delay (days)',fontsize=14)
plt.ylabel('Magnification',fontsize=14)
plt.savefig('%s/test_sim_tau.onetrial.chisq_conplot.interp.triangle_mod_plot.%s.png'%(proot,date))
