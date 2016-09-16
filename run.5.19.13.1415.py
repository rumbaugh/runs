import numpy as np
import os
execfile("/home/rumbaugh/LRIS_files_dict_master.py")

def run_swarp(outdir,mask,color,side):
    FILE = open('swarpinputlist_tmp.lst','w')
    FILE2 = open('swarpinweights_tmp.lst','w')
    for img in files_dict[mask][color]['images']:
        FILE.write('%s%s_%s_%s_%i_bgsub.fits\n'%(outdir,mask,color,side,img))
        FILE2.write('%s%s_%s_%s_%i_var.fits\n'%(outdir,mask,color,side,img))
    FILE.close()
    FILE2.close()
    os.system("swarp @swarpinputlist_tmp.lst -IMAGEOUT_NAME '%s%s_%s_%s_coadd_bgsub.fits' -WEIGHTOUT_NAME '%s%s_%s_%s_coadd_bgsub.weight.fits' -WEIGHT_IMAGE @swarpinweights_tmp.lst -WEIGHT_TYPE MAP_VARIANCE"%(outdir,mask,color,side,outdir,mask,color,side))
    os.system("rm swarpinputlist_tmp.lst")
    os.system("rm swarpinweights_tmp.lst")

outdir = '/local/rumbaugh/LRIS/Marusa/reduced/LRIS19_022010/'
for mask in ['M0744_A','M0744_B','M0417_B','M1115_A']: 
    for color in ['red','blue']:
        for side in ['top','bottom']: run_swarp(outdir,mask,color,side)

outdir = '/local/rumbaugh/LRIS/Marusa/reduced/LRIS5_062011/'
for mask in ['miki10.f','miki22_z','miki21_B']: 
    for color in ['red','blue']:
        for side in ['top','bottom']: run_swarp(outdir,mask,color,side)

outdir = '/local/rumbaugh/LRIS/2011_01/reduced/'
for mask in ['1131m3','1131m4']: 
    for color in ['red','blue']:
        for side in ['top']: run_swarp(outdir,mask,color,side)
            
