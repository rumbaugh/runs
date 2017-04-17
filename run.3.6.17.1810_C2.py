import numpy as np
import pyfits as py
SN="C2"
bands=['g','r','i','z']
hdu=py.open('/home/rumbaugh/%s_lc.fits'%SN)
data=hdu[1].data
outcr_dict= {b: np.zeros((len(data)*np.shape(data['LC_MJD_%s'%b.upper()])[1],),dtype={'names':('COADD_OBJECT_ID','RA','DEC','MJD','MAG_PSF','MAG_PSF_ERROR','BAND','FLAGS'),'formats':('i8','f8','f8','f8','f8','f8','|S4','i8')}) for b in bands}
for b in bands:
    outcr_dict[b]['BAND']=b
    outcr_dict[b]['COADD_OBJECT_ID'],outcr_dict[b]['RA'],outcr_dict[b]['DEC'],outcr_dict[b]['FLAGS'] = np.repeat(data['COADD_OBJECT_ID'],np.shape(data['LC_MJD_%s'%b.upper()])[1]),np.repeat(data['RA'],np.shape(data['LC_MJD_%s'%b.upper()])[1]),np.repeat(data['DEC'],np.shape(data['LC_MJD_%s'%b.upper()])[1]),np.repeat(data['FLAGS_%s'%b.upper()],np.shape(data['LC_MJD_%s'%b.upper()])[1])
    outcr_dict[b]['MJD'],outcr_dict[b]['MAG_PSF'],outcr_dict[b]['MAG_PSF_ERROR']=data['LC_MJD_%s'%b.upper()].flatten(),data['LC_MAG_PSF_%s'%b.upper()].flatten(),data['LC_MAGERR_PSF_%s'%b.upper()].flatten()
    outcr_dict[b]=outcr_dict[b][outcr_dict[b]['MJD']!=0]
outcr=np.concatenate((outcr_dict['g'],outcr_dict['r'],outcr_dict['i'],outcr_dict['z']),axis=0)
outcr['MAG_PSF'][outcr['MAG_PSF']==np.inf]=0
outcr['MAG_PSF'][outcr['MAG_PSF']<-99]=0
outcr['MAG_PSF_ERROR'][outcr['MAG_PSF_ERROR']>99]=0
outcr['MAG_PSF'][np.isnan(outcr['MAG_PSF'])]=0
outcr['MAG_PSF_ERROR'][np.isnan(outcr['MAG_PSF_ERROR'])]=0
np.savetxt('/home/rumbaugh/Eric_LC_%s.csv'%SN,outcr,fmt='%i,%f,%f,%f,%f,%f,%4s,%i')