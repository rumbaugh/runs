import numpy as np

cr = np.loadtxt('/home/rumbaugh/KAST/Science/sci_fits_list.txt',dtype='string')

FILECR=open('/home/rumbaugh/KAST/Science/CRmask_list.txt','w')
FILEvarout=open('/home/rumbaugh/KAST/Science/skysub_noCR_var_out_list.txt','w')

for i in range(0,len(cr)):
    if len(cr[i]) == 13:
        color=cr[i][4]
        num = cr[i][5:8]
        FILEvarout.write('sci-%s%s.var_skysub_CRmask.fits\n'%(color,num))
        FILECR.write('CRmask-%s%s.skysub.fits\n'%(color,num))
FILEvarout.close()
FILECR.close()
