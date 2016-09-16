import numpy as np
import matplotlib.pyplot as plt

execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/setup_adam_cats.py')
rkeys=np.array(reffile_dict.keys())
for field in ['rxj0910','cl0023','rxj1757']:
    pzcat='%s/%s/%s.zout.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crpz=np.loadtxt(pzcat,dtype=pzdict)
    fz0,fzl,fzu=spec_dict[field]['z'][0],spec_dict[field]['z'][1],spec_dict[field]['z'][2]
    try:
        crPI=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.P_inclus.7.19.16.dat'%(field,field,field))
    except:
        crPI=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.P_inclus.7.1.16.dat'%(field,field,field))
    try:
        crPIs=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.P_inclus_shift.7.28.16.dat'%(field,field,field))
        crzpz=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.zPz.7.19.16.dat'%(field,field,field))
        plt.figure(1)
        plt.clf()
        g=np.where(crPI>0.05)[0]
        gp=np.where((crpz['z_spec']>fzl)&(crpz['z_spec']<fzu))[0]
        gp2=np.where(((crpz['z_spec']<fzl)|(crpz['z_spec']>fzu))&(crpz['z_spec']>0.01))[0]
        plt.hist(crPIs[g]-crPI[g],range=(-0.5,0.5),bins=25)
        plt.xlabel("P'(z)-P(z)")
        plt.ylabel('Number of sources')
        plt.savefig('/home/rumbaugh/Chandra/plots/Pz_shift_test.%s.7.28.16.png'%field)

        plt.figure(1)
        plt.clf()
        g=np.where(crPI>0.05)[0]
        plt.scatter(crPI,crPIs,s=2)
        plt.scatter(crPI[gp],crPIs[gp],s=24,c='magenta')
        plt.scatter(crPI[gp2],crPIs[gp2],s=24,c='cyan')
        xdummy=np.linspace(0,1,100)
        plt.plot(xdummy,xdummy,lw=2,ls='dashed',c='r')
        plt.xlabel("P(z)")
        plt.ylabel("P'(z)")
        plt.xlim(0,1)
        plt.ylim(0,1)
        plt.savefig('/home/rumbaugh/Chandra/plots/Pz_shift_vs_Pz.%s.7.28.16.png'%field)

        plt.figure(1)
        plt.clf()
        g=np.where(crPI>0.05)[0]
        plt.scatter(crzpz,crPIs-crPI,s=2)
        plt.scatter(crzpz[gp],crPIs[gp]-crPI[gp],s=24,c='magenta')
        plt.axvline(fz0,lw=2,ls='dashed',color='r')
        plt.ylabel("P'(z)-P(z)")
        plt.xlabel("<z>")
        plt.xlim(0,3)
        plt.ylim(-1,1)
        plt.savefig('/home/rumbaugh/Chandra/plots/Pz_shift_vs_zPz.%s.7.28.16.png'%field)
        print field,np.sum(crPIs[g]-crPI[g]),np.sum(crPIs[gp]-crPI[gp])
    except:
        pass
