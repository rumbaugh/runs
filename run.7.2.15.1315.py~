import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/ReverseSigmaClip.py')
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

pairs = np.arange(100)+1
#pairs = np.delete(pairs,[14,25,39,48,55,57,75,78])
#pairs = np.delete(pairs,[14,25,39,48,55,57,75,78,79,90,92])

critwidth=3.716/2.35482

date='6.30.15'
ldate='6.10.15'
cbase='/home/rumbaugh/Fermi/TimeBombs/output/'

def reviewresults(pair,tau,mu,ldate='6.10.15',ddate='6.10.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=True,ntrials=10000,testplot=False,errstd=np.sqrt(2)*7.5,T='ACFT',showfullsample=False):
    sampleFile='%ssample.testlightcurve.tau_%i_%i.mu_%.3f.%s.dat'%(cbase,tau,pair,mu,ldate)
    sample_infoFile='%ssample_info.testlightcurve.tau_%i_%i.mu_%.3f.%s.dat'%(cbase,tau,pair,mu,ldate)
    levelsFile='%slevels.testlightcurve.tau_%i_%i.mu_%.3f.%s.dat'%(cbase,tau,pair,mu,ldate)
    DataFile='/home/rumbaugh/Fermi/data/test/testlightcurve.tau_%i_%i.mu_%.3f.%s.dat'%(tau,pair,mu,ddate)
    posteriorFile='%sposterior.testlightcurve.tau_%i_%i.mu_%.3f.%s.dat'%(cbase,tau,pair,mu,ldate)
    weightFile='%sweights.testlightcurve.tau_%i_%i.mu_%.3f.%s.dat'%(cbase,tau,pair,mu,ldate)
    plotfilebase='testlightcurve.tau_%i_%i.mu_%.3f.%s.png'%(tau,pair,mu,ldate)
    acorrplot,acorrplot2 = '%s/../plots/Acorr_%s'%(cbase,plotfilebase),'%s/../plots/Acorr_norm_%s'%(cbase,plotfilebase)
    if showresults: ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,weightFile,plotfilebase,showfullsample=showfullsample)
    #PPMC(T,posteriorFile,DataFile,ntrials,plotfile=None,plotfile2='/home/rumbaugh/Fermi/TimeBombs/plots/PPMC_Td_vs_tau_%s_testlightcurve.tau_%i_%i.mu_%.3f.%s.png'%(T,tau,pair,mu,date),figN=7,testplot=testplot,errstd=errstd,truetau=tau)
    crpost = np.loadtxt(posteriorFile)
    return crpost

errstd = 7.5
cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.10.15.dat')
tau5,mu5,tau10,mu10,tau15,mu15,tau20,mu20=cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4],cr[:,5],cr[:,6],cr[:,7]
#avg_fwidth,medtau,cliptau=np.zeros(len(pairs)),np.zeros(len(pairs)),np.zeros(len(pairs))
#for tau,it in zip(np.array([5,10,15,20]),np.arange(4)):
for tau,it in zip(np.array([20]),np.array([3])):
    avg_fwidth,medtau,cliptau,wt_tau=np.zeros(100),np.zeros(100),np.zeros(100),np.zeros(100)
    taus=cr[:,2*it]
    for i,pair in zip(np.array([30]),np.array([31])):
        mus=cr[:,2*it+1]
        mu=mus[i]
        crpost=reviewresults(pair,tau,mu,showresults=True)
        crw=np.loadtxt('%sweights.testlightcurve.tau_%i_%i.mu_%.3f.%s.dat'%(cbase,tau,pair,mu,ldate))
        crs=np.loadtxt('%ssample.testlightcurve.tau_%i_%i.mu_%.3f.%s.dat'%(cbase,tau,pair,mu,ldate))
        gw=np.argsort(crw)
        wt_tau[i]=np.abs(crs[:,1][gw[-1]])
        crFP = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve.tau_%i_%i.flare_params_truthvalues.mu_%.3f%s.dat'%(taus[i],i+1,mus[i],ldate))
        try:
            Tfl = crFP[:,3]
        except:
            Tfl = crFP[3]
        fwidths = crpost[:,210:310]
        post_taus = np.abs(crpost[:,1])
        truetau=np.abs(taus[i])
        avg_fwidth[i]=np.mean(fwidths[fwidths>0])
        fwidth_tmp = np.zeros(len(post_taus))
        for j in range(0,len(post_taus)): fwidth_tmp[j] = np.mean(fwidths[j][fwidths[j]>0])
        medtau[i]=np.median(post_taus)
        g_clip=ReverseSigmaClip(post_taus,truetau,sig=3)
        cliptau[i]=np.median(post_taus[g_clip])
        figure(27)
        clf()
        scatter(post_taus,fwidth_tmp,s=4)
        #axhline(4*np.mean(Tfl),color='red',ls='dotted',lw=2)
        axvline(truetau,ls='dotted',color='red',lw=2)
        scatter([medtau[i]],[avg_fwidth[i]],color='blue',marker='x',s=300,lw=4)
        scatter([wt_tau[i]],[avg_fwidth[i]],color='green',marker='+',s=300,lw=4)
        xlabel('Posterior Time Delay (days)')
        ylabel('Average Flare Scale (days)')
        if np.max(np.abs(post_taus)>300):
            if np.min(post_taus)<-300: scatter(np.ones(len(post_taus[post_taus<-300]))*-290,fwidth_tmp[post_taus<-300],color='k',marker='<',s=6)
            if np.max(post_taus)>300: scatter(np.ones(len(post_taus[post_taus>300]))*290,fwidth_tmp[post_taus>300],color='k',marker='>',s=6)
            xlim(-300,300)
        xmin,xmax=xlim()
        ymin,ymax=ylim()
        xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
        plot(xtmp,xtmp/3.502,color='cyan',ls='dashed',lw=1)
        plot([3.502*avg_fwidth[i],medtau[i]],avg_fwidth[i]*np.ones(2),ls='dotted',color='cyan',lw=2)
        xlim(xmin,xmax)
        ylim(ymin,ymax)
        #savefig('/home/rumbaugh/Fermi/TimeBombs/plots/tau_vs_fwidth.testlightcurve.tau_%i_%i.mu_%.3f%s.png'%(taus[i],i+1,mus[i],ldate))
