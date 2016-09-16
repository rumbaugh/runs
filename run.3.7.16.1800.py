import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/LFC_color_param.py")
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/MCMC_delaylnprob.py")
import emcee
import time

oneminussigma = 0.317310507863
st=time.time()

A=np.linspace(0.25,0.75,501)
C=np.linspace(1.5,2,501)
z0=np.linspace(0.5,1.0,501)

zarr=np.linspace(0.5,1.2,701)
zhalf=np.median(zarr)

SEDs=np.array(['graz01_00100.dat','graz01_00400.dat','graz01_05000.dat','graz13_00050.av3.00.dat'])

carr=['blue','green','red','orange']

obsU,obsB=np.zeros((len(SEDs),len(zarr))),np.zeros((len(SEDs),len(zarr)))
RFU,RFB=np.zeros(len(SEDs)),np.zeros(len(SEDs))
obsR,obsI,obsZ=np.zeros((len(SEDs),len(zarr))),np.zeros((len(SEDs),len(zarr))),np.zeros((len(SEDs),len(zarr)))

#FRed,FBlue=np.zeros((len(SEDs),len(A),len(C),len(z0),len(zarr))),np.zeros((len(SEDs),len(A),len(C),len(z0),len(zarr)))
#mRed,mBlue=np.zeros((len(SEDs),len(A),len(C),len(z0),len(zarr))),np.zeros((len(SEDs),len(A),len(C),len(z0),len(zarr)))
metricR,metricB=np.zeros((len(A),len(C),len(z0))),np.zeros((len(A),len(C),len(z0)))

safeLB=950
safeUB=32000

crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
cc_z=crcc[:,0]

for iSED in range(0,len(SEDs)):
    SED=SEDs[iSED]
    curcr=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/%s'%SED)
    w,S=curcr[:,0],curcr[:,1]
    gdl=np.argsort(np.abs(0.8-cc_z))[0]
    RFU[iSED]=calc_rest_flux(w,S,safeLB,safeUB,D_L=D_L[gdl],filt='u')
    RFB[iSED]=calc_rest_flux(w,S,safeLB,safeUB,D_L=D_L[gdl],filt='B')
    for iz in range(0,len(zarr)):
        z=zarr[iz]
        gdl=np.argsort(np.abs(z-cc_z))[0]
        obsU[iSED][iz]=calc_obs_flux(w,S,z,safeLB,safeUB,D_L=D_L[gdl],filt='u')
        obsB[iSED][iz]=calc_obs_flux(w,S,z,safeLB,safeUB,D_L=D_L[gdl],filt='B')
        obsR[iSED][iz],obsI[iSED][iz],obsZ[iSED][iz]=calc_obs_flux(w,S,z,safeLB,safeUB,D_L=D_L[gdl],filt='r'),calc_obs_flux(w,S,z,safeLB,safeUB,D_L=D_L[gdl],filt='i'),calc_obs_flux(w,S,z,safeLB,safeUB,D_L=D_L[gdl],filt='z')

mR,mI,mZ=-2.5*log10(obsR),-2.5*log10(obsI),-2.5*log10(obsZ)
mU,mB=-2.5*log10(obsU),-2.5*log10(obsB)
MURF,MBRF=-2.5*log10(RFU),-2.5*log10(RFB)

def SC_lnprob(x,zarr=zarr):
    ABlue,ARed,CBlue,CRed,z0Blue,z0Red=x[0],x[1],x[2],x[3],x[4],x[5]
    FBlue,FRed=np.zeros((len(SEDs),len(zarr))),np.zeros((len(SEDs),len(zarr)))
    for iSED in range(0,len(SEDs)):
        FBlue[iSED]=ABlue*(1-CBlue*(zarr-z0Blue))*obsR[iSED]+(1-ABlue)*(CBlue*(zarr-z0Blue))*obsI[iSED]
        FRed[iSED]=ARed*(1-CRed*(zarr-z0Red))*obsI[iSED]+(1-ARed)*(CRed*(zarr-z0Red))*obsZ[iSED]
        FBlue[iSED][zarr>1/CBlue+z0Blue]=(CBlue*(zarr[zarr>1/CBlue+z0Blue]-z0Blue))*obsI[iSED][zarr>1/CBlue+z0Blue]
        FBlue[iSED][zarr<z0Blue]=(1-CBlue*(zarr[zarr<z0Blue]-z0Blue))*obsR[iSED][zarr<z0Blue]
        FRed[iSED][zarr>1/CRed+z0Red]=(CRed*(zarr[zarr>1/CRed+z0Red]-z0Red))*obsZ[iSED][zarr>1/CRed+z0Red]
        FRed[iSED][zarr<z0Red]=(1-CRed*(zarr[zarr<z0Red]-z0Red))*obsI[iSED][zarr<z0Red]
    mRed,mBlue=np.ones(np.shape(FRed))*999,np.ones(np.shape(FRed))*999
    gR,gB=np.where(FRed>0),np.where(FBlue>0)
    mRed[gR],mBlue[gB]=-2.5*log10(FRed[gR]),-2.5*log10(FBlue[gB])
    cterm=mB[2][len(zarr)/2]-mRed[2][len(zarr)/2]
    mRed,mBlue=mRed+cterm,mBlue+cterm
    mcomb=np.append(mRed,mBlue,axis=1)
    SCvar=np.ones(np.shape(mcomb))/10.
    chisq_tmp=calc_chi_squared(mcomb,np.append(mB,mU,axis=1),SCvar)
    return -1.*chisq_tmp


    

ndim,nwalkers = 6,18

