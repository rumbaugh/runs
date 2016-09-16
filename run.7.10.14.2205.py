import numpy as np
date = '7.10.14'

cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')

FILE = open('/home/rumbaugh/runs/run.7.10.14.2205.sh','w')
FILE.write('rm -f TimeBombs.*.7.10.14.tar\n')
for i in np.array([3,4,5,6,7,8,10,11,12,13,14,15,16,17,20])-1:
    tau,mu = cr[:,0][i],cr[:,1][i]
    flrfile = '/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f.6.3.14.dat'%(i+1,tau,mu)
    histfile = '/mnt/data2/rumbaugh/Fermi/TimeBombs/plots/output.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(i+1,tau,mu,date)
    lcfile = '/mnt/data2/rumbaugh/Fermi/plots/testlightcurve_%i.tau_%.2f.mu_%.3f.6.3.14.png'%(i+1,tau,mu)
    flrfile2 = 'testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f.6.3.14.dat'%(i+1,tau,mu)
    histfile2 = 'output.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(i+1,tau,mu,date)
    lcfile2 = 'testlightcurve_%i.tau_%.2f.mu_%.3f.6.3.14.png'%(i+1,tau,mu)
    FILE.write('cp %s .\ncp %s .\ncp %s .\n'%(flrfile,histfile,lcfile))
    if i == 2:
        FILE.write('tar -cvf TimeBombs.flare_params.7.10.14.tar %s\n'%flrfile2)
        FILE.write('tar -cvf TimeBombs.hist_plots.7.10.14.tar %s\n'%histfile2)
        FILE.write('tar -cvf TimeBombs.lc_plots.7.10.14.tar %s\n'%lcfile2)
    else:
        FILE.write('tar -rvf TimeBombs.flare_params.7.10.14.tar %s\n'%flrfile2)
        FILE.write('tar -rvf TimeBombs.hist_plots.7.10.14.tar %s\n'%histfile2)
        FILE.write('tar -rvf TimeBombs.lc_plots.7.10.14.tar %s\n'%lcfile2)
    FILE.write('rm %s\nrm %s\nrm %s\n'%(flrfile2,histfile2,lcfile2))
FILE.close()
