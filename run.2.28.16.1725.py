import numpy as np
import matplotlib.pyplot as plt


z=np.linspace(0.5,2,1000)

delz=0.01

u=((1+z+delz)**2-(1+z)**2)/((1+z+delz)**2+(1+z)**2)

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.plot(z,u*3*10**5)
plt.xlabel('Redshift')
plt.ylabel('Relative Velocity (km/s)')

