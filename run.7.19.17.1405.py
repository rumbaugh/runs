import carmcmc as cm
import numpy as np
import pandas as pd
import pickle
import pyfits as py
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

outlier_window=300
outlier_thresh=0.5
num=5000

ri=30122
normfrac=0.317310507863
nsamples=20000

iLB,iUB=int(normfrac*0.5*nsamples),int((1-0.5*normfrac)*nsamples)

hdu=py.open('/home/rumbaugh/S2_lc.fits')
sndata=hdu[1].data

cenra,cendec=sndata['RA'][ri],sndata['DEC'][ri]
gri=np.sort(np.where((np.abs(cenra-sndata["RA"])<0.3)&(np.abs(cendec-sndata['DEC'])<0.3))[0])
data=sndata[gri]

outdf=pd.DataFrame({x: np.zeros(len(gri)) for x in ['RMS','numepoch']})
outdf['DataID']=gri
for ind in np.arange(len(data['COADD_OBJECT_ID'])):
    DBID=data['COADD_OBJECT_ID'][ind]
    try:
        DRWsample=pickle.load(open('/home/rumbaugh/CARpickles/SN_fields/S2/%i.DRWsample_OR.pickle'%DBID,'rb'))
    except:
        continue
    outdf['RMS'][ind]=np.sqrt(np.sum((DRWsample.y.values-np.mean(DRWsample.y.values))**2))
    outdf['numepoch']=len(DRWsample.y.values)
outdf['cid']=data['COADD_OBJECT_ID']
outdf['RA'],outdf["DEC"]=data['RA'],data['DEC']
outdf.to_csv('/home/rumbaugh/SN_fields.S2.cen_{}.RMS.csv'.format(ri),index=False)
