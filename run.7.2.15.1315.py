import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/ReverseSigmaClip.py')
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

pairs = np.arange(100)+1
#pairs = np.delete(pairs,[14,25,39,48,55,57,75,78])
#pairs = np.delete(pairs,[14,25,39,48,55,57,75,78,79,90,92])

critwidth=3.716/2.35482

oldate='5.13.15'
date='7.2.15'
ldate='7.1.15'
cbase='/home/rumbaugh/Fermi/TimeBombs/output/'

cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.5.13.15.dat')

def reviewresults(pair,ldate='7.1.15',ddate='7.1.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=True,ntrials=10000,testplot=False,errstd=np.sqrt(2)*7.5,T='ACFT',showfullsample=False):
    sampleFile='%ssample.testlightcurve_notau_%i.%s.dat'%(cbase,pair,ldate)
    sample_infoFile='%ssample_info.testlightcurve_notau_%i.%s.dat'%(cbase,pair,ldate)
    levelsFile='%slevels.testlightcurve_notau_%i.%s.dat'%(cbase,pair,ldate)
    DataFile='/home/rumbaugh/Fermi/data/test/testlightcurve_notau_%i.%s.dat'%(pair,ddate)
    posteriorFile='%sposterior.testlightcurve_notau_%i.%s.dat'%(cbase,pair,ldate)
    weightFile='%sweights.testlightcurve_notau_%i.%s.dat'%(cbase,pair,ldate)
    plotfilebase='testlightcurve_notau_%i.%s.png'%(pair,ldate)
    acorrplot,acorrplot2 = '%s/../plots/Acorr_%s'%(cbase,plotfilebase),'%s/../plots/Acorr_norm_%s'%(cbase,plotfilebase)
    if showresults: ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,weightFile,plotfilebase,showfullsample=showfullsample)
    #PPMC(T,posteriorFile,DataFile,ntrials,plotfile=None,plotfile2='/home/rumbaugh/Fermi/TimeBombs/plots/PPMC_Td_vs_tau_%s_testlightcurve_notau_%i.%s.png'%(T,pair,date),figN=7,testplot=testplot,errstd=errstd,truetau=tau)
    crpost = np.loadtxt(posteriorFile)
    return crpost

def reviewresults2(pair,ldate='5.13.15',ddate='5.13.15',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=False,ntrials=10000,testplot=False,errstd=np.sqrt(2)*7.5,T='ACFT',showfullsample=False):
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
taus,mus=cr[:,0],cr[:,1]
#tau5,mu5,tau10,mu10,tau15,mu15,tau20,mu20=cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4],cr[:,5],cr[:,6],cr[:,7]
#avg_fwidth,medtau,cliptau=np.zeros(len(pairs)),np.zeros(len(pairs)),np.zeros(len(pairs))
#for tau,it in zip(np.array([5,10,15,20]),np.arange(4)):
avg_fwidth,medtau,avg_fwidth2,medtau2=np.zeros(100),np.zeros(100),np.zeros(100),np.zeros(100)
pairs=np.arange(100)+1
pairs=np.delete(pairs,[55])
for i,pair in zip(pairs-1,pairs):
    tau,mu=taus[i],mus[i]
    crpost=reviewresults(pair,showresults=False)
    crpost2=reviewresults2(pair,showresults=False)
    crw=np.loadtxt('%sweights.testlightcurve_notau_%i.%s.dat'%(cbase,pair,ldate))
    crs=np.loadtxt('%ssample.testlightcurve_notau_%i.%s.dat'%(cbase,pair,ldate))
    gw=np.argsort(crw)
    crFP = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_notau_%i.flare_params_truthvalues.%s.dat'%(i+1,ldate))
    try:
        crFP2 = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f%s.dat'%(i+1,tau,mu,oldate))
    except:
        try:
            crFP2 = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f%s.dat'%(i+1,tau+0.01,mu,oldate))
        except:
            try:
                crFP2 = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f%s.dat'%(i+1,tau-0.01,mu,oldate))
            except:
                try:
                    crFP2 = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f%s.dat'%(i+1,tau,mu+0.001,oldate))
                except:
                    try:
                        crFP2 = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f%s.dat'%(i+1,tau,mu-0.001,oldate))
                    except:
                        try:
                            crFP2 = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f%s.dat'%(i+1,tau,mu-0.002,oldate))
                        except:
                            try:
                                crFP2 = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f%s.dat'%(i+1,tau,mu+0.002,oldate))
                            except:
                                crFP2 = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_%i.flare_params_truthvalues.tau_%.2f.mu_%.3f%s.dat'%(i+1,tau-0.001,mu,oldate))
    try:
        Tfl = crFP2[:,3]
    except:
        Tfl = crFP2[3]
    fwidths = crpost[:,210:310]
    fwidths2 = crpost2[:,210:310]
    post_taus = np.abs(crpost[:,1])
    post_taus2 = np.abs(crpost2[:,1])
    avg_fwidth[i]=np.mean(fwidths[fwidths>0])
    avg_fwidth2[i]=np.mean(fwidths2[fwidths2>0])
    fwidth_tmp = np.zeros(len(post_taus))
    for j in range(0,len(post_taus)): fwidth_tmp[j] = np.mean(fwidths[j][fwidths[j]>0])
    medtau[i]=np.median(post_taus)
    medtau2[i]=np.median(post_taus2)
    figure(27)
    clf()
    dum_post_taus=np.copy(post_taus)
    dum_post_taus[dum_post_taus>300]=300
    hist(dum_post_taus)
    xlabel('Posterior Time Delay (days)')
    ylabel('Num. of Samples')
    if np.max(np.abs(post_taus)>300):
        xlim(0,300)
    xmin,xmax=xlim()
    ymin,ymax=ylim()
    savefig('/home/rumbaugh/Fermi/TimeBombs/plots/tau_hist.testlightcurve_notau_%i.%s.png'%(i+1,ldate))
