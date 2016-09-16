import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/ReverseSigmaClip.py')
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

pairs = np.arange(100)+1
#pairs = np.delete(pairs,[14,25,39,48,55,57,75,78])
pairs = np.delete(pairs,[14,25,39,48,55,57,75,78,79,90,92])

critwidth=3.716/2.35482

date='6.10.15'
ldate='5.13.15'

def reviewresults(pair,ldate='5.13.15',ddate='5.13.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=False,ntrials=10000,testplot=False,errstd=np.sqrt(2)*7.5,T='ACFT',showfullsample=False):
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    sampleFile='%ssample.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    sample_infoFile='%ssample_info.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    levelsFile='%slevels.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    DataFile='/home/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ddate)
    posteriorFile='%sposterior.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    plotfilebase='testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(pair,tau,mu,ldate)
    acorrplot,acorrplot2 = '%s/../plots/Acorr_%s'%(cbase,plotfilebase),'%s/../plots/Acorr_norm_%s'%(cbase,plotfilebase)
    if showresults: ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,plotfilebase,showfullsample=showfullsample)
    #PPMC(T,posteriorFile,DataFile,ntrials,plotfile=None,plotfile2='/home/rumbaugh/Fermi/TimeBombs/plots/PPMC_Td_vs_tau_%s_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(T,pair,tau,mu,date),figN=7,testplot=testplot,errstd=errstd,truetau=tau)
    crpost = np.loadtxt(posteriorFile)
    return crpost

errstd = 7.5
cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.5.13.15.dat')
taus,mus=cr[:,0],cr[:,1]
#avg_fwidth,medtau,cliptau=np.zeros(len(pairs)),np.zeros(len(pairs)),np.zeros(len(pairs))
avg_fwidth,medtau,cliptau=np.zeros(100),np.zeros(100),np.zeros(100)
for i,pair in zip(pairs-1,pairs):
    crpost=reviewresults(pair)
    crFP = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f%s.dat'%(i+1,taus[i],mus[i],ldate))
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
    #scatter([cliptau[i]],[avg_fwidth[i]],color='green',marker='+',s=300,lw=4)
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
    #savefig('/home/rumbaugh/Fermi/TimeBombs/plots/tau_vs_fwidth.testlightcurve_%i.tau_%.2f.mu_%.3f%s.png'%(i+1,taus[i],mus[i],ldate))
figure(25)
clf()
scatter(taus[avg_fwidth!=0],np.abs(medtau[avg_fwidth!=0]-taus[avg_fwidth!=0]),s=4)
g=np.where(taus[avg_fwidth!=0]/avg_fwidth[avg_fwidth!=0]<3.502)[0]
scatter(taus[avg_fwidth!=0][g],np.abs(medtau[avg_fwidth!=0][g]-taus[avg_fwidth!=0][g]),s=4,color='cyan')
#scatter(taus[avg_fwidth!=0]/avg_fwidth[avg_fwidth!=0],np.abs(medtau[avg_fwidth!=0]-taus[avg_fwidth!=0]),s=4)
#g=np.where(medtau[avg_fwidth!=0]<3.502*avg_fwidth[avg_fwidth!=0])[0]
#if len(g)>0:scatter(taus[avg_fwidth!=0][g]/avg_fwidth[avg_fwidth!=0][g],np.abs(medtau[avg_fwidth!=0][g]-taus[avg_fwidth!=0][g]),s=4,color='red')
#axvline(3.502,color='cyan',ls='dashed',lw=2)
xlabel('Normalized True Delay (Flare widths)')
ylabel('Absolute Deviation from True Delay (days)')
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/Timebombs_accuracy_vs_tau.%s.png'%date)
figure(29)
clf()
scatter(taus[avg_fwidth!=0]/avg_fwidth[avg_fwidth!=0],medtau[avg_fwidth!=0]-taus[avg_fwidth!=0],s=4)
g=np.where(medtau[avg_fwidth!=0]<3.502*avg_fwidth[avg_fwidth!=0])[0]
if len(g)>0:scatter(taus[avg_fwidth!=0][g]/avg_fwidth[avg_fwidth!=0][g],medtau[avg_fwidth!=0][g]-taus[avg_fwidth!=0][g],s=4,color='red')
axvline(3.502,color='cyan',ls='dashed',lw=2)
xlabel('Normalized True Delay (Flare widths)')
ylabel('Deviation from True Delay (days)')
#savefig('/home/rumbaugh/Fermi/TimeBombs/plots/Timebombs_bias_vs_flarewidths.%s.png'%date)
figure(26)
clf()
scatter(taus[avg_fwidth!=0]/avg_fwidth[avg_fwidth!=0],np.abs(cliptau[avg_fwidth!=0]-taus[avg_fwidth!=0]),s=4)
g=np.where(cliptau[avg_fwidth!=0]<3.502*avg_fwidth[avg_fwidth!=0])[0]
if len(g)>0:scatter(taus[avg_fwidth!=0][g]/avg_fwidth[avg_fwidth!=0][g],np.abs(cliptau[avg_fwidth!=0][g]-taus[avg_fwidth!=0][g]),s=4,color='red')
axvline(3.502,color='cyan',ls='dashed',lw=2)
xlabel('Normalized True Delay (Flare widths)')
ylabel('Absolute Deviation from True Delay (days) Using Clip Locator')
#savefig('/home/rumbaugh/Fermi/TimeBombs/plots/Timebombs_accuracy_vs_flarewidths.clip_loc.%s.png'%date)
