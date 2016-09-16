import numpy as np
import os

cbase='/home/rumbaugh/Fermi/TimeBombs/plots/'
cdate='7.17.15'
ddate='6.10.15'
date='7.17.15'

cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.10.15.dat')
tau5,mu5,tau10,mu10,tau15,mu15,tau20,mu20=cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4],cr[:,5],cr[:,6],cr[:,7]

for tau,it in zip(np.array([5,10,15,20]),np.array([0,1,2,3])):
    taus=cr[:,2*it]
    mus=cr[:,2*it+1]
    pairs=np.arange(100)+1
    for i,pair in zip(pairs-1,pairs):
        mu=mus[i]
        cfile='%s/corner_plt.tau_%i_%i_%s.png'%(cbase,tau,pair,cdate)
        dfile='/home/rumbaugh/Fermi/plots/testlightcurve.tau_%i_%i.mu_%.3f.%s.png'%(tau,pair,mu,ddate)
        os.system('cp %s /home/rumbaugh/Fermi/TimeBombs/plots/galleryfiles/Run1_tau_%i_pair%i_corner_plt.png'%(cfile,tau,pair))
        os.system('cp %s /home/rumbaugh/Fermi/TimeBombs/plots/galleryfiles/Run1_tau_%i_pair%i_Atestlightcurve.png'%(dfile,tau,pair))
os.chdir('/home/rumbaugh/git/scriptutils/perl')
os.sys('perl gallery.pl -o /home/rumbaugh/Fermi/TimeBombs/plots/galleryfiles/TimeBombs_corner_plots.%s.pdf /home/rumbaugh/Fermi/TimeBombs/plots/galleryfiles/Run1*pair*png -pdf -x 1')
