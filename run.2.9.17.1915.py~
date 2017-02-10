import numpy as np
DB_path='/home/rumbaugh/var_database/Y3A1'

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DatabaseID','Y3A1_COADD_OBJECTS_ID','SDSS_DR13_thingid','SDR7ID'),'formats':('|S64','|S64','|S64','|S64')})

candidate_flag=np.zeros(len(crdb),dtype='bool')
for DBID,idb in zip(crdb['DatabaseID'],np.arange(len(crdb))):
    cr=np.loadtxt('%s/Y3A1/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    ggood=np.where((cr['MAG']>15)&(cr['MAG']<30))[0]#&(cr['FLAG']<16))[0]
    cr=cr[ggood]
    mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
    for band in ['g','r','i','z']:
        gSDSS,gDES=np.where(survey[bands==band]=='SDSS')[0],np.where(survey[bands==band]=='DES')[0]
        if ((len(gSDSS)==0)|(len(gDES)==0)): continue
        SDSSmags,DESmags=mag[bands==band][gSDSS],mag[bands==band][gDES]
        SDSSmagerrs,DESmagerrs=magerr[bands==band][gSDSS],magerr[bands==band][gDES]
        magpairs=np.zeros([len(SDSSmags)*len(DESmags),2])
        magpairs[:,1],magpairs[:,0]=np.repeat(SDSSmags,len(DESmags)),np.tile(DESmags,len(SDSSmags))
        magerrpairs=np.zeros([len(SDSSmagerrs)*len(DESmagerrs),2])
        magerrpairs[:,1],magerrpairs[:,0]=np.repeat(SDSSmagerrs,len(DESmagerrs)),np.tile(DESmagerrs,len(SDSSmagerrs))
        magdiffs,differrs=magpairs[:,0]-magpairs[:,1],np.sqrt(np.sum(magerrpairs**2,axis=1))
        diffsigs=magdiffs/differrs
        gsig=np.where((magdiffs>2)&(diffsigs>3))[0]
        if len(gsig)>0: candidate_flag[idb]=True
outcr=np.zeros((len(crdb),),dtype={'names':('DatabaseID','CandidateFlag'),'formats':('|S64','i8')})
outcr['DatabaseID'],outcr['CandidateFlag']=crdb['DatabaseID'],candidate_flag
np.savetxt('/home/rumbaugh/var_database/CLQ_candidate_flags.dat',outcr,fmt='%s %i',header='DatabaseID CandidateFlag',comments='')
