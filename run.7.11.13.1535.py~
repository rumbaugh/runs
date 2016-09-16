import numpy as np
import os
execfile("/home/rumbaugh/LRIS_files_dict_master.py")
execfile("/home/rumbaugh/slit_name_dict_master.py")

def run_swarp(outdir,mask,color,side,combine_type='SUM',resample='Y'):
    FILE = open('swarpinputlist_tmp.lst','w')
    FILE2 = open('swarpinweights_tmp.lst','w')
    #try:
    #    for night in files_dict[mask]['night']:
    #        images = np.append(images,files_dict[mask]['night'][night][color]['images'])
    #except KeyError:
    #    images = files_dict[mask][color]['images']
    for maskt in ['0414m3_1','0414m3_2']:
        for img in files_dict[maskt][color]['images']:
            FILE.write('%s%s_%s_%s_%i_bgsub.fits\n'%(outdir,maskt,color,side,img))
            FILE2.write('%s%s_%s_%s_%i_var.fits\n'%(outdir,maskt,color,side,img))
    FILE.close()
    FILE2.close()
    os.system("swarp @swarpinputlist_tmp.lst -IMAGEOUT_NAME '%s%s_%s_%s_coadd_bgsub.fits' -WEIGHTOUT_NAME '%s%s_%s_%s_coadd_bgsub.weight.fits' -WEIGHT_IMAGE @swarpinweights_tmp.lst -WEIGHT_TYPE MAP_VARIANCE -BLANK_BADPIXELS Y -RESCALE_WEIGHTS N -BACK_TYPE MANUAL -SUBTRACT_BACK N -COMBINE_TYPE %s -RESAMPLE %s"%(outdir,mask,color,side,outdir,mask,color,side,combine_type,resample))
    os.system("rm swarpinputlist_tmp.lst")
    os.system("rm swarpinweights_tmp.lst")

#outdir = '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/'
#for mask in ['miki22.f','miki21.f','miki04.f','miki04_A']: 
#    for color in ['blue','red']:
#        for side in ['top','bottom']: run_swarp(outdir,mask,color,side)

#outdir = '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/'
#for mask in ['miki21C.']: 
#    for color in ['red']:
#        for side in ['bottom']: run_swarp(outdir,mask,color,side)

#outdir = '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/'
for mask in ['0414m3']: 
    outdir = '/mnt/data3/rumbaugh/LRISdata/reduced/'
    for color in ['blue']:
        for side in ['top']: run_swarp(outdir,mask,color,side,combine_type='MEDIAN')
    for color in ['red']:
        for side in ['top']: run_swarp(outdir,mask,color,side,combine_type='MEDIAN',resample='N')
    for color in ['blue']:
        for side in ['bottom']: run_swarp(outdir,mask,color,side,resample='N')
    for color in ['red']:
        for side in ['bottom']: run_swarp(outdir,mask,color,side,combine_type='MEDIAN')
