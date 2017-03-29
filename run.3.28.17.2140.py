import numpy as np
import pyfits as py
crm=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)
crm2=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.28.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data

diffdrops=crm2['drop']-crm['drop']
g=np.where((diffdrops!=0)&(np.abs(crm2['drop']-crm['drop'])>1))[0]
gmf=np.zeros(len(g),dtype='i8')
for i in range(0,len(g)):
    gmf[i]=np.where(data['DatabaseID']==crdb['DatabaseID'][g[i]])[0][0]

outcr=np.zeros((len(g),),dtype={'names':('DatabaseID','RA','Dec','COADD_OBJECT_ID','MaxMagDrop','redshift'),'formats':('|S24','f8','f8','i8','f8','f8')})

outcr['DatabaseID'],outcr['RA'],outcr['Dec'],outcr['COADD_OBJECT_ID'],outcr['MaxMagDrop'],outcr['redshift']=crm2['DBID'][g],data['RA_DES'][gmf],data['RA_DES'][gmf],crdb['CID'][g],crm2['drop'][g],data['Redshift'][gmf]

np.savetxt('/home/rumbaugh/var_database/Y3A1/DR7_SN_EVQ_list.tab',outcr,fmt='%24s %f %f %i %f %f',header='DatabaseID RA Dec COADD_OBJECT_ID MaxMagDrop redshift',comments='')
