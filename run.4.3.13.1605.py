import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm
import os,errno

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: 
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

try:
    runs
except NameError:
    runs = 1000

try:
    date
except NameError:
    date = '4.3.13'

try:
    useseasons
except NameError:
    useseasons = np.arange(10)+1

try:
    nwalkers
except NameError:
    nwalkers = 30

try:
    tau_init
except NameError:
    tau_init = 0.0

try:
    nwalkers_tau_init_scale
except NameError:
    nwalkers_tau_init_scale = 0.1
try:
    nwalkers_mu_init_scale
except NameError:
    nwalkers_mu_init_scale = 0.01

try:
    burnin
except NameError:
    burnin = True

seasons_dict = {1: {'Beg': 0, 'End': 119}, 2: {'Beg': 371, 'End': 483}, 3: {'Beg': 735, 'End': 847}, 4: {'Beg': 1099, 'End': 1211}, 5: {'Beg': 1463, 'End': 1575}, 6: {'Beg': 1827, 'End': 1939}, 7: {'Beg': 2191, 'End': 2393}, 8: {'Beg': 2555, 'End': 2674}, 9: {'Beg': 2926, 'End': 3038}, 10: {'Beg': 3290, 'End': 3402}}

mu_init_dict = dict(zip(useseasons,np.ones(len(useseasons))))

def calc_chi_squared(obs,exp,var,nozero=True):
    if ((len(obs) != len(exp)) | (len(obs) != len(var))): sys.exit("Inputs to calc_chi_squared must have same length: %i,%i,%i,%i"%(len(obs),len(exp),len(x_grid),len(var)))
    if nozero:
        gcs = np.where((var > 0) & (obs != 0) & (var != 0))
    else:
        gcs = np.where((var > 0))
    gcs = gcs[0]
    if len(gcs) == 0: sys.exit("Calc_chi_squared failure: var is zero everywhere")
    chi_sq = np.sum((obs[gcs]-exp[gcs])*(obs[gcs]-exp[gcs])/var[gcs])
    return chi_sq

#FILE = open('/home/rumbaugh/BDemceetest.3.5.13.txt','w')

def delaylnprob(x,A,B,A_err,B_err,ltime,maxtime=60,mintime=None,t_grid_spacing=0.5,smooth_param=10.):
    #x is a vector with x[0] = tau and x[1,2,3] = mu1,2,3 for the 3 seasons of data
    if mintime == None: mintime = -1*maxtime
    if ((x[0] > maxtime) | (x[0] < mintime)):
        #print x[0],x[1],np.log(0.00001)
        return -9999999999.
        #FILE.write('%f %f %f %f\n'%(x[0],x[1],0.0,-9999999999.))
    else:
        goverlap_dict = 
        if x[0] < 0:
            gltime1,gltime2,gltime3 = np.where(ltime1 < ltime.max()+x[0]),np.where(ltime2 < ltime.max()+x[0]),np.where(ltime3 < ltime.max()+x[0])
        else:
            gltime1,gltime2,gltime3 = np.where(ltime1 > x[0]),np.where(ltime2 > x[0]),np.where(ltime3 > x[0])
        gltime1,gltime2,gltime3 = gltime1[0],gltime2[0],gltime3[0]
        gltime = np.append(gltime1,np.append(gltime2+season1len,gltime3+season1len+season2len))
        if ((len(gltime1) <= 3) | (len(gltime2) <= 3) | (len(gltime3) <= 3)): print "Short gltime: %i %i %i"%(len(gltim1),len(gltime2),len(gltime3))
        Btmp,Berrtmp = B.copy(),B_err.copy()
        Btmp[0:season1len] *= x[1]
        Btmp[season1len:season1len+season2len] *= x[2]
        Btmp[season2len:season1len+season2len+season3len] *= x[3]
        Berrtmp[0:season1len] *= x[1]
        Berrtmp[season1len:season1len+season2len] *= x[2]
        Berrtmp[season2len:season1len+season2len+season3len] *= x[3]
        smB,smB_var = sm.boxcar(ltime+x[0],Btmp,np.append(ltime1[gltime1],np.append(ltime2[gltime2],ltime3[gltime3])),smooth_param,y_var=Berrtmp*Berrtmp)
        chisq_tmp = calc_chi_squared(smB,A[gltime],A_err[gltime]*A_err[gltime]+smB_var)
        Neff = (ltime[len(ltime)-1]-np.abs(x[0]))/3.7
        #print x[0],x[1],Neff,-1.*(chisq_tmp/Neff)
        #FILE.write('%f %f %f %f\n'%(x[0],x[1],Neff,-1.*(chisq_tmp/Neff)))
        return -1.*(chisq_tmp/Neff)

