import numpy as np
import os

files_dict = {'M0417_B': {'prefix': '100214_', \
'red': {'arc': 999, 'flat': 45, 'flat_array': np.array([3,42,43,44,45]), 'images': np.array([48,49,50,51,52,53])}, \
'blue': {'arc': 56, 'flat': 42, 'flat_array': np.array([1,40,41,42]), 'images': np.array([49,50,51,53,54,55])}}, \
'M0744_A': {'prefix': '100214_', \
'red': {'arc': None, 'flat': 41, 'flat_array': np.array([5,38,39,40,41]), 'images': np.array([54,55,56,57,58,59])}, \
'blue': {'arc': 70, 'flat': 38, 'flat_array': np.array([2,36,37,38]), 'images': np.array([61,62,63,67,68])}}, \
'M0744_B': {'prefix': '100214_', \
'red': {'arc': None, 'flat': 37, 'flat_array': np.array([7,35,36,37]), 'images': np.array([60,61,62,63,64])}, \
'blue': {'arc': 84, 'flat': 35, 'flat_array': np.array([7,33,34,35]), 'images': np.array([78,79,80,82,83])}}, \
'M1115_A': {'prefix': '100214_', \
'red': {'arc': None, 'flat': 34, 'flat_array': np.array([9,32,33,34]), 'images': np.array([65,66,67,68,69,70])}, \
'blue': {'arc': 96, 'flat': 32, 'flat_array': np.array([30,31,32]), 'images': np.array([89,90,91,93,94,95])}}, \
'Feige67': {'prefix': '100214_', \
'red': {'wavelengths': np.array(['8179','8899']), \
'8179': {'arc': 71, 'flat': 76, 'images': np.array([75])}, \
'8889': {'arc': 72, 'flat': 77, 'images': np.array([73,74])}}, \
'blue': {'arc': 98, 'flat': 101, 'images': np.array([99,100])}}}


indir = '/local/rumbaugh/LRIS/Marusa/LRIS19_022010'
outdir = '/local/rumbaugh/LRIS/Marusa/reduced/LRIS19_022010/'
for mask in ['M0417_B','M0744_A','M0744_B','M1115_A']: 
    for color in ['red','blue']:
        for side in ['top','bottom']:
            FILE = open('swarpinputlist_tmp.lst','w')
            FILE2 = open('swarpinweights_tmp.lst','w')
            for img in files_dict[mask][color]['images']:
                FILE.write('%s%s_%s_%s_%i_bgsub.fits\n'%(outdir,mask,color,side,img))
                FILE2.write('%s%s_%s_%s_%i_var.fits\n'%(outdir,mask,color,side,img))
            FILE.close()
            FILE2.close()
            os.system("swarp @swarpinputlist_tmp.lst -IMAGEOUT_NAME '%s%s_%s_%s_coadd_bgsub.fits' -WEIGHTOUT_NAME '%s%s_%s_%s_coadd_bgsub.weight.fits -WEIGHT_IMAGE @swarpinweights_tmp.lst"%(outdir,mask,color,side,outdir,mask,color,side))
            
