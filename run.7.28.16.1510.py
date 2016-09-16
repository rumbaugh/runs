import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/setup_adam_cats.py')
xdummy=np.linspace(0,2,1000)

fitfunc  = lambda p, x: p[0]*np.exp(-0.5*((x-p[1])/p[2])**2)
errfunc  = lambda p, x, y: (y - fitfunc(p, x))

shiftdict={'rxj1716':-0.006,'cl1604':0.,'cl0023':-0.015,'rxj0910':-0.016,'rxj1757':-0.016,'rxj1821':-0.018}
sigdict={'rxj1716': .139,'cl1604': .162,'cl0023': .14, 'rxj0910': .242, 'rxj1757':.149,'rxj1821':.183}

rkeys=np.array(reffile_dict.keys())
for field in ['cl0023','rxj0910','rxj1757']:
    pzcat='%s/%s/%s.zout.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crpz=np.loadtxt(pzcat,dtype=pzdict)
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj1821':
        cr=np.loadtxt(refcat,dtype=refdict_1821)
    elif field in ['rxj1716','cl0023']:
        cr=np.loadtxt(refcat,dtype=refdict1716)
    elif field in ['rxj1757']:
        cr=np.loadtxt(refcat,dtype=refdict1757)
    elif field in ['rxj0910','rcs0224']:
        cr=np.loadtxt(refcat,dtype=refdict0910)
    else:
        cr=np.loadtxt(refcat,dtype=refdict)
    crzpz=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.zPz.7.19.16.dat'%(field,field,field))
    crpz['z_peak']=(crpz['z_peak']-shiftdict[field])/(1.+shiftdict[field])
    fz0,fzl,fzu=spec_dict[field]['z'][0],spec_dict[field]['z'][1],spec_dict[field]['z'][2]
    fzl,fzu=fzl-sigdict[field],fzu+sigdict[field]
    g=np.where((cr['use']==1)&(crpz['z_spec']>fzl)&(crpz['z_spec']<fzu))[0]
    plt.figure(1)
    plt.clf()
    plt.scatter(crpz['z_peak'][g],crzpz[g],color='k',s=2)
    plt.plot(xdummy,xdummy,lw=2,ls='dashed',color='r')
    plt.xlim(fzl*0.9,fzu*1.1)
    plt.ylim(0,2)
    plt.xlabel('z_peak')
    plt.ylabel('<z>')
    plt.savefig('/home/rumbaugh/Chandra/plots/zpeak_vs_zPz.%s.7.28.16.png'%(field))
        
    plt.figure(1)
    plt.clf()
    plt.scatter(crpz['z_spec'][g],crzpz[g],color='k',s=2)
    plt.plot(xdummy,xdummy,lw=2,ls='dashed',color='r')
    plt.xlim(fzl*0.9,fzu*1.1)
    plt.ylim(0,2)
    plt.xlabel('z_spec')
    plt.ylabel('<z>')
    plt.savefig('/home/rumbaugh/Chandra/plots/zspec_vs_zPz.%s.7.28.16.png'%(field))
                                        
        
    plt.figure(1)
    plt.clf()
    plt.scatter(crpz['z_peak'][g],(crzpz[g]-crpz['z_peak'][g])/(1.+crpz['z_peak'][g]),color='k',s=2)
    plt.axhline(0,lw=2,ls='dashed',color='r')
    plt.xlim(fzl*0.9,fzu*1.1)
    plt.ylim(-0.2,0.2)
    plt.ylabel(r'$\Delta$ z /(1+z)')
    plt.xlabel('z_spec')
    plt.savefig('/home/rumbaugh/Chandra/plots/zpeak_vs_zPz_norm.%s.7.28.16.png'%(field))
        
           
        
    plt.figure(1)
    plt.clf()
    plt.scatter(crpz['z_spec'][g],(crzpz[g]-crpz['z_spec'][g])/(1.+crpz['z_spec'][g]),color='k',s=2)
    plt.axhline(0,lw=2,ls='dashed',color='r')
    plt.xlim(fzl*0.9,fzu*1.1)
    plt.ylim(-0.2,0.2)
    plt.ylabel(r'$\Delta$ z /(1+z)')
    plt.xlabel('z_spec')
    plt.savefig('/home/rumbaugh/Chandra/plots/zspec_vs_zPz_norm.%s.7.28.16.png'%(field))
        
        
        
    plt.figure(1)
    plt.clf()
    a=plt.hist((crzpz[g]-crpz['z_spec'][g])/(1.+crpz['z_spec'][g]),range=(-0.1,0.1),bins=20)
    plt.xlim(-0.1,0.1)
    plt.ylabel('Number of sources')
    plt.xlabel(r'$\Delta$ z /(1+z)')
        
    xa=0.5*(a[1][1:]+a[1][:-1])
    init=[np.max(a[0]),np.mean((crzpz[g]-crpz['z_spec'][g])/(1.+crpz['z_spec'][g])),np.std((crzpz[g]-crpz['z_spec'][g])/(1.+crpz['z_spec'][g]))]
    out=leastsq( errfunc, init, args=(xa,a[0]))
    c=out[0]
    print field,c[0],c[1],np.abs(c[2])
    plt.plot(xa,fitfunc(c,xa))
    plt.xlim(-0.1,0.1)
    plt.savefig('/home/rumbaugh/Chandra/plots/zspec_vs_zPz_norm_hist.%s.7.28.16.png'%(field))
