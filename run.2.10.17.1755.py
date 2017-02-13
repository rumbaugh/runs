import numpy as np
import pyfits as py

try:
    doload
except NameError:
    doload=True

if doload: cr=np.loadtxt('/home/rumbaugh/Eric_LC_Y3A1.tab',dtype={'names':('COADD_OBJECT_ID','RA','DEC','MJD','MAG_PSF','MAG_PSF_ERROR','MAG_AUTO','MAG_AUTO_ERROR','BAND','FLAGS'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','|S4','i8')},skiprows=1)
cr['MAG_PSF'][cr['MAG_PSF']<-99]=0
cr['MAG_PSF_ERROR'][cr['MAG_PSF_ERROR']>99]=0
cr['MAG_AUTO'][cr['MAG_AUTO']<-99]=0
cr['MAG_AUTO_ERROR'][cr['MAG_AUTO_ERROR']>99]=0
np.savetxt('/home/rumbaugh/Eric_LC_Y3A1.csv',cr,header=('COADD_OBJECT_ID RA DEC MJD MAG_PSF MAG_PSF_ERROR MAG_AUTO MAG_AUTO_ERROR BAND FLAGS'),fmt=('%i,%f,%f,%f,%f,%f,%f,%f,%4s,%i'),comments='')
py.PrimaryHDU(cr).writeto('/home/rumbaugh/Eric_LC_Y3A1.fits',clobber=True)
