import numpy as np
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')

def reviewresults(ldate='7.7.14',cbase='/mnt/data2/rumbaugh/Fermi/TimeBombs/output/'):
    sampleFile='%ssample.0218.%s.dat'%(cbase,ldate)
    sample_infoFile='%ssample_info.0218.%s.dat'%(cbase,ldate)
    levelsFile='%slevels.0218.%s.dat'%(cbase,ldate)
    DataFile='/mnt/data2/rumbaugh/Fermi/data/0218_TimeBombsInput.dat'
    posteriorFile='%sposterior.0218.%s.dat'%(cbase,ldate)
    plotfilebase='0218.%s.png'%(ldate)
    ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,plotfilebase)
