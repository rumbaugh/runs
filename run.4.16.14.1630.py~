import numpy as np
import time
import matplotlib.pylab as py

date = '4.16.14'
ldate = '4.16.14'

disp_type,delta = 'D_4_2',10.5

infile = '/mnt/data2/rumbaugh/Fermi/output/0218/disp_out.daily_lc.%s.delta_%4.1f.%s.dat'%(disp_type,delta,ldate)
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
#print V
py.clf()
py.rc('axes',linewidth=2)
py.fontsize = 14
py.tick_params(which='major',length=8,width=2,labelsize=14)
py.tick_params(which='minor',length=4,width=1.5,labelsize=14)
py.contour(Ztau,Zmu,np.transpose(Z),V,colors='k')
py.ylabel('Magnification')
py.xlabel('Time Delay (days)')
py.fontsize = 14
py.savefig('/mnt/data2/rumbaugh/Fermi/plots/0218/Disp.con_plot.0218.daily_lc.%s.delta_%4.1f.%s.png'%(disp_type,delta,date))
#for delta in np.arange(18)+2.5:
#        infile = '/home/rumbaugh/EVLA/light_curves/Dispersions/dispmat.delta_var.0414_B%s.D_4_2.delta_%.1f.%s.dat'%(imgname[imgnum],delta,ldate)
#        cr = np.loadtxt(infile)
#        tau,mu,disp = cr[:,0],cr[:,1],cr[:,2]
#        len_mu = len(tau[tau==tau[0]])
#        len_tau = len(mu[mu==mu[0]])
#        Z = np.reshape(disp,(len_tau,len_mu))
#        Ztau = np.reshape(tau,(len_tau,len_mu))[:,0]
#        Zmu = np.reshape(mu,(len_tau,len_mu))[0]
#V = np.min(Z)+np.array([2.3,6.18,11.8])
#        V = np.exp(np.arange(10)/10.*(np.max(np.log(Z))-np.min(np.log(Z)))+np.min(np.log(Z)))
#print V
#        py.clf()
#        py.rc('axes',linewidth=2)
#        py.fontsize = 14
#        py.tick_params(which='major',length=8,width=2,labelsize=14)
#        py.tick_params(which='minor',length=4,width=1.5,labelsize=14)
#        py.contour(Ztau,Zmu,np.transpose(Z),V,colors='k')
#        py.ylabel('Magnification')
#        py.xlabel('Time Delay (days)')
#        py.fontsize = 14
#        py.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/Disp.con_plot.0414_B%s.D_4_2.delta_%.1f.%s.ps'%(imgname[imgnum],delta,date))

g = np.where(mu == 1)[0]
py.clf()
py.rc('axes',linewidth=2)
py.fontsize = 14
py.tick_params(which='major',length=8,width=2,labelsize=14)
py.tick_params(which='minor',length=4,width=1.5,labelsize=14)
py.plot(tau[g],disp[g])
py.ylabel('Dispersion')
py.xlabel('Time Delay (days)')
py.fontsize = 14
py.savefig('/mnt/data2/rumbaugh/Fermi/plots/0218/Disp_vs_tau.0218.daily_lc.%s.delta_%4.1f.%s.png'%(disp_type,delta,date))




