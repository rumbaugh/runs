import numpy as np
import pyfits as py

def calcFitsCD(refWCS,refpix,exRA,exDec,exX,exY):
    #refWCS is array with RA,Dec of reference pixel in degrees.
    #refpix is array with image coordinates of ref. pixel.
    #exRA,exDec,exX,exY are four arrays, each with two components. They 
    #are the coordinates of four points in the image. Cannot be the same
    #as the reference pixel.

    exRA = (exRA-refWCS[0])*np.cos(exDec*np.pi/180.)
    exDec -= refWCS[1]
    exX -= refpix[0]
    exY -= refpix[1]
    ror = exY[0]*1./exY[1]
    bottom = exX[0]-ror*exX[1]
    CD1_1 = (exRA[0]-ror*exRA[1])/bottom
    CD1_2 = (exRA[0]-CD1_1*exX[0])*1./exY[0]
    CD2_1 = (exDec[0]-ror*exDec[1])/bottom
    CD2_2 = (exDec[0]-CD2_1*exX[0])*1./exY[0]
    return CD1_1,CD1_2,CD2_1,CD2_2


cr = py.open('HST/test0737_4.fits')
hd1 = cr[0].header
refWCS = np.array([114.40243,32.260599])
refpix = np.array([264.5,264.5])
exRA = np.array([114.42106,114.36514])
exDec = np.array([32.307513,32.319961])
exX = np.array([233,333.60401])
exY = np.array([364.5,389.02713])


hd1['CTYPE1'] = 'RA---TAN'
hd1['CTYPE2'] = 'DEC--TAN'
hd1['CRVAL1'] = refWCS[0]
hd1['CRVAL2'] = refWCS[1]
hd1['CRPIX1'] = refpix[0]
hd1['CRPIX2'] = refpix[1]

CD1_1,CD1_2,CD2_1,CD2_2 = calcFitsCD(refWCS,refpix,exRA,exDec,exX,exY)

hd1['CD2_2'],hd1['CD1_1'],hd1['CD1_2'],hd1['CD2_1'] = CD2_2,CD1_1,CD1_2,CD2_1

cr.writeto('HST/test0737_8.fits')

