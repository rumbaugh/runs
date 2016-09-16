execfile("/home/rumbaugh/FindPeaks.py")
execfile("/home/rumbaugh/FindCloseSources.py")

import numpy as np
import math as m
import time
import sys

obsIDS = np.array(['10845','10856','10984','21','4472','4485','4510','49899','616','6399','7246','7421','7447','9922'])

names = np.array(['3572','4807'])
mnames = '423+424'

FILE = open("/home/rumbaugh/COSMOS/peak.anal.1.29.11.dat","w")

for i in range(0,len(names)):
    cr2 = read_file("/scratch/rumbaugh/ciaotesting/" + names[i] + "/regions/chips" + names[i] + ".S7.img.reg.txt")
    bx = get_colvals(cr2,'col1')
    by = get_colvals(cr2,'col2')
    bx -= 1
    bx = np.append(bx,bx[0])
    by -= 1
    by = np.append(by,by[0])
    imcr = read_file('/scratch/rumbaugh/ciaotesting/%s/conv.beta.1.29.11.fits'%(names[i]))
    imcr2 = get_piximgvals(imcr)
    g = mkinArr(imcr2,by,bx)
    imcrcut = imcr2[g]
    imeantemp,istdtemp,imaxtemp = imcrcut.mean(),imcrcut.std(),imcrcut.max()
    overtemp = (imaxtemp-imeantemp)/istdtemp
    FILE.write('%5s %9.7f %9.7f %9.7f %6.3f\n'%(names[i],imeantemp,istdtemp,imaxtemp,overtemp))
    print '%5s: Mean: %9.7f  Deviation: %6.3f'%(names[i],imeantemp,overtemp)
cr2 = read_file("/scratch/rumbaugh/ciaotesting/merged/chips423+424.img.reg.txt")
bx = get_colvals(cr2,'col1')
by = get_colvals(cr2,'col2')
bx -= 1
bx = np.append(bx,bx[0])
by -= 1
by = np.append(by,by[0])
imcr = read_file('/scratch/rumbaugh/ciaotesting/merged/conv.beta.1.29.11.423+424.fits')
imcr2 = get_piximgvals(imcr)
g = mkinArr(imcr2,by,bx)
imcrcut = imcr2[g]
imeantemp,istdtemp,imaxtemp = imcrcut.mean(),imcrcut.std(),imcrcut.max()
overtemp = (imaxtemp-imeantemp)/istdtemp
FILE.write('%5s %9.7f %9.7f %9.7f %6.3f\n'%(mnames[i],imeantemp,istdtemp,imaxtemp,overtemp))
print '%5s: Mean: %9.7f  Deviation: %6.3f'%(mnames[i],imeantemp,overtemp)
FILE.close()
