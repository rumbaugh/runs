import numpy as np
import matplotlib as py

date = '8.22.14'
ddate = '6.3.14'

crt = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')
pairs = np.array([3,4,5,6,7,8,10,11,12,13,14,15,16,17,20])
redone_pairs = np.array([3,5,6,10,11])

for pair in pairs:
    ldate = '8.8.14'
    if pair in redone_pairs: ldate = '8.22.14'
    if pair == 11: ldate = '8.24.14'
    tau_t,mu_t = crt[:,0][pair-1],crt[:,1][pair-1]

    DataFile='/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau_t,mu_t,ddate)
    datacr = np.loadtxt(DataFile)
    cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/TimeBombs/output/posterior.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau_t,mu_t,ldate))

    slen = 110

    figure(1)
    clf()

    for i in range(0,np.shape(cr)[0]):

#lc1 = cr[0][-slen:]
#lct = cr[0][-2*slen:-slen]
        lc1 = cr[i][-2*slen:-slen]
        lct = cr[i][-slen:]
        lc2 = lct-lc1
        mu = cr[i][2]
        tau = cr[i][1]
        if mu > 1: lc1,lc2=lc2,lc1

    #lc2_th = lc1*mu

        plot(lc1,color='red',lw=1)
        plot(lc2,color='blue',lw=1)
    #plot(np.arange(len(lc2_th))-tau/3.,lc2_th,color='green',lw=1)
    plot(datacr[:,1],color='cyan',lw=2)
    savefig('/mnt/data2/rumbaugh/Fermi/TimeBombs/plots/plotsforgifposterior_output_curves.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(pair,tau_t,mu_t,date))
