import numpy as np
import pandas as pd
import pickle
import pyfits as py
import matplotlib
import matplotlib.pyplot as plt
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

outdf=pd.DataFrame({x: data[x] for x in ['COADD_OBJECT_ID','RA','DEC']})
outdf['DataID']=gri
outdf['numrow']=np.arange(len(gri))

outdf.to_csv('/home/rumbaugh/SN_fields.S2.cen_{}.radecid.csv'.format(ri),index=False)
