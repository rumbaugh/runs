import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GMM
execfile('/home/rumbaugh/ReverseSigmaClip.py')
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

pairs = np.arange(100)+1
#pairs = np.delete(pairs,[14,25,39,48,55,57,75,78,79,90,92])


color_arr=np.array(['blue','red','cyan','magenta','green','brown','orange','yellow','pink'])
marker_arr=['o','+','x','D']

critwidth=3.716/2.35482

date='8.19.15'
ddate='8.19.15'
cbase='/home/rumbaugh/Fermi/TimeBombs/output/'

def reviewresults(pair,suffix,ldate='8.18.15',ddate='5.13.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=False,ntrials=10000,testplot=False,errstd=np.sqrt(2)*7.5,T='ACFT',showfullsample=False):
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
avg_fwidth,medtau,cliptau,wt_tau=np.zeros(100),np.zeros(100),np.zeros(100),np.zeros(100)
fulltaus,halftaus,halftaudiffs,expandtaudiffs=np.zeros(100),np.zeros(200),np.zeros(100),np.zeros(200)
for i,pair in zip(pairs-1,pairs):
    for suffix in ['','_A','_B']:
        crpost=reviewresults(pair,suffix,showresults=True)
        crFP = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i%s.tau_%.2f.mu_%.3f.flare_params_truthvalues.%s.dat'%(i+1,'',taus[i],mus[i],ddate))
        if suffix=='_A':
            crFP=crFP[crFP[:,0]<=550]
        elif suffix=='_B':
            crFP=crFP[crFP[:,0]>550]
        fwidths = crpost[:,210:310]
        post_taus = np.abs(crpost[:,1])
        truetau=np.abs(taus[i])
        #avg_fwidth[i]=np.mean(fwidths[fwidths>0])
        #fwidth_tmp = np.zeros(len(post_taus))
        #for j in range(0,len(post_taus)): fwidth_tmp[j] = np.mean(fwidths[j][fwidths[j]>0])
        medtau=np.median(post_taus)
        if suffix=='':
            fulltaus[i]=medtau
        elif suffix=='_A':
            halftaus[2*i]=medtau
        else:
            halftaus[2*i+1]=medtau
        #g_clip=ReverseSigmaClip(post_taus,truetau,sig=3)
        #cliptau=np.median(post_taus[g_clip])

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
        savefig('/home/rumbaugh/Fermi/TimeBombs/plots/tau_hist.testlightcurve_%i%s.tau_%.2f.mu_%.3f.AIC.%s.png'%(i+1,suffix,taus[i],mus[i],date))

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
        savefig('/home/rumbaugh/Fermi/TimeBombs/plots/tau_hist.testlightcurve_%i%s.tau_%.2f.mu_%.3f.BIC.%s.png'%(i+1,suffix,taus[i],mus[i],date))
fullabstaus=np.abs(fulltaus)
halfabstaus=np.abs(halftaus)
halfdiffs=np.abs(halfabstaus[np.arange(0,len(fulltaus),2)]-halfabstaus[np.arange(0,len(fulltaus),2)+1])
fulldiffs=np.zeros(len(halftaus))
fulldiffs[np.arange(0,len(fulltaus),2)]=np.abs(fullabstaus-halfabstaus[np.arange(0,len(fulltaus),2)])
fulldiffs[np.arange(0,len(fulltaus),2)+1]=np.abs(fullabstaus-halfabstaus[np.arange(0,len(fulltaus),2)+1])
fullacc=np.abs(fullabstaus-taus)
halfacc=np.zeros(200)
halfacc[np.arange(0,len(fulltaus),2)]=np.abs(halfabstaus[np.arange(0,len(fulltaus),2)]-taus)
halfacc[np.arange(0,len(fulltaus),2)+1]=np.abs(halfabstaus[np.arange(0,len(fulltaus),2)+1]-taus)

figure(28)
clf()
hist(halfdiffs,bins=20)
xlabel('Difference in Posterior Time Delay Between Half Ranges(days)')
ylabel('Fraction of Posterior')
xmin,xmax=xlim()
ymin,ymax=ylim()
xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
xlim(xmin,xmax)
def mjrFormatter(x, pos, maxperc=len(halfdiffs)):
    return "%.2f"%(x*1./maxperc)
if ymax*1./len(halfdiffs) >= 0.5:
    fracstep=0.1
elif ymax*1./len(halfdiffs) <= 0.1:
    fracstep=0.01
else:
    fracstep=0.05
maxytick=int(ymax*1./len(halfdiffs)/fracstep)+1
ytickstep=fracstep*len(halfdiffs)
yticks(np.arange(0,maxytick*ytickstep,ytickstep))
ax=gca()
ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(mjrFormatter))
draw()
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/halfdiffs.tau_posterior.8.19.15.png')


figure(27)
clf()
hist(fulldiffs,bins=20)
xlabel('Difference in Posterior Time Delay Between Full and Half Range(days)')
ylabel('Fraction of Posterior')
xmin,xmax=xlim()
ymin,ymax=ylim()
xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
xlim(xmin,xmax)
def mjrFormatter(x, pos, maxperc=len(fulldiffs)):
    return "%.2f"%(x*1./maxperc)
if ymax*1./len(fulldiffs) >= 0.5:
    fracstep=0.1
elif ymax*1./len(fulldiffs) <= 0.1:
    fracstep=0.01
else:
    fracstep=0.05
maxytick=int(ymax*1./len(fulldiffs)/fracstep)+1
ytickstep=fracstep*len(fulldiffs)
yticks(np.arange(0,maxytick*ytickstep,ytickstep))
ax=gca()
ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(mjrFormatter))
draw()
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/fulldiffs.tau_posterior.8.19.15.png')


figure(29)
clf()
hist((np.append(fullacc,fullacc),halfacc),bins=40)
xlabel('Tau Accuracy')
ylabel('')
xmin,xmax=xlim()
ymin,ymax=ylim()
xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
xlim(xmin,xmax)
def mjrFormatter(x, pos, maxperc=len(halfdiffs)):
    return "%.2f"%(x*1./maxperc)
if ymax*1./len(halfdiffs) >= 0.5:
    fracstep=0.1
elif ymax*1./len(halfdiffs) <= 0.1:
    fracstep=0.01
else:
    fracstep=0.05
maxytick=int(ymax*1./len(halfdiffs)/fracstep)+1
ytickstep=fracstep*len(halfdiffs)
yticks(np.arange(0,maxytick*ytickstep,ytickstep))
ax=gca()
ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(mjrFormatter))
draw()
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/fulldiffs.tau_posterior.8.19.15.png')


