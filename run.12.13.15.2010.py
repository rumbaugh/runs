import numpy as np

execfile('/home/rumbaugh/python_mwa/run_gui.py')

namebase='/home/rumbaugh/HST/models'
outbase='/home/rumbaugh/python_mwa'
imgName='%s/SDSS-J0956+5100_cutout_image.fits'%namebase
sigName='%s/SDSS-J0956+5100_cutout_sigma.fits'%namebase
psfName='%s/0959_smallcut_PSF_image.fits'%namebase
guiFile='%s/0959_result_5.mod'%outbase
outFile='%s/0959_opt_result.12.13.15.dat'%outbase

rungui(imgName,sigName,psfName)
