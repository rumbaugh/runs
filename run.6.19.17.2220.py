import numpy as np
import os
import pandas as pd
import pyfits as py

phdu=py.open('/home/rumbaugh/plates-dr12.fits')
pdata=phdu[1].data

pdata_df=pd.DataFrame({'plateid':pdata['PLATEID'],'plate':pdata['PLATE'],'run2d':pdata['RUN2D'],'mjd':pdata['MJD']})

try:
    dotest
except NameError:
    dotest=False

indf=pd.read_csv('/home/rumbaugh/random_SDSS_specs.csv',na_values='null')
if dotest:
    indf=indf.iloc[:10]

indf=pd.merge(indf,pdata_df,on=['plate','mjd'])

outcr=np.zeros(len(indf.sourcetype.values)+2,dtype='|S120')
outcr[0],outcr[1]='mkdir -p /home/rumbaugh/SDSS_PCA/spec','cd /home/rumbaugh/SDSS_PCA/spec'
for i in range(0,len(outcr)-2):
    #if indf.plate.values[i]<1963:
    #    redux='26'
    #elif indf.plate.values[i]<3140:
    #    redux='103'
    #elif indf.plate.values[i]<4190:
    #    redux='104'
    #else:
    #    redux='v5_7_0'
    outcr[i+2]='wget https://dr12.sdss.org/sas/dr12/sdss/spectro/redux/%s/spectra/%04i/spec-%04i-%05i-%04i.fits'%(indf.run2d.values[i],indf.plate.values[i],indf.plate.values[i],indf.mjd.values[i],indf.fiberid.values[i])
np.savetxt('/home/rumbaugh/runs/run.6.19.17.2220.sh',outcr,fmt='%s')
os.system('chmod +x /home/rumbaugh/runs/run.6.19.17.2220.sh')
