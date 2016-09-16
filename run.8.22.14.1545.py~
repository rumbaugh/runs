import numpy as np
import matplotlib as py

ldate = '8.8.14'


crt = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')

tau,mu = crt[:,0][pair-1],crt[:,1][pair-1]

cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/TimeBombs/output/sample.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ldate))

slen = 110

#lc1 = cr[0][-slen:]
#lct = cr[0][-2*slen:-slen]
lc1 = cr[0][-2*slen:-slen]
lct = cr[0][-slen:]
lc2 = lct-lc1
mu = cr[0][2]
tau = cr[0][1]

lc2_th = lc1*mu

plot(lc1,color='red',lw=1)
plot(lc2,color='blue',lw=1)
plot(np.arange(len(lc2_th))-tau/3.,lc2_th,color='green',lw=1)
