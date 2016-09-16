import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/LFC_color_param.py")
import emcee

A=np.linspace(0.25,0.75,501)
C=np.linspace(1.5,2,501)
z0=np.linspace(0.5,1.0,501)

zarr=np.linspace(0.5,1.2,701)
zhalf=np.median(zarr)

ARed,ABlue=0.424*(1-1.794*(zarr-0.628)),0.45*(1-1.824*(zarr-0.679))
BRed,BBlue=0.576*(1.794*(zarr-0.628)),0.55*(1.824*(zarr-0.679))
ARed[zarr>1/1.794+0.628]=0
BRed[zarr<0.628]=0
ABlue[zarr>1/1.824+0.679]=0
BBlue[zarr<0.679]=0

SEDs=np.array(['graz01_00100.dat','graz01_00400.dat','graz01_05000.dat','graz13_00050.av3.00.dat'])

carr=['blue','green','red','orange']

obsU,obsB=np.zeros((len(SEDs),len(zarr))),np.zeros((len(SEDs),len(zarr)))
obsR,obsI,obsZ=np.zeros((len(SEDs),len(zarr))),np.zeros((len(SEDs),len(zarr))),np.zeros((len(SEDs),len(zarr)))

#FRed,FBlue=np.zeros((len(SEDs),len(A),len(C),len(z0),len(zarr))),np.zeros((len(SEDs),len(A),len(C),len(z0),len(zarr)))
#mRed,mBlue=np.zeros((len(SEDs),len(A),len(C),len(z0),len(zarr))),np.zeros((len(SEDs),len(A),len(C),len(z0),len(zarr)))
metricR,metricB=np.zeros((len(A),len(C),len(z0))),np.zeros((len(A),len(C),len(z0)))

safeLB=950
safeUB=32000

crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
DM=crcc[:,15]
cc_z=crcc[:,0]
gdls=np.zeros(len(zarr),dtype='i8')
for iSED in range(0,len(SEDs)):
    SED=SEDs[iSED]
    curcr=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/%s'%SED)
    w,S=curcr[:,0],curcr[:,1]
    for iz in range(0,len(zarr)):
        z=zarr[iz]
        gdl=np.argsort(np.abs(z-cc_z))[0]
        gdls[iz]=gdl
        obsU[iSED][iz]=calc_obs_flux(w,S,z,safeLB,safeUB,D_L=D_L[gdl],filt='u')
        obsB[iSED][iz]=calc_obs_flux(w,S,z,safeLB,safeUB,D_L=D_L[gdl],filt='B')
        obsR[iSED][iz],obsI[iSED][iz],obsZ[iSED][iz]=calc_obs_flux(w,S,z,safeLB,safeUB,D_L=D_L[gdl],filt='r'),calc_obs_flux(w,S,z,safeLB,safeUB,D_L=D_L[gdl],filt='i'),calc_obs_flux(w,S,z,safeLB,safeUB,D_L=D_L[gdl],filt='z')

    #for iA in range(0,len(A)):
    #    for iC in range(0,len(C)):
    #        for iz0 in range(0,len(z0)):
    #            FBluetmp=A[iA]*(1-C[iC]*(zarr-z0[iz0]))*obsR[iSED]+(1-A[iA])*(C[iC]*(zarr-z0[iz0]))*obsI[iSED]
    #            FRedtmp=A[iA]*(1-C[iC]*(zarr-z0[iz0]))*obsI[iSED]+(1-A[iA])*(C[iC]*(zarr-z0[iz0]))*obsZ[iSED]
    #            mRedtmp,mBluetmp=-2.5*np.log10(FRedtmp),-2.5*np.log10(FBluetmp)
#mRed,mBlue=-2.5*log10(FRed),-2.5*log10(FBlue)
mR,mI,mZ=-2.5*np.log10(obsR),-2.5*np.log10(obsI),-2.5*np.log10(obsZ)
mU,mB=-2.5*np.log10(obsU),-2.5*np.log10(obsB)


plt.figure(1)
plt.figure(5)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for iSED in range(0,len(SEDs)):
    SED=SEDs[iSED]
    plt.plot(zarr,mR[iSED],lw=2,color=carr[iSED])
    plt.plot(zarr,mI[iSED],lw=2,color=carr[iSED],ls='--')
    plt.plot(zarr,mZ[iSED],lw=2,color=carr[iSED],ls=':')
plt.xlabel('Redshift')
plt.ylabel('Magnitude')
plt.title('r-i-z magnitudes')
plt.savefig('/home/rumbaugh/LFC_color_param/rizmag_vs_redshift.3.14.16.png')
plt.figure(2)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for iSED in range(0,len(SEDs)):
    SED=SEDs[iSED]
    plt.plot(zarr,mR[iSED]-mI[iSED],lw=2,color=carr[iSED])
    plt.plot(zarr,mI[iSED]-mZ[iSED],lw=2,color=carr[iSED],ls='--')
plt.xlabel('Redshift')
plt.ylabel('Color')
plt.title('r-i-z colors')
plt.savefig('/home/rumbaugh/LFC_color_param/rizcolor_vs_redshift.3.14.16.png')
plt.figure(3)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for iSED in range(0,len(SEDs)):
    SED=SEDs[iSED]
    plt.plot(zarr,mU[iSED],lw=2,color=carr[iSED])
    plt.plot(zarr,mB[iSED],lw=2,color=carr[iSED],ls='--')
plt.xlabel('Redshift')
plt.ylabel('Magnitude')
plt.title('UB magnitudes')
plt.figure(8)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for iSED in range(0,len(SEDs)):
    SED=SEDs[iSED]
    #mBout,mRout,dum1,dum2=calc_param_mags(mR[iSED],mI[iSED],mZ[iSED],np.ones(len(mR[iSED]))/10.,np.ones(len(mR[iSED]))/10.,np.ones(len(mR[iSED]))/10.,zarr,param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr})
    mBout,mRout,dum1,dum2=calc_param_mags(mR[iSED],mI[iSED],mZ[iSED],0,0,0,zarr,param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr})
    mBout,mRout=mBout-DM[gdls]+2.5*np.log10(1+zarr),mRout-DM[gdls]+2.5*np.log10(1+zarr)
    plt.plot(zarr,mRout,lw=2,color=carr[iSED])
    plt.plot(zarr,mBout,lw=2,color=carr[iSED],ls='--')
plt.xlabel('Redshift')
plt.ylabel('Magnitude')
plt.title('Supercolor magnitudes')
plt.savefig('/home/rumbaugh/LFC_color_param/supercolorRF_vs_redshift.3.14.16.png')
plt.figure(4)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for iSED in range(0,len(SEDs)):
    SED=SEDs[iSED]
    plt.plot(zarr,mU[iSED]-mB[iSED],lw=2,color=carr[iSED])
plt.xlabel('Redshift')
plt.ylabel('Color')
plt.title('UB colors')

plt.figure(7)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.plot(zarr,ARed,lw=2,color='r',label='A(Red)')
plt.plot(zarr,BRed,lw=2,color='r',ls='--',label='B(Red)')
plt.plot(zarr,ABlue,lw=2,color='b',label='A(Blue)')
plt.plot(zarr,BBlue,lw=2,color='b',ls='--',label='B(Blue)')
plt.xlabel('Redshift')
plt.ylabel('Supercolor Coefficient')
plt.xlim(0.66,1.2)
plt.legend(loc=7)
plt.savefig('/home/rumbaugh/LFC_color_param/supercolor_coeff.3.14.16.png')


