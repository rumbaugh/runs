import numpy as np
import matplotlib.pyplot as plt

execfile('/home/rumbaugh/setup_adam_cats.py')
rkeys=np.array(reffile_dict.keys())
for field in rkeys[rkeys!='rcs0224']:
    try:
        crPI=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.P_inclus.7.19.16.dat'%(field,field,field))
    except:
        crPI=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.P_inclus.7.1.16.dat'%(field,field,field))
    try:
        crPIs=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.P_inclus_shift.7.26.16.dat'%(field,field,field))
        plt.figure(1)
        plt.clf()
        g=np.where(crPI>0.05)[0]
        plt.hist(crPIs[g]-crPI[g],range=(-0.5,0.5),bins=25)
        plt.xlabel("P'(z)-P(z)")
        plt.ylabel('Number of sources')
        plt.savefig('/home/rumbaugh/Chandra/plots/Pz_shift_test.%s.7.28.16.png'%field)
        plt.figure(1)
        plt.clf()
        g=np.where(crPI>0.05)[0]
        plt.scatter(crPI,crPIs,s=3)
        plt.xlabel("P(z)")
        plt.ylabel("P'(z)")
        plt.xlim(0,1)
        plt.ylim(0,1)
        plt.savefig('/home/rumbaugh/Chandra/plots/Pz_shift_vs_Pz.%s.7.28.16.png'%field)
    except:
        pass
