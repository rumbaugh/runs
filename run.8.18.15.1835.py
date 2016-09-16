import numpy as np

cr = np.loadtxt('/home/rumbaugh/KAST/Science/sci_fits_list.txt',dtype='string')

FILEin = open('/home/rumbaugh/KAST/Science/in_list.txt','w')
FILEit = open('/home/rumbaugh/KAST/Science/invtargets_list.txt','w')
FILEio = open('/home/rumbaugh/KAST/Science/invout_list.txt','w')
FILEsky=open('/home/rumbaugh/KAST/Science/skyfile_list.txt','w')
FILEout=open('/home/rumbaugh/KAST/Science/skysub_out_list.txt','w')
FILEvarout=open('/home/rumbaugh/KAST/Science/skysub_var_out_list.txt','w')
FILEones=open('/home/rumbaugh/KAST/Science/ones_list.txt','w')

for i in range(0,len(cr)):
    if len(cr[i]) == 13:
        color=cr[i][4]
        num = cr[i][5:8]
        FILEin.write('%s[0]\n'%cr[i])
        FILEit.write('%s[1]\n'%cr[i])
        FILEio.write('sci-%s%s.var.fits\n'%(color,num))
        FILEsky.write('%s[2]\n'%cr[i])
        FILEout.write('sci-%s%s.skysub.fits\n'%(color,num))
        FILEvarout.write('sci-%s%s.var_skysub.fits\n'%(color,num))
        FILEones.write('1\n')
FILEin.close()
FILEit.close()
FILEio.close()
FILEsky.close()
FILEout.close()
FILEones.close()
FILEvarout.close()
