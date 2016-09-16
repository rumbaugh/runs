import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm
import sys

try:
    runs
except NameError:
    runs = 10000


try:
    nwalkers
except NameError:
    nwalkers = 10

try:
    maxtime
except NameError:
    maxtime = 100


try:
    date
except NameError:
    date = '4.23.13'

try:
    maxmuratio
except NameError:
    maxmuratio = 0.2

def find_middle(arr):
    #only works if arr is monotonically increasing
    middle = 0.5*(np.max(arr)+np.min(arr))
    higher,lower = arr[arr > middle][np.argsort(arr[arr > middle])[0]],arr[arr <= middle][np.argsort(arr[arr <= middle])[len(arr[arr <= middle])-1]]
    if np.fabs(higher-middle) < np.fabs(lower-middle):
        return len(lower)
    else:
        return len(lower)-1
    

def calc_chi_squared(obs,exp,var,nozero=True):
    if ((len(obs) != len(exp)) | (len(obs) != len(var))): sys.exit("Inputs to calc_chi_squared must have same length: %i,%i,%i,%i"%(len(obs),len(exp),len(x_grid),len(var)))
    if nozero:
        gcs = np.where((var > 0) & (obs != 0) & (exp != 0))
    else:
        gcs = np.where((var > 0))
    gcs = gcs[0]
    if len(gcs) == 0: sys.exit("Calc_chi_squared failure: var is zero everywhere")
    chi_sq = np.sum((obs[gcs]-exp[gcs])*(obs[gcs]-exp[gcs])/var[gcs])
    return chi_sq

#FILE = open('/home/rumbaugh/BDemceetest.3.5.13.txt','w')

def delaylnprob(x,A,B,A_err,B_err,ltime,numbelow,numabove,tau0,smooth_param=10.):
    #x is a vector with x[0] = tau and x[1,2,3] = mu1,2,3 for the 3 seasons of data
    muoutrange = False
    #for im in range(0,3):
    #    if np.fabs(x[im+1]/mu_init_dict[im+1][idelay]-1) > maxmuratio: muoutrange = True
    if ((x[0] > tau0+maxtime) | (x[0] < tau0-maxtime)):
        #print x[0],x[1],np.log(0.00001)
        return -9999999999.
        #FILE.write('%f %f %f %f\n'%(x[0],x[1],0.0,-9999999999.))
    elif muoutrange:
        return -9999999999.
    else:
        if x[0] < 0:
            midpoint1,midpoint2,midpoint3 = 0.5*(ltime1.max()+ltime1.min()-x[0]),0.5*(ltime2.max()+ltime2.min()-x[0]),0.5*(ltime3.max()+ltime3.min()-x[0])
        else:
            midpoint1,midpoint2,midpoint3 = 0.5*(ltime1.max()+ltime1.min()+x[0]),0.5*(ltime2.max()+ltime2.min()+x[0]),0.5*(ltime3.max()+ltime3.min()+x[0])
        gmp1above,gmp2above,gmp3above = np.where(ltime1 > midpoint1)[0],np.where(ltime2 > midpoint2)[0],np.where(ltime3 > midpoint3)[0]
        gmp1below,gmp2below,gmp3below = np.where(ltime1 < midpoint1)[0],np.where(ltime2 > midpoint2)[0],np.where(ltime3 > midpoint3)[0]
        gltime1,gltime2,gltime3 = np.append(gmp1below[len(gmp1below)-numbelow[0]:len(gmp1below)],gmp1above[0:numabove[0]]+len(gmp1below)),np.append(gmp2below[len(gmp2below)-numbelow[1]:len(gmp2below)],gmp2above[0:numabove[1]]+len(gmp2below)),np.append(gmp3below[len(gmp3below)-numbelow[2]:len(gmp3below)],gmp3above[0:numabove[2]]+len(gmp3below))
        gltime = np.append(gltime1,np.append(gltime2,gltime3))
        Btmp,Berrtmp = B.copy(),B_err.copy()
        Btmp *= x[1]
        Berrtmp *= x[1]
        smB,smB_var = sm.boxcar(ltime+x[0],Btmp,ltime[gltime],smooth_param,y_var=Berrtmp*Berrtmp)
        chisq_tmp = calc_chi_squared(smB,A[gltime],A_err[gltime]*A_err[gltime]+smB_var)
        Neff = len(ltime)-x[0]
        #print x[0],x[1],Neff,-1.*(chisq_tmp/Neff)
        #FILE.write('%f %f %f %f\n'%(x[0],x[1],Neff,-1.*(chisq_tmp/Neff)))
        return -1.*(chisq_tmp)

