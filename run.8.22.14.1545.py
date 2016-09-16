import numpy as np
import matplotlib as py

ldate = '8.8.14'
ddate = '6.3.14'

crt = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')

tau,mu = crt[:,0][pair-1],crt[:,1][pair-1]

DataFile='/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ddate)
datacr = np.loadtxt(DataFile)
cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/TimeBombs/output/posterior.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ldate))

slen = 110

figure(1)
clf()
figure(2)
clf()

for i in range(0,np.shape(cr)[0]):

#lc1 = cr[0][-slen:]
#lct = cr[0][-2*slen:-slen]
    lc1 = cr[i][-2*slen:-slen]
    lct = cr[i][-slen:]
    lc2 = lct-lc1
    mu = cr[i][2]
    tau = cr[i][1]
    if mu > 1: 
        figure(1)
        print tau, 1./mu
    else: 
        figure(2)
        print -tau, mu

    #lc2_th = lc1*mu

    plot(lc1,color='red',lw=1)
    plot(lc2,color='blue',lw=1)
    #plot(np.arange(len(lc2_th))-tau/3.,lc2_th,color='green',lw=1)
figure(1)
plot(datacr[:,1],color='cyan',lw=2)
figure(2)
plot(datacr[:,1],color='cyan',lw=2)
