import numpy as np
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')

cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')

def reviewresults(pair,ldate='7.31.14',ddate='6.3.14',cbase='/mnt/data2/rumbaugh/Fermi/TimeBombs/output/test.'):
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    sampleFile='%ssample.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    sample_infoFile='%ssample_info.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    levelsFile='%slevels.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    DataFile='/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ddate)
    posteriorFile='%sposterior.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    plotfilebase='testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(pair,tau,mu,ldate)
    ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,plotfilebase)
