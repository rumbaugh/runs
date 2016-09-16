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

def setHeader(infile,outfile,refWCS,refpix,exRA,exDec,exX,exY):
    cr = py.open(infile)
    hd1 = cr[0].header
    hd1['CTYPE1'] = 'RA---TAN'
    hd1['CTYPE2'] = 'DEC--TAN'
    hd1['CRVAL1'] = refWCS[0]
    hd1['CRVAL2'] = refWCS[1]
    hd1['CRPIX1'] = refpix[0]
    hd1['CRPIX2'] = refpix[1]
    CD1_1,CD1_2,CD2_1,CD2_2 = calcFitsCD(refWCS,refpix,exRA,exDec,exX,exY)
    hd1['CD2_2'],hd1['CD1_1'],hd1['CD1_2'],hd1['CD2_1'] = CD2_2,CD1_1,CD1_2,CD2_1
    cr.writeto(outfile)

refWCS = np.array([114.4008,32.262513])
refpix = np.array([109.5,109.5])
exRA = np.array([114.44743,114.36492])
exDec = np.array([32.250934,32.294048])
exX = np.array([25.493022,174.98147])
exY = np.array([86.532606,175.12424])
setHeader('/home/rumbaugh/HST/test0737_9.fits','/home/rumbaugh/HST/SDSS_0737.fits',refWCS,refpix,exRA,exDec,exX,exY)

refWCS = np.array([123.39337,25.756161])
refpix = np.array([109.5,109.5])
exRA = np.array([123.41531,123.36358])
exDec = np.array([25.782777,25.733545])
exX = np.array([67.157843,166.7582])
exY = np.array([165.53509,62.074887])
setHeader('/home/rumbaugh/HST/test0810.fits','/home/rumbaugh/HST/SDSS_0810.fits',refWCS,refpix,exRA,exDec,exX,exY)

refWCS = np.array([149.12185,51.03755])
refpix = np.array([109.5,109.5])
exRA = np.array([149.17455,149.0737])
exDec = np.array([51.024852,51.072863])
exX = np.array([37.687047,178.22318])
exY = np.array([87.163635,180.0813])
setHeader('/home/rumbaugh/HST/test0956.fits','/home/rumbaugh/HST/SDSS_0956.fits',refWCS,refpix,exRA,exDec,exX,exY)



