import numpy as np
import matplotlib
import matplotlib.pyplot as plt


cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
crs=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7.evq_spreads.4.30.17.dat')
drop=np.abs(cr['glo']-cr['ghi'])
crevq=crs[drop>1]
spreads=np.append(crs[:,0],crs[:,1])
spreaderrs=np.append(crs[:,2],crs[:,3])
evqspreads=np.append(crevq[:,0],crevq[:,1])
evqspreaderrs=np.append(crevq[:,2],crevq[:,3])
magautos=np.append(crs[:,4],crs[:,5])
magautoerrs=np.append(crs[:,6],crs[:,7])
evqmagautos=np.append(crevq[:,4],crevq[:,5])
evqmagautoerrs=np.append(crevq[:,6],crevq[:,7])
magpsfs=np.append(cr['glo'],cr['ghi'])
magpsferrs=np.append(cr['siglo'],cr['sighi'])
evqmagpsfs=np.append(cr['glo'][drop>1],cr['ghi'][drop>1])
evqmagpsferrs=np.append(cr['siglo'][drop>1],cr['sighi'][drop>1])

psfmetric=spreads/np.sqrt(0.003**2+4*spreaderrs**2)
evqpsfmetric=evqspreads/np.sqrt(0.003**2+4*evqspreaderrs**2)

xdummy=np.linspace(0.0000001,0.1,1000)
ydummy=np.sqrt(0.003**2+4*xdummy**2)

plt.figure(1)
plt.clf()
plt.scatter(spreaderrs,spreads,color='b',s=6,edgecolor='None',alpha=0.2)
plt.plot(xdummy,ydummy,color='r',lw=2,ls='dashed')
plt.plot(xdummy,-ydummy,color='r',lw=2,ls='dashed')
plt.xlabel('Spread Error')
plt.ylabel('Spread')
plt.xlim(0,0.054)
plt.ylim(-0.009,0.024)
plt.savefig('/home/rumbaugh/spread_ps_check.5.1.17.png')

glog=np.where(spreaderrs>0)[0]
plt.figure(1)
plt.clf()
plt.xscale('log')
plt.scatter(spreaderrs[glog],spreads[glog],color='b',s=6,edgecolor='None',alpha=0.2)
plt.plot(xdummy,ydummy,color='r',lw=2,ls='dashed')
plt.plot(xdummy,-ydummy,color='r',lw=2,ls='dashed')
plt.xlabel('Spread Error')
plt.ylabel('Spread')
plt.xlim(0.00003,0.054)
plt.ylim(-0.009,0.024)
plt.savefig('/home/rumbaugh/spread_ps_check.loglog.5.1.17.png')

plt.figure(1)
plt.clf()
plt.scatter(psfmetric,magautos-magpsfs,color='b',s=6,edgecolor='None',alpha=0.2)
plt.xlabel('PSF Metric')
plt.ylabel('Mag_auto - Mag_PSF')
plt.ylim(-2,2)
plt.savefig('/home/rumbaugh/spread_magdiff_corr_check.5.1.17.png')

plt.figure(1)
plt.clf()
plt.scatter(psfmetric,magpsfs,color='b',s=6,edgecolor='None',alpha=0.2)
plt.xlabel('PSF Metric')
plt.ylabel('Mag_PSF')
plt.ylim(15,25)
plt.savefig('/home/rumbaugh/spread_mag_check.5.1.17.png')

plt.figure(1)
plt.clf()
plt.scatter(psfmetric,np.append(drop,drop),color='b',s=6,edgecolor='None',alpha=0.2)
plt.xlabel('PSF Metric')
plt.ylabel('Mag Drop')
plt.ylim(-5,5)
plt.savefig('/home/rumbaugh/spread_drop_check.5.1.17.png')



plt.figure(1)
plt.clf()
plt.scatter(evqspreaderrs,evqspreads,color='b',s=6,edgecolor='None',alpha=0.2)
plt.plot(xdummy,ydummy,color='r',lw=2,ls='dashed')
plt.plot(xdummy,-ydummy,color='r',lw=2,ls='dashed')
plt.xlabel('Spread Error')
plt.ylabel('Spread')
plt.xlim(0,0.054)
plt.ylim(-0.009,0.024)
plt.savefig('/home/rumbaugh/spreadevq_ps_check.5.1.17.png')


glog=np.where(evqspreaderrs>0)[0]
plt.figure(1)
plt.clf()
plt.xscale('log')
plt.scatter(evqspreaderrs[glog],evqspreads[glog],color='b',s=6,edgecolor='None',alpha=0.2)
plt.plot(xdummy,ydummy,color='r',lw=2,ls='dashed')
plt.plot(xdummy,-ydummy,color='r',lw=2,ls='dashed')
plt.xlabel('Spread Error')
plt.ylabel('Spread')
plt.xlim(0.00003,0.054)
plt.ylim(-0.009,0.024)
plt.savefig('/home/rumbaugh/spreadevq_ps_check.loglog.5.1.17.png')


plt.figure(1)
plt.clf()
plt.scatter(evqpsfmetric,evqmagautos-evqmagpsfs,color='b',s=6,edgecolor='None',alpha=0.2)
plt.xlabel('PSF Metric')
plt.ylabel('Mag_auto - Mag_PSF')
plt.ylim(-2,2)
plt.savefig('/home/rumbaugh/spreadevq_magdiff_corr_check.5.1.17.png')

plt.figure(1)
plt.clf()
plt.scatter(evqpsfmetric,evqmagpsfs,color='b',s=6,edgecolor='None',alpha=0.2)
plt.xlabel('PSF Metric')
plt.ylabel('Mag_PSF')
plt.ylim(15,25)
plt.savefig('/home/rumbaugh/spreadevq_mag_check.5.1.17.png')

plt.figure(1)
plt.clf()
plt.scatter(evqpsfmetric,np.append(drop[np.abs(drop)>1],drop[np.abs(drop)>1]),color='b',s=6,edgecolor='None',alpha=0.2)
plt.xlabel('PSF Metric')
plt.ylabel('Mag Drop')
plt.ylim(-5,5)
plt.savefig('/home/rumbaugh/spreadevq_drop_check.5.1.17.png')

