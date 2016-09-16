import numpy as np
import time
import matplotlib.pylab as py
try:
    lens
except NameError:
    lens = '1938'

date = '2.17.14'

infile = '/home/rumbaugh/EVLA/light_curves/Dispersions/dispmat.delta_var.1938.D_2.2.12.14.dat'
cr = np.loadtxt(infile)
tau,mu,disp = cr[:,0],cr[:,1],cr[:,2]
len_mu = len(tau[tau==tau[0]])
len_tau = len(mu[mu==mu[0]])
Z = np.reshape(disp,(len_tau,len_mu))
Ztau = np.reshape(tau,(len_tau,len_mu))[:,0]
Zmu = np.reshape(mu,(len_tau,len_mu))[0]
#V = np.min(Z)+np.array([2.3,6.18,11.8])
#V = np.arange(10)/10.*(np.max(Z)-np.min(Z))+np.min(Z)
V = np.exp(np.arange(10)/10.*(np.max(np.log(Z))-np.min(np.log(Z)))+np.min(np.log(Z)))
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
py.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/Disp.con_plot.1938.D_2.%s.ps'%(date))
for delta in np.arange(18)+2.5:
    infile = '/home/rumbaugh/EVLA/light_curves/Dispersions/dispmat.delta_var.1938.D_4_2.delta_%.1f.2.12.14.dat'%delta
    cr = np.loadtxt(infile)
    tau,mu,disp = cr[:,0],cr[:,1],cr[:,2]
    len_mu = len(tau[tau==tau[0]])
    len_tau = len(mu[mu==mu[0]])
    Z = np.reshape(disp,(len_tau,len_mu))
    Ztau = np.reshape(tau,(len_tau,len_mu))[:,0]
    Zmu = np.reshape(mu,(len_tau,len_mu))[0]
    V = np.array([2.5E-07,4.5E-07,8E-07,1.5E-6])
    #V = np.exp(np.arange(10)/10.*(np.max(np.log(Z))-np.min(np.log(Z)))+np.min(np.log(Z)))
    print 'delta = %4.1f'%delta
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
    py.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/Disp.con_plot.1938.D_4_2.delta_%.1f.%s.ps'%(delta,date))
