import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
import emcee
execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')

ldate = '12.11.14'
date = '12.15.14'

for lens in ['0712','1030']:
    cr = np.loadtxt('/home/rumbaugh/EVLA/light_curves/Dispersions/simulations/flat_sims.%s.interp_bs.%s.dat'%(lens,ldate),dtype={'names': ('tau', 'tau_err', 'mu', 'mu_err'), 'formats': ('float','float','float','float')})
    tau,mu = cr['tau'],cr['mu']
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    hist2d(tau,1./mu,V=np.array([0.682689,0.9545,0.9973]))#, extent=[extents[j], extents[i]],
    plt.xlabel('Time Delay (days)',fontsize=14)
    plt.ylabel('Magnification',fontsize=14)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/simulations/flatsim.%s.chisq_conplot.interp.triangle_mod_plot.%s.png'%(lens,date))
