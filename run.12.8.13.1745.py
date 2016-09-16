import numpy as np
import os
import lris_extract
import pyfits

execfile('/home/rumbaugh/slit_name_dict_master.py')

def doextract(mask,side,slit,colors=['blue','red'],maxpeaks=3):
    osv = os.system('mkdir -p %s%s'%(slit_name_dict[mask]['redux_dir'],mask))
    osv = os.chdir('%sslits'%(slit_name_dict[mask]['redux_dir']))
    osv = os.system("mkdir -p %sslits/plots"%(slit_name_dict[mask]['redux_dir']))
    osv = os.system("mkdir -p %sslits/spec_output"%(slit_name_dict[mask]['redux_dir']))
    for color in colors:
        try:
            lris_extract.lris_extract("%s_%s_%s_%s_coadd_bgsub.fits"%(mask,slit,color,side),"spec_output/outspec.%s_%s_%s_%s_coadd_bgsub.dat"%(mask,slit,color,side),weightfile="%s_%s_%s_%s_coadd_bgsub.weight.fits"%(mask,slit,color,side),output_plot="%s_%s_%s_%s_coadd_bgsub.ps"%(mask,slit,color,side),output_plot_dir = '%sslits/plots'%(slit_name_dict[mask]['redux_dir']),nan_to_zero=True,findmultiplepeaks=True,maxpeaks=maxpeaks)
        except IOError:
            print 'File %s_%s_%s_%s_coadd_bgsub.fits not found. Skipping to next slit.'%(mask,slit,color,side)

slit_name_dict = {'0435m2': {'redux_dir': '/mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/', \
'blue': {'top': ['1','85','189','324','628'], 'bottom': ['761','167']}, \
'red': {'top': ['1','85','189','324','628'], 'bottom': ['761','455']}}}


for mask in ['0435m2']:
    sides,colors = ['top','bottom'],['blue','red']
    outdir = '/mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/'
    for side in sides:
        for color in colors:
            for slit in slit_name_dict[mask][color][side]:
                if color == 'blue':
                    doextract(mask,side,slit,colors=[color],maxpeaks=3)
                    if slit in slit_name_dict[mask]['red'][side]: doextract(mask,side,slit,colors=['red'],maxpeaks=3)
                else:
                    if not (slit in slit_name_dict[mask]['blue'][side]): doextract(mask,side,slit,colors=['red'],maxpeaks=3)
