import numpy as np
import time
import matplotlib.pylab as py

date = '5.18.14'
ldate = '5.16.14'
source = 'B1938'
disp_type,delta = 'D_2',10.5

infile = '/mnt/data2/rumbaugh/EVLA/11A-138/disp_results/disp_out.%s.D_2.%s.dat'%(source,ldate)
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
py.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/Disp.con_plot.B1938.%s.%s.png'%(disp_type,date))
disp_type,delta = 'D_4_2',10.5
for delta in np.arange(19)+3.5:
    infile = '/mnt/data2/rumbaugh/EVLA/11A-138/disp_results/disp_out.%s.D_4_2.delta_%.1f.%s.dat'%(source,delta,ldate)
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
    py.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/Disp.con_plot.B1938.%s.delta_%.1f.%s.png'%(disp_type,delta,date))
    mintaus = np.zeros(len_tau)
    for i in range(0,len_tau):
        mintaus[i] = np.min(Z[i])
    py.clf()
    py.rc('axes',linewidth=2)
    py.fontsize = 14
    py.tick_params(which='major',length=8,width=2,labelsize=14)
    py.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    py.plot(np.arange(tau[0],tau[-1]+0.5,0.5),mintaus)
    py.ylabel('Minimum Dispersion')
    py.xlabel('Time Delay (days)')
    py.fontsize = 14
    py.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/Disp.tau_1D_plot.B1938.%s.delta_%.1f.%s.png'%(disp_type,delta,date))
    
