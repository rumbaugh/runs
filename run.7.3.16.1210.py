import numpy as np
import matplotlib.pyplot as plt

date='7.3.16'

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

g=np.where((cr['cluster']=='RXJ1716A')|(cr['cluster']=='Cluster_A')|(cr['cluster']=='Cluster_B'))[0]

cr,cr2=cr[g],cr2[g]

crf=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_fits.dat',dtype={'names':('cluster','r0','r0-','r0+','bkg','bkg-','bkg+','r500','r500_NC','NC'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

carr=['r','b','g']

SBarr=np.zeros((np.shape(cr)[0],len(cr[0])-4))
errarr=np.zeros((np.shape(cr)[0],len(cr[0])-4))
prevrad=0
for j in range(0,len(cr[0])-4):
    SBarr[:,j]=cr[annnames[j]]/(np.pi*(rads[j]**2-prevrad**2))
    errarr[:,j]=np.sqrt(cr2[annnames[j]])*cr[annnames[j]]/cr2[annnames[j]]/(np.pi*(rads[j]**2-prevrad**2))
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.yscale('log')
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for i in range(0,len(cr['field'])):
    gf=np.where(cr['cluster'][i]==crf['cluster'])[0][0]
    r0=np.abs(crf['r0'][gf])
    SBarr[i]-=np.average(SBarr[i][-6:])
    #plt.errorbar(rads/r0,SBarr[i],errarr[i],color=carr[i])
    #plt.scatter(rads/r0,SBarr[i],color=carr[i],label=cr['cluster'][i])
    plt.errorbar(rads/r0,SBarr[i]/np.average(SBarr[i][2:5]),errarr[i]/np.average(SBarr[i][2:5]),color=carr[i])
    plt.scatter(rads/r0,SBarr[i]/np.average(SBarr[i][2:5]),color=carr[i],label=cr['cluster'][i])
ylim=plt.ylim()
#for j in np.arange(25,325,25): plt.axvline(j,ls='--',c='k')
plt.ylim(ylim)
#plt.ylim(0.95*np.min(SBarr[i]),1.05*np.max(SBarr[i]))
plt.legend(loc='upper right')
plt.xlabel('Normalized Annulus Radius')
plt.ylabel('Normalized Surface Brightness (counter per square arcsec)')
plt.title(cr['cluster'][i])
plt.savefig('/home/rumbaugh/Chandra/plots/SB_annuli_log_comp.%s.png'%(date))

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for i in range(0,len(cr['field'])):
    gf=np.where(cr['cluster'][i]==crf['cluster'])[0][0]
    r0=np.abs(crf['r0'][gf])
    #plt.errorbar(rads/r0,SBarr[i],errarr[i],color=carr[i])
    #plt.scatter(rads/r0,SBarr[i],color=carr[i],label=cr['cluster'][i])
    plt.errorbar(rads/r0,SBarr[i]/np.average(SBarr[i][2:5]),errarr[i]/np.average(SBarr[i][2:5]),color=carr[i])
    plt.scatter(rads/r0,SBarr[i]/np.average(SBarr[i][2:5]),color=carr[i],label=cr['cluster'][i])
ylim=plt.ylim()
#for j in np.arange(25,325,25): plt.axvline(j,ls='--',c='k')
plt.ylim(ylim)
#plt.ylim(0,1.05*np.max(SBarr[i]))
plt.legend(loc='upper right')
plt.xlabel('Normalized Annulus Radius')
plt.ylabel('Normalized Surface Brightness (counter per square arcsec)')
plt.title(cr['cluster'][i])
plt.savefig('/home/rumbaugh/Chandra/plots/SB_annuli_comp.%s.png'%(date))
    
