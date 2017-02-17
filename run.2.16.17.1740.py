import numpy as np


crsp=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EpochG','EpochR','EpochI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_r_SDSS','g_SDSS','g_ERR','r_SDSS','r_ERR','i_SDSS','i_ERR'),'formats':('f8','f8','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S12','f8','f8','|S12','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8')})

crmi=np.loadtxt('/home/rumbaugh/var_database/Y3A1/match_index.dat',dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSSNAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('i8','i8','|S32','f8','f8','i8','i8','|S32')},skiprows=1)

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SP_rownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})
ggood=np.where(crmi['COADD_OBJECTS_ID']>0)[0]
crmi=crmi[ggood]

sdr7ids=np.array(crsp['SDR7ID'][crmi['SP_ROWNUM']],dtype='|S24')
sdr7ids[crmi['SP_ROWNUM']<0]='None'
thingids=np.ones(len(crmi),dtype='i8')*-1
DBIDs,primDBID=np.zeros(len(crmi),dtype='|S128'),np.zeros(len(crmi),dtype='|S32')
for comparr,srcarr,prefix in zip([crmi['MQ_ROWNUM'],crmi['SP_ROWNUM'],crmi['SDSSNAME']],[crmi['MQ_ROWNUM'],sdr7ids,crmi['SDSSNAME']],['MQ','SDSSPOSS','DR7BH']):
    for i in range(0,len(DBIDs)):
        if str(comparr[i])!='-1':
            if primDBID[i]=='': 
                primDBID[i]='%s%s'%(prefix,str(srcarr[i]))
                DBIDs[i]='%s%s'%(prefix,str(srcarr[i]))
            else:
                DBIDs[i]='%s;%s%s'%(DBIDs[i],prefix,str(srcarr[i]))
            gdb=np.where(crdb['DBID']==primDBID[i])[0][0]
            thingids[i]=crdb['thingid'][gdb]
outcr=np.zeros((len(crmi),),dtype={'names':('DBID','DBIDS','MQ_ROWNUM','SP_ROWNUM','SDR7ID','THINGID','SDSSNAME','COADD_OBJECTS_ID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S32','|S32','i8','|S32')})
outcr['DBID'],outcr['DBIDS'],outcr['MQ_ROWNUM'],outcr['SP_ROWNUM'],outcr['SDR7ID'],outcr['THINGID'],outcr['SDSSNAME'],outcr['COADD_OBJECTS_ID'],outcr['TILENAME']=primDBID,DBIDs,crmi['MQ_ROWNUM'],crmi['SP_ROWNUM'],sdr7ids,thingids,crmi['SDSSNAME'],crmi['COADD_OBJECTS_ID'],crmi['TILENAME']
np.savetxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',outcr,header=('PrimaryDatabaseID AllDatabaseIDs MQ_ROWNUM SP_ROWNUM SDR7ID THINGID SDSSNAME COADD_OBJECTS_ID TILENAME'),fmt='%32s %128s %i %i %s %i %s %i %s',comments='') 
                  
