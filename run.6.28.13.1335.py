import numpy as np
import os
import lris_extract
import pyfits

execfile('/home/rumbaugh/slit_name_dict_master.py')

#for mask in ['miki21_B','miki22_z','M0417_B','M0744_A','M0744_B','M1115_A','miki10.f']:
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

for mask in ['miki21_B','1131m3','1131m4']:
#for mask in ['miki21D.','miki16B.','bc3.file','bc3B.fil','miki21C.']:
    outdir = slit_name_dict[mask]['redux_dir']
    if mask in ['1131m3','1131m4','miki16B.']:
        sides,colors = ['top'],['blue','red']
    elif mask in ['miki04.f','miki04_B']:
        sides,colors = ['bottom'],['blue']
    elif mask in ['miki03_B']:
        sides,colors = ['top'],['red']
    else:
        sides,colors = ['top','bottom'],['blue','red']
    for side in sides:
        for color in colors:
            for slit in slit_name_dict[mask][color][side]:
                if not (((mask in ['miki03_A','miki22.f','miki21.f','miki04_A']) & (color == 'blue') & (side == 'top')) | ((mask in ['miki21_B']) & (((color == 'blue') & ((slit in ['42702','3','113','44624'])))))):
                    if color == 'blue':
                        doextract(mask,side,slit,colors=[color],maxpeaks=3)
                        if slit in slit_name_dict[mask]['red'][side]: doextract(mask,side,slit,colors=['red'],maxpeaks=3)
                    else:
                        if ((not slit in slit_name_dict[mask]['blue'][side]) | (not ('blue' in colors)) | ((mask in ['miki03_A','miki22.f','miki21.f','miki04_A']) & (side == 'top'))): doextract(mask,side,slit,colors=['red'],maxpeaks=3)
