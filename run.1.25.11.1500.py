execfile("/home/rumbaugh/FindPeaks.py")
execfile("/home/rumbaugh/FindCloseSources.py")

import numpy as np
import math as m
import time
import sys
rc = np.array([36.45,28.32,19.55,16.62,15.44])
names = np.array(['7757+363','9515+10576','427+3461','419+1629','423+424'])
obsIDS = np.array(['10845','10856','10984','21','4472','4485','4510','49899','616','6399','7246','7421','7447','9922'])
conv = np.array(['1.24.11.7757+363','9515+10576.12.9.10','1.24.11.427+3461','1.24.11.419+1629','423+424.12.9.10'])

FILE = open("/home/rumbaugh/COSMOS/analysis/FPerroranal/merged.lens.anal.1.25.11.dat","w")

for i in range(0,len(names)):
    cr2 = read_file("/scratch/rumbaugh/ciaotesting/merged/chips" + names[i] + ".img.txt")
    bx = get_colvals(cr2,'col1')
    by = get_colvals(cr2,'col2')
    bx -= 1
    bx = np.append(bx,bx[0])
    by -= 1
    by = np.append(by,by[0])
    imcr = read_file('/scratch/rumbaugh/ciaotesting/merged/conv.beta.%s.fits'%(conv[i]))
    imcr2 = get_piximgvals(imcr)
    g = mkinArr(imcr2,by,bx)
    imcrcut = imcr2[g]
    imeantemp,istdtemp,imaxtemp = imcrcut.mean(),imcrcut.std(),imcrcut.max()
    overtemp = (imaxtemp-imeantemp)/istdtemp
    FILE.write('%5s %5s %9.7f %9.7f %9.7f %6.3f\n'%(names[i],rc[i],imeantemp,istdtemp,imaxtemp,overtemp))
    print '%5s - %5s: Mean: %9.7f  Deviation: %6.3f'%(names[i],rc[i],imeantemp,overtemp)
FILE.close()
