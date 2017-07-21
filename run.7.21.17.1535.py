import numpy as np
import pandas as pd
import pickle
import pyfits as py

for field in ['S1','S2']:

    hdu=py.open('/home/rumbaugh/{}_lc.fits'.format(field))
    data=hdu[1].data

    outdf=pd.DataFrame({x: data[x] for x in ['COADD_OBJECT_ID','RA','DEC']})
    outdf['DataID']=outdf.index.values
    outdf['numrow']=np.arange(len(outdf))

    outdf.to_csv('/home/rumbaugh/SN_fields.{}.radecid.csv'.format(field),index=False)
