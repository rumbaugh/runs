import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/LFC_color_param.py')

carr=['blue','green','red','orange']

safeLB=950
safeUB=32000
SED='/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/graz01_00100.dat'
SEDs=np.array(['graz01_00100.dat','graz01_00400.dat','graz01_05000.dat','graz13_00050.av3.00.dat'])

zarr=np.linspace(0.66,1.18,1000)

plt.figure(1)
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
    print SED
    print magU,magB,magU-magB
    print magr,magi,magz,magr-magi,magi-magz
    magr,magi,magz=np.zeros(1000),np.zeros(1000),np.zeros(1000)
    obsr,obsi,obsz=np.zeros(1000),np.zeros(1000),np.zeros(1000)
    for z,i in zip(zarr,np.arange(len(zarr))):
        obsr[i],obsi[i],obsz[i]=calc_obs_flux(w,S,z,safeLB,safeUB,filt='r'),calc_obs_flux(w,S,z,safeLB,safeUB,filt='i'),calc_obs_flux(w,S,z,safeLB,safeUB,filt='z')
    magr,magi,magz=-48.6 - 2.5*np.log10(obsr),-48.6 - 2.5*np.log10(obsi),-48.6 - 2.5*np.log10(obsz)
    plt.plot(zarr,magr-magi,color=carr[iSED],lw=2)
    plt.plot(zarr,magi-magz,color=carr[iSED],lw=2,ls='--')
plt.xlim(0.66,1.18)
plt.ylim(-0.3,1.6)

