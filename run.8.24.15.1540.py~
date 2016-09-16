import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GMM
execfile('/home/rumbaugh/ReverseSigmaClip.py')
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

pairs = np.arange(100)+1
#pairs = np.delete(pairs,[14,25,39,48,55,57,75,78])
pairs = np.delete(pairs,[14,25,39,48,55,57,75,78,79,90,92])


color_arr=np.array(['blue','red','cyan','magenta','green','brown','orange','yellow','pink'])
marker_arr=['o','+','x','D']

critwidth=3.716/2.35482

date='8.4.15'
ldate='5.13.15'
cbase='/home/rumbaugh/Fermi/TimeBombs/output/'

def reviewresults(pair,jiter,ldate='8.4.15',ddate='5.13.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=True,ntrials=10000,testplot=False,errstd=np.sqrt(2)*7.5,T='ACFT',showfullsample=False):
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    DataFile='/home/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ddate)
    sampleFile='%ssample.testlightcurve_%i.iter_%i.%s.dat'%(cbase,pair,jiter,ldate)
    sample_infoFile='%ssample_info.testlightcurve_%i.iter_%i.%s.dat'%(cbase,pair,jiter,ldate)
    levelsFile='%slevels.testlightcurve_%i.iter_%i.%s.dat'%(cbase,pair,jiter,ldate)
    weightFile='%sweights.testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,jiter,tau,mu,ldate)
    posteriorFile='%sposterior.testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,jiter,tau,mu,ldate)
    plotfilebase='testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.png'%(pair,jiter,tau,mu,ldate)
    if showresults: ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,weightFile,plotfilebase,showfullsample=showfullsample)
    crpost = np.loadtxt(posteriorFile)
    return crpost

for tau,it in zip(np.array([5,10,15,20]),np.array([0,1,2,3])):
    pairs=np.arange(50,60)
    for i,pair in zip(pairs-1,pairs):
        for j in range(0,10): crpost=reviewresults(pair,j)
