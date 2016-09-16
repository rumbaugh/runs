import numpy as np

cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_16.flare_params_truthvalues.tau_30.34.mu_0.906.6.3.14.dat')
nflares = np.shape(cr)[0]
tau,mu=30.34,0.906
ftimes,amp,skew,Tfl = cr[:,4],cr[:,1],cr[:,2],cr[:,3]
Tfl = 30.*np.ones(len(amp))
ltime = np.arange(220.,550.,3.)
Td,Tr = 0.25*Tfl*(1+skew),0.25*Tfl*(1-skew)
F1,F2 = np.zeros(len(ltime)),np.zeros(len(ltime))
for iflr in range(0,nflares):
    F1 += amp[iflr]/(np.exp((ftimes[iflr]-ltime)/Tr[iflr])+np.exp(-1*(ftimes[iflr]-ltime)/Td[iflr]))
    F2 += mu*amp[iflr]/(np.exp((ftimes[iflr]-(ltime+tau))/Tr[iflr])+np.exp(-1*(ftimes[iflr]-(ltime+tau))/Td[iflr]))

figure(20)
clf()
scatter(ltime,F1)
scatter(ltime-tau,F2,color='red')
scatter(ltime,F1+F2,color='cyan')
