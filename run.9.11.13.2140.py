import numpy as np
import matplotlib.pylab as plt

try:
    dayoffset
except NameError:
    dayoffset = 0.2

EarlyCSOs = ['J0204+0903','J0427+4133','J0754+5324']

execfile("/home/rumbaugh/Load1938.py")
CSOdict,timedict = Load1938(returnCSOs=True)
CSOdict['J1400+6210'],CSOdict['J1414+4554'],CSOdict['J1545+4751'],CSOdict['J1816+3457'],CSOdict['J1823+7938'],CSOdict['J1945+7055'] = np.delete(CSOdict['J1400+6210'],[5]),np.delete(CSOdict['J1414+4554'],[5]),np.delete(CSOdict['J1545+4751'],[5]),np.delete(CSOdict['J1816+3457'],[11]),np.delete(CSOdict['J1823+7938'],[10]),np.delete(CSOdict['J1945+7055'],[10])
timedict['J1400+6210'],timedict['J1414+4554'],timedict['J1545+4751'],timedict['J1816+3457'],timedict['J1823+7938'],timedict['J1945+7055'] = np.delete(timedict['J1400+6210'],[5]),np.delete(timedict['J1414+4554'],[5]),np.delete(timedict['J1545+4751'],[5]),np.delete(timedict['J1816+3457'],[11]),np.delete(timedict['J1823+7938'],[10]),np.delete(timedict['J1945+7055'],[10])
alltimes = np.array([])
CSOarr = np.array([],dtype='string')
for CSO in timedict: alltimes = np.append(alltimes,timedict[CSO])
mintime = np.min(alltimes)
cbool = True
for CSO in CSOdict:
    if not CSO in EarlyCSOs:
        if CSO in ['J0003+4807','J1414+4554','J1734+0926','J1823+7938','J1927+7358']:
            tcol = 'blue'
        else:
            tcol = 'red'
        plt.figure(1)
        plt.clf()
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        times = (timedict[CSO]-mintime)/86400.
        nflux = CSOdict[CSO]/np.mean(CSOdict[CSO])
        plt.scatter(times,nflux,color=tcol)
        plt.plot(times,nflux,lw=2,color=tcol)
        CSOarr=np.append(CSOarr,CSO)
        plt.xlabel('Days',fontsize=14)
        plt.ylabel('Normalized Flux',fontsize=14)
        plt.title('%s Lightcurve'%CSO)
        #plt.legend(CSOarr,loc=3)
        plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSO_%s.B1938.lc_norm_plot.9.11.13.png'%CSO)
        cbool = not cbool
