import numpy as np
import matplotlib.pylab as py
execfile('/home/rumbaugh/Dispersion.py')

ref_dict = {'tdc1_rung1_double_pair7':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung1_double_pair202':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung1_double_pair302':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung1_double_pair322':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_double_pair342':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_double_pair382':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_double_pair403':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung1_double_pair502':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_quad_pair7A': {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_quad_pair7B': {'infile':  '', 'range': np.array([60,90])}}


infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung1/tdc1_rung1_double_pair502'
for tdcfile in ['tdc1_rung1_double_pair202','tdc1_rung1_double_pair382']:
    infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung1/output/%s.BA_extended_mu+tau.dat'%tdcfile
    outfile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung1/output/conplot.%s.BA_extended_mu+tau.ps'%tdcfile
    cr = np.loadtxt(infile)
    tau,mu,disp = cr[:,0],cr[:,1],cr[:,2]
    len_mu = len(tau[tau==tau[0]])
    len_tau = len(mu[mu==mu[0]])
    Z = np.reshape(disp,(len_tau,len_mu))
    Ztau = np.reshape(tau,(len_tau,len_mu))[:,0]
    Zmu = np.reshape(mu,(len_tau,len_mu))[0]
    #V = np.min(Z)+np.array([2.3,6.18,11.8])
    V = np.arange(10)/10.*(np.max(Z)-np.min(Z))+np.min(Z)
    g = np.where(disp == np.min(disp))[0]
    #print V
    py.clf()
    py.rc('axes',linewidth=2)
    py.fontsize = 14
    py.tick_params(which='major',length=8,width=2,labelsize=14)
    py.tick_params(which='minor',length=4,width=1.5,labelsize=14)
#py.contour(Ztau,Zmu,np.transpose(Z),V,colors='k')
    py.contour(Ztau,Zmu,np.transpose(Z))
    py.scatter(tau[g],mu[g],color='red')
    py.ylabel('Magnification')
    py.xlabel('Time Delay (days)')
    py.fontsize = 14
    py.savefig(outfile)
    g= np.where(disp == np.min(disp))[0]
    if tdcfile == 'tdc1_rung1_double_pair202': 
        g= np.where(disp[tau > 60] == np.min(disp[tau > 60]))[0]
        print tdcfile,mu[tau > 60][g],tau[tau > 60][g]
    else:
        print tdcfile,mu[g],tau[g]
