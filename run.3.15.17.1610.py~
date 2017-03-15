import numpy as np
execfile('/home/rumbaugh/pythonscripts/SphDist.py')
DB_path='/home/rumbaugh/var_database/Y3A1'
DBdir='/home/rumbaugh/var_database/Y3A1'
outputdir=DB_path
#crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DatabaseID','Y3A1_COADD_OBJECTS_ID','SDSSNAME'),'formats':('|S64','|S64','|S64')},usecols=(0,1,6))

#name_prefs=np.array(crdb['DatabaseID'],dtype='|S2')
#crdb=crdb[name_prefs=='DR']

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
crdb=crdb[crdb['SDSSNAME']!='-1']


hdu=py.open('%s/masterfile.fits'%DBdir)
data=hdu[1].data

maxdrop=np.zeros(len(crdb))
s82flag=np.zeros(len(crdb))
surveys_max,mjd_max,g_max,sig_max=np.zeros((len(crdb),2),dtype='|S8'),np.zeros((len(crdb),2),dtype='f8'),np.zeros((len(crdb),2),dtype='f8'),np.zeros((len(crdb),2),dtype='f8')
redshifts=np.zeros(len(crdb))
ra,dec=np.zeros(len(crdb)),np.zeros(len(crdb))
for DBID,idb in zip(crdb['DatabaseID'],np.arange(len(crdb))):
    cr=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    if np.shape(cr)==(0,): continue
    ggood=np.where((cr['MAG']>15)&(cr['MAG']<30)&(cr['Survey']!='POSS'))[0]#&(cr['FLAG']<16))[0]
    SNflag=False
    if np.shape(cr)==():
        if '82' in np.array([cr['TAG']]): s82flag[idb]=1
        if len(ggood)<1:
            continue
        else:
            mjd,mag,magerr,bands,survey=np.array([cr['MJD']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['BAND']]),np.array([cr['Survey']])
            ra[idb],dec[idb]=cr['RA'],cr['DEC']
    else:
        ra[idb],dec[idb]=cr['RA'][0],cr['DEC'][0]
        if '82' in cr['TAG']: s82flag[idb]=1
        cr=cr[ggood]
        mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
        gb=np.where(bands=='g')[0]
        if len(cr)>1:
            initdists=SphDist(cr['RA'][0],cr['DEC'][0],cr['RA'][1:],cr['DEC'][1:])
            if np.max(initdists)>0.3: SNflag=True
    if ((len(gb)>0)&(not(SNflag))):
        magpairs=np.zeros((len(gb)**2,2))
        magpairs[:,1],magpairs[:,0]=np.repeat(mag[gb],len(gb)),np.tile(mag[gb],len(gb))
        magerrpairs=np.zeros((len(gb)**2,2))
        magerrpairs[:,1],magerrpairs[:,0]=np.repeat(magerr[gb],len(gb)),np.tile(magerr[gb],len(gb))
        gpairs=np.zeros((len(gb)**2,2),dtype='i8')
        gpairs[:,1],gpairs[:,0]=np.repeat(gb,len(gb)),np.tile(gb,len(gb))
        magdiffs,differrs,maxerrs=magpairs[:,0]-magpairs[:,1],np.sqrt(np.sum(magerrpairs**2,axis=1)),np.max(magerrpairs,axis=1)
        diffsigs=magdiffs/differrs
        gsig=np.where(maxerrs<0.15)[0]
        if len(gsig)>0:
            maxdiff=np.max(magdiffs[gsig])
            gmax=np.argsort(magdiffs[gsig])[-1]
            gst,gend=gpairs[:,1][gsig[gmax]],gpairs[:,0][gsig[gmax]]
            mjd_st,mjd_end,surv_st,surv_end=mjd[gst],mjd[gend],survey[gst],survey[gend]
            mag_st,mag_end,sig_st,sig_end=mag[gst],mag[gend],magerr[gst],magerr[gend]
            mjd_max[idb][0],mjd_max[idb][1]=mjd_st,mjd_end
            sig_max[idb][0],sig_max[idb][1]=sig_st,sig_end
            g_max[idb][0],g_max[idb][1]=mag_st,mag_end
            if mjd_st>mjd_end:
                surv_st,surv_end,maxdiff=surv_end,surv_st,-maxdiff
            maxdrop[idb]=maxdiff
            surveys_max[idb]=np.array([surv_st,surv_end])
            gm=np.where(data['DatabaseID']==DBID)[0]
            if len(gm)>0:
                gm=gm[0]
                redshifts[idb]=data['Redshift'][gm]
gsig=np.where(np.abs(maxdrop)>1)[0]
crdb,maxdrop,surveys_max,s82flag,redshifts,mjd_max,g_max,sig_max,ra,dec=crdb[gsig],maxdrop[gsig],surveys_max[gsig],s82flag[gsig],redshifts[gsig],mjd_max[gsig],g_max[gsig],sig_max[gsig],ra[gsig],dec[gsig]
gswap=np.where(g_max[:,1]>g_max[:,0])[0]
g_max[:,0][gswap],g_max[:,1][gswap],sig_max[:,0][gswap],sig_max[:,1][gswap],mjd_max[:,0][gswap],mjd_max[:,1][gswap]=g_max[:,1][gswap],g_max[:,0][gswap],sig_max[:,1][gswap],sig_max[:,0][gswap],mjd_max[:,1][gswap],mjd_max[:,0][gswap]
#outcr=np.zeros((len(crdb),),dtype={'names':('DatabaseID','RA','DEC','Redshift','MJD_lo','g_lo','sig_lo','MJD_hi','g_hi','sig_hi'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
outcr=np.zeros((len(crdb),),dtype={'names':('RA','DEC','Redshift','MJD_lo','g_lo','sig_lo','MJD_hi','g_hi','sig_hi'),'formats':('f8','f8','f8','f8','f8','f8','f8','f8','f8')})
outcr['RA'],outcr['DEC'],outcr['Redshift'],outcr['MJD_lo'],outcr['g_lo'],outcr['sig_lo'],outcr['MJD_hi'],outcr['g_hi'],outcr['sig_hi']=ra,dec,redshifts,mjd_max[:,0],g_max[:,0],sig_max[:,0],mjd_max[:,1],g_max[:,1],sig_max[:,1]
np.savetxt('/home/rumbaugh/var_database/Y3A1/DR7_CLQ_candidates.3.14.17.tab',outcr,header='RA DEC Redshift MJD_lo g_lo sig_lo MJD_hi g_hi sig_hi')
