import numpy as np
import pyfits as py
import pandas as pd

hdu=py.open('/home/rumbaugh/DR12Q.fits')
qdata=hdu[1].data

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
try:
    indsdf=pd.read_csv('/home/rumbaugh/DR12Q_DR7_match.csv')
except IOError:
    import pydl.pydlutils.spheregroup
    sout=pydl.pydlutils.spheregroup.spherematch(bhdata['RA'],bhdata['DEC'],qdata['RA'],qdata['DEC'],0.3/3600)
    indsdf=pd.DataFrame({'DR7IND':sout[0],'DR12IND':sout[1],'DIST':sout[2]})
    indsdf.to_csv('/home/rumbaugh/DR12Q_DR7_match.csv')
notinDR7=np.in1d(np.arange(len(qdata)),indsdf['DR12IND'],invert=True)

qdata=qdata[notinDR7]
qdf=pd.DataFrame({x: qdata[x] for x in ['SDSS_NAME','RA','DEC','THING_ID']},columns=['SDSS_NAME','RA','DEC','THING_ID'])
qdf.to_csv('/home/rumbaugh/DR12Q_notinDR7_SNRADECTID.csv',index=False)
