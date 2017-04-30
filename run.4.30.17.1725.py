import numpy as np
import matplotlib
import matplotlib.pyplot as plt


cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
crs=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7.evq_spreads.4.30.17.dat')
drop=np.abs(cr['glo']-cr['ghi'])

plt.figure(1)
plt.clf()
plt.hist(crs.flatten(),range=(0.001,0.02),bins=20,lw=2,color='k',normed=True)
plt.hist(crs[drop>1].flatten(),range=(0,0.02),bins=20,lw=2,color='r',edgecolor='r',facecolor='None',normed=True)
plt.xlim(0,0.02)
plt.xlabel('Spread')
plt.ylabel('Normalized Number of Objects')
plt.savefig('/home/rumbaugh/spreadcheck.evqs_normed.4.30.17.png')

plt.figure(1)
plt.clf()
plt.hist(crs.flatten(),range=(0.001,0.02),bins=20,lw=2,color='k')
plt.hist(crs[drop>1].flatten(),range=(0,0.02),bins=20,lw=2,color='r',edgecolor='r',facecolor='None')
plt.xlim(0,0.02)
plt.xlabel('Spread')
plt.ylabel('Normalized Number of Objects')
plt.savefig('/home/rumbaugh/spreadcheck.evqs.4.30.17.png')
