import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GMM
execfile('/home/rumbaugh/ReverseSigmaClip.py')
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

pairs = np.arange(30)+1
#pairs = np.delete(pairs,np.array([1,2,3])-1)
#pairs = np.delete(pairs,np.array([17,18,31,35,37,40,42,53,54,56,57,58,72,74,85,100])-1)
npairs=len(pairs)
cutoff=-544

color_arr=np.array(['blue','red','cyan','magenta','green','brown','orange','yellow','pink'])
marker_arr=['o','+','x','D']

critwidth=3.716/2.35482

date='9.10.15'
ddate='8.19.15'
cbase='/home/rumbaugh/Fermi/TimeBombs/output/'

def reviewresults(pair,jiter,ldate='9.10.15',ddate='8.19.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=False,ntrials=10000,testplot=False,errstd=np.sqrt(2)*7.5,T='ACFT',showfullsample=False):
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    sampleFile='%ssample.testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,jiter,tau,mu,ldate)
    sample_infoFile='%ssample_info.testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,jiter,tau,mu,ldate)
    levelsFile='%slevels.testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,jiter,tau,mu,ldate)
    DataFile='/home/rumbaugh/Fermi/data/test/testlightcurve_%i_A.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ddate)
    weightFile='%sweights.testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,jiter,tau,mu,ldate)
    posteriorFile='%sposterior.testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,jiter,tau,mu,ldate)
    plotfilebase='testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.png'%(pair,jiter,tau,mu,ldate)
    acorrplot,acorrplot2 = '%s/../plots/Acorr_%s'%(cbase,plotfilebase),'%s/../plots/Acorr_norm_%s'%(cbase,plotfilebase)
    if showresults: ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,weightFile,plotfilebase,showfullsample=showfullsample)
    #PPMC(T,posteriorFile,DataFile,ntrials,plotfile=None,plotfile2='/home/rumbaugh/Fermi/TimeBombs/plots/PPMC_Td_vs_tau_%s_testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.png'%(T,pair,tau,mu,date),figN=7,testplot=testplot,errstd=errstd,truetau=tau)
    crpost = np.loadtxt(posteriorFile)
    return crpost

errstd = 7.5
cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.8.19.15.dat')
taus,mus=cr[:,0],cr[:,1]
#avg_fwidth,medtau,cliptau=np.zeros(len(pairs)),np.zeros(len(pairs)),np.zeros(len(pairs))
avg_fwidth,medtau,cliptau,wt_tau=np.zeros(npairs),np.zeros(npairs),np.zeros(npairs),np.zeros(npairs)
fulltaus,halftaus,halftaudiffs,expandtaudiffs=np.zeros(npairs),np.zeros(npairs*2),np.zeros(npairs),np.zeros(npairs*2)
for i,pair,j in zip(pairs-1,pairs,np.arange(npairs)):
    for jiter in range(0,10):
        print '%i_%i'%(pair,jiter)
        if pair<cutoff:
            crpost=reviewresults(pair,jiter,showresults=False)
        else:
            crpost=reviewresults(pair,jiter,showresults=True)
        #crFP = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.flare_params_truthvalues.%s.dat'%(i+1,'',taus[i],mus[i],ddate))
        #if jiter=='_A':
        #    crFP=crFP[crFP[:,0]<=550]
        #elif jiter=='_B':
        #    crFP=crFP[crFP[:,0]>550]
        #fwidths = crpost[:,210:310]
        post_taus = np.abs(crpost[:,1])
        truetau=np.abs(taus[i])
        #avg_fwidth[i]=np.mean(fwidths[fwidths>0])
        #fwidth_tmp = np.zeros(len(post_taus))
        #for j in range(0,len(post_taus)): fwidth_tmp[j] = np.mean(fwidths[j][fwidths[j]>0])
        medtau=np.median(post_taus)
        fulltaus[j]=medtau
        #g_clip=ReverseSigmaClip(post_taus,truetau,sig=3)
        #cliptau=np.median(post_taus[g_clip])
        maxclass=20
        if len(post_taus)<maxclass:maxclass=len(post_taus)
        classifiers = dict((n_comp, GMM(n_components=n_comp)) for n_comp in np.arange(1,maxclass))
        BICs=np.zeros(maxclass-1)
        AICs=np.zeros(maxclass-1)
        sort_post_taus=np.sort(post_taus)
        for index, (name, classifier) in enumerate(classifiers.items()):
            classifier.fit(sort_post_taus)
            BICs[index]=classifier.bic(sort_post_taus)
            AICs[index]=classifier.aic(sort_post_taus)
        n_compB=np.argsort(BICs)[0]+1
        n_compA=np.argsort(AICs)[0]+1
        classifierA=GMM(n_components=n_compA)
        classifierA.fit(sort_post_taus)
        scoresA=classifierA.score_samples(sort_post_taus)
        groupindsA=np.argsort(scoresA[1])[:,-1]
        classifierB=GMM(n_components=n_compB)
        classifierB.fit(sort_post_taus)
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
        ylabel('Fraction of Posterior')
        if np.max(np.abs(post_taus)>300):
            xlim(0,300)
        xmin,xmax=xlim()
        ymin,ymax=ylim()
        xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
        #plot(xtmp,xtmp/3.502,color='cyan',ls='dashed',lw=1)
        #plot([3.502*avg_fwidth[i],medtau[i]],avg_fwidth[i]*np.ones(2),ls='dotted',color='cyan',lw=2)
        #xlim(xmin,xmax)
        #ylim(ymin,ymax)
        def mjrFormatter(x, pos, maxperc=len(sort_post_taus)):
            return "%.2f"%(x*1./maxperc)
        if ymax*1./len(sort_post_taus) >= 0.5:
            fracstep=0.1
        elif ymax*1./len(sort_post_taus) <= 0.1:
            fracstep=0.01
        else:
            fracstep=0.05
        maxytick=int(ymax*1./len(sort_post_taus)/fracstep)+1
        ytickstep=fracstep*len(sort_post_taus)
        yticks(np.arange(0,maxytick*ytickstep,ytickstep))
        ax=gca()
        ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(mjrFormatter))
        draw()
        savefig('/home/rumbaugh/Fermi/TimeBombs/plots/tau_hist.testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.AIC.%s.png'%(i+1,jiter,taus[i],mus[i],date))

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
        ylabel('Fraction of Posterior')
        if np.max(np.abs(post_taus)>300):
            xlim(0,300)
        xmin,xmax=xlim()
        ymin,ymax=ylim()
        xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
        #plot(xtmp,xtmp/3.502,color='cyan',ls='dashed',lw=1)
        #plot([3.502*avg_fwidth[i],medtau[i]],avg_fwidth[i]*np.ones(2),ls='dotted',color='cyan',lw=2)
        xlim(xmin,xmax)
        #ylim(ymin,ymax)
        def mjrFormatter(x, pos, maxperc=len(sort_post_taus)):
            return "%.2f"%(x*1./maxperc)
        if ymax*1./len(sort_post_taus) >= 0.5:
            fracstep=0.1
        elif ymax*1./len(sort_post_taus) <= 0.1:
            fracstep=0.01
        else:
            fracstep=0.05
        maxytick=int(ymax*1./len(sort_post_taus)/fracstep)+1
        ytickstep=fracstep*len(sort_post_taus)
        yticks(np.arange(0,maxytick*ytickstep,ytickstep))
        ax=gca()
        ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(mjrFormatter))
        draw()
        savefig('/home/rumbaugh/Fermi/TimeBombs/plots/tau_hist.testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.BIC.%s.png'%(i+1,jiter,taus[i],mus[i],date))
