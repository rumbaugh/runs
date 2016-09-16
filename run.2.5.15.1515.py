import numpy as np

oneminussigma = 0.317310507863
import matplotlib.pyplot as plt
import emcee
execfile('/home/rumbaugh/MCMC_delaylnprob.py')
execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')
execfile('Dispersion.py')
execfile('/home/rumbaugh/LoadVLA_2001.py')

try:
    runs
except NameError:
    runs = 10

fainter_plot = np.array([(1418,415),(1471,493),(1517,388),(1563,454),(1684,476),(1767,594),(1851,431),(1935,597)])

fainter_plot_err = np.array([0.5*(-385+446),0.5*(-462+523),0.5*(419-357),0.5*(484-423),0.5*(506-445),0.5*(625-563),0.5*(461-400),0.5*(627-566)])

brighter_plot = np.array([(593,354),(645,493),(690,400),(735,548),(854,442),(936,653),(1018,642),(1100,513)])

brighter_plot_err = np.array([0.5*(387-321),0.5*(526-460),0.5*(433-367),0.5*(581-515),0.5*(475-409),0.5*(686-620),0.5*(675-609),0.5*(546-480)])

fainter_plot_axes = {'y': {20: 331, 19: 516}, 'x': {280: 1449, 290: 1525, 300: 1601, 310: 1677, 320: 1753, 330: 1829, 340: 1905}}

brighter_plot_axes = {'y': {230: 340, 220: 523}, 'x': {280: 623, 290: 698, 300: 772, 310: 847, 320: 922, 330: 996, 340: 1071}}

fainter_flux = 19+(20-19)/(331.-516.)*(fainter_plot[:,1]-516.)

brighter_flux = 220+(230-220)/(340.-523.)*(brighter_plot[:,1]-523.)

ferr,berr = fainter_plot_err/(516.-331.),brighter_plot_err*10./(523.-340.)

fx,fy = fainter_plot_axes['x'].values(),fainter_plot_axes['x'].keys()
bx,by = brighter_plot_axes['x'].values(),brighter_plot_axes['x'].keys()
fA,bA = np.vstack([fx, np.ones(len(fx))]).T,np.vstack([bx, np.ones(len(bx))]).T
fm,fc = np.linalg.lstsq(fA,fy)[0]
bm,bc = np.linalg.lstsq(bA,by)[0]
ft,bt = fx*fm+fc,bx*bm+bc
ltime = 0.5*(ft+bt)



days,flux,ferr=LoadVLA_2001('1030')
days = (days-days[0])#/86400
gd = np.arange(len(days))[:len(days)-10]
fA,fB,Aerr,Berr = flux[0],flux[1],ferr[0],ferr[1]
days,fA,fB,Aerr,Berr=days[gd],fA[gd],fB[gd],Aerr[gd],Berr[gd]

days_t = np.append(days,ltime+1000)
flux_t1 = np.append(fA,brighter_flux)
flux_t2 = np.append(fB,fainter_flux)
flux_err1,flux_err2 = np.append(Aerr,berr),np.append(Berr,ferr)

tau_init,mu_init = 100.,np.mean(flux_t2)/np.mean(flux_t1)
ndim,nwalkers = 2,10
maxtime,mintime = 155.,-155.


p0 = np.zeros((nwalkers,ndim))
p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[flux_t2,flux_t1,flux_err2,flux_err1,days_t,mu_init,mintime,maxtime,False,True,True,'interp',10.,0.5,None])
pos,prob,state=sampler.run_mcmc(p0,100)
sampler.reset()
pos,prob,state=sampler.run_mcmc(pos,runs)
tmp_srt_chain_tau,tmp_srt_chain_mu = np.sort(sampler.flatchain[:,0]),np.sort(sampler.flatchain[:,1])
tau_trials,tau_err_trials,mu_trials,mu_err_trials = np.median(tmp_srt_chain_tau),0.5*(tmp_srt_chain_tau[int(runs*10*(1-oneminussigma/2))]-tmp_srt_chain_tau[int(oneminussigma/2*runs*10)]),np.median(tmp_srt_chain_mu),0.5*(tmp_srt_chain_mu[int(runs*10*(1-oneminussigma/2))]-tmp_srt_chain_mu[int(oneminussigma/2*runs*10)])

proot = '/home/rumbaugh/sim_ltcurve_testing/VLA/plots'

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
hist2d(sampler.flatchain[:,0],1./sampler.flatchain[:,1],V=np.array([0.682689,0.9545,0.9973]))#, extent=[extents[j], extents[i]],
plt.xlabel('Time Delay (days)',fontsize=14)
plt.ylabel('Magnification',fontsize=14)
plt.savefig('%s/1030_wGurkan.chisq_conplot.interp.triangle_mod_plot.png'%(proot))
