import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/setup_adam_cats.py')
xdummy=np.linspace(0,2,1000)

rkeys=np.array(reffile_dict.keys())
for field in rkeys:
    pzcat='%s/%s/%s.zout.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crpz=np.loadtxt(pzcat,dtype=pzdict)
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj1821':
        cr=np.loadtxt(refcat,dtype=refdict_1821)
    elif field in ['rxj0910','rcs0224']:
        cr=np.loadtxt(refcat,dtype=refdict0910)
    else:
        cr=np.loadtxt(refcat,dtype=refdict)
    
    for zm in ['z_m1','z_m2','z_mc']:
        plt.figure(1)
        plt.clf()
        plt.scatter(crpz['z_peak'][cr['use']==1],crpz[zm][cr['use']==1],color='k',s=2)
        plt.plot(xdummy,xdummy,lw=2,ls='dashed',color='r')
        plt.xlim(0,2)
        plt.ylim(0,2)
        plt.xlabel('z_peak')
        plt.ylabel(zm)
        plt.savefig('/home/rumbaugh/Chandra/plots/zpeak_vs_%s.%s.7.25.16.png'%(zm,field))
        
