import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
ldate='6.20.16'
date='6.22.16'

zrange=np.arange(0.65,1.28,0.05)
lumpnts=np.linspace(42,44.5,100)
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

carr,lsarr=['blue','red','cyan','green','magenta','gray','orange'],['solid','dashed','dotted','dashdot']

for target,it in zip(targets,np.arange(0,len(targets))):
    for band,ib in zip(['soft','hard','full'],np.arange(0,3)):
        if target=='cl1324':
            cr1=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%('cl1324_north','cl1324_north','cl1324_north',band,ldate))
            cr2=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%('cl1324_south','cl1324_south','cl1324_south',band,ldate))
            cr=0.5*(cr1+cr2)
        elif target=='cl1604':
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%(target,target,target,band,'6.20.16'))
        else:
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%(target,target,target,band,ldate))
        plt.figure(1)
        plt.clf()
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        for i in range(0,np.shape(cr)[0]):
            plt.plot(lumpnts,cr[i],color=carr[i%len(carr)],ls=lsarr[i%len(lsarr)],label='z=%.2f'%zrange[i])
        plt.legend()
        plt.xlabel('Luminosity (log10)')
        plt.ylabel('Completeness Fraction')
        plt.xlim(42,44.5)
        plt.ylim(0.3,1)
        plt.title(target)
        plt.savefig('/home/rumbaugh/Chandra/plots/X-ray_completeness_MCsim.true.%s_%s.%s.png'%(target,band,date))

for target,it in zip(targets,np.arange(0,len(targets))):
    for band,ib in zip(['soft','hard','full'],np.arange(0,3)):
        if target=='cl1324':
            cr1=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%('cl1324_north','cl1324_north','cl1324_north',band,ldate))
            cr2=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%('cl1324_south','cl1324_south','cl1324_south',band,ldate))
            cr=0.5*(cr1+cr2)
        elif target=='cl1604':
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%(target,target,target,band,date))
        else:
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%(target,target,target,band,ldate))
        plt.figure(1)
        plt.clf()
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        for i in range(0,np.shape(cr)[0]):
            plt.plot(lumpnts,cr[i],color=carr[i%len(carr)],ls=lsarr[i%len(lsarr)],label='z=%.2f'%zrange[i])
        plt.legend()
        plt.xlabel('Luminosity (log10)')
        plt.ylabel('Completeness Fraction')
        plt.xlim(42,44.5)
        plt.ylim(0.3,1)
        plt.title(target)
        plt.savefig('/home/rumbaugh/Chandra/plots/X-ray_completeness_MCsim.%s_%s.%s.png'%(target,band,date))

for band,ib in zip(['soft','hard','full'],np.arange(0,3)):
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    for target,it in zip(targets,np.arange(0,len(targets))):
        if target=='cl1324':
            cr1=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%('cl1324_north','cl1324_north','cl1324_north',band,ldate))
            cr2=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%('cl1324_south','cl1324_south','cl1324_south',band,ldate))
            cr=0.5*(cr1+cr2)
        elif target=='cl1604':
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%(target,target,target,band,date))
        else:
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%(target,target,target,band,ldate))
        gz=np.argsort(np.abs(zrange-spec_dict[target]['z'][0]))[0]
        plt.plot(lumpnts,cr[gz],color=carr[it%len(carr)],ls=lsarr[it%len(lsarr)],label=target)
        plt.legend()
        plt.xlabel('Luminosity (log10)')
        plt.ylabel('Completeness Fraction')
        plt.xlim(42,44.5)
        plt.ylim(0.3,1)
    plt.savefig('/home/rumbaugh/Chandra/plots/X-ray_completeness_MCsim.all_%s.%s.png'%(band,date))
