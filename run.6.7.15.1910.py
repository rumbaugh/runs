import numpy as np
import matplotlib.pyplot as plt
import copy
execfile('/home/rumbaugh/ReverseSigmaClip.py')
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

num_nbrs=10

color_arr=np.array(['blue','red','cyan','magenta','green','brown','orange','yellow','pink'])
marker_arr=['o','+','x','D']

pairs = np.arange(100)+1
#pairs = np.delete(pairs,[14,25,39,48,55,57,75,78])
pairs = np.delete(pairs,[14,25,39,48,55,57,75,78,79,90,92])

critwidth=3.716/2.35482

date='6.7.15'
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
    #g_clip=ReverseSigmaClip(post_taus,truetau,sig=3)
    g_dict=FindGroups(post_taus,sig=4,num_nbrs=num_nbrs)
    #cliptau[i]=np.median(post_taus[g_clip])
    figure(27)
    clf()
    ci,mi=0,0
    scatter(post_taus,fwidth_tmp,color='black',s=2)
    for k in g_dict.keys():
        scatter(post_taus[g_dict[k]['group']],fwidth_tmp[g_dict[k]['group']],color=color_arr[ci],marker=marker_arr[mi],s=6)
        ci += 1
        if ci >= len(color_arr):
            ci=0
            mi+=1
    #scatter(post_taus,fwidth_tmp,s=4)
    #axhline(4*np.mean(Tfl),color='red',ls='dotted',lw=2)
    axvline(truetau,ls='dotted',color='red',lw=2)
    #scatter([medtau[i]],[avg_fwidth[i]],color='blue',marker='x',s=300,lw=4)
    #scatter([cliptau[i]],[avg_fwidth[i]],color='green',marker='+',s=300,lw=4)
    xlabel('Posterior Time Delay (days)')
    ylabel('Average Flare Scale (days)')
    if np.max(np.abs(post_taus)>300):
        if np.min(post_taus)<-300: scatter(np.ones(len(post_taus[post_taus<-300]))*-195,fwidth_tmp[post_taus<-300],color='k',marker='<',s=6)
        if np.max(post_taus)>300: scatter(np.ones(len(post_taus[post_taus>300]))*195,fwidth_tmp[post_taus>300],color='k',marker='>',s=6)
        xlim(-300,300)
    xmin,xmax=xlim()
    ymin,ymax=ylim()
    xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
    plot(xtmp,xtmp/3.502,color='cyan',ls='dashed',lw=1)
    plot([3.502*avg_fwidth[i],medtau[i]],avg_fwidth[i]*np.ones(2),ls='dotted',color='cyan',lw=2)
    xlim(xmin,xmax)
    ylim(ymin,ymax)
    savefig('/home/rumbaugh/Fermi/TimeBombs/plots/tau_vs_fwidth.testlightcurve_%i.tau_%.2f.mu_%.3f%s.png'%(i+1,taus[i],mus[i],ldate))
