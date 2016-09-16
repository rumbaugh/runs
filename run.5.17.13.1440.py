import numpy as np
import os
execfile("/home/rumbaugh/LRIS_files_dict_master.py")

outdir = '/local/rumbaugh/LRIS/Marusa/reduced/LRIS19_022010/'
for mask in ['M0744_B']: 
    for color in ['red']:
        for side in ['top']:
            FILE = open('swarpinputlist_tmp.lst','w')
            FILE2 = open('swarpinweights_tmp.lst','w')
            for img in files_dict[mask][color]['images']:
                FILE.write('%s%s_%s_%s_%i_bgsub.fits\n'%(outdir,mask,color,side,img))
                FILE2.write('%s%s_%s_%s_%i_var.fits\n'%(outdir,mask,color,side,img))
            FILE.close()
            FILE2.close()
            os.system("swarp @swarpinputlist_tmp.lst -IMAGEOUT_NAME '%s%s_%s_%s_coadd_bgsub.fits' -WEIGHTOUT_NAME '%s%s_%s_%s_coadd_bgsub.weight.fits' -WEIGHT_IMAGE @swarpinweights_tmp.lst -WEIGHT_TYPE MAP_VARIANCE"%(outdir,mask,color,side,outdir,mask,color,side))
            #os.system("rm swarpinputlist_tmp.lst")
            #os.system("rm swarpinweights_tmp.lst")
            
