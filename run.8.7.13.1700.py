import numpy as np
import os
import lris_extract
import pyfits

execfile('/home/rumbaugh/slit_name_dict_master.py')

def doextract(mask,side,slit,colors=['blue','red'],maxpeaks=3):
    osv = os.system('mkdir -p %s%s'%(slit_name_dict[mask]['redux_dir'],mask))
    osv = os.chdir('%s%s'%(slit_name_dict[mask]['redux_dir'],mask))
    osv = os.system("mkdir -p %s%s/plots"%(slit_name_dict[mask]['redux_dir'],mask))
    osv = os.system("mkdir -p %s%s/spec_output"%(slit_name_dict[mask]['redux_dir'],mask))
    for color in colors:
        try:
            lris_extract.lris_extract("%s_%s_%s_%s_coadd_bgsub.fits"%(mask,slit,color,side),"spec_output/outspec.%s_%s_%s_%s_coadd_bgsub.dat"%(mask,slit,color,side),weightfile="%s_%s_%s_%s_coadd_bgsub.weight.fits"%(mask,slit,color,side),output_plot="%s_%s_%s_%s_coadd_bgsub.ps"%(mask,slit,color,side),output_plot_dir = '%s/%s/plots'%(slit_name_dict[mask]['redux_dir'],mask),nan_to_zero=True,findmultiplepeaks=True,maxpeaks=maxpeaks)
        except IOError:
            print 'File %s_%s_%s_%s_coadd_bgsub.fits not found. Skipping to next slit.'%(mask,slit,color,side)

for mask in ['1131m3']:
    sides,colors = ['bottom'],['blue']
    outdir = slit_name_dict[mask]['redux_dir']
    for side in sides:
        for color in colors:
            for slit in ['302','176','77']:
                if slit == '302': 
                    doextract(mask,side,slit,colors=[color],maxpeaks=6)
                    doextract(mask,side,slit,colors=['red'],maxpeaks=6)
                else:
                    doextract(mask,side,slit,colors=[color],maxpeaks=3)
