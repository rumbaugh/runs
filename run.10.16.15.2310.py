import numpy as np
import pyfits as py
import os
os.chdir('/home/rumbaugh/Chandra/2227+2452')

n={'soft':'500-2000','hard':'2000-8000','full':'500-8000'}

for band in ['soft','hard','full']:
    os.system('cp acis2227+2452.img.%s.fits bkup_acis2227+2452.img.%s.fits'%(n[band],n[band]))
    cr=py.open('acis2227+2452.img.%s.fits'%(n[band]))
    hdu=cr[0]
    hdr=hdu.header
    hdr['DEC_NOM']=54.332598330688
    hdr['RA_NOM']=137.66683284603
    hdr['DEC_PNT']=54.332598330688
    hdr['RA_PNT']=137.66683284603
    hdr['ROLL_NOM']=252.8319816219
    hdr['ROLL_PNT']=252.8319816219
    cr.writeto('acis2227+2452.img.%s.fits'%(n[band]),clobber=True)
