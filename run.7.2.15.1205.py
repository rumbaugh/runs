import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/ReverseSigmaClip.py')
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')

cbase='/home/rumbaugh/Fermi/TimeBombs/output/'

critwidth=3.716/2.35482

date='7.2.15'
ldate='6.10.15'

errstd = 7.5
cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.10.15.dat')
tau5,mu5,tau10,mu10,tau15,mu15,tau20,mu20=cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4],cr[:,5],cr[:,6],cr[:,7]

pairs=np.arange(100)+1

for tau,it in zip(np.array([10]),np.array([1])):
    avg_fwidth,medtau,cliptau=np.zeros(100),np.zeros(100),np.zeros(100)
    mean_amp,mean_skew,mean_Tfl=np.zeros(100),np.zeros(100),np.zeros(100)
    mean_pamp,mean_pskew,mean_pfwidth=np.zeros(100),np.zeros(100),np.zeros(100)
    mean_pnflares,true_nflares=np.zeros(100),np.zeros(100)
    taus=cr[:,2*it]
    mus=cr[:,2*it+1]
    pairs=np.arange(100)+1
    #if tau==5: pairs=np.delete(pairs,[72])
    for i,pair in zip(pairs-1,pairs):
        mu=mus[i]
        posteriorFile='%sposterior.testlightcurve.tau_%i_%i.mu_%.3f.%s.dat'%(cbase,tau,pair,mu,ldate)
        crpost = np.loadtxt(posteriorFile)
        crFP = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve.tau_%i_%i.flare_params_truthvalues.mu_%.3f%s.dat'%(taus[i],i+1,mus[i],ldate))
        try:
            amp,skew,Tfl = crFP[:,1],crFP[:,2],crFP[:,3]
            mean_amp[i],mean_skew[i],mean_Tfl[i]=np.average(amp),np.average(skew),np.average(Tfl)
            true_nflares[i]=np.shape(crFP)[0]
        except:
            amp,skew,Tfl = crFP[1],crFP[2],crFP[3]
            true_nflares[i]=1
            mean_amp[i],mean_skew[i],mean_Tfl[i]=amp,skew,Tfl
        fwidths = crpost[:,210:310]
        pamps,pskews = crpost[:,110:210],crpost[:,310:410]
        pnflares=crpost[:,9]
        mean_pnflares[i]=np.average(pnflares)
        post_taus = np.abs(crpost[:,1])
        truetau=np.abs(taus[i])
        avg_fwidth[i]=np.mean(fwidths[fwidths>0])
        fwidth_tmp,pamp_tmp,pskew_tmp = np.zeros(len(post_taus)),np.zeros(len(post_taus)),np.zeros(len(post_taus))
        for j in range(0,len(post_taus)): 
            fwidth_tmp[j] = np.mean(fwidths[j][:pnflares[j]])
            pamp_tmp[j] = np.mean(pamps[j][:pnflares[j]])
            pskew_tmp[j] = np.mean(pskews[j][:pnflares[j]])
        medtau[i]=np.median(post_taus)
        mean_pamp[i],mean_pskew[i],mean_pfwidth[i]=np.average(pamp_tmp),np.average(pskew_tmp),np.average(fwidth_tmp)
    plt.clf()
    figure(it+1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    #plt.scatter(tau,mu)
    #plt.xlabel('Time Delay (days)',fontsize=14)
    #plt.ylabel('Magnification')
    #plt.title('%s'%lens)
    #full_arr=np.concatenate(([np.abs(medtau-tau)],[tau/mean_pfwidth],[true_nflares],[mean_pnflares],[mean_amp],[mean_pamp],[mean_Tfl],[mean_pfwidth],[mean_skew],[mean_pskew]),axis=0)
    full_arr=np.concatenate(([np.abs(medtau-tau)],[mean_amp],[mean_pamp],[mean_Tfl],[mean_pfwidth]),axis=0)
    full_arr=full_arr[:,np.array(1-isnan(np.sum(full_arr,axis=0)),dtype='bool')]
    #label_arr=np.array(['DelTau','Norm.Tau','N(flares)','P.N(flares)','Amp.','P.Amp.','Tfl','P.Width','Skew','P.Skew'])
    label_arr=np.array(['Tau Accuracy','True Amp.','Post. Amp.','True Width','Post.Width'])
    #extent_dict={5:[1.,1.,1.,1.,1.,1.,1.,(0,42),1.,(0,12)],10:[1.,1.,1.,1.,1.,1.,1.,(0,52),1.,(0,30)],15:[1.,1.,1.,1.,1.,1.,1.,(0,35),1.,(0,25)],20:[1.,1.,1.,1.,1.,1.,1.,(0,40),1.,(0,7.5)]}
    extent_dict={5:[1.,1.,1.,1.,(0,42)],10:[1.,1.,1.,1.,(0,52)],15:[1.,1.,1.,1.,(0,35)],20:[1.,1.,1.,1.,(0,40)]}
    figure=corner(np.transpose(full_arr),labels=label_arr,extents=extent_dict[tau])
    #corner(np.transpose(full_arr))
    plt.savefig('/home/rumbaugh/Fermi/TimeBombs/plots/corner_plt.tau_%i_%s.png'%(tau,date))
   
