import numpy as np

execfile('/home/rumbaugh/python_mwa/modelOpt.py')

namebase='/home/rumbaugh/python_mwa'
imgName='%s/HS0810_smallcut_814_image.fits'%namebase
sigName='%s/HS0810_smallcut_814_sigma.fits'%namebase
psfName='%s/HS0810_smallcut_PSF_814_image.fits'%namebase
guiFile='%s/HS0810_result_2.mod'%namebase
outFile='%s/HS0810_opt_result.12.10.15.dat'%namebase

modelOpt(imgName,sigName,psfName,guiFile,outFile)
