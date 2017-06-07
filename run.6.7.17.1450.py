import numpy as np
import healpy as hp
import pandas as pd
df=pd.read_csv('/home/rumbaugh/DR12Q_notinDR7_SNRADECTID.csv')
names,ra,dec=df['SDSS_NAME'],df['RA'],df['DEC']

hpix=hp.ang2pix(16384,(90-dec)*np.pi/180.,ra*np.pi/180,nest=True)
outdf=pd.DataFrame({'SDSS_NAME':names,'RA':ra,'DEC':dec,'HPIX':hpix},columns=['SDSS_NAME','RA','DEC','HPIX'])
outdf.to_csv('/home/rumbaugh/DR12Q_notinDR7_hpix.csv',index=False)
