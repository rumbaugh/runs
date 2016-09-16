import numpy as np
from pyds9 import *
import os
import sys
import time


obsids=np.array([3181,4987,927,1708,2227,2452,4936,1662,2229,548,6932,6933,7343,7914,9403,9840,9404,9836,10443,11999,10444,10924,4161])

os.system('ds9 &')
time.sleep(2.5)
dtgts=ds9_targets()
ds9targ=dtgts[-1][8:]
d=DS9(ds9targ)
for i in obsids:
    fitsfile='/home/rumbaugh/Chandra/%s/acis%s.img.500-8000.fits'%(i,i)
    regfile='/home/rumbaugh/Chandra/%s/chip%s.reg'%(i,i)
    outfile='/home/rumbaugh/Chandra/%s/chips_wcs.%s.reg'%(i,i)
    d.set('file %s'%fitsfile)
    d.set('regions delete all')
    d.set('regions load %s'%regfile)
    d.set('regions sky fk5')
    d.set('regions format ds9')
    d.set('regions skyformat degrees')
    d.set('regions system wcs')
    d.set('regions save %s'%outfile)
    
