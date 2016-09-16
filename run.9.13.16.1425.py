import numpy as np
import matplotlib.pyplot as plt

cry,crs=np.loadtxt('/home/rumbaugh/compliance_test_091316_Y1A1.tab',skiprows=1),np.loadtxt('/home/rumbaugh/compliance_test_091316_SVA1.tab',skiprows=1)

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(crs[:,1],crs[:,2],s=2,color='b')
plt.scatter(cry[:,1],cry[:,2],s=16,color='r',marker='o',facecolor='None',edgecolor='r')
plt.xlabel('R.A.')
plt.ylabel('Dec')
xlim=plt.xlim()
plt.xlim(xlim[1],xlim[0])
plt.savefig('/home/rumbaugh/spatcomp_SV_Y1A1.png')
