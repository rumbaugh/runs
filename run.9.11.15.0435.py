import numpy as np
import os

cbase='/home/rumbaugh/Fermi/TimeBombs/plots/'

cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.10.15.dat')
tau5,mu5,tau10,mu10,tau15,mu15,tau20,mu20=cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4],cr[:,5],cr[:,6],cr[:,7]

os.chdir('/home/rumbaugh/git/scriptutils/perl')
os.system('perl gallery.pl -o /home/rumbaugh/Fermi/TimeBombs/plots/galleryfiles/TimeBombs_lengthtest_plots.9.11.15.pdf /home/rumbaugh/Fermi/TimeBombs/plots/galleryfiles/lengthtest/*png -pdf -x 2 -y 2')
