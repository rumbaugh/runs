import numpy as np
import matplotlib
import matplotlib.pyplot as plt

cro=np.loadtxt('/home/rumbaugh/DR7_OVV_maxvar.thresh_90.dat',dtype={'names':('SDSSNAME','maxvar','medvar'),'formats':('|S24','f8','f8')})
crno=np.loadtxt('/home/rumbaugh/DR7_notOVV_maxvar.thresh_90.dat',dtype={'names':('SDSSNAME','maxvar','medvar'),'formats':('|S24','f8','f8')})
crob=np.loadtxt('/home/rumbaugh/DR7_OVV_maxvar.thresh_90.buffer_10.dat',dtype={'names':('SDSSNAME','maxvar','medvar'),'formats':('|S24','f8','f8')})
crnob=np.loadtxt('/home/rumbaugh/DR7_notOVV_maxvar.thresh_90.buffer_10.dat',dtype={'names':('SDSSNAME','maxvar','medvar'),'formats':('|S24','f8','f8')})


fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax2.tick_params(which='major',length=12,width=4,labelsize=20)
ax2.tick_params(which='minor',length=6,width=3,labelsize=20)
a=ax.hist(crno['medvar'],color='k',edgecolor='k',facecolor='None')
b=ax.hist(cro['medvar'],color='r',edgecolor='r',facecolor='None')
p=ax2.plot(np.sort(crno['medvar']),(np.arange(len(crno))+1.)/len(crno),lw=3,color='k',ls='dashed',label='FIRST_FR_TYPE=0')
q=ax2.plot(np.sort(cro['medvar']),(np.arange(len(cro))+1.)/len(cro),lw=3,color='r',label='FIRST_FR_TYPE>0')
plt.legend
ax.set_xlabel('Median Variation (magnitudes)')
ax.set_ylabel('Number of Objects')
ax2.set_ylabel('Cumulative Fraction')
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/OVV_medvar_comp.thresh_90.4.4.17.png')

fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax2.tick_params(which='major',length=12,width=4,labelsize=20)
ax2.tick_params(which='minor',length=6,width=3,labelsize=20)
a=ax.hist(crnob['medvar'],color='k',edgecolor='k',facecolor='None')
b=ax.hist(crob['medvar'],color='r',edgecolor='r',facecolor='None')
p=ax2.plot(np.sort(crnob['medvar']),(np.arange(len(crnob))+1.)/len(crnob),lw=3,color='k',ls='dashed',label='FIRST_FR_TYPE=0')
q=ax2.plot(np.sort(crob['medvar']),(np.arange(len(crob))+1.)/len(crob),lw=3,color='r',label='FIRST_FR_TYPE>0')
plt.legend
ax.set_xlabel('Median Variation (magnitudes)')
ax.set_ylabel('Number of Objects')
ax2.set_ylabel('Cumulative Fraction')
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/OVV_medvar_comp.thresh_90.buffer_10.4.4.17.png')
