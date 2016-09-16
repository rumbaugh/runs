import carmcmc as cm
import numpy as np
import matplotlib.pyplot as plt
import emcee
import smoothing_1d as sm
execfile('/home/rumbaugh/MCMC_delaylnprob.py')
execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')
execfile("/home/rumbaugh/Dispersion.py")

oneminussigma = 0.317310507863

try:
    opt
except NameError:
    opt=False

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

delta=10.5

date = '1.21.15'
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

carma_params = {'1030': {'minflux': 300, 'maxflux': 400, 'sigmay': 25., 'min_mu': 12.35, 'max_mu': 12.8, 'avgerr': [1.9,0.16], 'errstd': [0.075, 0.006], 'mintau': 80, 'maxtau': 150, 'imgs': ['A','B']},'0712':{'minflux': 21, 'maxflux': 27, 'sigmay': 1., 'min_mu': 4.266, 'max_mu': 4.48, 'avgerr': [0.09,0.03], 'errstd': [0.03, 0.0011], 'mintau': 5, 'maxtau': 50, 'imgs': ['A+B','C']}} 

proot = '/home/rumbaugh/sim_ltcurve_testing/VLA/plots'

def sim_lc(lens):
    days,flux,ferr=LoadVLA_2001(lens)
    days = (days-days[0])#/86400
    gd = np.arange(len(days))[:len(days)-10]
    fA,fB,Aerr,Berr = flux[0],flux[1],ferr[0],ferr[1]
    if lens == '0712':
        fA,fB,Aerr,Berr = flux[0]+flux[1],flux[2],np.sqrt(ferr[0]**2+ferr[1]**2),ferr[2]
    days,fA,fB,Aerr,Berr=days[gd],fA[gd],fB[gd],Aerr[gd],Berr[gd]
    minflux,maxflux,sigmay,min_mu,max_mu,avgerr,errstd,mintau,maxtau = carma_params[lens]['minflux'],carma_params[lens]['maxflux'],carma_params[lens]['sigmay'],carma_params[lens]['min_mu'],carma_params[lens]['max_mu'],carma_params[lens]['avgerr'],carma_params[lens]['errstd'],carma_params[lens]['mintau'],carma_params[lens]['maxtau']
    mn = np.random.uniform(minflux,maxflux)
    mu = 1./np.random.uniform(min_mu,max_mu)
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
    plt.savefig('%s/sim_lc_noerr.%s_%s.tau_%.1f.%s.png'%(proot,lens,carma_params[lens]['imgs'][0],np.abs(lag),date))
    plt.clf()
    plt.plot(days_t,flux_t2,'k')
    plt.plot(days_t,flux_t2,'b.')
    plt.xlabel('Time (days)')
    plt.ylabel('Image %s Flux'%carma_params[lens]['imgs'][1])
    plt.savefig('%s/sim_lc_noerr.%s_%s.tau_%.1f.%s.png'%(proot,lens,carma_params[lens]['imgs'][1],np.abs(lag),date))
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
    eflux_t1,eflux_t2 = y,y2
    flux_err1,flux_err2 = err1,err2

    maxtime = int(0.75*np.max(days))
    mintime = -1*maxtime
    tau_init,mu_init = 50.,np.mean(eflux_t2)/np.mean(eflux_t1)
    ndim,nwalkers = 2,10
    if lens == '1938':
        maxtimestep = 60.
    else:
        maxtimestep = 155.
    maxtime,mintime = 155.,-155.
    if lens == '0712':  maxtime,mintime = 105.,-105.
    ttmp,mtmp,BA_disp = calc_disp_delay(eflux_t1,eflux_t2,days_t,days_t,flux_err1,flux_err2,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta,output=2,opt=opt,outfile='%s/../Disp_grid_out.%s.delta_10.5_%s.dat'%(proot,lens,date))
    print mtmp,mu,np.mean(y)/np.mean(y2)
    print ttmp,lag
    t2=t+lag
    t_comb = np.append(t,t2)
    g_sort = np.argsort(t_comb)
    flags_arr = np.append(np.zeros(len(t)),np.ones(len(t2)))[g_sort]
    g_t,g_t2 = np.where(flags_arr==0)[0],np.where(flags_arr==1)[0]
    comp_lc = np.append(eflux_t1,eflux_t2*mtmp)[g_sort]
    #print comp_lc
    t_comb = t_comb[g_sort]
    master_lc = sm.vw_boxcar(t_comb,comp_lc,t_comb,5,variance_weighting=False,output_var=False)
    #print master_lc
    diff_lc1,diff_lc2 = np.abs(master_lc[g_t]-eflux_t1),np.abs(master_lc[g_t2]/mtmp-eflux_t2)
    #print diff_lc1,diff_lc2
    test_ttmps,test_mtmps=np.zeros(ntrials),np.zeros(ntrials)
    maxtime=ttmp+50
    if lens=='0712': mintime=ttmp-50
    print mintime,maxtime
    for n in range(0,ntrials):
        test_y,test_y2 = master_lc[g_t]+np.random.normal(np.zeros(len(g_t)),diff_lc1),(master_lc[g_t2]/mtmp+np.random.normal(np.zeros(len(g_t2)),diff_lc2))
        test_ttmps[n],test_mtmps[n],BA_disp = calc_disp_delay(test_y,test_y2,days_t,days_t,flux_err1,flux_err2,maxtime,timestep,minmu,maxmu,mustep,'D_4_2',delta,output=2,mintime=mintime)#,outfile='%s/../Disp_grid_out.%s.delta_10.5_%s.dat'%(proot,lens,date))
    if ntrials > 0:
        sort_tau,sort_mu = np.sort(test_ttmps),np.sort(test_mtmps)
        tau_err = 0.5*(sort_tau[int(ntrials*(1-0.5*oneminussigma))]-sort_tau[int(ntrials*0.5*oneminussigma)])
        mu_err = 0.5*(sort_mu[int(ntrials*(1-0.5*oneminussigma))]-sort_mu[int(ntrials*0.5*oneminussigma)])
        print '\n%s:\nTime Delay = %5.1f +/- %f\nMagnification = %6.3f +/- %7.3f\n\n'%(lens,ttmp,tau_err,mtmp,mu_err)
        print test_ttmps,test_mtmps
        FILE=open('%s/../sim_test_out.%s.%s.dat'%(proot,lens,date),'w')
        FILE.write('#tau_true  tau_out  tau_err  mu_true  mu_out  mu_err\n')
        FILE.write('%7.2f %6.1f %7.2f %7.3f %7.3f %7.3f\n'%(lag,ttmp,tau_err,mu,mtmp,mu_err))
        FILE.close()
    