load1608_1 = np.loadtxt('/home/rumbaugh/B1608_files/1608_season1.dat')
ltime1_orig = load1608_1[:,0].copy()
Aflux1,Bflux1,Cflux1,Dflux1,Aerr1,Berr1,Cerr1,Derr1 = load1608_1[:,1].copy(),load1608_1[:,2].copy(),load1608_1[:,3].copy(),load1608_1[:,4].copy(),load1608_1[:,5].copy(),load1608_1[:,6].copy(),load1608_1[:,7].copy(),load1608_1[:,8].copy()
season1len = len(ltime1_orig)
load1608_2 = np.loadtxt('/home/rumbaugh/B1938+666_files/1608_season2.dat')
ltime2_orig = load1608_2[:,0].copy()
Aflux2,Bflux2,Cflux2,Dflux2,Aerr2,Berr2,Cerr2,Derr2 = load1608_2[:,1].copy(),load1608_2[:,2].copy(),load1608_2[:,3].copy(),load1608_2[:,4].copy(),load1608_2[:,5].copy(),load1608_2[:,6].copy(),load1608_2[:,7].copy(),load1608_2[:,8].copy()
season2len = len(ltime2_orig)
load1608_3 = np.loadtxt('/home/rumbaugh/B1938+666_files/1608_g.ab922_nh')
ltime3_orig = load1608_3[:,0].copy()
Aflux3,Bflux3,Cflux3,Dflux3,Aerr3,Berr3,Cerr3,Derr3 = load1608_3[:,1].copy(),load1608_3[:,2].copy(),load1608_3[:,3].copy(),load1608_3[:,4].copy(),load1608_3[:,5].copy(),load1608_3[:,6].copy(),load1608_3[:,7].copy(),load1608_3[:,8].copy()
season3len = len(ltime3_orig)

ltime1,ltime2,ltime3 = ltime1_orig - ltime1_orig[0],ltime2_orig - ltime1_orig[0],ltime3_orig - ltime1_orig[0]

tau_init,mu3_init = np.array([31.5,36.5,75.]),np.array([2.0124,1.03083,0.3471])
#tau_init,mu3_init = np.array([40.3,36.5,85.5]),np.array([2.0124,1.03083,0.3471])

ltime = np.append(ltime1,np.append(ltime2,ltime3))
Aflux,Bflux,Cflux,Dflux = np.append(Aflux1,np.append(Aflux2,Aflux3)),np.append(Bflux1,np.append(Bflux2,Bflux3)),np.append(Cflux1,np.append(Cflux2,Cflux3)),np.append(Dflux1,np.append(Dflux2,Dflux3))
Aerr,Berr,Cerr,Derr = np.append(Aerr1,np.append(Aerr2,Aerr3)),np.append(Berr1,np.append(Berr2,Berr3)),np.append(Cerr1,np.append(Cerr2,Cerr3)),np.append(Derr1,np.append(Derr2,Derr3))

mu1_init,mu2_init = np.zeros(3),np.zeros(3)
fluxes_dict = {'A': {0: Aflux, 1: Aflux1, 2: Aflux2, 3: Aflux3}, 'B': {0: Bflux, 1: Bflux1, 2: Bflux2, 3: Bflux3}, 'C': {0: Cflux, 1: Cflux1, 2: Cflux2, 3: Cflux3}, 'D': {0: Dflux, 1: Dflux1, 2: Dflux2, 3: Dflux3}, 1: {0: Aflux, 1: Aflux1, 2: Aflux2, 3: Aflux3}, 0: {0: Bflux, 1: Bflux1, 2: Bflux2, 3: Bflux3}, 2: {0: Cflux, 1: Cflux1, 2: Cflux2, 3: Cflux3}, 3: {0: Dflux, 1: Dflux1, 2: Dflux2, 3: Dflux3}}
errs_dict = {'A': {0: Aerr, 1: Aerr1, 2: Aerr2, 3: Aerr3}, 'B': {0: Berr, 1: Berr1, 2: Berr2, 3: Berr3}, 'C': {0: Cerr, 1: Cerr1, 2: Cerr2, 3: Cerr3}, 'D': {0: Derr, 1: Derr1, 2: Derr2, 3: Derr3}, 1: {0: Aerr, 1: Aerr1, 2: Aerr2, 3: Aerr3}, 0: {0: Berr, 1: Berr1, 2: Berr2, 3: Berr3}, 2: {0: Cerr, 1: Cerr1, 2: Cerr2, 3: Cerr3}, 3: {0: Derr, 1: Derr1, 2: Derr2, 3: Derr3}}
ltime_dict = {'rel': {0: ltime, 1: ltime1, 2: ltime2, 3: ltime3}, 'orig': {1: ltime1_orig, 2: ltime2_orig, 3: ltime3_orig}}
mu_init_dict = {1: mu1_init,2: mu2_init,3: mu3_init}

