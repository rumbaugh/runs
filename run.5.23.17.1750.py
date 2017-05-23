import numpy as np
import pyfits as py

hdu=py.open('/home/rumbaugh/var_database/Y3A1/old_masterfile.fits')
data=hdu[1].data

data=data[(data['SDSSNAME']!='-1')|(data['SP_ROWNUM']>-1)]

tids,inds=np.unique(data['DR13_thingid'],True)
tids,inds=tids[tids>0],inds[tids>0]
outcr=np.zeros((len(tids),),dtype={'names':('inds','tids'),'formats':('i8','i8')})
outcr['inds'],outcr['tids']=inds,tids

np.savetxt('/home/rumbaugh/DR13_thingids.noMQ.tab',outcr,fmt='%i %i',header='IND THINGID',comments='')
