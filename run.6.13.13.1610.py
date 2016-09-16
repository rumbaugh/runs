import numpy as np
import os
execfile("/home/rumbaugh/LRIS_files_dict_master.py")

def run_swarp(outdir,mask,color,side):
    FILE = open('swarpinputlist_tmp.lst','w')
    FILE2 = open('swarpinweights_tmp.lst','w')
    images = []
    try:
        for night in files_dict[mask]['night']:
            images = np.append(images,files_dict[mask]['night'][night][color]['images'])
    except KeyError:
        images = files_dict[mask][color]['images']
    for img in images:
        FILE.write('%s%s_%s_%s_%i_bgsub.fits\n'%(outdir,mask,color,side,img))
        FILE2.write('%s%s_%s_%s_%i_var.fits\n'%(outdir,mask,color,side,img))
    FILE.close()
    FILE2.close()
    os.system("swarp @swarpinputlist_tmp.lst -IMAGEOUT_NAME '%s%s_%s_%s_coadd_bgsub.fits' -WEIGHTOUT_NAME '%s%s_%s_%s_coadd_bgsub.weight.fits' -WEIGHT_IMAGE @swarpinweights_tmp.lst -WEIGHT_TYPE MAP_VARIANCE"%(outdir,mask,color,side,outdir,mask,color,side))
    os.system("rm swarpinputlist_tmp.lst")
    os.system("rm swarpinweights_tmp.lst")

outdir = '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/'
for mask in ['miki22.f','miki21.f','miki04.f','miki04_B','miki04_A','miki03_B','miki03_A']: 
    for color in ['red','blue']:
        for side in ['top','bottom']: run_swarp(outdir,mask,color,side)

outdir = '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/'
for mask in ['miki21D.','miki16B.','bc3.file','bc3B.fil']: 
    for color in ['red','blue']:
        for side in ['top','bottom']: run_swarp(outdir,mask,color,side)

outdir = '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/'
for mask in ['miki21C.']: 
    for color in ['blue']:
        for side in ['top']: run_swarp(outdir,mask,color,side)
    for color in ['red']:
        for side in ['top','bottom']: run_swarp(outdir,mask,color,side)
            
