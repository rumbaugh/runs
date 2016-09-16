execfile("/home/rumbaugh/FindPeaks.py")
execfile("/home/rumbaugh/FindCloseSources.py")

import numpy as np
import math as m
import time
import sys

obsIDS = np.array(['10845','10856','10984','21','4472','4485','4510','49899','616','6399','7246','7421','7447','9922'])

FILE = open("/home/rumbaugh/COSMOS/test/peak.anal.1.8.11.dat","w")

for i in range(0,len(obsIDS)):
    cr2 = read_file("/home/rumbaugh/COSMOS/test/" + obsIDS[i] + "/regions/chips" + obsIDS[i] + ".S7.img.reg.txt")
    bx = get_colvals(cr2,'col1')
    by = get_colvals(cr2,'col2')
    bx -= 1
    bx = np.append(bx,bx[0])
    by -= 1
    by = np.append(by,by[0])
    for j in ('18.83','27.27','35.1'):
        imcr = read_file('/home/rumbaugh/COSMOS/test/%s/conv.beta.r_%s.fits'%(obsIDS[i],j))
        imcr2 = get_piximgvals(imcr)
        if j == '18.83': g = mkinArr(imcr2,by,bx)
        imcrcut = imcr2[g]
        imeantemp,istdtemp,imaxtemp = imcrcut.mean(),imcrcut.std(),imcrcut.max()
        overtemp = (imaxtemp-imeantemp)/istdtemp
        FILE.write('%5s %5s %9.7f %9.7f %9.7f %6.3f\n'%(obsIDS[i],j,imeantemp,istdtemp,imaxtemp,overtemp))
        print '%5s - %5s: Mean: %9.7f  Deviation: %6.3f'%(obsIDS[i],j,imeantemp,overtemp)
FILE.close()
