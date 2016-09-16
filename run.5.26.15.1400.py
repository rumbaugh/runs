import numpy as np
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.5.11.15.dat')

date = '5.26.15'

def reviewresults(ms,dasht=16,ldate='5.26.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=True,showfullsample=False):
    sampleFile='%ssample.0218.t%i.ms_%i.%s.dat'%(cbase,dasht,ms,ldate)
    sample_infoFile='%ssample_info.0218.t%i.ms_%i.%s.dat'%(cbase,dasht,ms,ldate)
    levelsFile='%slevels.0218.t%i.ms_%i.%s.dat'%(cbase,dasht,ms,ldate)
    DataFile='/home/rumbaugh/Fermi/data/0218/0218_TimeBombsInput.dat'
    posteriorFile='%sposterior.0218.t%i.ms_%i.%s.dat'%(cbase,dasht,ms,ldate)
    plotfilebase='0218.t%i.ms_%i.%s.png'%(dasht,ms,ldate)
    acorrplot,acorrplot2 = '%s/../plots/Acorr_0218.t%i.ms_%i.%s'%(cbase,dasht,ms,plotfilebase),'%s/../plots/Acorr_norm_0218.t%i.ms_%i.%s'%(cbase,dasht,ms,plotfilebase)
    if showresults: ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,plotfilebase,showfullsample=showfullsample)
    PPMC(T,posteriorFile,DataFile,ntrials,plotfile=None,plotfile2='/home/rumbaugh/Fermi/TimeBombs/plots/PPMC_Td_vs_tau_%s_0218.t%i.ms_%i.%s.png'%(T,date),figN=7,testplot=testplot,errstd=errstd,truetau=tau)
