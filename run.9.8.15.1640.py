import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GMM
execfile('/home/rumbaugh/ReverseSigmaClip.py')
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

pairs = np.arange(100)+1
pairs = np.delete(pairs,np.arange(99))
npairs=len(pairs)
cutoff=54

color_arr=np.array(['blue','red','cyan','magenta','green','brown','orange','yellow','pink'])
marker_arr=['o','+','x','D']

critwidth=3.716/2.35482

date='9.5.15'
ddate='8.19.15'
cbase='/home/rumbaugh/Fermi/TimeBombs/output/'

def reviewresults(pair,suffix,ldate='9.5.15',ddate='8.19.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=False,ntrials=10000,testplot=False,errstd=np.sqrt(2)*7.5,T='ACFT',showfullsample=False):
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    sampleFile='%ssample.testlightcurve_%i%s.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,suffix,tau,mu,ldate)
    sample_infoFile='%ssample_info.testlightcurve_%i%s.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,suffix,tau,mu,ldate)
    levelsFile='%slevels.testlightcurve_%i%s.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,suffix,tau,mu,ldate)
    DataFile='/home/rumbaugh/Fermi/data/test/testlightcurve_%i%s.tau_%.2f.mu_%.3f.%s.dat'%(pair,suffix,tau,mu,ddate)
    weightFile='%sweights.testlightcurve_%i%s.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,suffix,tau,mu,ldate)
    posteriorFile='%sposterior.testlightcurve_%i%s.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,suffix,tau,mu,ldate)
    plotfilebase='testlightcurve_%i%s.tau_%.2f.mu_%.3f.%s.png'%(pair,suffix,tau,mu,ldate)
    acorrplot,acorrplot2 = '%s/../plots/Acorr_%s'%(cbase,plotfilebase),'%s/../plots/Acorr_norm_%s'%(cbase,plotfilebase)
    if showresults: ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,weightFile,plotfilebase,showfullsample=showfullsample)
    #PPMC(T,posteriorFile,DataFile,ntrials,plotfile=None,plotfile2='/home/rumbaugh/Fermi/TimeBombs/plots/PPMC_Td_vs_tau_%s_testlightcurve_%i%s.tau_%.2f.mu_%.3f.%s.png'%(T,pair,tau,mu,date),figN=7,testplot=testplot,errstd=errstd,truetau=tau)
    crpost = np.loadtxt(posteriorFile)
    return crpost


errstd = 7.5
cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.8.19.15.dat')
taus,mus=cr[:,0],cr[:,1]
#avg_fwidth,medtau,cliptau=np.zeros(len(pairs)),np.zeros(len(pairs)),np.zeros(len(pairs))
avg_fwidth,medtau,cliptau,wt_tau=np.zeros(npairs),np.zeros(npairs),np.zeros(npairs),np.zeros(npairs)
fulltaus,halftaus,halftaudiffs,expandtaudiffs=np.zeros(npairs),np.zeros(npairs*2),np.zeros(npairs),np.zeros(npairs*2)
for i,pair in zip(pairs-1,pairs):
    #for suffix in ['','_A','_B']:
    for suffix in ['_B']:
        print '%i%s'%(pair,suffix)
        crpost=reviewresults(pair,suffix,showresults=True)
