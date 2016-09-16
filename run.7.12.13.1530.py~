import numpy as np
import os
import lris_extract
import pyfits

execfile('/home/rumbaugh/slit_name_dict_master.py')

def doextract(mask,side,colors=['blue','red'],maxpeaks=3):
    osv = os.system('mkdir -p %s%s'%('/mnt/data2/rumbaugh/LRIS/2011_01/reduced/',mask))
    osv = os.chdir('%s%s'%('/mnt/data2/rumbaugh/LRIS/2011_01/reduced/',mask))
    osv = os.system("mkdir -p %s%s/plots"%('/mnt/data2/rumbaugh/LRIS/2011_01/reduced/',mask))
    osv = os.system("mkdir -p %s%s/spec_output"%('/mnt/data2/rumbaugh/LRIS/2011_01/reduced/',mask))
    for color in colors:
        try:
            osv = os.system("ln -s %s%s_%s_%s_coadd_bgsub.fits ."%('/mnt/data2/rumbaugh/LRIS/2011_01/reduced/',mask,color,side))
            osv = os.system("ln -s %s%s_%s_%s_coadd_bgsub.weight.fits ."%('/mnt/data2/rumbaugh/LRIS/2011_01/reduced/',mask,color,side))
            lris_extract.lris_extract("%s_%s_%s_coadd_bgsub.fits"%(mask,color,side),"spec_output/outspec.%s_%s_%s_coadd_bgsub.dat"%(mask,color,side),weightfile="%s_%s_%s_coadd_bgsub.weight.fits"%(mask,color,side),output_plot="%s_%s_%s_coadd_bgsub.ps"%(mask,color,side),output_plot_dir = '%s/%s/plots'%('/mnt/data2/rumbaugh/LRIS/2011_01/reduced/',mask),nan_to_zero=True,findmultiplepeaks=True,maxpeaks=maxpeaks)
        except IOError:
            print 'File %s_%s_%s_coadd_bgsub.fits not found. Skipping to next observation.'%(mask,color,side)

for mask in ['0435_slit1','0435_slit2']:
    outdir = '/mnt/data2/rumbaugh/LRIS/2011_01/reduced/'
    sides,colors = ['top'],['blue','red']
    for side in sides:
        for color in colors:
            doextract(mask,side,colors=[color],maxpeaks=3)
