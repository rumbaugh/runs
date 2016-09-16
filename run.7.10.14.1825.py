import numpy as np

cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')
tau,mu = cr[:,0],cr[:,1]


for i in range(0,20):
    FILE = open('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f.6.3.14.dat'%(i+1,tau[i],mu[i]),'w')
    if i != 14:
        tcr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/bkup/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f6.3.14.dat'%(i+1,tau[i],mu[i]))
    else:
        tcr = np.zeros(0)
    if np.shape(tcr)[0] > 0:
        ltime,amp,skew,Tfl = tcr[:,0],tcr[:,1],tcr[:,2],tcr[:,3]
        g = np.argsort(ltime)
        for j in range(len(g)):
            FILE.write('%6.2f %7.2f %7.4f %6.2f %6.2f\n'%(ltime[g[j]],amp[g[j]],skew[g[j]],Tfl[g[j]],ltime[g[j]]+220))
        FILE.close()
    else:
        FILE.write('')
        FILE.close()
