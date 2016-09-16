import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm

try:
    runs
except NameError:
    runs = 10

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

def delaylnprob(x,A,B,A_err,B_err,ltime,maxtime=60,t_grid_spacing=0.5,smooth_param=10.):
    #x is a vector with x[0] = tau and x[1] = mu
    if ((x[0] > maxtime) | (x[0] < -1*maxtime)):
        print x[0],x[1],np.log(0.00001)
        return np.log(0.00001)
    else:
        grid_spaces = int((np.max(ltime)-np.min(ltime)-np.abs(x[0]))/t_grid_spacing)+2
        t_grid = (np.arange(grid_spaces)-1)*t_grid_spacing
        if x[0] > 0: t_grid += x[0]
        if x[0] < 0:
            gltime = np.where(ltime < ltime.max()-x[0])
        else:
            gltime = np.where(ltime > x[0])
        gltime = gltime[0]
        smB,smB_var = sm.boxcar(ltime+x[0],B*x[1],ltime[gltime],smooth_param,y_var=x[1]*x[1]*B_err*B_err)
        chisq_tmp = calc_chi_squared(smB,A[gltime],A_err[gltime]*A_err[gltime]+smB_var)
        Neff = (ltime[len(ltime)-1]-np.abs(x[0]))/3.7
        print x[0],x[1],Neff,np.log(chisq_tmp/Neff)
        return np.log(1.0/(chisq_tmp/Neff))

load1608 = np.loadtxt('/home/rumbaugh/B1938+666_files/1608_g.ab922_nh')
ltime = load1608[:,0].copy()
Aflux,Bflux,Cflux,Dflux,Aerr,Berr,Cerr,Derr = load1608[:,1].copy(),load1608[:,2].copy(),load1608[:,3].copy(),load1608[:,4].copy(),load1608[:,5].copy(),load1608[:,6].copy(),load1608[:,7].copy(),load1608[:,8].copy()

ndim,nwalkers = 2,10
ltime -= ltime[0]
p0 = np.zeros((nwalkers,ndim))
p0[:,0],p0[:,1] = np.ones(nwalkers)*36.5+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*1.03083+np.random.normal(scale=0.01,size=nwalkers)
sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[Cflux,Bflux,Cerr,Berr,ltime])
sampler.run_mcmc(p0,runs)
