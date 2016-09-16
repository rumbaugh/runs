import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
ldate='7.10.16'
date='7.10.16'

group_dict={'Passive':['cl1350','rcs0224','rxj1221','rxj1757','rxj1821'],'Intermediate':['cl1324','cl1324_north','cl1324_south','rxj1716'],'Cl0023 & Cl1604':['cl0023','cl1604'],'High-z':['rxj0910','rxj1053','cl0849']}

zrange=np.arange(0.65,1.28,0.05)
lumpnts=np.linspace(42,44.5,20)
lumpnts=0.5*(lumpnts[1:]+lumpnts[:-1])

glZ,gl,glA,glB,glC=np.where((lumpnts>=42)&(lumpnts<=42.5))[0],np.where((lumpnts>=42.5)&(lumpnts<=43))[0],np.where((lumpnts>=43)&(lumpnts<=43.5))[0],np.where((lumpnts>=43.5)&(lumpnts<=44))[0],np.where((lumpnts>=44)&(lumpnts<=44.5))[0]
gzrlow,gzrmed,gzrhi=np.where((zrange<=0.8))[0],np.where((zrange>=0.8)&(zrange<=0.96))[0],np.where((zrange>=0.96))[0]
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

carr,lsarr=['blue','red','cyan','green','magenta','gray','orange'],['solid','dashed','dotted','dashdot']

namedict={'rxj1757':'RXJ1757','rxj1221':'RXJ1221','cl1324':'SC1324','rcs0224':'RCS0224','cl1350':'Cl1350','rxj1716':'RXJ1716','rxj1821':'RXJ1821','cl0023':'SG0023','cl1604':'SC1604','cl1137':'Cl1137','rxj0910':'RXJ0910','rxj1053':'RXJ1053','cl0849':'Cl0849'}

tot_comp_dict={x:{'-1':0,'0':0,'A':0,'B':0,'C':0} for x in ['z<0.8','0.8<z<0.96','z>0.96','All']}
totweight=len(targets)+1

FILE=open('/home/rumbaugh/Chandra/X-ray_completeness.MC_sim_true.z_range.%s.dat'%date,'w')
FILE.write('# Field Z_range 42-42.5 42.5-43 43-43.5 43.5-44 44-44.5\n')
for target,it in zip(targets,np.arange(0,len(targets))):
    for band,ib in zip(['soft','hard','full'],np.arange(0,3)):
        if target=='cl1324':
            cr1=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%('cl1324_north','cl1324_north','cl1324_north',band,ldate))
            cr2=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%('cl1324_south','cl1324_south','cl1324_south',band,ldate))
            cr=0.5*(cr1+cr2)
        elif target=='cl1604':
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%(target,target,target,band,ldate))
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
        if band=='full':
            for zr,gzrtmp in zip(['z<0.8','0.8<z<0.96','z>0.96','All'],[gzrlow,gzrmed,gzrhi,np.arange(len(zrange))]):
                FILE.write('%12s %10s '%(target,zr))
                for gltmp,l in zip([glZ,gl,glA,glB,glC],['-1','0','A','B','C']):
                    if len(gzrtmp)==1:
                        comptmp=np.average(cr[gzrtmp].reshape((len(cr[0])))[:,gltmp])
                    else:
                        comptmp=np.average(cr[gzrtmp][:,gltmp])
                    if target != 'cl1137':
                        tot_comp_dict[zr][l]+=comptmp
                        if target in ['cl1324','cl1604']: tot_comp_dict[zr][l]+=comptmp
                    FILE.write(' %.4f'%(comptmp))
                FILE.write('\n')
        plt.legend()
        plt.xlabel('Luminosity (log10)')
        plt.ylabel('Completeness Fraction')
        plt.xlim(42,44.5)
        plt.ylim(0.3,1)
        plt.title(target)
        plt.savefig('/home/rumbaugh/Chandra/plots/X-ray_completeness_MCsim.true.%s_%s.%s.png'%(target,band,date))
for zr in ['z<0.8','0.8<z<0.96','z>0.96','All']:
    FILE.write('%12s %10s'%('Combined',zr))
    for l in ['-1','0','A','B','C']:
        FILE.write(' %.4f'%(tot_comp_dict[zr][l]/totweight))
    FILE.write('\n')
FILE.close()

for target,it in zip(targets,np.arange(0,len(targets))):
    for band,ib in zip(['soft','hard','full'],np.arange(0,3)):
        if target=='cl1324':
            cr1=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%('cl1324_north','cl1324_north','cl1324_north',band,ldate))
            cr2=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%('cl1324_south','cl1324_south','cl1324_south',band,ldate))
            cr=0.5*(cr1+cr2)
        elif target=='cl1604':
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%(target,target,target,band,ldate))
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
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%(target,target,target,band,ldate))
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


FILE=open('/home/rumbaugh/Chandra/X-ray_completeness.MC_sim_true.z_clus.%s.dat'%date,'w')
FILE.write('# Field 42-42.5 42.5-43 43-43.5 43.5-44 44-44.5\n')

grp_comp_dict={x:{'-1':0,'0':0,'A':0,'B':0,'C':0} for x in ['Passive','Intermediate','Cl0023 & Cl1604','High-z']}
weight_dict={'Passive':5,'Intermediate':3,'Cl0023 & Cl1604':3,'High-z':3}

for band,ib in zip(['soft','hard','full'],np.arange(0,3)):
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    #for target,it in zip(targets,np.arange(0,len(targets))):
    for target,it in zip(np.array(['rxj1757','rxj1221','cl1324','rcs0224','cl1350','rxj1716','rxj1821','cl0023','cl1604','cl1137','rxj0910','rxj1053','cl0849']),np.arange(0,len(targets))):
        if target=='cl1324':
            cr1=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%('cl1324_north','cl1324_north','cl1324_north',band,ldate))
            cr2=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%('cl1324_south','cl1324_south','cl1324_south',band,ldate))
            cr=0.5*(cr1+cr2)
        elif target=='cl1604':
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%(target,target,target,band,ldate))
        else:
            cr=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%(target,target,target,band,ldate))
        gz=np.argsort(np.abs(zrange-spec_dict[target]['z'][0]))[0]
        plt.plot(lumpnts,cr[gz],lw=2,color=carr[it%len(carr)],ls=lsarr[it%len(lsarr)],label=namedict[target])
        plt.legend()
        plt.xlabel('log(Rest-frame Full-Band X-ray Luminosity)')
        plt.ylabel('Completeness Fraction')
        plt.xlim(42,44.5)
        plt.ylim(0.3,1)
        if band=='full':
            FILE.write('%16s '%(target))
            for gltmp,l in zip([glZ,gl,glA,glB,glC],['-1','0','A','B','C']):
                comptmp=np.average(cr[gz][gltmp])
                FILE.write(' %.4f'%(comptmp))
                for group in group_dict.keys():
                    if target in group_dict[group]:
                        grp_comp_dict[group][l]+=comptmp
                        if target in ['cl1604','cl1324']: grp_comp_dict[group][l]+=comptmp
            FILE.write('\n')
    plt.savefig('/home/rumbaugh/Chandra/plots/X-ray_completeness_MCsim.true_all_%s.%s.png'%(band,date))
for group in group_dict.keys():
    FILE.write('%16s '%(group))
    for l in ['-1','0','A','B','C']:
        FILE.write(' %.4f'%(grp_comp_dict[group][l]/weight_dict[group]))
    FILE.write('\n')
FILE.close()