for i in range(0,3):
    for j in range(0,2):
        gacd,gb = np.where(ltime_dict['rel'][j+1]-ltime_dict['rel'][j+1][0] > tau_init[i]),np.where(ltime_dict['rel'][j+1] < ltime_dict['rel'][j+1][len(ltime_dict['rel'][j+1])-1] - tau_init[i])
        gacd,gb = gacd[0],gb[0]
        mean_b_tmp,mean_acd_tmp = np.mean(fluxes_dict['B'][j+1][gb]),np.mean(fluxes_dict[i+1][j+1][gacd])
        mu_init_dict[j+1][i] = mean_acd_tmp/mean_b_tmp

lens2_names = np.array(['A','C','D'])
lens2_fluxes = np.array([Aflux,Cflux,Dflux])
lens2_errs = np.array([Aerr,Cerr,Derr])
for i in range(0,3):
    ndim = 4
    p0 = np.zeros((nwalkers,ndim))
    p0[:,0],p0[:,1],p0[:,2],p0[:,3] = np.ones(nwalkers)*tau_init[i]+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu1_init[i]+np.random.normal(scale=0.01,size=nwalkers),np.ones(nwalkers)*mu2_init[i]+np.random.normal(scale=0.01,size=nwalkers),np.ones(nwalkers)*mu3_init[i]+np.random.normal(scale=0.01,size=nwalkers)
    maxoffset = maxtime
    numbelow,numabove = np.zeros(3),np.zeros(3)
    for j in range(0,3):
        arr_tmp_maxtrials_below = ltime_dict['rel'][j][ltime_dict['rel'][j] < ltime_dict['rel'][j].max()-maxoffset]
        arr_tmp_maxtrials_above = ltime_dict['rel'][j][ltime_dict['rel'][j] > maxoffset]
        maxbelow,maxabove = len(arr_tmp_maxtrials_below),len(arr_tmp_maxtrials_above)
        if maxbelow < maxabove:
            numbelow[j],numabove[j] = len(arr_tmp_maxtrials_below[arr_tmp_maxtrials_below < 0.5*(np.max(arr_tmp_maxtrials_below)+np.min(arr_tmp_maxtrials_below))]),len(arr_tmp_maxtrials_below[arr_tmp_maxtrials_below > 0.5*(np.max(arr_tmp_maxtrials_below)+np.min(arr_tmp_maxtrials_below))])
        else:
            numbelow[j],numabove[j] = len(arr_tmp_maxtrials_above[arr_tmp_maxtrials_above < 0.5*(np.max(arr_tmp_maxtrials_above)+np.min(arr_tmp_maxtrials_above))]),len(arr_tmp_maxtrials_above[arr_tmp_maxtrials_above > 0.5*(np.max(arr_tmp_maxtrials_above)+np.min(arr_tmp_maxtrials_above))])
    if i != 0: sampler.reset()
    sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[fluxes_dict[i+1][0],Bflux,lens2_errs[i],Berr,ltime,numbelow,numabove,tau_init[i]])
    #pos,prob,state=sampler.run_mcmc(p0,runs)
    pos,prob,state=sampler.run_mcmc(p0,100)
    sampler.reset()
    pos,prob,state=sampler.run_mcmc(pos,runs)
    tau_sort = np.sort(sampler.flatchain[:,0])
    print 'B%s delay tau range: %f,%f,%f'%(lens2_names[i],np.median(tau_sort),tau_sort[int(0.16*len(tau_sort))],tau_sort[int(0.84*len(tau_sort))])
    py.hist(sampler.flatchain[:,0])
    py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_hist_tau.B%s_delay.%s.ps'%(lens2_names[i],date))
    py.close()
    py.plot(sampler.flatchain[:,1])
    py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_chain_plot_mu1.B%s_delay.%s.ps'%(lens2_names[i],date))
    py.close()
    py.plot(sampler.flatchain[:,2])
    py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_chain_plot_mu2.B%s_delay.%s.ps'%(lens2_names[i],date))
    py.close()
    py.plot(sampler.flatchain[:,3])
    py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_chain_plot_mu3.B%s_delay.%s.ps'%(lens2_names[i],date))
    py.close()
    py.plot(sampler.flatchain[:,0])
    py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_chain_plot_tau.B%s_delay.%s.ps'%(lens2_names[i],date))
    py.close()
    for j in range(0,nwalkers):
        py.plot(sampler.chain[j,:,0])
        py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_all_chain_plot_tau.B%s_delay.%s.ps'%(lens2_names[i],date))
    py.close()
    for k in range(1,4):
        for j in range(0,nwalkers):
            py.plot(sampler.chain[j,:,k])
            py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_all_chain_plot_mu%i.B%s_delay.%s.ps'%(k,lens2_names[i],date))
        py.close()
    py.scatter(sampler.flatchain[:,0],sampler.flatlnprobability)
    py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_tau-prob_scatter.B%s_delay.%s.ps'%(lens2_names[i],date))
    py.close()
    #for j in range(0,len(sampler.flatchain[:,0])): FILE.write('%f %f %f\n'%(sampler.flatchain[j,0],sampler.flatchain[j,1],sampler.flatlnprobability[j]))
    #sampler.reset()
#FILE.close()
