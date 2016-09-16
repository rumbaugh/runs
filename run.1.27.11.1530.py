execfile("/home/rumbaugh/FindPeaks.py")
execfile("/home/rumbaugh/FindCloseSources.py")

import numpy as np
import math as m
import time
import sys
rc = np.array([1])
names = np.array(['5603'])
obsIDS = np.array(['5603'])

FILE = open("/home/rumbaugh/COSMOS/analysis/FPerroranal/lens.anal.1.27.11.dat","w")

for i in range(0,len(names)):
    cr2 = read_file('/scratch/rumbaugh/ciaotesting/%s/regions/chips%s.S7.img.reg.txt'%(names[i],names[i]))
    bx = get_colvals(cr2,'col1')
    by = get_colvals(cr2,'col2')
    bx -= 1
    bx = np.append(bx,bx[0])
    by -= 1
    by = np.append(by,by[0])
    imcr = read_file('/scratch/rumbaugh/ciaotesting/%s/conv.beta.12.4.10.fits'%(names[i]))
    imcr2 = get_piximgvals(imcr)
    g = mkinArr(imcr2,by,bx)
    imcrcut = imcr2[g]
    imeantemp,istdtemp,imaxtemp = imcrcut.mean(),imcrcut.std(),imcrcut.max()
    overtemp = (imaxtemp-imeantemp)/istdtemp
    FILE.write('%5s %5s %9.7f %9.7f %9.7f %6.3f\n'%(names[i],rc[i],imeantemp,istdtemp,imaxtemp,overtemp))
    print '%5s - %5s: Mean: %9.7f  Deviation: %6.3f'%(names[i],rc[i],imeantemp,overtemp)
FILE.close()
