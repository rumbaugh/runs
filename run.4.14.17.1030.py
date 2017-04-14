import numpy as np
import matplotlib.pyplot as plt
import pyfits as py
execfile('/home/rumbaugh/pythonscripts/StructureFunction.py')
try:
    indtrials
except NameError:
    indtrials=10000
try:
    ntrials
except NameError:
    ntrials=10000

Sarr,ltimearr=np.zeros(0,dtype='object'),np.zeros(0,dtype='object')
for n in range(0,ntrials):
    timestep=1.
    walks=np.random.uniform(-.05,.05,indtrials)
    mags,tau=np.array([20+walks[0]]),np.zeros(1)
    i=np.random.randint(1,100)
    rand=np.random.randint(1,100)
    while i<len(walks):
        mags,tau=np.append(mags,mags[-1]+np.sum(walks[i-rand+1:i+1])),np.append(tau,tau[-1]+rand)
        rand=np.random.randint(1,100)
        i+=rand
    Sarr,ltimearr=np.append(Sarr,0),np.append(ltimearr,0)
    Sarr[-1],ltimearr[-1]=mags+np.random.normal(0,0.05,len(mags)),tau


plt.figure(1)
plt.clf()
plt.scatter(tau,mags)


tauarr,Varr=EnsembleStructureFunction_IQR(Sarr,ltimearr,binwidth=0.2,calcerror=False,ntrials=1000)
plt.figure(2)
plt.clf()
plt.loglog(tauarr,Varr)
