import numpy as np
import pyfits as py
import pydl.pydlutils.spheregroup

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
data=hdubh[1].data

outdf=pd.DataFrame({'RA': data['RA'],'DEC':data['DEC']})
outdf.to_csv('/home/rumbaugh/DR7_radec.csv',index=False)
hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
