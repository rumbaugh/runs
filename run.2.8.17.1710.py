import numpy as np


crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DatabaseID','Y3A1_COADD_OBJECTS_ID','SDSS_DR13_thingid','SDR7ID'),'formats':('|S64','|S64','|S64','|S64')})

crf=np.loadtxt('/home/rumbaugh/var_database/CLQ_candidate_flags.dat',dtype={'names':('DBID','Flag'),'formats':('|S64','i8')},skiprows=1)

good_dbids=crf['DBID'][crf['Flag']==1]
DESras,DESdecs=np.zeros(len(good_dbids)),np.zeros(len(good_dbids))
SDSSras,SDSSdecs=np.zeros(len(good_dbids)),np.zeros(len(good_dbids))
for i,DBID in zip(np.arange(len(good_dbids)),good_dbids):
    cr=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    gdes,gsdss=np.where(cr['Survey']=='DES')[0],np.where(cr['Survey']=='SDSS')[0]
    if len(gdes)>0:
        DESras[i],DESdecs[i]=np.mean(np.array([cr['RA'][gdes]])),np.mean(np.array([cr['DEC'][gdes]]))
    if len(gsdss)>0:
        SDSSras[i],SDSSdecs[i]=np.mean(np.array([cr['RA'][gsdss]])),np.mean(np.array([cr['DEC'][gsdss]]))


gooddes,goodsdss=np.where((DESras!=0)&(DESdecs!=0))[0],np.where((SDSSras!=0)&(SDSSdecs!=0))[0]

outcr=np.zeros((len(gooddes,)),dtype={'names':('RA','DEC','Name'),'formats':('f8','f8','i8')})
outcr_radec=np.zeros((len(gooddes),2))
outcr['RA'],outcr['DEC'],outcr['Name']=DESras[gooddes],DESdecs[gooddes],good_dbids[gooddes]
outcr_radec[:,0],outcr_radec[:,1]=DESras[gooddes],DESdecs[gooddes]
np.savetxt('/home/rumbaugh/radecname_forDEScutouts.2.8.17.csv',outcr,fmt='%f,%f,%s_DEScutout')
np.savetxt('/home/rumbaugh/radec_forDEScutouts.2.8.17.csv',outcr_radec,fmt='%f,%f')

outcr=np.zeros((len(goodsdss,)),dtype={'names':('RA','DEC','Name'),'formats':('f8','f8','i8')})
outcr_radec=np.zeros((len(goodsdss),2))
outcr['RA'],outcr['DEC'],outcr['Name']=SDSSras[goodsdss],SDSSdecs[goodsdss],good_dbids[goodsdss]
outcr_radec[:,0],outcr_radec[:,1]=SDSSras[goodsdss],SDSSdecs[goodsdss]
np.savetxt('/home/rumbaugh/radecname_forSDSScutouts.2.8.17.csv',outcr,fmt='%f,%f,%s_SDSScutout')
np.savetxt('/home/rumbaugh/radec_forSDSScutouts.2.8.17.csv',outcr_radec,fmt='%f,%f')
