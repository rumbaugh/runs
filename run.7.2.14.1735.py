import pyfits as pf
import os

hdu = pf.open('LateSB1_10.7.21.11.11A-138.B1938+666.fits')
data = hdu[0].data.copy()
newdat = data[0,0,:,:]
hdr = hdu[0].header.copy()
pf.PrimaryHDU(newdat,hdr).writeto('B1938_map_for_plot.fits')
hdu.close()
