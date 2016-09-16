import carmcmc as cm
import numpy as np
import matplotlib.pyplot as plt
import emcee
execfile('/home/rumbaugh/MCMC_delaylnprob.py')
execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')

oneminussigma = 0.317310507863

date = '1.19.15'
p=5
try:
    runs
except NameError:
    runs = 10

try:
    ntrials
except NameError:
    ntrials=10

execfile('/home/rumbaugh/LoadVLA_2001.py')

def setup_t(ny=50,dt_low=1.,dt_hi=7.5,seasons=2,sgap=465.):
    t=np.zeros(0)
    for s in range(0,seasons):
        dt=np.random.uniform(dt_low,dt_hi,ny)
        ttmp=np.cumsum(dt)
        ttmp-=ttmp[0]
        t = np.append(t,ttmp+(s+1)*(sgap+np.random.normal(0,1)))
    return t

def exp_carmapack(t,lag=0,mu=1.,sigmay=25.,p=5,mn=100.,qpo_width=np.array([1.0/100.0, 1.0/300.0, 1.0/200.0]),qpo_cent=np.array([1.0/100.0, 1.0/500.0]),ma_coefs=np.array([1.0, 4.5, 1.25, 0.0, 0.0])):
    ar_roots = cm.get_ar_roots(qpo_width, qpo_cent) # compute the roots r_k from the Lorentzian function parameters
    ar_coefs = np.poly(ar_roots)
    # convert CARMA model variance to variance in the driving white noise
    sigsqr = sigmay ** 2 / cm.carma_variance(1.0, ar_roots, ma_coefs=ma_coefs)  # carma_variance computes the autcovariance function
    t2=t+lag
    t_comb = np.append(t,t2)
    g_sort = np.argsort(t_comb)
    #print np.min(t_comb[g_sort[1:]]-t_comb[g_sort[:-1]])
    flags_arr = np.append(np.zeros(len(t)),np.ones(len(t2)))[g_sort]
    g_t,g_t2 = np.where(flags_arr==0)[0],np.where(flags_arr==1)[0]
    cmp_tmp=mn+cm.carma_process(t_comb[g_sort],sigsqr,ar_roots,ma_coefs=ma_coefs)
    #print t_comb[g_sort],t_comb[g_sort][g_t],t_comb[g_sort][g_t2],cmp_tmp
    #print cmp_tmp
    y,y2=cmp_tmp[g_t],mu*cmp_tmp[g_t2]
    return y,y2

carma_params = {'1030': {'minflux': 300, 'maxflux': 400, 'sigmay': 25., 'minmu': 12.35, 'maxmu': 12.8, 'avgerr': [1.9,0.16], 'errstd': [0.075, 0.006], 'mintau': 80, 'maxtau': 150, 'imgs': ['A','B']},'0712':{'minflux': 21, 'maxflux': 27, 'sigmay': 1., 'minmu': 4.266, 'maxmu': 4.48, 'avgerr': [0.09,0.03], 'errstd': [0.03, 0.0011], 'mintau': 5, 'maxtau': 50, 'imgs': ['A+B','C']}} 

proot = '/home/rumbaugh/sim_ltcurve_testing/VLA/plots'

