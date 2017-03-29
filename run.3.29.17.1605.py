import numpy as np
import pyfits as py


crm=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)
crm2=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.28.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
crm=crm[crdb['SDSSNAME']!='-1']
crm2=crm2[crdb['SDSSNAME']!='-1']
crdb=crdb[crdb['SDSSNAME']!='-1']

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data

cr=np.loadtxt('/home/rumbaugh/gemini_target',dtype={'names':('DR7ID','SDSSNAME','RA','DEC','z','FIRST','lastgmjd','gmag','lastimjd','imag','S82ID','DBID'),'formats':('i8','|S24','f8','f8','f8','i8','i8','f8','i8','f8','i8','|S24')})

outcr=np.zeros((len(cr),),dtype={'names':('ra','dec','SDSSNAME'),'formats':('f8','f8','|S24')})
outcr['ra'],outcr['dec'],outcr['SDSSNAME']=cr['ra'],cr['dec'],cr['SDSSNAME']
np.savetxt('/home/rumbaugh/radecname_forcutouts.gemini.tab',outcr,fmt='%f,%f,%s')

outcr=np.zeros((len(cr),),dtype={'names':('ra','dec'),'formats':('f8','f8')})
outcr['ra'],outcr['dec']=cr['ra'],cr['dec']
np.savetxt('/home/rumbaugh/radec_forcutouts.gemini.tab',outcr,fmt='%f,%f')
