import numpy as np
import os
execfile('/home/rumbaugh/plot_red_and_blue.py')

pltfmt='eps'
dpi=1200

fsize=(12,7.5)

infile={'red':'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0737_2_red_2.19.dat',
'blue':'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0737_2_blue_2.19.dat'} 
uselines={'absorption': np.array([True,True,True,False,True,True,True,True,False,True,False,True,True,True]), 'emission': None}

plot_red_and_blue(infile,yl=(-25,200),fact=5,z=0.323,fsize=fsize,uselines=uselines)

savefig('/home/rumbaugh/KAST/plots/comb_spec.0737_2_full.2.19_10.13.15.%s'%pltfmt,format=pltfmt,dpi=dpi)

infile={'red':'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0813_red.dat',
'blue':'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0813_blue.dat'}


plot_red_and_blue(infile,yl=(-5,35),fact=5,fsize=fsize,z=None)


savefig('/home/rumbaugh/KAST/plots/comb_spec.0813_full_10.13.15.%s'%pltfmt,format=pltfmt,dpi=dpi)

infile={'red':'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0956_red.dat',
'blue':'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0956_blue.dat'}

fsize=(15,9)

uselines={'absorption': np.array([True,True,True,True,True,False,True,False,False,False,False,False,True,True]), 'emission': np.array([False,False,False,False,True,False,False,False,False,True,True,False,True,False,False,False,False,False])}

plot_red_and_blue(infile,yl=(-10,650),fact=3.5,z=0.1322,fsize=fsize,uselines=uselines)

savefig('/home/rumbaugh/KAST/plots/comb_spec.0956_full_10.13.15.%s'%pltfmt,format=pltfmt,dpi=dpi)
