import numpy as np
import healpy as hp
import pydl
import pydl.pydlutils

mcdict={'names':('DBID','RA','DEC','SDR5ID','Mi','Micorr','redshift','massBH','Lbol','u','g','r','i','z','Au'),'formats':('i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
delims=(8,11,11,6,8,8,7,6,7,7,7,7,7,7,7)
crmc=np.genfromtxt('/home/rumbaugh/macleodQSOs/DB_QSO_S82.dat',dtype=mcdict,delimiter=delims)

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data

data=data[crdb['SDSSNAME']!='-1']
crdb=crdb[crdb['SDSSNAME']!='-1']

gdb,gmac,dists=pydl.pydutils.spheregroup.spherematch(crdb['
