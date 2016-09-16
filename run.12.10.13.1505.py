import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm
import time

st = time.time()

try:
    runs
except NameError:
    runs = 1000

try:
    date
except NameError:
    date = '12.10.13'

try:
    maxmuratio
except NameError:
    maxmuratio = 0.5

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

def delaylnprob(x,A,B,A_err,B_err,ltime,mu_init,maxtime=30,mintime=0,t_grid_spacing=0.5,smooth_param=10.):
    #x is a vector with x[0] = tau and x[1] = mu
    muoutrange = False
    #if np.fabs(x[1]/mu_init-1) > maxmuratio: muoutrange = True
    if np.fabs(x[1]/mu_init-1) > maxmuratio: muoutrange = True
    if ((x[0] > maxtime) | (x[0] < mintime)):
        #print x[0],x[1],np.log(0.00001)
        return -9999999999.
        #FILE.write('%f %f %f %f\n'%(x[0],x[1],0.0,-9999999999.))
    elif muoutrange:
        return -9999999999.
    else:
        if x[0] < 0:
            gltime = np.where(ltime < ltime.max()+x[0])[0]
        else:
            gltime = np.where(ltime > x[0])[0]
        Btmp,Berrtmp = B.copy()*x[1],B_err.copy()*x[1]
        smB,smB_var = sm.boxcar(ltime+x[0],Btmp,ltime[gltime],smooth_param,y_var=Berrtmp*Berrtmp)
        chisq_tmp = calc_chi_squared(smB,A[gltime],A_err[gltime]*A_err[gltime]+smB_var)
        Neff = (ltime[len(ltime)-1]-np.abs(x[0]))/3.7
        #print x[0],x[1],Neff,-1.*(chisq_tmp/Neff)
        #FILE.write('%f %f %f %f\n'%(x[0],x[1],Neff,-1.*(chisq_tmp/Neff)))
        return -1.*(chisq_tmp/Neff)

cr = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/tdc1_rung0_quad_pair6A.txt')
ltime,A,B,Aerr,Berr = cr[:,0],cr[:,1],cr[:,3],cr[:,2],cr[:,4]

tau_init,mu_init = 15.,np.mean(B)/np.mean(A)

ndim,nwalkers = 2,10
p0 = np.zeros((nwalkers,ndim))
p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[B,A,Berr,Aerr,ltime,mu_init])
#pos,prob,state=sampler.run_mcmc(p0,runs)
pos,prob,state=sampler.run_mcmc(p0,100)
sampler.reset()
pos,prob,state=sampler.run_mcmc(pos,runs)
tau_sort = np.sort(sampler.flatchain[:,0])
FILE = open('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/emcee/tdc1_rung0_quad_pair6A.emcee_output_hist_tau.%s.dat'%date,'w')
for i in range(0,len(tau_sort)): FILE.write(str(sampler.flatchain[:,0][i]) + '\n')
FILE.close()
print 'BA delay tau range: %f,%f,%f'%(np.median(tau_sort),tau_sort[int(0.16*len(tau_sort))],tau_sort[int(0.84*len(tau_sort))])
py.hist(sampler.flatchain[:,0])
py.savefig('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/emcee/tdc1_rung0_quad_pair6A.emcee_output_hist_tau.BA_delay.%s.ps'%(date))
py.close()
    #py.plot(sampler.flatchain[:,1])
    #py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_chain_plot_mu1.B%s_delay.%s.ps'%(lens2_names[i],date))
    #py.close()
    #py.plot(sampler.flatchain[:,2])
    #py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_chain_plot_mu2.B%s_delay.%s.ps'%(lens2_names[i],date))
    #py.close()
    #py.plot(sampler.flatchain[:,3])
    #py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_chain_plot_mu3.B%s_delay.%s.ps'%(lens2_names[i],date))
    #py.close()
    #py.plot(sampler.flatchain[:,0])
    #py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_chain_plot_tau.B%s_delay.%s.ps'%(lens2_names[i],date))
    #py.close()
    #for j in range(0,nwalkers):
    #    py.plot(sampler.chain[j,:,0])
    #    py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_all_chain_plot_tau.B%s_delay.%s.ps'%(lens2_names[i],date))
    #py.close()
    #for k in range(1,4):
    #    for j in range(0,nwalkers):
    #        py.plot(sampler.chain[j,:,k])
    #        py.savefig('/home/rumbaugh/B1608_files/B1608.emcee_output_all_chain_plot_mu%i.B%s_delay.%s.ps'%(k,lens2_names[i],date))
    #    py.close()
    #for j in range(0,len(sampler.flatchain[:,0])): FILE.write('%f %f %f\n'%(sampler.flatchain[j,0],sampler.flatchain[j,1],sampler.flatlnprobability[j]))
    #sampler.reset()
#FILE.close()

print '\n\nAll Done! Elapsed time: %.0f seconds\n'%(time.time()-st)
