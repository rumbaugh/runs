import numpy as np

crids=np.loadtxt('/home/rumbaugh/var_database/maxdiffs_DBID.12.1.16.txt',dtype={'names':('DBID','maxdiff'),'formats':('i8','f8')})

good_dbids=crids['DBID'][crids['maxdiff']>2]
outcr=np.zeros((len(good_dbids,)),dtype={'names':('RA','DEC','Name'),'formats':('f8','f8','|S20')})
outcr_radec=np.zeros((len(good_dbids),2))
ras,decs=np.zeros(len(good_dbids)),np.zeros(len(good_dbids))
for i,DBID in zip(np.arange(len(good_dbids)),good_dbids):
    cr=np.loadtxt('%s/%i/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    ras,decs]
