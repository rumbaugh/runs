import numpy as np
import pyfits as py

crm=np.loadtxt('/home/rumbaugh/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)


crdb=np.loadtxt('/home/rumbaugh/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

crm=crm[crdb['SDSSNAME']!='-1']
np.savetxt('/home/rumbaugh/DR7_full_magdiffs.3.23.17.dat',crm,fmt='%24s %6.3f %4s %4s %i %7.1f',header='DatabaseID MaxMagDrop SurveyInit SurveyFinal Stripe82 Baseline',comments='')
