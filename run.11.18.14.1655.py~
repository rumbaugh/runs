import numpy as np
import matplotlib.pylab as plt
execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')
date = '9.12.14'
ldate = '9.12.14'
tau1030 = 156/1.4

for lens in ['1030','0712']:
#for lens in ['1030']:
    nbins = 70
    ldate = '9.12.14'
    if lens == '1938': 
        nbins = 40
        ldate = '6.8.14'
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/Dispersions/%s.emcee_output_full_chain_interp_bs.%s.dat'%(lens,ldate))
    tau,mu = cr[:,0],cr[:,1]
    if lens == '0712': tau *= -1
    #plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.hist(tau,bins=nbins,color='white',lw=2)
    plt.xlabel('Time Delay (days)',fontsize=14)
    plt.ylabel('Number of Trials (thousands)',fontsize=14)
    plt.title('%s'%lens)
    if lens == '0712': 
        plt.axvline(9,lw=2,c='k',ls='dashed')
        plt.xlim(-105,105)
    if lens == '1938':plt.xlim(-60,60)
    if lens == '1030':
        plt.axvline(tau1030,lw=2,c='k',ls='dashed')
        plt.xlim(-155,155)
    yticklocs = plt.yticks()[0]
    plt.yticks(yticklocs,np.array(np.array(yticklocs/1000,dtype='int'),dtype='string'))
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.tau_hist_plot.%s.png'%(lens,date))
    plt.clf()
    #plt.figure = corner(cr,plot_hists=False)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    source = lens
    if source == '0712':
        plt.ylim(3.840758,4.694260)
    if source == '1030':
        plt.ylim(10.870289,13.285909)
    if source == '1938':
        plt.ylim(4.75,5.375)
    hist2d(tau,1./mu,V=np.array([0.682689,0.9545,0.9973]))#, extent=[extents[j], extents[i]],
    #hist2d(tau,mu,V=np.array([4,11,406])/100000.)#, extent=[extents[j], extents[i]],
                   #plot_contours=plot_contours,
                   #plot_datapoints=plot_datapoints,
                   #weights=weights, **kwargs)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.xlabel('Time Delay (days)',fontsize=14)
    plt.ylabel('Magnification',fontsize=14)
    source = lens
    if source == '0712':
        plt.ylim(3.840758,4.694260)
    if source == '1938':
        plt.ylim(4.75,5.375)
    if lens == '1938':plt.xlim(-60,60)
    yticklocs = plt.yticks()[0]
    if lens == '0712': 
        plt.xlim(-105,105)
        plt.axvline(9,lw=2,c='k',ls='dashed')
        plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.chisq_conplot.interp.triangle_mod_plot.%s.png'%(lens,date))
    if source == '1030':
        plt.xlim(-155,155)
        plt.ylim(10.870289,13.285909)
        plt.axvline(tau1030,lw=2,c='k',ls='dashed')
        plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.chisq_conplot.interp.triangle_mod_plot.%s.png'%(lens,date))
