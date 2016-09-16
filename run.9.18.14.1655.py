import pyfits as pf
import os

a = os.chdir('/mnt/data2/rumbaugh/HST/models')
hdu = pf.open('HS0810_smallcut_image.fits')
hdu2 = pf.open('HS0810_smallcut_814_image.fits')
data = hdu[0].data.copy()
data2 = hdu2[0].data.copy()
newdat = data+data2
hdr = hdu[0].header.copy()
pf.PrimaryHDU(newdat,hdr).writeto('HS0810_smallcut_image_green.fits')
hdu.close()
hdu2.close()
