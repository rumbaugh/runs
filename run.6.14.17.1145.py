import numpy as np
import pandas as pd
import carmcmc as cm
import astroML.time_series as ts
import matplotlib.pyplot as plt


try:
    docalc
except NameError:
    docalc=True
normfrac=0.317310507863
nsample=20000
ntrials=100
LCsize=200
iLB,iUB=int(normfrac*0.5*nsample),int((1-0.5*normfrac)*nsample)

if docalc:
    true_ltaus,true_lsigs=np.random.uniform(2,4,ntrials),np.random.uniform(-1,-0.5,ntrials)

    xmean,errmean,errsig=19,0.02,0.04
    yerrs=np.random.gamma(5,errsig,((ntrials,LCsize)))
    times=np.random.uniform(50000,56000,((ntrials,LCsize)))
    times=np.sort(times,axis=1)
    
    SFinfs=np.sqrt(2)*10**true_lsigs
    #SFinfs=np.sqrt(10**true_ltaus)*10**true_lsigs

    RW_arr=np.zeros((ntrials,LCsize))
    ntrials_tmp=ntrials
    for i in range(0,ntrials):
        RW_arr[i]=ts.generate_damped_RW(times[i],tau=10**true_ltaus[i],z=0,SFinf=SFinfs[i],xmean=xmean)
    
    RW_arr+=np.random.normal(0,yerrs)
    df=pd.DataFrame({x: np.zeros(ntrials) for x in ['tau','taulb','tauub','drwvar','varlb','varub','sigma','sigmalb','sigmaub',]})
else:
    ntrials_tmp=0
for i in range(0,ntrials_tmp):
    DRWmodel=cm.CarmaModel(times[i],RW_arr[i],yerrs[i],p=1,q=0)
    DRWsample=DRWmodel.run_mcmc(nsample)
    lomega_samples,var_samples,sigma_samples=np.sort(DRWsample.get_samples('log_omega').flatten()),np.sort(DRWsample.get_samples('var').flatten()),np.sort(DRWsample.get_samples('sigma').flatten())
    lomega,drwvar,sigma=np.median(lomega_samples),np.median(var_samples),np.median(sigma_samples)
    lomegaLB,lomegaUB,varLB,varUB,sigmaLB,sigmaUB=lomega_samples[iLB],lomega_samples[iUB],var_samples[iLB],var_samples[iUB],sigma_samples[iLB],sigma_samples[iUB]
    df.iloc[i]['tau'],df.iloc[i]['drwvar'],df.iloc[i]['sigma']=np.exp(-lomega),drwvar,sigma
    df.iloc[i]['taulb'],df.iloc[i]['tauub'],df.iloc[i]['varlb'],df.iloc[i]['varub'],df.iloc[i]['sigmalb'],df.iloc[i]['sigmaub']=np.exp(-lomegaUB),np.exp(-lomegaLB),varLB,varUB,sigmaLB,sigmaUB
df['ltauub'],df['lsigmaub'],df['lvarub']=np.log10(df.tauub),np.log10(df.sigmaub),np.log10(df.varub)
df['ltaulb'],df['lsigmalb'],df['lvarlb']=np.log10(df.taulb),np.log10(df.sigmalb),np.log10(df.varlb)
df['ltau'],df['lsigma'],df['lvar']=np.log10(df.tau),np.log10(df.sigma),np.log10(df.drwvar)

df['ltau_errl'],df['lsigma_errl'],df['lvar_errl']=np.log10(df.tau)-np.log10(df.taulb),np.log10(df.sigma)-np.log10(df.sigmalb),np.log10(df.drwvar)-np.log10(df.varlb)
df['ltau_erru'],df['lsigma_erru'],df['lvar_erru']=-np.log10(df.tau)+np.log10(df.tauub),-np.log10(df.sigma)+np.log10(df.sigmaub),-np.log10(df.drwvar)+np.log10(df.varub)
xdummy=np.linspace(1,5,100)
true_taus,true_sigs=10**true_ltaus,10**true_lsigs
plt.figure(1)
plt.clf()
#plt.scatter(true_ltaus,df.ltau)
plt.errorbar(true_ltaus,df.ltau,yerr=[df.ltau_errl,df.ltau_erru],fmt='co',lw=1,capsize=2,mew=1,ms=4)
xlim=plt.xlim()
ylim=plt.ylim()
plt.plot(xdummy,xdummy,lw=2,color='k',ls='dashed')
plt.xlim(xlim[0],xlim[1])
plt.ylim(ylim[0],ylim[1])
plt.xlabel(r'log(True $\tau$ (days))')
plt.ylabel(r'log(Fit $\tau$ (days))')
plt.savefig('/home/rumbaugh/DRWmocktest.tau.png')

