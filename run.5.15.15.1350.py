import numpy as np
cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.5.13.15.dat')
ddate='5.13.15'

for i,pair in zip(np.arange(100),np.arange(100)+1):
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    DataFile='/home/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ddate)
    crd = np.loadtxt(DataFile)
