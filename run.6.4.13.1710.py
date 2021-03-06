import numpy as np
import os
import lris_extract

execfile('/home/rumbaugh/slit_name_dict_master.py')

for mask in ['1131m4']:
    osv = os.chdir('%s%s'%(slit_name_dict[mask]['redux_dir'],mask))
    osv = os.system("mkdir -p %s%s/plots"%(slit_name_dict[mask]['redux_dir'],mask))
    osv = os.system("mkdir -p %s%s/spec_output"%(slit_name_dict[mask]['redux_dir'],mask))
    for color in ['red']:
        for side in ['top']:
            for slit in slit_name_dict[mask][color][side]:
                if slit == '600': lris_extract.lris_extract("%s_%s_%s_%s_coadd_bgsub.fits"%(mask,slit,color,side),"spec_output/outspec.%s_%s_%s_%s_coadd_bgsub.dat"%(mask,slit,color,side),weightfile="%s_%s_%s_%s_coadd_bgsub.weight.fits"%(mask,slit,color,side),output_plot="%s_%s_%s_%s_coadd_bgsub.ps"%(mask,slit,color,side),output_plot_dir = '%s/%s/plots'%(slit_name_dict[mask]['redux_dir'],mask),nan_to_zero=True,findmultiplepeaks=True,maxpeaks=3)
