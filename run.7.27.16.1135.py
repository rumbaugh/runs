import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/setup_adam_cats.py')
xdummy=np.linspace(0,2,1000)

rkeys=np.array(reffile_dict.keys())
for field in rkeys[((rkeys!='rcs0224')&(rkeys!='cl1604'))]:
    pzcat='%s/%s/%s.zout.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crpz=np.loadtxt(pzcat,dtype=pzdict)
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj1821':
        cr=np.loadtxt(refcat,dtype=refdict_1821)
    elif field in ['rxj0910','rcs0224']:
        cr=np.loadtxt(refcat,dtype=refdict0910)
    else:
        cr=np.loadtxt(refcat,dtype=refdict)
    crzpz=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.zPz.7.19.16.dat'%(field,field,field))
    
    fz0,fzl,fzu=spec_dict[field]['z'][0],spec_dict[field]['z'][1],spec_dict[field]['z'][2]
    g=np.where((cr['use']==1)&(crpz['z_spec']>fzl)&(crpz['z_spec']<fzu))[0]
    plt.figure(1)
    plt.clf()
    plt.scatter(crpz['z_peak'][g],crzpz[g[,color='k',s=2)
    plt.plot(xdummy,xdummy,lw=2,ls='dashed',color='r')
    plt.xlim(0,2)
    plt.ylim(0,2)
    plt.xlabel('z_peak')
    plt.ylabel('<z>')
    plt.savefig('/home/rumbaugh/Chandra/plots/zpeak_vs_zPz.%s.7.25.16.png'%(field))
        
