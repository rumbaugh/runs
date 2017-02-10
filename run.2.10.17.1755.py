import numpy as np
import pyfits as py

cr=np.loadtxt('/home/rumbaugh/Eric_LC_Y3A1.tab',dtype={'names':('COADD_OBJECT_ID','RA','DEC','MJD','MAG_PSF','MAG_PSF_ERROR','MAG_AUTO','MAG_AUTO_ERROR','BAND','FLAGS'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','|S4','i8')},skiprows=1)
py.PrimaryHDU(cr).writeto('/home/rumbaugh/Eric_LC_Y3A1.fits',clobber=True)
