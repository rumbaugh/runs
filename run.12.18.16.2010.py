import numpy as np
outputdir='/home/rumbaugh/var_database'
DB_path='/home/rumbaugh/var_database'

crids=np.loadtxt('/home/rumbaugh/var_database/maxdiffs_sig_DBID.12.18.16.txt',dtype={'names':('DBID','maxdiff'),'formats':('i8','f8')})

good_dbids=crids['DBID'][crids['maxdiff']>2]

maxdists=np.zeros(len(good_dbids))
for DBID,i in zip(good_dbids,np.arange(len(good_dbids))):
    cr=np.loadtxt('%s/%i/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    maxdists[i]=np.sqrt((np.max(cr['RA'])-np.min(cr['RA']))**2+(np.max(cr['DEC'])-np.min(cr['DEC']))**2)
    
