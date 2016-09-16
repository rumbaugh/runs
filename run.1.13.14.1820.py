import numpy as np
import time
import matplotlib.pylab as py
try:
    lens
except NameError:
    lens = '1030'

infile1 = '/home/rumbaugh/EVLA/light_curves/Dispersions/Chisq_grid_out.%s.1.13.14.dat'%lens
infile2 = '/home/rumbaugh/EVLA/light_curves/Dispersions/Chisq_grid_out.%s.1.2.14.dat'%lens
cr1 = np.loadtxt(infile1)
tau1,mu1,disp1 = cr1[:,0],cr1[:,1],cr1[:,2]
cr2 = np.loadtxt(infile2)
tau,mu,disp2 = cr2[:,0],cr2[:,1],cr2[:,2]
disp = (disp1-disp2)/disp1
len_mu = len(tau[tau==tau[0]])
len_tau = len(mu[mu==mu[0]])
Z = np.reshape(disp,(len_tau,len_mu))
Ztau = np.reshape(tau,(len_tau,len_mu))[:,0]
Zmu = np.reshape(mu,(len_tau,len_mu))[0]
#V = np.min(Z)+np.array([2.3,6.18,11.8])
V = np.arange(10)/10.*(np.max(Z)-np.min(Z))+np.min(Z)
print V
py.clf()
py.rc('axes',linewidth=2)
py.fontsize = 14
py.tick_params(which='major',length=8,width=2,labelsize=14)
py.tick_params(which='minor',length=4,width=1.5,labelsize=14)
py.contour(Ztau,Zmu,np.transpose(Z),V,colors='k')
py.ylabel('Magnification')
py.xlabel('Time Delay (days)')
py.fontsize = 14
py.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/Diffplot.chisq.con_plot.%s.1.13.14.ps'%lens)
