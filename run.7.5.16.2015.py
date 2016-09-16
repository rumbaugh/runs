import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
ldate='7.5.16'
date='7.5.16'

zrange=np.arange(0.65,1.28,0.1)
lumpnts=np.linspace(42,44.5,20)
lumpnts=0.5*(lumpnts[1:]+lumpnts[:-1])
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])
targets=np.array(["cl0023","rxj1716"])

carr,lsarr=['blue','red','cyan','green','magenta','gray','orange'],['solid','dashed','dotted','dashdot']
#targets=['cl1324']
zrange=np.array([0.775,0.83,0.91])

CHrad_dict={'cl0023':5*487.805/4,'rxj1716':7*487.805/4}

band,ib='full',2
for target,it in zip(targets,np.arange(0,len(targets))):
    CHrad=CHrad_dict[target]
    cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.CHrad_%i.%s.dat'%(target,target,target,band,CHrad,ldate))
    for z,iz in zip(zrange,np.arange(len(zrange))):
        plt.figure(1)
        plt.clf()
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        plt.plot(lumpnts,cr[iz])
        plt.xlabel('Luminosity (log10)')
        plt.ylabel('Completeness Fraction')
        plt.xlim(42,44.5)
        plt.ylim(0.3,1)
        plt.title(target)
        plt.savefig('/home/rumbaugh/Chandra/plots/X-ray_completeness_MCsim.true.CH_rad_%i.%s_%s.z_%.2f.%s.png'%(int(CHrad*4/487.805),target,band,z,date))

target='cl0023'
CHrad=CHrad_dict['rxj1716']
cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.CHrad_%i.%s.dat'%(target,target,target,band,CHrad,ldate))
for z,iz in zip(zrange,np.arange(len(zrange))):
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.plot(lumpnts,cr[iz])
    plt.xlabel('Luminosity (log10)')
    plt.ylabel('Completeness Fraction')
    plt.xlim(42,44.5)
    plt.ylim(0.3,1)
    plt.title(target)
    plt.savefig('/home/rumbaugh/Chandra/plots/X-ray_completeness_MCsim.true.CH_rad_%i.%s_%s.z_%.2f.%s.png'%(int(CHrad*4/487.805),target,band,z,date))
