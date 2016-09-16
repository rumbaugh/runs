import numpy as np
import matplotlib.pyplot as plt

cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/TimeBombs/output/sample.testlightcurve_3.tau_26.97.mu_0.766.5.27.14.dat',usecols=(0,1,2))
bkgd,tau,mu = cr[:,0],cr[:,1],cr[:,2]

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.plot(tau)
plt.xlabel('Time delay (days)',fontsize=14)
plt.title('Lightcurve 3 - tau: 26.97')
plt.ylim(-5,105)
plt.savefig('/mnt/data2/rumbaugh/Fermi/TimeBombs/plots/TimeBombs_output.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(3,26.97,0.766,'5.27.14'))

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(tau,bins=80,range=[-200,200])
plt.xlabel('Time delay (days)',fontsize=14)
plt.title('Lightcurve 3 - tau: 26.97')
plt.savefig('/mnt/data2/rumbaugh/Fermi/TimeBombs/plots/TimeBombs_output.hist.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(3,26.97,0.766,'5.27.14'))