plt.figure(1)
plt.clf()
#plt.scatter(true_lsigs,df.lsigma,color='b',label='sig')
plt.errorbar(true_lsigs,df.lsigma,yerr=[df.lsigma_errl,df.lsigma_erru],fmt='bo',lw=1,capsize=2,mew=1,ms=4)
#plt.scatter(true_lsigs,np.log10(0.5*df.sigma.values**2*df.tau.values),color='cyan',label='sig_form')
plt.errorbar(true_lsigs,np.log10(np.sqrt(0.5*df.sigma.values**2*df.tau.values)),yerr=[np.sqrt(4*df.lsigma_errl**2+(0.5*(df.ltau_errl+df.ltau_erru))**2),np.sqrt(4*df.lsigma_erru**2+(0.5*(df.ltau_errl+df.ltau_erru))**2)],fmt='co',lw=1,capsize=2,mew=1,ms=4)
#plt.scatter(true_lsigs,df.drwvar,color='r',label='var')
plt.errorbar(true_lsigs,df.drwvar,yerr=[df.lvar_errl,df.lvar_erru],fmt='ro',lw=1,capsize=2,mew=1,ms=4)
#plt.scatter(true_lsigs,np.log10(0.5*df.drwvar.values**2*df.tau.values))#,color='orange',label='var_form')
plt.errorbar(true_lsigs,np.log10(np.sqrt(0.5*df.drwvar.values**2*df.tau.values)),yerr=[np.sqrt(4*df.lvar_errl**2+(0.5*(df.ltau_errl+df.ltau_erru))**2),np.sqrt(4*df.lvar_erru**2+(0.5*(df.ltau_errl+df.ltau_erru))**2)],fmt='ko',lw=1,capsize=2,mew=1,ms=4)
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(xlim[0],xlim[1],100)
plt.plot(xdummy,xdummy,lw=2,color='k',ls='dashed')
plt.xlim(xlim[0],xlim[1])
plt.ylim(ylim[0],ylim[1])
plt.xlabel(r'log(True $\sigma$)')
plt.ylabel(r'log(Fit $\sigma$)')
plt.legend(loc='upper right',frameon=False)
plt.savefig('/home/rumbaugh/DRWmocktest.sigma.png')

plt.figure(1)
plt.clf()
plt.errorbar(true_lsigs,np.log10(np.sqrt(0.5*df.sigma.values**2*df.tau.values)),yerr=[np.sqrt(4*df.lsigma_errl**2+(0.5*(df.ltau_errl+df.ltau_erru))**2),np.sqrt(4*df.lsigma_erru**2+(0.5*(df.ltau_errl+df.ltau_erru))**2)],fmt='co',lw=1,capsize=2,mew=1,ms=4)
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(xlim[0],xlim[1],100)
plt.plot(xdummy,xdummy,lw=2,color='k',ls='dashed')
plt.xlim(xlim[0],xlim[1])
plt.ylim(ylim[0],ylim[1])
plt.xlabel(r'log(True $\sigma$)')
plt.ylabel(r'log(Fit $\sigma$)')
plt.legend(loc='upper right',frameon=False)
plt.savefig('/home/rumbaugh/DRWmocktest.sigma_conv.png')

plt.figure(1)
plt.clf()
#plt.scatter(true_lsigs,true_lsigs-df.lsigma,color='b',label='sig')
plt.errorbar(true_lsigs,true_lsigs-df.lsigma,yerr=[df.lsigma_errl,df.lsigma_erru],fmt='bo',lw=1,capsize=2,mew=1,ms=4)
#plt.scatter(true_lsigs,true_lsigs-np.log10(0.5*df.sigma.values**2*df.tau.values),color='cyan',label='sig_form')
plt.errorbar(true_lsigs,true_lsigs-np.log10(np.sqrt(0.5*df.sigma.values**2*df.tau.values)),yerr=[np.sqrt(4*df.lsigma_errl**2+(0.5*(df.ltau_errl+df.ltau_erru))**2),np.sqrt(4*df.lsigma_erru**2+(0.5*(df.ltau_errl+df.ltau_erru))**2)],fmt='co',lw=1,capsize=2,mew=1,ms=4)
#plt.scatter(true_lsigs,true_lsigs-df.drwvar,color='r',label='var')
plt.errorbar(true_lsigs,true_lsigs-df.drwvar,yerr=[df.lvar_errl,df.lvar_erru],fmt='ro',lw=1,capsize=2,mew=1,ms=4)
#plt.scatter(true_lsigs,true_lsigs-np.log10(0.5*df.drwvar.values**2*df.tau.values))#,color='orange',label='var_form')
plt.errorbar(true_lsigs,true_lsigs-np.log10(np.sqrt(0.5*df.drwvar.values**2*df.tau.values)),yerr=[np.sqrt(4*df.lvar_errl**2+(0.5*(df.ltau_errl+df.ltau_erru))**2),np.sqrt(4*df.lvar_erru**2+(0.5*(df.ltau_errl+df.ltau_erru))**2)],fmt='ko',lw=1,capsize=2,mew=1,ms=4)
xlim=plt.xlim()
ylim=plt.ylim()
plt.axhline(0,color='k',lw=2,ls='dashed')
plt.xlim(xlim[0],xlim[1])
plt.ylim(ylim[0],ylim[1])
plt.xlabel(r'log(True $\sigma$)')
plt.ylabel(r'log(True $\sigma$ - Fit $\sigma$)')
plt.legend(loc='upper right',frameon=False)
plt.savefig('/home/rumbaugh/DRWmocktest.sigma_diff.png')


plt.figure(1)
plt.clf()
#plt.scatter(true_ltaus-df.ltau,true_lsigs-np.log10(0.5*df.sigma.values**2*df.tau.values),color='cyan',label='sig_form')
plt.errorbar(true_ltaus-df.ltau,true_lsigs-np.log10(np.sqrt(0.5*df.sigma.values**2*df.tau.values)),xerr=[df.ltau_errl,df.ltau_erru],yerr=[np.sqrt(4*df.lsigma_errl**2+(0.5*(df.ltau_errl+df.ltau_erru))**2),np.sqrt(4*df.lsigma_erru**2+(0.5*(df.ltau_errl+df.ltau_erru))**2)],fmt='co',lw=1,capsize=2,mew=1,ms=4)
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(xlim[0],xlim[1],100)
plt.plot(xdummy,xdummy,lw=2,color='k',ls='dashed')
plt.xlim(xlim[0],xlim[1])
plt.ylim(ylim[0],ylim[1])
plt.xlabel(r'log($\tau$ diff. (days))')
plt.ylabel(r'log($\sigma$ diff.)')
plt.legend(loc='upper right',frameon=False)
plt.savefig('/home/rumbaugh/DRWmocktest.diff_diff.png')
