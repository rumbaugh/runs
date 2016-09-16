import numpy as np
import matplotlib.pyplot as plt

cr=np.loadtxt('/home/rumbaugh/Chandra/coadds.allORELSE.AGN.type1excluded.Xraylumcutnnon.magcut.winfillcorr.cat',dtype={'names':('field','lumcut','N_AGN','OII','OIIerr','Hd','Hderr','D4000','D4000err','Hdcorr'),'formats':('|S24','|S4','i8','f8','f8','f8','f8','f8','f8','f8')})

glc=np.where((cr['lumcut']=='N')&((cr['field']=='Intermediate')|(cr['field']=='Quiescent')|(cr['field']=='High-z')|(cr['field']=='SC1604nSG0023')))[0]

textdict={'Intermediate':'Intermediate','Quiescent':'Passive','SC1604nSG0023':'SG0023 & SC1604','High-z':'High-z'}

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(cr['D4000'][glc],cr['Hd'][glc],xerr=cr['D4000err'][glc],yerr=cr['Hderr'][glc],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['D4000'][glc],cr['Hd'][glc],color='r',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
for i in range(0,len(cr['D4000'][glc])): plt.text(cr['D4000'][glc][i]+xrng/50.,cr['Hd'][glc][i],textdict[cr['field'][glc][i]],color='b')
plt.xlabel('D(4000)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
#plt.savefig('/home/rumbaugh/Chandra/plots/coadds_AGN.D4000_vs_Hd.png')



execfile('/home/rumbaugh/runs/run.7.14.16.1845.py')
plt.errorbar(cr['D4000'][glc],cr['Hdcorr'][glc],xerr=cr['D4000err'][glc],yerr=cr['Hderr'][glc],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['D4000'][glc],cr['Hdcorr'][glc],color='r',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
for i in range(0,len(cr['D4000'][glc])): plt.text(cr['D4000'][glc][i]+xrng/50.,cr['Hdcorr'][glc][i],textdict[cr['field'][glc][i]],color='b')
plt.xlabel('D(4000)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds_AGN.D4000_vs_Hdcorr.png')


glc=np.where((cr['lumcut']=='Y')&((cr['field']=='Intermediate')|(cr['field']=='Quiescent')|(cr['field']=='High-z')|(cr['field']=='SC1604nSG0023')))[0]


plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(cr['D4000'][glc],cr['Hd'][glc],xerr=cr['D4000err'][glc],yerr=cr['Hderr'][glc],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['D4000'][glc],cr['Hd'][glc],color='r',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
for i in range(0,len(cr['D4000'][glc])): plt.text(cr['D4000'][glc][i]+xrng/50.,cr['Hd'][glc][i],textdict[cr['field'][glc][i]],color='b')
plt.xlabel('D(4000)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
#plt.savefig('/home/rumbaugh/Chandra/plots/coadds_AGN_lumcut.D4000_vs_Hd.png')



execfile('/home/rumbaugh/runs/run.7.14.16.1845.py')
plt.errorbar(cr['D4000'][glc],cr['Hdcorr'][glc],xerr=cr['D4000err'][glc],yerr=cr['Hderr'][glc],color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(cr['D4000'][glc],cr['Hdcorr'][glc],color='r',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
for i in range(0,len(cr['D4000'][glc])): plt.text(cr['D4000'][glc][i]+xrng/50.,cr['Hdcorr'][glc][i],textdict[cr['field'][glc][i]],color='b')
plt.xlabel('D(4000)')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds_AGN_lumcut.D4000_vs_Hdcorr.png')