loadfile = np.loadtxt('/home/rumbaugh/time_delay_files/lc_test_chris_v2.txt')
ltime,Aflux,Aerr,Bflux,Berr = loadfile[:,0],loadfile[:,1],loadfile[:,2],loadfile[:,3],loadfile[:,4]

gseason_dict = dict(zip(useseasons,np.array([np.zeros(1,dtype='int')]*10)))

for i in range(0,len(useseasons)):
    gmu_tmp = np.where((ltime > seasons_dict[useseasons[i]]['Beg']-0.1) & (ltime < seasons_dict[useseasons[i]]['End']+0.1))
    gmu_tmp = gmu_tmp[0]
    gseason_dict[useseasons[i]] = gmu_tmp
    mu_init_dict[useseasons[i]] = np.mean(Aflux[gmu_tmp])/np.mean(Bflux[gmu_tmp])

ndim,nwalkers = len(useseasons)+1,nwalkers
p0 = np.zeros((nwalkers,ndim))
p0[:,0] = np.ones(nwalkers)*tau_init+np.random.normal(scale=nwalkers_tau_init_scale,size=nwalkers)
for i in range(0,len(useseasons)): p0[:,i+1] = np.ones(nwalkers)*mu_init_dict[useseasons[i]]+np.random.normal(scale=nwalkers_mu_init_scale,size=nwalkers)
sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[Aflux,Bflux,Aerr,Berr,ltime])
if burnin:
    pos,prob,state=sampler.run_mcmc(p0,100)
    sampler.reset()
    pos,prob,state=sampler.run_mcmc(pos,runs)
else:
    pos,prob,state=sampler.run_mcmc(p0,runs)

mkdir_p('/home/rumbaugh/time_delay_files/plots.%s'%date)

tau_sort = np.sort(sampler.flatchain[:,0])
print 'BA test delay tau range: %f,%f,%f'%(np.median(tau_sort),tau_sort[int(0.16*len(tau_sort))],tau_sort[int(0.84*len(tau_sort))])
py.hist(sampler.flatchain[:,0])
py.savefig('/home/rumbaugh/time_delay_files/plots.%s/testcurve.emcee_output_hist_tau.BA_delay.%s.ps'%(date,date))
py.close()
for i in range(0,len(useseasons)):
    py.plot(sampler.flatchain[:,i+1])
    py.savefig('/home/rumbaugh/time_delay_files/plots.%s/testcurve.emcee_output_chain_plot_mu%i.BA_delay.%s.ps'%(date,useseasons[i],date))
    py.close()
py.plot(sampler.flatchain[:,0])
py.savefig('/home/rumbaugh/time_delay_files/plots.%s/testcurve.emcee_output_chain_plot_tau.BA_delay.%s.ps'%(date,date))
py.close()
for j in range(0,nwalkers):
    py.plot(sampler.chain[j,:,0])
    py.savefig('/home/rumbaugh/time_delay_files/plots.%s/testcurve.emcee_output_all_chain_plot_tau.BA_delay.%s.ps'%(date,date))
    py.close()
for k in range(0,len(useseasons)):
    for j in range(0,nwalkers):
        py.plot(sampler.chain[j,:,k+1])
        py.savefig('/home/rumbaugh/time_delay_files/plots.%s/testcurve.emcee_output_all_chain_plot_mu%i.BA_delay.%s.ps'%(date,useseasons[k],date))
    py.close()
