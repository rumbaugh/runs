import numpy as np
execfile('/home/rumbaugh/pythonscripts/SphDist.py')
DB_path='/home/rumbaugh/var_database/Y3A1'
outputdir=DB_path
crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DatabaseID','Y3A1_COADD_OBJECTS_ID','SDSSNAME'),'formats':('|S64','|S64','|S64')},usecols=(0,1,6))

name_prefs=np.array(crdb['DatabaseID'],dtype='|S2')
crdb=crdb[name_prefs=='DR']

#crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
maxdrop=np.zeros(len(crdb))
surveys_max=np.zeros((len(crdb),2),dtype='|S8')
for DBID,idb in zip(crdb['DatabaseID'],np.arange(len(crdb))):
    cr=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    if np.shape(cr)==(0,): continue
    ggood=np.where((cr['MAG']>15)&(cr['MAG']<30)&(cr['Survey']!='POSS'))[0]#&(cr['FLAG']<16))[0]
    SNflag=False
    if np.shape(cr)==():
        if len(ggood)<1:
            continue
        else:
            mjd,mag,magerr,bands,survey=np.array([cr['MJD']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['BAND']]),np.array([cr['Survey']])
    else:
        cr=cr[ggood]
        mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
        gb=np.where(bands=='g')
        if len(cr)>1:
            initdists=SphDist(cr['RA'][0],cr['DEC'][0],cr['RA'][1:],cr['DEC'][1:])
            if np.max(initdists)>0.3: SNflag=True
    if ((len(gb)>0)&(not(SNflag))):
        magpairs=np.zeros((len(gb)**2,2))
        magpairs[:,1],magpairs[:,0]=np.repeat(mag[gb],len(gb)),np.tile(mag[gb],len(gb))
        magerrpairs=np.zeros((len(gb)**2,2))
        magerrpairs[:,1],magerrpairs[:,0]=np.repeat(magerr[gb],len(gb)),np.tile(magerr[gb],len(gb))
        gpairs=np.zeros((len(gb)**2,2))
        gpairs[:,1],gpairs[:,0]=np.repeat(gb,len(gb)),np.tile(gb,len(gb))
        magdiffs,differrs,maxerrs=magpairs[:,0]-magpairs[:,1],np.sqrt(np.sum(magerrpairs**2,axis=1)),np.max(magerrpairs,axis=1)
        diffsigs=magdiffs/differrs
        gsig=np.where(maxerrs<0.15)[0]
        if len(gsig)>0:
            maxdiff=np.max(magdiffs[gsig])
            gmax=np.argsort(magdiffs[gsig])[-1]
            gst,gend=gpairs[:,1][gmax],gpairs[:,0][gmax]
            mjd_st,mjd_end,surv_st,surv_end=mjd[gb[gst]],mjd[gb[gend]],survey[gb[gst]],survey[gb[gend]]
            if mjd_st>mjd_end:
                surv_st,surv_end,maxdiff=surv_end,surv_st,-maxdiff
            maxdrop[idb]=maxdiff
            surveys_max[idb]=np.array([surv_st,surv_end])
outcr=np.zeros((len(crdb),),dtype={'names':('DatabaseID','MaxDrop','SurvST','SurvEnd'),'formats':('|S64','f8','|S8','|S8')})
outcr['DatabaseID'],outcr['MaxDrop'],outcr['SurvST'],outcr['SurvEnd']=crdb['DatabaseID'],maxdrop,surveys_max[:,0],surveys_max[:,1]
np.savetxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.8.17.dat',outcr,fmt='%s %f',header='DatabaseID MaxMagDrop SurveyInit SurveyFinal',comments='')
