import numpy as np
import matplotlib.pyplot as plt

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.power_ratios.dat',dtype={'names':('field','clus','Rmax','xcen','ycen','P3','P4','P3LB','P3UB','P4LB','P4UB'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

crh=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.power_ratios.halved_SF.dat',dtype={'names':('field','clus','Rmax','xcen','ycen','P3','P4','P3LB','P3UB','P4LB','P4UB'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

fig=plt.figure(1)
fig.clf()
plt.clf()
ax=fig.add_subplot(1,1,1)
ax.set_frame_on(False)
ax.get_yaxis().tick_left()
ax.axes.get_xaxis().set_visible(False)

for i in range(0,len(cr)):
    ax.semilogy(np.array([i,i]),np.array([cr['P3LB'][i],cr['P3UB'][i]]),color='purple',lw=2)
ax.scatter(np.arange(len(cr)),cr['P3LB'],s=40,color='blue')
ax.scatter(np.arange(len(cr)),cr['P3UB'],s=40,color='red')
ax.scatter(np.arange(len(cr)),cr['P3'],s=40,color='k')

for i in range(0,len(crh)):
    ax.semilogy(np.array([i,i])+0.2,np.array([crh['P3LB'][i],crh['P3UB'][i]]),color='purple',lw=2)
ax.scatter(np.arange(len(crh))+0.2,crh['P3LB'],s=40,color='blue')
ax.scatter(np.arange(len(crh))+0.2,crh['P3UB'],s=40,color='red')
ax.scatter(np.arange(len(crh))+0.2,crh['P3'],s=40,color='k')



xmin, xmax = ax.get_xaxis().get_view_interval()
ymin, ymax = ax.get_yaxis().get_view_interval()
#ax.add_artist(Line2D((xmin, xmin), (ymin, ymax), color='black', linewidth=2))

ax.set_ylabel('P3')
plt.savefig('/home/rumbaugh/Chandra/plots/power_ratios.comp_halved_SF.5.24.17.png')
