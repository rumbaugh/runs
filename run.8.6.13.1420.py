import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm
import spec_simple as ss

try:
    runs
except NameError:
    runs = 1000

try:
    date
except NameError:
    date = '8.6.13'

try:
    maxmuratio
except NameError:
    maxmuratio = 0.2

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

def gausslnprob(x,flux,flux_var,w,p_init):
    #x is a vector with x[0] = sigma and x[1,2,3] = mean,norm, and continumm level
    if ((x[1] > (p_init[1]+p_init[0])) | (x[1] < (p_init[1]-p_init[0]))):
        return -9999999999.
    elif ((x[0] < 0.5) | (x[0] > 5)):
        return -9999999999.
    elif ((x[2] > 20) | (x[2] < 5)):
        return -9999999999.
    elif ((x[3] > 6) | (x[3] < 4.5)):
        return -9999999999.
    else:
        testf = x[3] + x[2]*np.exp((w-x[1])**2/(2.*x[0]**2))
        chisq_tmp = calc_chi_squared(flux,testf,flux_var)
        return -1.*(chisq_tmp/len(flux))

mask,slit,color,side,line = '1131m2_v2','600','red','top',1
indir = '/mnt/data2/rumbaugh/LRIS/2011_01/reduced/%s'%(mask)
plotfile,title = '%s/spec_output/outspec.%s_%s_%s_%s_coadd_bgsub.dat'%(indir,mask,slit,color,side),'%s %s %s %s'%(mask,slit,color,side)
w,f,v = ss.read_spectrum(plotfile,line=line)
g = np.where((w > 5756) & (w < 5783))[0]
p_init = np.array([3.,5771.,6.5,5.5])
ndim,nwalkers = 4,10
p0 = np.zeros((nwalkers,ndim))
p0[:,0],p0[:,1],p0[:,2],p0[:,3] = np.ones(nwalkers)*p_init[0]+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*p_init[1]+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*p_init[2]+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*p_init[3]+np.random.normal(scale=0.1,size=nwalkers)
sampler = emcee.EnsembleSampler(nwalkers,ndim,gausslnprob,args=[f[g],v[g],w[g],p_init])
#pos,prob,state=sampler.run_mcmc(p0,runs)
pos,prob,state=sampler.run_mcmc(p0,100)
sampler.reset()
pos,prob,state=sampler.run_mcmc(pos,runs)
sig_sort = np.sort(sampler.flatchain[:,0])
mean_sort = np.sort(sampler.flatchain[:,1])
norm_sort = np.sort(sampler.flatchain[:,2])
bkg_sort = np.sort(sampler.flatchain[:,3])
print '%s slit %s %s %s'%(mask,slit,color,side)
print 'H-delta sigma range: %f,%f,%f'%(np.median(sig_sort),sig_sort[int(0.16*len(sig_sort))],sig_sort[int(0.84*len(sig_sort))])
py.figure(1)
py.hist(sampler.flatchain[:,0])
py.title('Sigma Distribution')
py.savefig('%s/plots/%s_%s_%s_%s.emcee_output_hist_sig.%s.ps'%(indir,mask,slit,color,side,date))
py.figure(2)
py.hist(sampler.flatchain[:,1]-5771)
py.title('Mean Distribution-5771')
py.savefig('%s/plots/%s_%s_%s_%s.emcee_output_hist_mean.%s.ps'%(indir,mask,slit,color,side,date))
py.figure(3)
py.hist(sampler.flatchain[:,2])
py.title('Norm Distribution')
py.savefig('%s/plots/%s_%s_%s_%s.emcee_output_hist_norm.%s.ps'%(indir,mask,slit,color,side,date))
py.figure(4)
py.hist(sampler.flatchain[:,3])
py.title('Background Distribution')
py.savefig('%s/plots/%s_%s_%s_%s.emcee_output_hist_bkg.%s.ps'%(indir,mask,slit,color,side,date))
py.figure(5)
ss.smooth_boxcar(plotfile,7,varwt=True,title=title,line=line,output=False,clear=True)
py.xlim(5756,5783)
py.ylim(4,13)
py.plot(w[g],np.median(bkg_sort)+np.median(norm_sort)*np.exp(-(w[g]-np.median(mean_sort))**2/(2*np.median(sig_sort)**2)))
py.savefig('%s/plots/%s_%s_%s_%s.emcee_output_lineplot.%s.ps'%(indir,mask,slit,color,side,date))
