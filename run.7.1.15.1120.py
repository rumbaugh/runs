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

date='7.1.15'
ldate='5.13.15'
cbase='/home/rumbaugh/Fermi/TimeBombs/output/'

def reviewresults(pair,ldate='5.13.15',ddate='5.13.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=False,ntrials=10000,testplot=False,errstd=np.sqrt(2)*7.5,T='ACFT',showfullsample=False):
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    sampleFile='%ssample.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    sample_infoFile='%ssample_info.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    levelsFile='%slevels.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    DataFile='/home/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ddate)
    weightFile='%sweights.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    posteriorFile='%sposterior.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    plotfilebase='testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(pair,tau,mu,ldate)
    acorrplot,acorrplot2 = '%s/../plots/Acorr_%s'%(cbase,plotfilebase),'%s/../plots/Acorr_norm_%s'%(cbase,plotfilebase)
    if showresults: ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,weightFile,plotfilebase,showfullsample=showfullsample)
    #PPMC(T,posteriorFile,DataFile,ntrials,plotfile=None,plotfile2='/home/rumbaugh/Fermi/TimeBombs/plots/PPMC_Td_vs_tau_%s_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(T,pair,tau,mu,date),figN=7,testplot=testplot,errstd=errstd,truetau=tau)
    crpost = np.loadtxt(posteriorFile)
    return crpost

errstd = 7.5
cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.5.13.15.dat')
taus,mus=cr[:,0],cr[:,1]
#avg_fwidth,medtau,cliptau=np.zeros(len(pairs)),np.zeros(len(pairs)),np.zeros(len(pairs))
avg_fwidth,medtau,cliptau,wt_tau=np.zeros(100),np.zeros(100),np.zeros(100),np.zeros(100)
for i,pair in zip(pairs-1,pairs):
    crpost=reviewresults(pair,showresults=False)
    crFP = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f%s.dat'%(i+1,taus[i],mus[i],ldate))
    crw=np.loadtxt('%sweights.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,taus[i],mus[i],ldate))
    crs=np.loadtxt('%ssample.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,taus[i],mus[i],ldate))
    gw=np.argsort(crw)
    wt_tau[i]=np.abs(crs[:,1][gw[-1]])
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

    classifiers = dict((n_comp, GMM(n_components=n_comp)) for n_comp in np.arange(1,20))
    BICs=np.zeros(19)
    AICs=np.zeros(19)
    sort_post_taus=np.sort(post_taus)
    for index, (name, classifier) in enumerate(classifiers.items()):
        classifier.fit(sort_post_taus)
        BICs[index]=classifier.bic(sort_post_taus)
        AICs[index]=classifier.aic(sort_post_taus)
    n_compB=np.argsort(BICs)[0]+1
    n_compA=np.argsort(AICs)[0]+1
    classifierA=GMM(n_components=n_compA)
    classifierA.fit(taus)
    scoresA=classifierA.score_samples(sort_post_taus)
    groupindsA=np.argsort(scoresA[1])[:,-1]
    classifierB=GMM(n_components=n_compB)
    classifierB.fit(taus)
    scoresB=classifierB.score_samples(sort_post_taus)
    groupindsB=np.argsort(scoresB[1])[:,-1]


    figure(27)
    clf()
    cind,mind=0,0
    for group,gind in zip(np.arange(1,n_compA+1),np.arange(0,n_compA)):
        if len(sort_post_taus[groupindsA==gind])>0:
            hrange=np.max(sort_post_taus[groupindsA==gind])-np.min(sort_post_taus[groupindsA==gind])
            if hrange<=0:hrange=1.
            hist(sort_post_taus[groupindsA==gind],bins=ceil(hrange/5.),color=color_arr[cind])
            #scatter(sort_post_taus[groupindsA==gind],fwidth_tmp[np.argsort(post_taus)[groupindsA==gind]],s=4,color=color_arr[cind],marker=marker_arr[mind])
            cind+=1
            if cind >= len(color_arr):
                mind+=1
                cind=0
    #axhline(4*np.mean(Tfl),color='red',ls='dotted',lw=2)
    axvline(truetau,ls='dotted',color='red',lw=2)
    #scatter([medtau[i]],[avg_fwidth[i]],color='blue',marker='x',s=300,lw=4)
    #scatter([cliptau[i]],[avg_fwidth[i]],color='green',marker='+',s=300,lw=4)
    xlabel('Posterior Time Delay (days)')
    ylabel('Num. of Samples')
    if np.max(np.abs(post_taus)>300):
    #    if np.min(post_taus)<-300: scatter(np.ones(len(post_taus[post_taus<-300]))*-290,fwidth_tmp[post_taus<-300],color='k',marker='<',s=6)
    #    if np.max(post_taus)>300: scatter(np.ones(len(post_taus[post_taus>300]))*290,fwidth_tmp[post_taus>300],color='k',marker='>',s=6)
        xlim(0,300)
    xmin,xmax=xlim()
    ymin,ymax=ylim()
    xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
    #plot(xtmp,xtmp/3.502,color='cyan',ls='dashed',lw=1)
    #plot([3.502*avg_fwidth[i],medtau[i]],avg_fwidth[i]*np.ones(2),ls='dotted',color='cyan',lw=2)
    #xlim(xmin,xmax)
    #ylim(ymin,ymax)
    savefig('/home/rumbaugh/Fermi/TimeBombs/plots/tau_hist.testlightcurve_%i.tau_%.2f.mu_%.3f.AIC.%s.png'%(i+1,taus[i],mus[i],date))

    figure(28)
    clf()
    cind,mind=0,0
    for group,gind in zip(np.arange(1,n_compB+1),np.arange(0,n_compB)):
        if len(sort_post_taus[groupindsB==gind])>0:
            hrange=np.max(sort_post_taus[groupindsB==gind])-np.min(sort_post_taus[groupindsB==gind])
            if hrange<=0:hrange=1.
            hist(sort_post_taus[groupindsB==gind],bins=ceil(hrange/5.),color=color_arr[cind])
            cind+=1
            if cind >= len(color_arr):
                mind+=1
                cind=0
    #axhline(4*np.mean(Tfl),color='red',ls='dotted',lw=2)
    axvline(truetau,ls='dotted',color='red',lw=2)
    #scatter([medtau[i]],[avg_fwidth[i]],color='blue',marker='x',s=300,lw=4)
    #scatter([cliptau[i]],[avg_fwidth[i]],color='green',marker='+',s=300,lw=4)
    xlabel('Posterior Time Delay (days)')
    ylabel('Num. of Samples')
    if np.max(np.abs(post_taus)>300):
    #    if np.min(post_taus)<-300: scatter(np.ones(len(post_taus[post_taus<-300]))*-290,fwidth_tmp[post_taus<-300],color='k',marker='<',s=6)
    #    if np.max(post_taus)>300: scatter(np.ones(len(post_taus[post_taus>300]))*290,fwidth_tmp[post_taus>300],color='k',marker='>',s=6)
        xlim(0,300)
    xmin,xmax=xlim()
    ymin,ymax=ylim()
    xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
    #plot(xtmp,xtmp/3.502,color='cyan',ls='dashed',lw=1)
    #plot([3.502*avg_fwidth[i],medtau[i]],avg_fwidth[i]*np.ones(2),ls='dotted',color='cyan',lw=2)
    xlim(xmin,xmax)
    #ylim(ymin,ymax)
    savefig('/home/rumbaugh/Fermi/TimeBombs/plots/tau_hist.testlightcurve_%i.tau_%.2f.mu_%.3f.BIC.%s.png'%(i+1,taus[i],mus[i],date))
