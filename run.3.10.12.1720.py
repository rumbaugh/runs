import numpy as np
import math as m
import time
import sys
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/angconvert.py")

names = ['Cl1604','Cl1324']
files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
sfiles = [files[5],files[1]]
mfiles = np.array(['/scratch/rumbaugh/ciaotesting/Cl1604/master/opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat.new','/scratch/rumbaugh/ciaotesting/Cl1324/master/opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat'])
mfiles = ['matched.Cl1604.Xray_opt_spec.bothmatches_serendips.8.15.11.cat','matched.Cl1324.Xray_opt_spec.bothmatches_serendips.8.9.11.cat']
ylims = np.array([9.5,6])
zm = np.array([0.9,0.72])
for i in range(0,2):
    mfile = '/home/rumbaugh/paperstuff/important/%s'%(mfiles[i])
    cr = read_file(mfile)
    xID = copy_colvals(cr,'Xray_ID')
    nm = copy_colvals(cr,'num_opt_matches')
    z = copy_colvals(cr,'z')
    q = copy_colvals(cr,'q')
    g = np.where((nm > 0.1) & (q > 2.2))
    g = g[0]
    pylab.tick_params(labelsize=14,width=1.7)
    pylab.xlim(-0.003,1.5)
    pylab.ylim(0,ylims[i]+0.01)
    pylab.xlabel('Redshift',fontsize=16)
    pylab.ylabel('N(Galaxies)',fontsize=16)
    pylab.hist(z,bins=20,facecolor='none',range=[0,1.5],lw=2)
    pylab.plot([zm[i],zm[i]],[-100,100],ls='dashed',lw=3,color='red')
    pylab.axhline(y=0,lw=2,color='black')
    pylab.axhline(y=ylims[i]-0.003,lw=2,color='black')
    pylab.axvline(x=0,lw=2,color='black')
    pylab.axvline(x=1.5-0.003,lw=2,color='black')
    pylab.savefig('/home/rumbaugh/%s.zhist.ml.3.10.12.png'%(names[i]))
    pylab.close('all')


