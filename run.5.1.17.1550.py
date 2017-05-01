import numpy as np
import matplotlib
import matplotlib.pyplot as plt


cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
crs=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7.evq_spreads.4.30.17.dat')
spreads=np.append(crs[:,0],crs[:,1])
spreaderrs=np.append(crs[:,2],crs[:,3])
drop=np.abs(cr['glo']-cr['ghi'])

xdummy=np.linspace(0.0000001,0.1,1000)
ydummy=np.sqrt(0.003**2+4*xdummy)

plt.figure(1)
plt.clf()
plt.scatter(spreaderrs,spreads,color='b',s=6,edgecolor='None',alpha=0.2)
plt.plot(xdummy,ydummy,color='r',lw=2,ls='dashed')
plt.plot(xdummy,-ydummy,color='r',lw=2,ls='dashed')
plt.xlabel('Spread Error')
plt.ylabel('Spread')
plt.savefig('/home/rumbaugh/spread_ps_check.5.1.17.png')
glog=np.where(spreaderrs>0)[0]
plt.figure(1)
plt.clf()
plt.yscale('log')
plt.scatter(spreaderrs[glog],spreads[glog],color='b',s=6,edgecolor='None',alpha=0.2)
plt.plot(xdummy,ydummy,color='r',lw=2,ls='dashed')
plt.plot(xdummy,-ydummy,color='r',lw=2,ls='dashed')
plt.xlabel('Spread Error')
plt.ylabel('Spread')
plt.savefig('/home/rumbaugh/spread_ps_check.loglog.5.1.17.png')
