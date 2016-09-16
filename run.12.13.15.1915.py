import numpy as np

execfile('/home/rumbaugh/python_mwa/modelOpt.py')

namebase='/home/rumbaugh/HST/models'
outbase='/home/rumbaugh/python_mwa'
imgName='%s/0737+315_smallcut_image.fits'%namebase
sigName='%s/0737+315_smallcut_sigma.fits'%namebase
psfName='%s/0737+315_smallcut_PSF_image.fits'%namebase
guiFile='%s/0737+315_result_5.mod'%outbase
outFile='%s/0737+315_opt_result.12.13.15.dat'%outbase

modelOpt(imgName,sigName,psfName,guiFile,outFile)
