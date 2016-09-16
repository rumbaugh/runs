import numpy as np
import pyfits as py
import os

os.chdir('/home/rumbaugh/KAST/Science')
cr1 = py.open('sci-b373.fits')
cr2 = py.open('sci-b374.fits')
cr_out = py.open('sci-b373.fits')
cr_out[0].data = cr1[0].data+cr2[0].data
var1,var2 = cr1[1].data,cr2[1].data
cr_out[1].data = 1./(1./var1+1./var2)
hdr = cr1[1].header.copy()
cr_out.writeto('coadd.sci-b373-4.fits')