for lens in ('0712','1030'):
    sim_lc(lens)

    infile = '%s/../Disp_grid_out.%s.delta_10.5_%s.dat'%(proot,lens,date)
    cr = np.loadtxt(infile)
    tau,mu,disp = -1*cr[:,0],cr[:,1],cr[:,2]
    len_mu = len(tau[tau==tau[0]])
    len_tau = len(mu[mu==mu[0]])
    Z = np.reshape(disp,(len_tau,len_mu))
    Ztau = np.reshape(tau,(len_tau,len_mu))[:,0]
    Zmu = np.reshape(mu,(len_tau,len_mu))[0]
    #try:
    #    V
    #except NameError:
    #if lens == '1030':
    #    V = np.array([75,110,160,250,400])
    #elif lens == '0712':
    #    V = np.array([0.45,0.6,0.9,1.3])
    V = np.exp(np.arange(8)/8.*(np.log(np.max(Z))-np.log(np.min(Z)))*0.95+np.log(np.min(Z)*1.05))
    print V
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.contour(Ztau,Zmu,np.transpose(Z),V,colors='k')
    plt.ylabel('Magnification')
    plt.xlabel('Time Delay (days)')
    plt.fontsize = 14
    plt.savefig('%s/Disp.con_plot.%s.delta_10.5_%s.png'%(proot,lens,date))
    xl,xm = plt.xlim()
    yl,ym = plt.ylim()
