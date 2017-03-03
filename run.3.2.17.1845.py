import numpy as np
DB_path='/home/rumbaugh/var_database/Y3A1'
outputdir=DB_path
crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DatabaseID','Y3A1_COADD_OBJECTS_ID','SDSSNAME'),'formats':('|S64','|S64','|S64')},usecols=(0,1,6))

name_prefs=np.array(crdb['DatabaseID'],dtype='|S2')
crdb=crdb[name_prefs=='DR']

#crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
maxdrop=np.zeros(len(crdb))
for DBID,idb in zip(crdb['DatabaseID'],np.arange(len(crdb))):
    cr=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    if np.shape(cr)==(0,): continue
    ggood=np.where((cr['MAG']>15)&(cr['MAG']<30))[0]#&(cr['FLAG']<16))[0]
    if np.shape(cr)==():
        if len(ggood)<1:
            continue
        else:
            mjd,mag,magerr,bands,survey=np.array([cr['MJD']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['BAND']]),np.array([cr['Survey']])
    else:
        cr=cr[ggood]
        mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
    for band in ['g']:
        gSDSS,gDES=np.where(survey[bands==band]=='SDSS')[0],np.where(survey[bands==band]=='DES')[0]
        if ((len(gSDSS)==0)|(len(gDES)==0)): continue
        SDSSmags,DESmags=mag[bands==band][gSDSS],mag[bands==band][gDES]
        SDSSmagerrs,DESmagerrs=magerr[bands==band][gSDSS],magerr[bands==band][gDES]
        gSDSSsrt,gDESsrt=np.argsort(SDSSmags)[::-1],np.argsort(DESmags)
        SDSSmags,DESmags,SDSSmagerrs,DESmagerrs=SDSSmags[gSDSSsrt],DESmags[gDESsrt],SDSSmagerrs[gSDSSsrt],DESmagerrs[gDESsrt]
        magpairs=np.zeros([len(SDSSmags)*len(DESmags),2])
        magpairs[:,1],magpairs[:,0]=np.repeat(SDSSmags,len(DESmags)),np.tile(DESmags,len(SDSSmags))
        magerrpairs=np.zeros([len(SDSSmagerrs)*len(DESmagerrs),2])
        magerrpairs[:,1],magerrpairs[:,0]=np.repeat(SDSSmagerrs,len(DESmagerrs)),np.tile(DESmagerrs,len(SDSSmagerrs))
        magdiffs,differrs=magpairs[:,0]-magpairs[:,1],np.sqrt(np.sum(magerrpairs**2,axis=1))
        diffsigs=magdiffs/differrs
        gsig=np.where(diffsigs>3)[0]
        if len(gsig)>0:maxdrop[idb]=magdiffs[gsig[0]]
outcr=np.zeros((len(crdb),),dtype={'names':('DatabaseID','MaxDrop'),'formats':('|S64','f8')})
outcr['DatabaseID'],outcr['MaxDrop']=crdb['DatabaseID'],maxdrop
np.savetxt('/home/rumbaugh/var_database/Y3A1/faintest_mag_drop_DR7.dat',outcr,fmt='%s %f',header='DatabaseID MagDrop',comments='')
