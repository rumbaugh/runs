import numpy as np
import pyfits as py
import os
os.chdir('/home/rumbaugh/Chandra/3181+4987')

n={'soft':'500-2000','hard':'2000-8000','full':'500-8000'}

for band in ['soft','hard','full']:
    os.system('cp acis3181+4987.img.%s.fits bkup_acis3181+4987.img.%s.fits'%(n[band],n[band]))
    cr=py.open('acis3181+4987.img.%s.fits'%(n[band]))
    hdu=cr[0]
    hdr=hdu.header
    hdr['DEC_NOM']=-0.055434733548739
    hdr['RA_NOM']=36.157786351298
    hdr['DEC_PNT']=-0.055434733548739
    hdr['RA_PNT']=36.151988597363
    hdr['ROLL_NOM']=303.25754474283
    hdr['ROLL_PNT']=303.25754474283
    cr.writeto('acis3181+4987.img.%s.fits'%(n[band]),clobber=True)
