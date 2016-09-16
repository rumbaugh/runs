import numpy as np
import matplotlib.pylab as plt
execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')
date = '6.7.14'
ldate = '6.7.14'
for lens in ['1030','0712']:
#for lens in ['1030']:
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/Dispersions/%s.emcee_output_full_chain_interp_bs.%s.dat'%(lens,ldate))
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
    hist2d(tau,mu)#, extent=[extents[j], extents[i]],
                   #plot_contours=plot_contours,
                   #plot_datapoints=plot_datapoints,
                   #weights=weights, **kwargs)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/%s.chisq_conplot.interp.triangle_mod_plot.%s.png'%(lens,date))
