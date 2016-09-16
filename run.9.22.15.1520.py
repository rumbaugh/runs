import numpy as np
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

date = '9.21.15'

def reviewresults(band,ldate='9.21.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=True,showfullsample=False):
    sampleFile='%ssample.0218_%s.%s.dat'%(cbase,band,ldate)
    sample_infoFile='%ssample_info.0218_%s.%s.dat'%(cbase,band,ldate)
    levelsFile='%slevels.0218_%s.%s.dat'%(cbase,band,ldate)
    DataFile='/home/rumbaugh/Fermi/data/0218/0218_TimeBombsInput.dat'
    posteriorFile='%sposterior.0218_%s.%s.dat'%(cbase,band,ldate)
    plotfilebase='0218_%s.%s.png'%(band,ldate)
    acorrplot,acorrplot2 = '%s/../plots/Acorr_0218_%s.%s'%(cbase,band,plotfilebase),'%s/../plots/Acorr_norm_0218_%s.%s'%(cbase,band,plotfilebase)
    if showresults: ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,plotfilebase,showfullsample=showfullsample)
    #PPMC(T,posteriorFile,DataFile,ntrials,plotfile=None,plotfile2='/home/rumbaugh/Fermi/TimeBombs/plots/PPMC_Td_vs_tau_%s_0218_%s.%s.png'%(T,date),figN=7,testplot=testplot,errstd=errstd,truetau=tau)

for band in ['full','soft','hard']:
    reviewresults(band)
