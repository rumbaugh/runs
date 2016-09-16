import numpy as np
import matplotlib.pylab as plt

try:
    dayoffset
except NameError:
    dayoffset = 0.2

EarlyCSOs = ['J0204+0903','J0427+4133','J0754+5324']

execfile("/home/rumbaugh/Load1938.py")
CSOdict,timedict = Load1938(returnCSOs=True)
alltimes = np.array([])
CSOarr = np.array([],dtype='string')
for CSO in timedict: alltimes = np.append(alltimes,timedict[CSO])
mintime = np.min(alltimes)
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for CSO in CSOdict:
    if not CSO in EarlyCSOs:
        times = (timedict[CSO]-mintime)/86400.
        nflux = CSOdict[CSO]/np.mean(CSOdict[CSO])
        plt.scatter(times,nflux)
        plt.plot(times,nflux,lw=2)
        CSOarr=np.append(CSOarr,CSO)
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
plt.title('Normalized CSO Lightcurves')
plt.legend(CSOarr,loc=3)
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs.B1938.lc_norm_plot.9.11.13.png')
