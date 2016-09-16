import numpy as np
import matplotlib.pylab as plt
date = '7.30.14'

iter_dict = dict(zip(np.array([3,4,5,6,7,8,10,11,12,13,14,15,16,17,20]),np.array([2,3,2,2,3,3,3,2,3,2,0,1,3,3,3])))

xlim_dict = {5: (0,250), 10: (0,40), 11: (0,40), 13: (0,50), 14: (0,15), 15: (0,500), 17: (0,75)}

ldate_dict = {0: '6.19.14', 1: '6.27.14', 2: '7.7.14', 3: '7.9.14'}

cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')

#FILE = open('/mnt/data2/rumbaugh/Fermi/TimeBombs/output/results.testlightcurves.%s.dat'%date,'w')
for i,pair in zip(np.arange(len(iter_dict.keys())),iter_dict.keys()):
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    ldate = ldate_dict[iter_dict[pair]]
    pfile = '/mnt/data2/rumbaugh/Fermi/TimeBombs/output/posterior.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ldate)
    crp = np.loadtxt(pfile)
    tau_out,mu_out = np.abs(crp[:,1]),np.abs(crp[:,2])
    medtau,medmu = np.median(tau_out),np.median(mu_out)
    tausort,musort = np.sort(tau_out),np.sort(mu_out)
    tauerr,muerr = tausort[int(0.682689492*len(tausort))]-tausort[int(0.317310508*len(tausort))],musort[int(0.682689492*len(musort))]-musort[int(0.317310508*len(musort))]
    #FILE.write('%2i %7.4f %6.4f %7.4f %6.4f %7.4f %6.4f\n'%(pair,tau,mu,medtau,medmu,tauerr,muerr))
    crd = np.loadtxt('/mnt/data2/rumbaugh/Fermi/output/test/Dispersion.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,'6.3.14'))
    tau_d,mu_d,dtmp = crd[:,0],crd[:,1],crd[:,2]
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    if pair in xlim_dict.keys():
        plt.hist(tau_out,bins=50,range=(xlim_dict[pair][0],xlim_dict[pair][1]))
    else:
        plt.hist(tau_out,bins=50)
    ymin,ymax = plt.ylim()
    plt.plot(tau_d,dtmp*ymax/np.max(dtmp),lw=2)
    plt.axvline(tau,lw=2,ls='dashed',color='k')
    plt.xlabel('Time Delay (days)',fontsize=14)
    plt.title('Lightcurve %i'%pair)
    if pair in xlim_dict.keys():
        plt.xlim(xlim_dict[pair][0],xlim_dict[pair][1])
    else:
        plt.xlim(0,100)
    plt.savefig('/mnt/data2/rumbaugh/Fermi/TimeBombs/plots/Dispersion+TimeBombs_plot.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(pair,tau,mu,date))
    
#FILE.close()