Ainit,Cinit,z0init=0.5,1.8,0.7
p0 = np.zeros((nwalkers,ndim))
p0[:,0],p0[:,1],p0[:,2],p0[:,3],p0[:,4],p0[:,5] = np.ones(nwalkers)*Ainit+np.random.normal(scale=0.05,size=nwalkers),np.ones(nwalkers)*Ainit+np.random.normal(scale=0.05,size=nwalkers),np.ones(nwalkers)*Cinit+np.random.normal(scale=0.05,size=nwalkers),np.ones(nwalkers)*Cinit+np.random.normal(scale=0.05,size=nwalkers),np.ones(nwalkers)*z0init+np.random.normal(scale=0.05,size=nwalkers),np.ones(nwalkers)*z0init+np.random.normal(scale=0.05,size=nwalkers)

try:
    runs
except NameError:
    runs=1000
try:
    BIruns
except NameError:
    BIruns=100
setuptime=time.time()
print "About to initialize sampler. %.1f seconds elapsed"%(setuptime-st)
sampler = emcee.EnsembleSampler(nwalkers,ndim,SC_lnprob,args=[zarr])
print "Starting Burn-in Phase"
pos,prob,state=sampler.run_mcmc(p0,BIruns)
sampler.reset()
BItime=time.time()
print "Burn-in Done. Took %.1f seconds. \nStarting Main Run. ETA: %.1f seconds"%(BItime-setuptime,10*(BItime-setuptime))
pos,prob,state=sampler.run_mcmc(pos,runs)
endtime=time.time()
print "MCMC Complete! Total time elapse: %.0f seconds"%(endtime-st)

ABsrt,ARsrt,CBsrt,CRsrt,z0Bsrt,z0Rsrt = np.sort(sampler.flatchain[:,0]),np.sort(sampler.flatchain[:,1]),np.sort(sampler.flatchain[:,2]),np.sort(sampler.flatchain[:,3]),np.sort(sampler.flatchain[:,4]),np.sort(sampler.flatchain[:,5])

ABout,ABerr,ARout,ARerr,CBout,CBerr,CRout,CRerr,z0Bout,z0Berr,z0Rout,z0Rerr = np.median(ABsrt),0.5*(ABsrt[int(runs*nwalkers*(1-oneminussigma/2))]-ABsrt[int(oneminussigma/2*runs*nwalkers)]),np.median(ARsrt),0.5*(ARsrt[int(runs*nwalkers*(1-oneminussigma/2))]-ARsrt[int(oneminussigma/2*runs*nwalkers)]),  np.median(CBsrt),0.5*(CBsrt[int(runs*nwalkers*(1-oneminussigma/2))]-CBsrt[int(oneminussigma/2*runs*nwalkers)]),np.median(CRsrt),0.5*(CRsrt[int(runs*nwalkers*(1-oneminussigma/2))]-CRsrt[int(oneminussigma/2*runs*nwalkers)]), np.median(z0Bsrt),0.5*(z0Bsrt[int(runs*nwalkers*(1-oneminussigma/2))]-z0Bsrt[int(oneminussigma/2*runs*nwalkers)]),np.median(z0Rsrt),0.5*(z0Rsrt[int(runs*nwalkers*(1-oneminussigma/2))]-z0Rsrt[int(oneminussigma/2*runs*nwalkers)])

np.savetxt('/home/rumbaugh/LFC_color_param/MCfit_flatchain.out.3.7.16.dat',sampler.flatchain)

ARed,ABlue=ARout*(1-CRout*(zarr-z0Rout)),ABout*(1-CBout*(zarr-z0Bout))
BRed,BBlue=(1-ARout)*(CRout*(zarr-z0Rout)),(1-ABout)*(CBout*(zarr-z0Bout))
ARed[zarr>1/CRout+z0Rout]=0
BRed[zarr<z0Rout]=0
ABlue[zarr>1/CBout+z0Bout]=0
BBlue[zarr<z0Bout]=0



plt.figure(5)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for iSED in range(0,len(SEDs)):
    SED=SEDs[iSED]
    mBout,mRout,dum1,dum2=calc_param_mags(mR[iSED],mI[iSED],mZ[iSED],np.ones(len(mR[iSED]))/10.,np.ones(len(mR[iSED]))/10.,np.ones(len(mR[iSED]))/10.,zarr,param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr})
    plt.plot(zarr,mRout,lw=2,color=carr[iSED])
    plt.plot(zarr,mBout,lw=2,color=carr[iSED],ls='--')
plt.xlabel('Redshift')
plt.ylabel('Magnitude')
plt.title('Supercolor magnitudes')
plt.savefig('/home/rumbaugh/LFC_color_param/MCfit.UBmag_plot.runs_%i.3.7.16.png'%runs)

plt.figure(6)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for iSED in range(0,len(SEDs)):
    SED=SEDs[iSED]
    mBout,mRout,dum1,dum2=calc_param_mags(mR[iSED],mI[iSED],mZ[iSED],np.ones(len(mR[iSED]))/10.,np.ones(len(mR[iSED]))/10.,np.ones(len(mR[iSED]))/10.,zarr,param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr})
    plt.plot(zarr,mBout-mRout,lw=2,color=carr[iSED])
plt.xlabel('Redshift')
plt.ylabel('Color')
plt.title('Supercolors')
for iSED in range(0,len(SEDs)):
    plt.axhline((MURF-MBRF)[iSED],color=carr[iSED],lw=2,ls='--')
plt.savefig('/home/rumbaugh/LFC_color_param/MCfit.UBcolor_plot.runs_%i.3.7.16.png'%runs)
