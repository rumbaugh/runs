import numpy as np
import matplotlib.pyplot as plt

cr=np.loadtxt('/home/rumbaugh/Chandra/coadds.allORELSE.AGN.type1excluded.Xraylumcutnnon.magcut.winfillcorr.cat',dtype={'names':('field','lumcut','N_AGN','OII','OIIerr','Hd','Hderr','D4000','D4000err','Hdcorr'),'formats':('|S24','|S4','i8','f8','f8','f8','f8','f8','f8','f8')})

cro=np.loadtxt('/home/rumbaugh/Chandra/coadds.oldORELSE.cat',dtype={'names':('field','N_AGN','OII','OIIerr','Hd','Hderr','D4000','D4000err','Hdcorr'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8')})

glc=np.where((cr['lumcut']=='N')&(cr['field']!='SC1604_wSC2244'))[0]



plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(cr['OII'][glc],cr['Hdcorr'][glc],xerr=cr['OIIerr'][glc],yerr=cr['Hderr'][glc],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['OII'][glc],cr['Hdcorr'][glc],color='r',s=32)
plt.errorbar(cro['OII'],cro['Hd'],xerr=cro['OIIerr'],yerr=cro['Hderr'],color='green',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cro['OII'],cro['Hd'],color='green',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
plt.xlim(xlim[1],xlim[0])
for i in range(0,len(cr['OII'][glc])): plt.text(cr['OII'][glc][i]-xrng/50.,cr['Hdcorr'][glc][i],cr['field'][glc][i],color='b')
for i in range(0,len(cro['OII'])): plt.text(cro['OII'][i]-xrng/50.,cro['Hd'][i],cro['field'][i],color='b')
plt.axvline(-4,lw=2,color='k',ls='dashed')
plt.xlabel('EW(OII) (angstroms)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds_oldcomp_AGN.OII_vs_Hdcorr.png')



plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(cr['D4000'][glc],cr['Hdcorr'][glc],xerr=cr['D4000err'][glc],yerr=cr['Hderr'][glc],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['D4000'][glc],cr['Hdcorr'][glc],color='r',s=32)
plt.errorbar(cro['D4000'],cro['Hd'],xerr=cro['D4000err'],yerr=cro['Hderr'],color='green',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cro['D4000'],cro['Hd'],color='green',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
for i in range(0,len(cr['D4000'][glc])): plt.text(cr['D4000'][glc][i]+xrng/50.,cr['Hdcorr'][glc][i],cr['field'][glc][i],color='b')
for i in range(0,len(cro['D4000'])): plt.text(cro['D4000'][i]+xrng/50.,cro['Hd'][i],cro['field'][i],color='b')
plt.xlabel('D(4000)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds_oldcomp_AGN.D4000_vs_Hdcorr.png')


glc=np.where((cr['lumcut']=='Y')&(cr['field']!='SC1604_wSC2244'))[0]


plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(cr['OII'][glc],cr['Hdcorr'][glc],xerr=cr['OIIerr'][glc],yerr=cr['Hderr'][glc],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['OII'][glc],cr['Hdcorr'][glc],color='r',s=32)
plt.errorbar(cro['OII'],cro['Hd'],xerr=cro['OIIerr'],yerr=cro['Hderr'],color='green',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cro['OII'],cro['Hd'],color='green',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
plt.xlim(xlim[1],xlim[0])
for i in range(0,len(cr['OII'][glc])): plt.text(cr['OII'][glc][i]-xrng/50.,cr['Hdcorr'][glc][i],cr['field'][glc][i],color='b')
for i in range(0,len(cro['OII'])): plt.text(cro['OII'][i]-xrng/50.,cro['Hd'][i],cro['field'][i],color='b')
plt.axvline(-4,lw=2,color='k',ls='dashed')
plt.xlabel('EW(OII) (angstroms)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds_oldcomp_AGN_lumcut.OII_vs_Hdcorr.png')



plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(cr['D4000'][glc],cr['Hdcorr'][glc],xerr=cr['D4000err'][glc],yerr=cr['Hderr'][glc],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['D4000'][glc],cr['Hdcorr'][glc],color='r',s=32)
plt.errorbar(cro['D4000'],cro['Hd'],xerr=cro['D4000err'],yerr=cro['Hderr'],color='green',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cro['D4000'],cro['Hd'],color='green',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
for i in range(0,len(cr['D4000'][glc])): plt.text(cr['D4000'][glc][i]+xrng/50.,cr['Hdcorr'][glc][i],cr['field'][glc][i],color='b')
for i in range(0,len(cro['D4000'])): plt.text(cro['D4000'][i]+xrng/50.,cro['Hd'][i],cro['field'][i],color='b')
plt.xlabel('D(4000)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds_oldcomp_AGN_lumcut.D4000_vs_Hdcorr.png')
