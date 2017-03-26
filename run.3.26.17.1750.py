import numpy as np
import pyfits as py
execfile('/home/rumbaugh/pythonscripts/SphDist.py')
DB_path='/home/rumbaugh/var_database/Y3A1'
DBdir='/home/rumbaugh/var_database/Y3A1'
outputdir=DB_path
#crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DatabaseID','Y3A1_COADD_OBJECTS_ID','SDSSNAME'),'formats':('|S64','|S64','|S64')},usecols=(0,1,6))
crmcm=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_Macleod_S82_match.dat',dtype={'names':('DBID','MCID'),'formats':('|S24','i8')},skiprows=1)

hdu=py.open('%s/masterfile.fits'%DBdir)
data=hdu[1].data


crmcm=crmcm[crmcm['MCID']>-1]

#name_prefs=np.array(crdb['DatabaseID'],dtype='|S2')
#crdb=crdb[name_prefs=='DR']

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
maxdrop=np.zeros(len(crdb))
s82flag=np.zeros(len(crdb))
surveys_max,mjd_max,g_max,sig_max=np.zeros((len(crdb),2),dtype='|S8'),np.zeros((len(crdb),2),dtype='f8'),np.zeros((len(crdb),2),dtype='f8'),np.zeros((len(crdb),2),dtype='f8')
redshifts=np.zeros(len(crdb))
ra,dec=np.zeros(len(crdb)),np.zeros(len(crdb))
for DBID,idb in zip(crdb['DatabaseID'],np.arange(len(crdb))):
    cr=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    if np.shape(cr)==(0,): continue
    ggood=np.where((cr['MAG']>15)&(cr['MAG']<30)&(cr['Survey']!='POSS'))[0]#&(cr['FLAG']<16))[0]
    gmc=np.where(DBID==crmcm['DBID'])[0]
    if len(gmc)>0:
        crmac=np.loadtxt('%s/%s/Macleod_LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('i8','f8','f8','f8','|S4','f8','f8','i8')})
        crmac=crmac[(crmac['MAG']>0)&(crmac['MAG']<30)&(crmac['MAGERR']<5)]
        gb0,gbmac=np.where((cr['BAND']=='g')&(cr['MJD']>np.min(crmac['MJD'])-30)&(cr['MJD']<np.max(crmac['MJD'])+30))[0],np.where(crmac['BAND']=='g')[0]
        if ((len(gb0)>0)&(len(gbmac)>0)):
            mjd,mjdmac=cr['MJD'][gb0],crmac['MJD'][gbmac]
            mjddists=np.abs(mjdmac.reshape((len(mjdmac),1))-mjd.reshape((1,len(mjd)))*np.ones((len(mjdmac),1)))
            mindists=np.min(mjddists,axis=1)
            gmac2=np.where(mindists>5)[0]
        else:
            gmac2=np.arange(len(gbmac))
    SNflag=False
    if np.shape(cr)==():
        if '82' in np.array([cr['TAG']]): s82flag[idb]=1
        if len(ggood)<1:
            gb=np.zeros(0,dtype='i8')
        else:
            mjd,mag,magerr,bands,survey=np.array([cr['MJD']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['BAND']]),np.array([cr['Survey']])
            gb=np.where(bands=='g')[0]
    else:
        if '82' in cr['TAG']: s82flag[idb]=1
        cr=cr[ggood]
        mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
        if len(gmc)>0:
            surveymac=np.zeros(len(gmac2),dtype='|S8')
            surveymac[:]='SDSS'
            mjd,mag,magerr,bands,survey=np.append(mjd,crmac['MJD'][gbmac[gmac2]]),np.append(mag,crmac['MAG'][gbmac[gmac2]]),np.append(magerr,crmac['MAGERR'][gbmac[gmac2]]),np.append(bands,crmac['BAND'][gbmac[gmac2]]),np.append(survey,surveymac)
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
            gst,gend=gpairs[:,1][gmax],gpairs[:,0][gmax]
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
gswap=np.where(g_max[:,1]>g_max[:,0])[0]
g_max[:,0][gswap],g_max[:,1][gswap],sig_max[:,0][gswap],sig_max[:,1][gswap],mjd_max[:,0][gswap],mjd_max[:,1][gswap]=g_max[:,1][gswap],g_max[:,0][gswap],sig_max[:,1][gswap],sig_max[:,0][gswap],mjd_max[:,1][gswap],mjd_max[:,0][gswap]
#outcr=np.zeros((len(crdb),),dtype={'names':('DatabaseID','MaxDrop','SurvST','SurvEnd','S82'),'formats':('|S64','f8','|S8','|S8','i8')})
#outcr['DatabaseID'],outcr['MaxDrop'],outcr['SurvST'],outcr['SurvEnd'],outcr['S82']=crdb['DatabaseID'],maxdrop,surveys_max[:,0],surveys_max[:,1],s82flag

outcr=np.zeros((len(crdb),),dtype={'names':('RA','DEC','Redshift','MJD_lo','g_lo','sig_lo','MJD_hi','g_hi','sig_hi'),'formats':('f8','f8','f8','f8','f8','f8','f8','f8','f8')})
outcr['RA'],outcr['DEC'],outcr['Redshift'],outcr['MJD_lo'],outcr['g_lo'],outcr['sig_lo'],outcr['MJD_hi'],outcr['g_hi'],outcr['sig_hi']=ra,dec,redshifts,mjd_max[:,0],g_max[:,0],sig_max[:,0],mjd_max[:,1],g_max[:,1],sig_max[:,1]
np.savetxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs.3.16.17.tab',outcr,header='RA DEC Redshift MJD_lo g_lo sig_lo MJD_hi g_hi sig_hi',fmt='%f %f %f %f %f %f %f %f %f')

#outcr['SurvST'][outcr['SurvST']=='']='None'
#outcr['SurvEnd'][outcr['SurvEnd']=='']='None'
#np.savetxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.22.17.dat',outcr,fmt='%24s %6.3f %4s %4s %i',header='DatabaseID MaxMagDrop SurveyInit SurveyFinal Stripe82',comments='')