def sim_lc(lens):
    days,flux,ferr=LoadVLA_2001(lens)
    days = (days-days[0])#/86400
    gd = np.arange(len(days))[:len(days)-10]
    fA,fB,Aerr,Berr = flux[0],flux[1],ferr[0],ferr[1]
    if lens == '0712':
        fA,fB,Aerr,Berr = flux[0]+flux[1],flux[2],np.sqrt(ferr[0]**2+ferr[1]**2),ferr[2]
    days,fA,fB,Aerr,Berr=days[gd],fA[gd],fB[gd],Aerr[gd],Berr[gd]
    minflux,maxflux,sigmay,minmu,maxmu,avgerr,errstd,mintau,maxtau = carma_params[lens]['minflux'],carma_params[lens]['maxflux'],carma_params[lens]['sigmay'],carma_params[lens]['minmu'],carma_params[lens]['maxmu'],carma_params[lens]['avgerr'],carma_params[lens]['errstd'],carma_params[lens]['mintau'],carma_params[lens]['maxtau']
    mn = np.random.uniform(minflux,maxflux)
    mu = 1./np.random.uniform(minmu,maxmu)
    nanflag=True
    while nanflag:
        t = setup_t(seasons=5)
        lag = np.random.uniform(mintau,maxtau)
        if lens == '1030': lag*=-1
        y,y2=exp_carmapack(t,lag,mu,sigmay,p,mn)
        cmp_tmp=np.append(y,y2)
        nanflag=np.isnan(np.sum(cmp_tmp))
    print lens,mu,lag
    #days_t = np.append(days,t+1000)
    #flux_t = np.append(fA,y)
    #flux_t2 = np.append(fB,y2)
    days_t = t-t[0]
    flux_t = y
    flux_t2 = y2
    plt.clf()
    plt.plot(days_t,flux_t,'k')
    plt.plot(days_t,flux_t,'b.')
    plt.xlabel('Time (days)')
    plt.ylabel('Image %s Flux'%carma_params[lens]['imgs'][0])
    #plt.savefig('%s/sim_lc_noerr.%s_%s.%s.png'%(proot,lens,carma_params[lens]['imgs'][0],date))
    plt.clf()
    plt.plot(days_t,flux_t2,'k')
    plt.plot(days_t,flux_t2,'b.')
    plt.xlabel('Time (days)')
    plt.ylabel('Image %s Flux'%carma_params[lens]['imgs'][1])
    #plt.savefig('%s/sim_lc_noerr.%s_%s.%s.png'%(proot,lens,carma_params[lens]['imgs'][1],date))
    err1,err2 = np.random.normal(avgerr[0],errstd[0],len(t)),np.random.normal(avgerr[1],errstd[1],len(t))
    while(len(np.where(err1<=0)[0])>0):
        g = np.where(err1<=0)[0]
        err1[g] = np.random.normal(avgerr[0],errstd[0],len(g))
    while(len(np.where(err2<=0)[0])>0):
        g = np.where(err2<=0)[0]
        err2[g] = np.random.normal(avgerr[1],errstd[1],len(g))
    ey1,ey2 = y+np.random.normal(np.zeros(len(t)),err1),y2+np.random.normal(np.zeros(len(t)),err2)
    #eflux_t1,eflux_t2 = np.append(fA,ey1),np.append(fB,ey2)
    #flux_err1,flux_err2 = np.append(Aerr,err1),np.append(Berr,err2)
    eflux_t1,eflux_t2 = ey1,ey2
    flux_err1,flux_err2 = err1,err2
    plt.clf()
    plt.errorbar(days_t,eflux_t1,yerr=flux_err1,color='b',fmt='ro',lw=1,capsize=3,mew=1)
    plt.plot(days_t,eflux_t1,'k')
    plt.plot(days_t,eflux_t1,'b.')
    plt.xlabel('Time (days)')
    plt.ylabel('Image %s Flux'%carma_params[lens]['imgs'][0])
    #plt.savefig('%s/sim_lc.%s_%s.%s.png'%(proot,lens,carma_params[lens]['imgs'][0],date))
    plt.clf()
    plt.errorbar(days_t,eflux_t2,yerr=flux_err2,color='b',fmt='ro',lw=1,capsize=3,mew=1)
    plt.plot(days_t,eflux_t2,'k')
    plt.plot(days_t,eflux_t2,'b.')
    plt.xlabel('Time (days)')
    plt.ylabel('Image %s Flux'%carma_params[lens]['imgs'][1])
    #plt.savefig('%s/sim_lc.%s_%s.%s.png'%(proot,lens,carma_params[lens]['imgs'][1],date))
    maxtime = int(0.75*np.max(days))
    mintime = -1*maxtime
    tau_init,mu_init = 50.,np.mean(eflux_t2)/np.mean(eflux_t1)
    ndim,nwalkers = 2,20
    if lens == '1938':
        maxtimestep = 60.
    else:
        maxtimestep = 155.
    maxtime,mintime = 155.,-155.
    if lens == '0712':  maxtime,mintime = 105.,-105.
    p0 = np.zeros((nwalkers,ndim))
    p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
    sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[eflux_t2,eflux_t1,flux_err2,flux_err1,days_t,mu_init,mintime,maxtime,False,True,True,'interp',10.,0.5,None])
    pos,prob,state=sampler.run_mcmc(p0,100)
    sampler.reset()
    pos,prob,state=sampler.run_mcmc(pos,runs)
    tmp_srt_chain_tau,tmp_srt_chain_mu = np.sort(sampler.flatchain[:,0]),np.sort(sampler.flatchain[:,1])
    tau_trials,tau_err_trials,mu_trials,mu_err_trials = np.median(tmp_srt_chain_tau),0.5*(tmp_srt_chain_tau[int(runs*10*(1-oneminussigma/2))]-tmp_srt_chain_tau[int(oneminussigma/2*runs*10)]),np.median(tmp_srt_chain_mu),0.5*(tmp_srt_chain_mu[int(runs*10*(1-oneminussigma/2))]-tmp_srt_chain_mu[int(oneminussigma/2*runs*10)])
    mu_true = mu
    tau,mu = sampler.flatchain[:,0],sampler.flatchain[:,1]
    if lens == '0712': tau *= -1
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    hist2d(tau,1./mu,V=np.array([0.682689,0.9545,0.9973]))#, extent=[extents[j], extents[i]],
    if lens == '1030': lag *= -1
    plt.axvline(lag)
    plt.axhline(1./mu_true)
    plt.xlabel('Time Delay (days)',fontsize=14)
    plt.ylabel('Magnification',fontsize=14)
    plt.savefig('%s/only_sim_tau.onetrial.%s.chisq_conplot.interp.triangle_mod_plot.%s.png'%(proot,lens,date))
    
    
for lens in ('0712','1030'):
    sim_lc(lens)
