import numpy as np
import matplotlib.pylab as plt
execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')
try:
    kernel
except NameError:
    kernel = 'interp'
date = '8.18.14'
ldate = '8.18.14'
for lens in ['B0712']:
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/Dispersions/%s_jointfit.emcee_output_full_chain_%s_bs.%s.dat'%(lens,kernel,ldate))
    tau,mu = cr[:,0],cr[:,1]
    #plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.scatter(tau,mu)
    plt.xlabel('Time Delay (days)',fontsize=14)
    plt.ylabel('Magnification')
    plt.title('%s'%lens)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.chisq_conplot.%s.png'%(lens,date))
    plt.clf()
    #plt.figure = corner(cr,plot_hists=False)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    hist2d(tau,mu,V=np.array([0.682689,0.9545,0.9973]))#, extent=[extents[j], extents[i]],
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
    plt.ylim(3.840758,4.694260)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s_jointfit.chisq_conplot.%s.triangle_mod_plot.%s.png'%(lens,kernel,date))
