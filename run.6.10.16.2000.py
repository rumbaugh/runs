import numpy as np
import matplotlib.pyplot as plt

cr=np.loadtxt('/home/rumbaugh/Chandra/coadds.allORELSE.AGN.type1excluded.magcut.fourregions.winfillcorr.cat',dtype={'names':('file','region','N_AGN','OII','OIIerr','Hd','Hderr','D4000','D4000err','Hdcorr'),'formats':('|S124','i8','i8','f8','f8','f8','f8','f8','f8','f8')})


plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(cr['OII'],cr['Hd'],xerr=cr['OIIerr'],yerr=cr['Hderr'],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['OII'],cr['Hd'],color='r',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
plt.xlim(xlim[1],xlim[0])
for i in range(0,len(cr['OII'])): plt.text(cr['OII'][i]-xrng/50.,cr['Hd'][i],'Region %i'%cr['region'][i],color='b')
plt.axvline(-4,lw=2,color='k',ls='dashed')
plt.xlabel('EW(OII) (angstroms)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds_region_comp.OII_vs_Hd.png')



plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(cr['D4000'],cr['Hd'],xerr=cr['D4000err'],yerr=cr['Hderr'],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['D4000'],cr['Hd'],color='r',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
for i in range(0,len(cr['D4000'])): plt.text(cr['D4000'][i]+xrng/50.,cr['Hd'][i],'Region %i'%cr['region'][i],color='b')
plt.xlabel('D(4000)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds_region_comp.D4000_vs_Hd.png')




plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(cr['OII'],cr['Hdcorr'],xerr=cr['OIIerr'],yerr=cr['Hderr'],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['OII'],cr['Hdcorr'],color='r',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
plt.xlim(xlim[1],xlim[0])
for i in range(0,len(cr['OII'])): plt.text(cr['OII'][i]-xrng/50.,cr['Hdcorr'][i],'Region %i'%cr['region'][i],color='b')
plt.axvline(-4,lw=2,color='k',ls='dashed')
plt.xlabel('EW(OII) (angstroms)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds_region_comp.OII_vs_Hdcorr.png')



plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(cr['D4000'],cr['Hdcorr'],xerr=cr['D4000err'],yerr=cr['Hderr'],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['D4000'],cr['Hdcorr'],color='r',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
for i in range(0,len(cr['D4000'])): plt.text(cr['D4000'][i]+xrng/50.,cr['Hdcorr'][i],'Region %i'%cr['region'][i],color='b')
plt.xlabel('D(4000)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds_region_comp.D4000_vs_Hdcorr.png')
