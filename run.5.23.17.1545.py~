import numpy as np
import pyfits as py

hdu=py.open('/home/rumbaugh/var_database/Y3A1/old_masterfile.fits')
data=hdu[1].data

cids,inds=np.unique(data['Y3A1_CoaddObjectsID'],True)
cids,inds=cids[cids>0],inds[cids>0]
outcr=np.zeros((len(cids),),dtype={'names':('inds','cids'),'formats':('i8','i8')})
outcr['inds'],outcr['cids']=inds,cids

np.savetxt('/home/rumbaugh/all_coadd_object_ids.tab',outcr,fmt='%i %i',header='IND CID',comments='')
