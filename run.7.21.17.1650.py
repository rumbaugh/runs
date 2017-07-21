import numpy as np
import pandas as pd
import pickle
import pyfits as py

outlier_window=300
outlier_thresh=0.5
num=5000

hdu=py.open('/home/rumbaugh/S2_lc.fits')
data=hdu[1].data

outdf=pd.DataFrame({x: np.zeros(len(gri)) for x in ['RMS','RMSnorm','numepoch']})
outdf['DataID']=gri
for ind in np.arange(len(data['COADD_OBJECT_ID'])):
    len_lc=np.count_nonzero(data[ind]['LC_MJD_G'])
    outdf.numepoch_tot[ind]=len_lc
    if len_lc<6:
        outdf.numepoch[ind]=0
        continue
    DBID=data['COADD_OBJECT_ID'][ind]
    mjd,mag,magerr=np.zeros(len_lc),np.zeros(len_lc),np.zeros(len_lc)
    mjd[:],mag[:],magerr[:]=data[ind]['LC_MJD_G'][:len_lc],data[ind]['LC_MAG_PSF_G'][:len_lc],data[ind]['LC_MAGERR_PSF_G'][:len_lc]
    inf_or_nan=np.ones(len(mjd),dtype='bool')
    for arr in [mjd,mag,magerr]:
        for func in [np.isnan,np.isinf]:
            inf_or_nan*=np.invert(func(arr))
    mjd,mag,magerr=mjd[inf_or_nan],mag[inf_or_nan],magerr[inf_or_nan]
    len_lc=len(mjd)
    outlier_arr= np.zeros(len_lc,dtype='bool')
    for ipt in np.arange(len(outlier_arr)):
        gthresh=np.where(np.abs(mjd-mjd[ipt])<outlier_window)[0]
        if len(gthresh)>1:
            outlier_arr[ipt]= np.abs(np.median(mag[gthresh])-mag[ipt]) > outlier_thresh
    mjd,mag,magerr=mjd[outlier_arr==False],mag[outlier_arr==False],magerr[outlier_arr==False]
    outdf.numepoch[ind]=len(mjd)
    outdf['RMS'][ind]=np.sqrt(np.sum((mag-np.mean(mag))**2)/len(mag))
    outdf['RMSnorm'][ind]=np.sqrt(np.sum(((mag-np.mean(mag))/magerr)**2)/len(mag))
    outdf['numepoch'][ind]=len(mag)
outdf['cid']=data['COADD_OBJECT_ID']
outdf['RA'],outdf["DEC"]=data['RA'],data['DEC']
outdf.to_csv('/home/rumbaugh/SN_fields.S2.AUTO_RMS.csv',index=False)
