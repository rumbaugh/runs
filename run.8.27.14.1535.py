import numpy as np
import matplotlib.pyplot as plt
import os
execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')

FILE=open('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_plotvalues.8.27.14.dat','w')

date = '8.27.14'
ddate = '6.3.14'

crt = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')
pairs = np.array([3,4,5,6,7,8,10,11,12,13,14,15,16,17,20])
redone_pairs = np.array([3,5,6,10,11])

time_lim = (215,555)

tau_lim_dict = dict(zip(pairs,np.zeros(len(pairs))))
mu_lim_dict = dict(zip(pairs,np.zeros(len(pairs))))

tau_lim_dict[5] = (0,250)
tau_lim_dict[11] = (0,500)
tau_lim_dict[14] = (0,10)
tau_lim_dict[17] = (0,200)

for pair in pairs:
    ldate = '8.8.14'
    if pair in redone_pairs: ldate = '8.22.14'
    if pair == 11: ldate = '8.24.14'
    tau_t,mu_t = crt[:,0][pair-1],crt[:,1][pair-1]

    DataFile='/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau_t,mu_t,ddate)
    os.system('cp /mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat /home/rumbaugh/files_for_TimeBombs_animation/TimeBombsData/testlightcurve_%i.tau_%.2f.mu_%.3f.dat'%(pair,tau_t,mu_t,ddate,pair,tau_t,mu_t))
    datacr = np.loadtxt(DataFile)
    cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/TimeBombs/output/posterior.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau_t,mu_t,ldate))
    os.system('cp /mnt/data2/rumbaugh/Fermi/TimeBombs/output/posterior.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat /home/rumbaugh/files_for_TimeBombs_animation/TimeBombsData/posterior.testlightcurve_%i.tau_%.2f.mu_%.3f.dat'%(pair,tau_t,mu_t,ldate,pair,tau_t,mu_t))
    taus,mus = cr[:,1],cr[:,2]
    taus[taus<0]*=-1
    mus[mus>1]=1./mus[mus>1]

    mintau,maxtau,minmu,maxmu = np.min(taus),np.max(taus),np.min(mus),np.max(mus)

    slen = 110


    for i in range(0,1):
    #for i in range(0,np.shape(cr)[0]):
        plt.figure(1,figsize=(8,10))
        plt.clf()
#lc1 = cr[0][-slen:]
#lct = cr[0][-2*slen:-slen]
        lc1 = cr[i][-2*slen:-slen]
        lct = cr[i][-slen:]
        lc2 = lct-lc1
        mu = cr[i][2]
        tau = cr[i][1]
        if mu > 1: lc1,lc2=lc2,lc1

    #lc2_th = lc1*mu
        plt.subplot(211)
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        
        if np.shape(tau_lim_dict[pair]) != (): 
            hist2d(taus,mus,V=np.array([0.682689,0.9545,0.9973]),extent=[[tau_lim_dict[pair][0],tau_lim_dict[pair][1]],[0,1]])
        else:
            hist2d(taus,mus,V=np.array([0.682689,0.9545,0.9973]))
        if i == 0: 
            tau_lim_dict[pair] = plt.xlim()
            mu_lim_dict[pair] = plt.ylim()
            FILE.write('%i %f %f %f %f\n'%(pair,tau_lim_dict[pair][0],tau_lim_dict[pair][1],mu_lim_dict[pair][0],mu_lim_dict[pair][1]))
        plt.scatter(taus[i],mus[i],marker='+',s=300,lw=3,color='red')
        plt.xlim(tau_lim_dict[pair])
        plt.ylim(mu_lim_dict[pair])
        

        plt.subplot(212)
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        plt.plot(datacr[:,0],lc1,color='red',lw=1)
        plt.plot(datacr[:,0],lc2,color='blue',lw=1)
    #plot(np.arange(len(lc2_th))-tau/3.,lc2_th,color='green',lw=1)
        plt.scatter(datacr[:,0],datacr[:,1],color='cyan',lw=2,s=16)
        plt.xlim(time_lim)
        plt.ylim(-5,1.1*np.max(datacr[:,1]))
        plt.savefig('/mnt/data2/rumbaugh/Fermi/TimeBombs/plots/plotsforgif/posterior_output_curves.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.frame%i.png'%(pair,tau_t,mu_t,date,i))
FILE.close()
