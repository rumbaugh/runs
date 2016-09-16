import numpy as np
import matplotlib.pyplot as plt

date='1.29.16'

dictnames=('field','cluster','Xcen','Ycen')
annnames=()
dictfmts=('|S24','|S24','f8','f8')
annfmts=()
rads=np.arange(5,305,5)
for rad in rads:
    annnames=annnames+('%i'%rad,)
    annfmts=annfmts+('f8',)
dictnames=dictnames+annnames
dictfmts=dictfmts+annfmts

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_ann_counts.dat',dtype={'names':dictnames,'formats':dictfmts})
cr2=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_ann_counts_noVC.dat',dtype={'names':dictnames,'formats':dictfmts})

SBarr=np.zeros((np.shape(cr)[0],len(cr[0])-4))
errarr=np.zeros((np.shape(cr)[0],len(cr[0])-4))
prevrad=0
for j in range(0,len(cr[0])-4):
    SBarr[:,j]=cr[annnames[j]]/(np.pi*(rads[j]**2-prevrad**2))
    errarr[:,j]=np.sqrt(cr2[annnames[j]])*cr[annnames[j]]/cr2[annnames[j]]/(np.pi*(rads[j]**2-prevrad**2))
for i in range(0,np.shape(cr)[0]):
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.yscale('log')
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.errorbar(rads,SBarr[i],errarr[i])
    plt.scatter(rads,SBarr[i])
    ylim=plt.ylim()
    for j in np.arange(25,325,25): plt.axvline(j,ls='--',c='k')
    plt.ylim(ylim)
    plt.ylim(0.95*np.min(SBarr[i]),1.05*np.max(SBarr[i]))
    plt.xlabel('Annulus Radius')
    plt.ylabel('Surface Brightness (counter per square arcsec)')
    plt.title(cr['cluster'][i])
    plt.savefig('/home/rumbaugh/Chandra/plots/SB_annuli_log.%s.%s.png'%(cr['cluster'][i],date))
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.errorbar(rads,SBarr[i],errarr[i])
    plt.scatter(rads,SBarr[i])
    ylim=plt.ylim()
    for j in np.arange(25,325,25): plt.axvline(j,ls='--',c='k')
    plt.ylim(ylim)
    plt.ylim(0,1.05*np.max(SBarr[i]))
    plt.xlabel('Annulus Radius')
    plt.ylabel('Surface Brightness (counter per square arcsec)')
    plt.title(cr['cluster'][i])
    plt.savefig('/home/rumbaugh/Chandra/plots/SB_annuli.%s.%s.png'%(cr['cluster'][i],date))
    
