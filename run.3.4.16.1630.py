import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/LFC_color_param.py')
execfile('/home/rumbaugh/makeCMD.py')

carr=['blue','green','red','orange']

safeLB=950
safeUB=32000
SED='/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/graz01_00100.dat'
SEDs=np.array(['graz01_00100.dat','graz01_00400.dat','graz01_05000.dat','graz13_00050.av3.00.dat'])

zarr=np.linspace(0.66,1.18,1000)
ARed,ABlue=0.424*(1-1.794*(zarr-0.628)),0.45*(1-1.824*(zarr-0.679))
BRed,BBlue=0.576*(1.794*(zarr-0.628)),0.55*(1.824*(zarr-0.679))


plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.figure(2)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.figure(3)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for SED,iSED in zip(SEDs,np.arange(4)):
    curcr=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/%s'%SED)
    w,S=np.copy(curcr[:,0]),np.copy(curcr[:,1])

    restU,restB=calc_rest_flux(w,S,safeLB,safeUB,filt='u'),calc_rest_flux(w,S,safeLB,safeUB,filt='B')
    obsr,obsi,obsz=calc_obs_flux(w,S,0.7,safeLB,safeUB,filt='r'),calc_obs_flux(w,S,0.7,safeLB,safeUB,filt='i'),calc_obs_flux(w,S,0.7,safeLB,safeUB,filt='z')

    magU,magB=-48.6 - 2.5*np.log10(restU),-48.6 - 2.5*np.log10(restB)
    magr,magi,magz=-48.6 - 2.5*np.log10(obsr),-48.6 - 2.5*np.log10(obsi),-48.6 - 2.5*np.log10(obsz)
    magred,magblue,d1,d2=calc_param_mags(magr,magi,magz,0,0,0,zarr,param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr})
    print SED
    print magU,magB,magU-magB
    print magr,magi,magz,magr-magi,magi-magz
    magr,magi,magz=np.zeros(1000),np.zeros(1000),np.zeros(1000)
    obsr,obsi,obsz=np.zeros(1000),np.zeros(1000),np.zeros(1000)
    for z,i in zip(zarr,np.arange(len(zarr))):
        obsr[i],obsi[i],obsz[i]=calc_obs_flux(w,S,z,safeLB,safeUB,filt='r'),calc_obs_flux(w,S,z,safeLB,safeUB,filt='i'),calc_obs_flux(w,S,z,safeLB,safeUB,filt='z')
    magr,magi,magz=48.6 - 2.5*np.log10(obsr),48.6 - 2.5*np.log10(obsi),48.6 - 2.5*np.log10(obsz)
    plt.figure(1)
    plt.plot(zarr,magr-magi,color=carr[iSED],lw=2)
    plt.plot(zarr,magi-magz,color=carr[iSED],lw=2,ls='--')
    plt.figure(2)
    plt.plot(zarr,magr,color=carr[iSED],lw=2)
    plt.plot(zarr,magi,color=carr[iSED],lw=2,ls='--')
    plt.plot(zarr,magz,color=carr[iSED],lw=2,ls='-.')
    plt.figure(3)
    plt.plot(zarr,magred,color=carr[iSED],lw=2)
    plt.plot(zarr,magblue,color=carr[iSED],lw=2,ls='--')
    plt.xlabel('Redshift')
    plt.ylabel('Magnitude')
    plt.title('Supercolors')
    plt.savefig('/home/rumbaugh/LFC_color_param/supercolors_old_plot.png')
    
plt.figure(1)
plt.xlim(0.66,1.18)
plt.ylim(-0.3,1.6)

