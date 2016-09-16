import numpy as np
import time
import matplotlib.pylab as py
try:
    lens
except NameError:
    lens = '1938'

infile = '/home/rumbaugh/EVLA/light_curves/Dispersions/Disp_grid_out.%s.10.23.13.dat'%lens
cr = np.loadtxt(infile)
tau,mu,disp = cr[:,0],cr[:,1],cr[:,2]
len_mu = len(tau[tau==tau[0]])
len_tau = len(mu[mu==mu[0]])
Z = np.reshape(disp,(len_tau,len_mu))
Ztau = np.reshape(tau,(len_tau,len_mu))[:,0]
Zmu = np.reshape(mu,(len_tau,len_mu))[0]
try:
    V
except NameError:
    V = np.exp(np.arange(8)/8.*(np.log(np.max(Z))-np.log(np.min(Z)))*0.95+np.log(np.min(Z)*1.05))
py.clf()
py.rc('axes',linewidth=2)
py.fontsize = 14
py.tick_params(which='major',length=8,width=2,labelsize=14)
py.tick_params(which='minor',length=4,width=1.5,labelsize=14)
py.contour(Zmu,Ztau,Z,V,colors='k')
py.xlabel('Magnification')
py.ylabel('Time Delay (days)')
py.fontsize = 14
py.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/Disp.con_plot.%s.10.23.13.ps'%lens)