figure(28)
clf()
dum_medtau=np.copy(medtau)
dum_medtau[dum_medtau>300]=300
hist(dum_medtau)
xlabel('Median Time Delay (days)')
ylabel('Num. of Samples')
if np.max(np.abs(medtau)>300):
    xlim(0,300)
xmin,xmax=xlim()
ymin,ymax=ylim()
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/medtau_hist.testlightcurve_notau.%s.png'%(ldate))
figure(38)
clf()
dum_medtau=np.copy(medtau)
dum_medtau[dum_medtau>300]=300
#hist(dum_medtau,color='blue')
#hist(medtau2,color='red')
hist((dum_medtau,medtau2[isnan(medtau2)==False]),color=('blue','red'))
xlabel('Median Time Delay (days)')
ylabel('Num. of Samples')
if np.max(np.abs(medtau)>300):
    xlim(0,300)
xmin,xmax=xlim()
ymin,ymax=ylim()
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/medtau_hist.testlightcurve_notau_vs_tau.%s.png'%(ldate))
figure(29)
clf()
dum_medtau=np.copy(medtau)
scatter(dum_medtau,avg_fwidth,s=4)
xlabel('Median Time Delay (days)')
ylabel('Num. of Samples')
if np.max(np.abs(medtau)>300):
    if np.max(medtau)>300: scatter(np.ones(len(medtau[medtau>300]))*290,fwidth_tmp[medtau>300],color='k',marker='>',s=6)
    xlim(0,300)
xmin,xmax=xlim()
ymin,ymax=ylim()
xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
plot(xtmp,xtmp/3.502,color='cyan',ls='dashed',lw=1)
#plot([3.502*avg_fwidth[i],medtau[i]],avg_fwidth[i]*np.ones(2),ls='dotted',color='cyan',lw=2)
xlim(xmin,xmax)
ylim(ymin,ymax)
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/medtau_vs_fwidth.testlightcurve_notaus.%s.png'%(ldate))
figure(30)
clf()
dum_medtau=np.copy(medtau)
scatter(dum_medtau,avg_fwidth,s=4,color='blue')
scatter(medtau2,avg_fwidth2,s=4,color='red')
xlabel('Median Time Delay (days)')
ylabel('Num. of Samples')
if np.max(np.abs(medtau)>300):
    if np.max(medtau)>300: scatter(np.ones(len(medtau[medtau>300]))*290,avg_fwidth[medtau>300],color='k',marker='>',s=6)
    xlim(0,300)
if np.max(np.abs(medtau2)>300):
    if np.max(medtau2)>300: scatter(np.ones(len(medtau2[medtau2>300]))*290,avg_fwidth2[medtau2>300],color='k',marker='>',s=6)
    xlim(0,300)
xmin,xmax=xlim()
ymin,ymax=ylim()
xtmp=np.arange(xmin,xmax,(xmax-xmin)*1./10000)
plot(xtmp,xtmp/3.502,color='cyan',ls='dashed',lw=1)
#plot([3.502*avg_fwidth[i],medtau[i]],avg_fwidth[i]*np.ones(2),ls='dotted',color='cyan',lw=2)
xlim(xmin,xmax)
ylim(ymin,ymax)
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/medtau_vs_fwidth.testlightcurve_notau_vs_taus.%s.png'%(ldate))
