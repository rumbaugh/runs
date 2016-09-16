import numpy as np
import matplotlib.pylab as plt

space_inbetween = 0.2

try:
    fluxratio_err
except NameError:
    fluxratio_err = 0.0054

try:
    dayoffset
except NameError:
    dayoffset = 0.2

try:
    trials
except NameError:
    trials = 10000

Bcutoff = 2025-1839.

date = '2.16.15'

lens_dict = {'0414': {'name': 'MG0414','images': 4}, '0712': {'name': 'B0712','images': 4}, '1030': {'name': 'J1030','images': 2}, '1127': {'name': 'B1127','images': 2}, '1152': {'name': 'B1152','images': 2}}
color_arr = ['blue','red','green','purple']
ls_arr = ['solid','dashed','dotted','-.']
sizes=[6,6,6,9]
symbols = ["o","s","D","h"]

CSO1cr, CSO2cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/1244.edt'),np.loadtxt('/home/rumbaugh/EVLA/light_curves/1400.edt')
CSO1day,CSO2day = CSO1cr[:,0],CSO2cr[:,0]
CSO1S,CSO2S = CSO1cr[:,2],CSO2cr[:,2]

CSO1day -= CSO1day[0]
CSO2day -= CSO2day[0]

g = np.where(((CSO1S>0)&(CSO2S>0)&(np.arange(len(CSO1S))!=4)&(np.arange(len(CSO1S))!=19)&(np.arange(len(CSO1S))!=34)&(np.arange(len(CSO1S))!=46)))[0]

CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.bar([Bcutoff],[999],width=500,bottom=-200,edgecolor='k',facecolor='none',hatch='/')
plt.scatter(CSO1day[g],CSO1S[g]/np.mean(CSO1S[g]),color=color_arr[0],s=msize)
#plt.plot(CSO1day[g],CSO1S[g]/np.mean(CSO1S[g]),color=color_arr[0],lw=2,ls=ls_arr[0])
plt.scatter(CSO2day[g],CSO2S[g]/np.mean(CSO2S[g]),color=color_arr[1],marker='<',s=msize)
#plt.plot(CSO2day[g],CSO2S[g]/np.mean(CSO2S[g]),color=color_arr[1],lw=2,ls=ls_arr[1])
plt.plot(CSO1day[g],CSOnorm,color='k',lw=2)
plt.title('CSO Lightcurves')
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
plt.xlim(1820-1839,2105-1839)
plt.ylim(0.9,1.05)
#plt.legend(('CSO1244','CSO1400'),loc=2)
plt.axhline(y=1.0,lw=2,ls='dashed',color='k',label=None)
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs.lc_plot.%s.png'%date)

CSOnorm = 0.5*(CSO1S[g]/np.mean(CSO1S[g]) + CSO2S[g]/np.mean(CSO2S[g]))

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.bar([Bcutoff],[999],width=500,bottom=-200,edgecolor='k',facecolor='none',hatch='/')
plt.scatter(CSO1day[g],CSO1S[g]/np.mean(CSO1S[g])/CSOnorm,color=color_arr[0],s=msize)
#plt.plot(CSO1day[g],CSO1S[g]/np.mean(CSO1S[g])/CSOnorm,color=color_arr[0],lw=2,ls=ls_arr[0])
plt.scatter(CSO2day[g],CSO2S[g]/np.mean(CSO2S[g])/CSOnorm,color=color_arr[1],marker='<',s=msize)
#plt.plot(CSO2day[g],CSO2S[g]/np.mean(CSO2S[g])/CSOnorm,color=color_arr[1],lw=2,ls=ls_arr[1])
plt.title('Relative CSO Lightcurves')
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
plt.xlim(1820-1839,2105-1839)
plt.ylim(0.96,1.04)
#plt.legend(('CSO1244','CSO1400'),loc=2)
plt.axhline(y=1.0,lw=2,ls='dashed',color='k',label=None)
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs.lc_norm_plot.%s.png'%date)
