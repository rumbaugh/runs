import numpy as np
import pyfits as py
hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data

outcr=np.zeros((len(bhdata),),dtype={'names':('SDSSNAME','RA','DEC'),'formats':('|S36','f8','f8')})
outcr['SDSSNAME'],outcr['RA'],outcr['DEC']=bhdata['SDSS_NAME'],bhdata['RA'],bhdata['DEC']
np.savetxt('/home/rumbaugh/DR7_SDSSNAME_RADEC.csv',outcr,fmt='%s, %f, %f',header='SDSSNAME, RA, DEC',comments='')
