import numpy as np
import matplotlib.pyplot as plt

ddate = '6.3.14'
date = '8.26.14'

pairs = np.array([3,4,5,6,7,8,10,11,12,13,14,16,17,20])
goodpairs = np.array([7,12,17])
okpairs = np.array([4,5,11,16])

g_good,g_ok,g_bad = np.zeros(0,dtype='int'),np.zeros(0,dtype='int'),np.zeros(0,dtype='int')

crt = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')

shortest_flare,Tfls,amps = np.zeros(len(pairs)), np.zeros(len(pairs)),np.zeros(len(pairs))

for pair,i in zip(pairs,np.arange(len(pairs))):
    tau_t,mu_t = crt[:,0][pair-1],crt[:,1][pair-1]
    cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau_t,mu_t,ddate))
    flrtime,amp,skew,Tfl = cr[:,0],cr[:,1],cr[:,2],cr[:,4]
    meanamp,meanTfl,minTfl = np.mean(amp),np.mean(Tfl),np.min(Tfl)
    shortest_flare[i],Tfls[i],amps[i] = meanamp,meanTfl,minTfl
    if pair in goodpairs: g_good = np.append(g_good,i)
    elif pair in okpairs: g_ok = np.append(g_ok,i)
    else: g_bad = np.append(g_bad,i)

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

plt.scatter(shortest_flare[g_bad],amps[g_bad],s=20,color='blue')
plt.scatter(shortest_flare[g_ok],amps[g_ok],s=20,color='green')
plt.scatter(shortest_flare[g_good],amps[g_good],s=20,color='red')

plt.xlabel('Shortest Flare Length (days)')
plt.ylabel('Mean Amplitude')
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/min_Tfl_vs_amp.testlightcurves.8.26.14.png')
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

plt.scatter(Tfls[g_bad],amps[g_bad],s=20,color='blue')
plt.scatter(Tfls[g_ok],amps[g_ok],s=20,color='green')
plt.scatter(Tfls[g_good],amps[g_good],s=20,color='red')

plt.xlabel('Mean Flare Length (days)')
plt.ylabel('Mean Amplitude')
plt.savefig('/mnt/data2/rumbaugh/Fermi/plots/mean_Tfl_vs_amp.testlightcurves.8.26.14.png')
