import numpy as np
import math as m
import matplotlib
import matplotlib.pylab as pylab

load_data("/scratch/rumbaugh/ciaotesting/4199/acis4199.img.500-2000.S07.norand.fits")
set_coord("physical")
cen = '3591.4156,3740.6206'
ann = 2*np.arange(20)+2
cnts = np.zeros(len(ann))
SB = np.zeros(len(ann))
FILE=open('/home/rumbaugh/ChandraData/4199/psSB.2.23.11.dat','w')
for i in range(0,len(ann)):
    if i == 0:
        reg = 'circle(%s,%i)'%(cen,ann[0])
        bgarea = m.pi*ann[0]**2
    else:
        reg = 'circle(%s,%i)-circle(%s,%i)'%(cen,ann[i],cen,ann[i-1])
        bgarea = m.pi*(ann[i]**2-ann[i-1]**2)
    cnts[i] = calc_data_sum2d(reg)
    SB[i] = cnts[i]/bgarea
    FILE.write('%i %f\n'%(ann[i],SB[i]))
FILE.close()
pylab.plot(ann,SB)
pylab.savefig('/home/rumbaugh/pstestplot.png')
pylab.close('all')
