import numpy as np
import time
import matplotlib.pylab as py
try:
    lens
except NameError:
    lens = '1030'
date = '9.12.14'

tau1030 = 156/1.4

for lens in ['1030']:
    infile = '/home/rumbaugh/EVLA/light_curves/Dispersions/Disp_grid_out.%s.delta_10.5_9.12.14.dat'%(lens)
    cr = np.loadtxt(infile)
    tau,mu,disp = -1*cr[:,0],cr[:,1],cr[:,2]
    len_mu = len(tau[tau==tau[0]])
    len_tau = len(mu[mu==mu[0]])
    Z = np.reshape(disp,(len_tau,len_mu))
    Ztau = np.reshape(tau,(len_tau,len_mu))[:,0]
    Zmu = np.reshape(mu,(len_tau,len_mu))[0]
#try:
#    V
#except NameError:
    if lens == '1030':
        V = np.array([75,110,160,250,400])
    elif lens == '0712':
        V = np.array([0.45,0.6,0.9,1.3])
    #V = np.exp(np.arange(8)/8.*(np.log(np.max(Z))-np.log(np.min(Z)))*0.95+np.log(np.min(Z)*1.05))
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
    py.axvline(tau1030,lw=2,c='k',ls='dashed')
    py.savefig('/home/rumbaugh/EVLA/light_curves/Dispersions/Disp.con_plot.%s.delta_10.5_%s.png'%(lens,date))
    xl,xm = py.xlim()
    yl,ym = py.ylim()
    print '%s - x limits: (%f,%f)\ny limits: (%f,%f)\n\n'%(lens,xl,xm,yl,ym)
