import numpy as np
import os
import lris_extract
import pyfits

execfile('/home/rumbaugh/slit_name_dict_master.py')

for mask in ['miki21_B','miki22_z','M0417_B','M0744_A','M0744_B','M1115_A','miki10.f']:
#for mask in ['miki22_z','M0417_B','M0744_A','M0744_B','M1115_A','miki10.f']:
    osv = os.chdir('%s%s'%(slit_name_dict[mask]['redux_dir'],mask))
    osv = os.system("mkdir -p %s%s/plots"%(slit_name_dict[mask]['redux_dir'],mask))
    osv = os.system("mkdir -p %s%s/spec_output"%(slit_name_dict[mask]['redux_dir'],mask))
    for color in ['red','blue']:
        for side in ['top','bottom']:
            for slit in slit_name_dict[mask][color][side]:
                try:
                    lris_extract.lris_extract("%s_%s_%s_%s_coadd_bgsub.fits"%(mask,slit,color,side),"spec_output/outspec.%s_%s_%s_%s_coadd_bgsub.dat"%(mask,slit,color,side),weightfile="%s_%s_%s_%s_coadd_bgsub.weight.fits"%(mask,slit,color,side),output_plot="%s_%s_%s_%s_coadd_bgsub.ps"%(mask,slit,color,side),output_plot_dir = '%s/%s/plots'%(slit_name_dict[mask]['redux_dir'],mask),nan_to_zero=True,findmultiplepeaks=True,maxpeaks=3)
                except IOError:
                    print 'File %s_%s_%s_%s_coadd_bgsub.fits not found. Skipping to next slit.'%(mask,slit,color,side)
