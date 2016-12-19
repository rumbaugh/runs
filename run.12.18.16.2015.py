import numpy as np

crids=np.loadtxt('/home/rumbaugh/var_database/maxdiffs_sig_DBID.12.18.16.txt',dtype={'names':('DBID','maxdiff'),'formats':('i8','f8')})

good_dbids=crids['DBID'][crids['maxdiff']>2]
DESras,DESdecs=np.zeros(len(good_dbids)),np.zeros(len(good_dbids))
SDSSras,SDSSdecs=np.zeros(len(good_dbids)),np.zeros(len(good_dbids))
for i,DBID in zip(np.arange(len(good_dbids)),good_dbids):
    cr=np.loadtxt('%s/%i/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
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
np.savetxt('/home/rumbaugh/radecname_forDEScutouts.csv',outcr,fmt='%f,%f,DEScutout_DBID_%06i')
np.savetxt('/home/rumbaugh/radec_forDEScutouts.csv',outcr_radec,fmt='%f,%f')

outcr=np.zeros((len(goodsdss,)),dtype={'names':('RA','DEC','Name'),'formats':('f8','f8','i8')})
outcr_radec=np.zeros((len(goodsdss),2))
outcr['RA'],outcr['DEC'],outcr['Name']=SDSSras[goodsdss],SDSSdecs[goodsdss],good_dbids[goodsdss]
outcr_radec[:,0],outcr_radec[:,1]=SDSSras[goodsdss],SDSSdecs[goodsdss]
np.savetxt('/home/rumbaugh/radecname_forSDSScutouts.csv',outcr,fmt='%f,%f,SDSScutout_DBID_%06i')
np.savetxt('/home/rumbaugh/radec_forSDSScutouts.csv',outcr_radec,fmt='%f,%f')
