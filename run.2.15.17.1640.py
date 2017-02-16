import numpy as np
import os
DB_path='/home/rumbaugh/var_database/Y3A1'
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
POSSbands=np.array(['g','r','i'])

double_count_indexes=np.zeros(0,dtype='|S30')

crsp=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EpochG','EpochR','EpochI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_r_SDSS','g_SDSS','g_ERR','r_SDSS','r_ERR','i_SDSS','i_ERR'),'formats':('f8','f8','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S12','f8','f8','|S12','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8')})
crse=np.loadtxt('SDSSPOSS_lightcurve_entries.tab',dtype={'names':('cid','SP_ROWNUM','ra_y1a1','dec_y1a1','sdr7id','mjd_SDSS','EPOCHG','EPOCHR','EPOCHI','ra','dec','G_POSS','R_POSS','I_POSS','G_POSS_err','R_POSS_err','I_POSS_err','G_SDSS','R_SDSS','I_SDSS','G_SDSS_err','R_SDSS_err','I_SDSS_err'),'formats':('i8','i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
cryse=np.loadtxt('SDSSPOSS_lightcurve_entries_y3a1.tab',skiprows=1,dtype={'names':('SPid','cid','mjd','ra','dec','imageid','ofile','OBJECT_ID','mag','magerr','mag_auto','mag_auto_err','band','flags','flags_detmodel','flags_model','flags_weight'),'formats':('i8','i8','f8','f8','f8','i8','|S64','i8','f8','f8','f8','f8','|S12','i8','i8','i8','i8')})

crybh=np.loadtxt('dr7_bh_lightcurve_entries_y3a1.tab',dtype={'names':('SDSSNAME','cid','mjd','ra','dec','imageid','ofilename','OBJECT_ID','mag','magerr','mag_auto','mag_auto_err','band','flags','flags_detmodel','flags_model','flags_weight'),'formats':('|S24','i8','f8','f8','f8','i8','|S64','i8','f8','f8','f8','f8','|S12','i8','i8','i8','i8')},skiprows=1)
crbh=np.loadtxt('dr7_bh_lightcurve_entries_SDSS.y3a1.tab',skiprows=1,dtype={'names':('numrow','cid','SDSSNAME','ray3a1','decy3a1','objid','thingid','mjd_g','ra','dec','run','rerun','stripe','psfmag_u','psfmag_g','psfmag_r','psfmag_i','psfmag_z','psfmagerr_u','psfmagerr_g','psfmagerr_r','psfmagerr_i','psfmagerr_z'),'formats':('i8','i8','|S24','f8','f8','i8','i8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

crmqy=np.loadtxt('milliquas_lightcurve_entries_y3a1.tab',dtype={'names':('MQrownum','cid','mjd','ra','dec','imageid','ofilename','OBJECT_ID','mag','magerr','mag_auto','mag_auto_err','band','flags','flags_detmodel','flags_model','flags_weight'),'formats':('i8','i8','f8','f8','f8','i8','|S64','i8','f8','f8','f8','f8','|S12','i8','i8','i8','i8')},skiprows=1)
crmqs=np.loadtxt('milliquas_lightcurve_entries_SDSS.y3a1.tab',skiprows=1,dtype={'names':('numrow','cid','MQ','ray3a1','decy3a1','objid','thingid','mjd_g','ra','dec','run','rerun','stripe','psfmag_u','psfmag_g','psfmag_r','psfmag_i','psfmag_z','psfmagerr_u','psfmagerr_g','psfmagerr_r','psfmagerr_i','psfmagerr_z'),'formats':('i8','i8','i8','f8','f8','i8','i8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crmqSN=np.loadtxt('milliquas_lightcurve_entries_y3a1_SN.tab',dtype={'names':('MQrownum','cid','mjd','ra','dec','mag','magerr','mag_auto','mag_auto_err','band','flags',),'formats':('i8','i8','f8','f8','f8','f8','f8','f8','f8','|S12','i8')},skiprows=1)

crmi=np.loadtxt('/home/rumbaugh/var_database/Y3A1/match_index.dat',dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('i8','i8','|S32','f8','f8','i8','i8','|S32')},skiprows=1)
gcrmi_match=np.where(crmi['COADD_OBJECTS_ID']>0)[0]
crmim=crmi[gcrmi_match]

dbi_out=np.zeros((0,5),dtype='object')

for cid,MQrn,SPrn,SDSSNAME,imi in zip(crmim['COADD_OBJECTS_ID'],crmim['MQ_ROWNUM'],crmim['SP_ROWNUM'],crmim['SDSS_NAME'],np.arange(len(crmim))):
    outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    Y3A1outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    DR13outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    cur_dr7,tid='None',0
    curDBIDs=np.zeros(0,dtype='|S64')
    if MQrn!=-1:
        gMQy=np.where(crmqy['cid']==cid)[0]
        gMQs=np.where(crmqs['cid']==cid)[0]
        gMQSN=np.where(crmqSN['cid']==cid)[0]
        curMQ=MQrn
        curDBIDs=np.append(curDBIDs,'MQ%i'%curMQ)
        DBID=curDBIDs[0]
        des_outcr=np.zeros((len(gMQy),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
        if len(gMQy)>0:
            mjd,mag,magerr,magauto,magautoerr,cIDs,bands,yra,ydec,flags=crmqy['mjd'][gMQy],crmqy['mag'][gMQy],crmqy['magerr'][gMQy],crmqy['mag_auto'][gMQy],crmqy['mag_auto_err'][gMQy],crmqy['cid'][gMQy],crmqy['band'][gMQy],crmqy['ra'][gMQy],crmqy['dec'][gMQy],crmqy['flags'][gMQy]
            db_outcr=np.zeros((len(gMQy),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
            db_outcr['DatabaseID'],db_outcr['Survey'],db_outcr['SurveyCoaddID'],db_outcr['SurveyObjectID'],db_outcr['RA'],db_outcr['DEC'],db_outcr['MJD'],db_outcr['TAG'],db_outcr['BAND'],db_outcr['MAGTYPE'],db_outcr['MAG'],db_outcr['MAGERR'],db_outcr['FLAG']=DBID,'DES',cid,np.array(crmqy['OBJECT_ID'])[gMQy],yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
            outcr=np.append(outcr,db_outcr)
            des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,crmqy['imageid'][gMQy],crmqy['OBJECT_ID'][gMQy],cid,yra,ydec,magauto,magautoerr,mag,magerr,bands
        if len(gMQSN)>0:
            mjd,mag,magerr,magauto,magautoerr,cIDs,bands,yra,ydec,flags=crmqSN['mjd'][gMQSN],crmqSN['mag'][gMQSN],crmqSN['magerr'][gMQSN],crmqSN['mag_auto'][gMQSN],crmqSN['mag_auto_err'][gMQSN],crmqSN['cid'][gMQSN],crmqSN['band'][gMQSN],crmqSN['ra'][gMQSN],crmqSN['dec'][gMQSN],crmqSN['flags'][gMQSN]
            db_outcr=np.zeros((len(gMQSN),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
            db_outcr['DatabaseID'],db_outcr['Survey'],db_outcr['SurveyCoaddID'],db_outcr['SurveyObjectID'],db_outcr['RA'],db_outcr['DEC'],db_outcr['MJD'],db_outcr['TAG'],db_outcr['BAND'],db_outcr['MAGTYPE'],db_outcr['MAG'],db_outcr['MAGERR'],db_outcr['FLAG']=DBID,'DES',cid,0,yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
            outcr=np.append(outcr,db_outcr)
            if len(des_outcr)==0: des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,crmqSN['imageid'][gMQSN],crmqSN['OBJECT_ID'][gMQSN],cid,yra,ydec,magauto,magautoerr,mag,magerr,bands
        SDSSmjd,SDSScid=crmqs['mjd_g'][gMQs],crmqs['cid'][gMQs]
        SDSSra,SDSSdec=crmqs['ra'][gMQs],crmqs['dec'][gMQs]
        SDSStid,SDSSobjid,stripe=crmqs['thingid'][gMQs],crmqs['objid'][gMQs],crmqs['stripe'][gMQs]
        tid=SDSStid[0]
        SDSSmagdict,SDSSmagerrdict={b: crmqs['psfmag_%s'%(b.lower())][gMQs] for b in SDSSbands},{b: crmqs['psfmagerr_%s'%(b.lower())][gMQs] for b in SDSSbands}
        SDSS_outcr=np.zeros((5*len(gMQs),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
        for b,ib in zip(SDSSbands,np.arange(len(SDSSbands))):
            SDSS_outcr['DatabaseID'][ib::5],SDSS_outcr['Survey'][ib::5],SDSS_outcr['SurveyCoaddID'][ib::5],SDSS_outcr['SurveyObjectID'][ib::5],SDSS_outcr['RA'][ib::5],SDSS_outcr['DEC'][ib::5],SDSS_outcr['MJD'][ib::5],SDSS_outcr['TAG'][ib::5],SDSS_outcr['BAND'][ib::5],SDSS_outcr['MAGTYPE'][ib::5],SDSS_outcr['MAG'][ib::5],SDSS_outcr['MAGERR'][ib::5],SDSS_outcr['FLAG'][ib::5]=DBID,'SDSS',SDSStid,SDSSobjid,SDSSra,SDSSdec,SDSSmjd,stripe,b,'PSF',SDSSmagdict[b],SDSSmagerrdict[b],0
        outcr=np.append(outcr,SDSS_outcr)
    else:
        gMQy,gMQs,gMQSN=np.zeros(0),np.zeros(0),np.zeros(0)
    if SPrn!=-1:
        gSPy=np.where(cryse['cid']==cid)[0]
        gSPs=np.where(crse['cid']==cid)[0]
        cur_dr7=crse['sdr7id'][gSPs[0 ]]
        curDBIDs=np.append(curDBIDs,'SDSSPOSS%i'%cur_dr7)
        DBID=curDBIDs[0]
        SDSSmjd,SDSScid=crse['mjd_SDSS'][gSPs],crse['cid'][gSPs]
        SDSSra,SDSSdec=crse['ra'][gSPs],crse['dec'][gSPs]
        SDSSmagdict,SDSSmagerrdict={b: crse['%s_SDSS'%(b.upper())][gSPs] for b in POSSbands},{b: crse['%s_SDSS_err'%(b.upper())][gSPs] for b in POSSbands}
        POSScid=crse['cid'][gSPs]
        POSSra,POSSdec=crse['ra'][gSPs],crse['dec'][gSPs]
        POSSmagdict,POSSmagerrdict,POSSmjddict={b: crse['%s_POSS'%(b.upper())][gSPs] for b in POSSbands},{b: crse['%s_POSS_err'%(b.upper())][gSPs] for b in POSSbands},{b: 50448.+365.25*(crse['EPOCH%s'%(b.upper())][gSPs]-1997) for b in POSSbands}
        p_outcr=np.zeros((3,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
        SDSS_outcr=np.zeros((3,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
        for b,ib in zip(POSSbands,np.arange(len(POSSbands))):
            p_outcr['DatabaseID'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['Survey'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['SurveyCoaddID'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['SurveyObjectID'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['RA'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['DEC'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['MJD'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['TAG'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['BAND'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['MAGTYPE'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['MAG'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['MAGERR'][len(gSPs)*ib:len(gSPs)*(ib+1)],p_outcr['FLAG'][len(gSPs)*ib:len(gSPs)*(ib+1)]=DBID,'POSS','0','0',POSSra,POSSdec,POSSmjddict[b],'None',b,'PSF',POSSmagdict[b],POSSmagerrdict[b],0
            SDSS_outcr['DatabaseID'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['Survey'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['SurveyCoaddID'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['SurveyObjectID'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['RA'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['DEC'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['MJD'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['TAG'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['BAND'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['MAGTYPE'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['MAG'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['MAGERR'][len(gSPs)*ib:len(gSPs)*(ib+1)],SDSS_outcr['FLAG'][len(gSPs)*ib:len(gSPs)*(ib+1)]=DBID,'SDSS','DR7%i'%cur_dr7,'0',SDSSra,SDSSdec,SDSSmjd,'None',b,'PSF',SDSSmagdict[b],SDSSmagerrdict[b],0
        outcr=np.append(p_outcr,SDSS_outcr)
        if len(Y3A1outcr)==0:
            mjd,mag,magerr,magauto,magautoerr,cIDs,bands,yra,ydec,flags=cryse['mjd'][gSPy],cryse['mag'][gSPy],cryse['magerr'][gSPy],cryse['mag_auto'][gSPy],cryse['mag_auto_err'][gSPy],cryse['cid'][gSPy],cryse['band'][gSPy],cryse['ra'][gSPy],cryse['dec'][gSPy],cryse['flags'][gSPy]
            db_outcr=np.zeros((len(gSPy),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
            db_outcr['DatabaseID'],db_outcr['Survey'],db_outcr['SurveyCoaddID'],db_outcr['SurveyObjectID'],db_outcr['RA'],db_outcr['DEC'],db_outcr['MJD'],db_outcr['TAG'],db_outcr['BAND'],db_outcr['MAGTYPE'],db_outcr['MAG'],db_outcr['MAGERR'],db_outcr['FLAG']=DBID,'DES',cid,np.array(cryse['OBJECT_ID'])[gSPy],yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
            outcr=np.append(outcr,db_outcr)
            des_outcr=np.zeros((len(gSPy),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
            des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,cryse['imageid'][gSPy],cryse['OBJECT_ID'][gSPy],cid,yra,ydec,magauto,magautoerr,mag,magerr,bands
    else:
        gSPy,gSPs=np.zeros(0),np.zeros(0)
    if BHrn!=-1:
        gBHy=np.where(crybh['cid']==cid)[0]
        gBHs=np.where(crbh['cid']==cid)[0]
        curSN=SDSSNAME
        curDBIDs=np.append(curDBIDs,'DR7BH%s'%curSN)
        DBID=curDBIDs[0]
        des_outcr=np.zeros((len(gBHy),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
        mjd,mag,magerr,magauto,magautoerr,cIDs,bands,yra,ydec,flags=crbhy['mjd'][gBHy],crbhy['mag'][gBHy],crbhy['magerr'][gBHy],crbhy['mag_auto'][gBHy],crbhy['mag_auto_err'][gBHy],crbhy['cid'][gBHy],crbhy['band'][gBHy],crbhy['ra'][gBHy],crbhy['dec'][gBHy],crbhy['flags'][gBHy]
        db_outcr=np.zeros((len(gBHy),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
        db_outcr['DatabaseID'],db_outcr['Survey'],db_outcr['SurveyCoaddID'],db_outcr['SurveyObjectID'],db_outcr['RA'],db_outcr['DEC'],db_outcr['MJD'],db_outcr['TAG'],db_outcr['BAND'],db_outcr['MAGTYPE'],db_outcr['MAG'],db_outcr['MAGERR'],db_outcr['FLAG']=DBID,'DES',cid,np.array(crbhy['OBJECT_ID'])[gBHy],yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
        outcr=np.append(outcr,db_outcr)
        des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,crbhy['imageid'][gBHy],crbhy['OBJECT_ID'][gBHy],cid,yra,ydec,magauto,magautoerr,mag,magerr,bands
        SDSSmjd,SDSScid=crbh['mjd_g'][gBHs],crbh['cid'][gBHs]
        SDSSra,SDSSdec=crbh['ra'][gBHs],crbh['dec'][gBHs]
        SDSStid,SDSSobjid,stripe=crbh['thingid'][gBHs],crbh['objid'][gBHs],crbh['stripe'][gBHs]
        if tid==0:tid=SDSStid[0]
        SDSSmagdict,SDSSmagerrdict={b: crbh['psfmag_%s'%(b.lower())][gBHs] for b in SDSSbands},{b: crbh['psfmagerr_%s'%(b.lower())][gBHs] for b in SDSSbands}
        SDSS_outcr=np.zeros((5*len(gBHs),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
        for b,ib in zip(SDSSbands,np.arange(len(SDSSbands))):
            SDSS_outcr['DatabaseID'][ib::5],SDSS_outcr['Survey'][ib::5],SDSS_outcr['SurveyCoaddID'][ib::5],SDSS_outcr['SurveyObjectID'][ib::5],SDSS_outcr['RA'][ib::5],SDSS_outcr['DEC'][ib::5],SDSS_outcr['MJD'][ib::5],SDSS_outcr['TAG'][ib::5],SDSS_outcr['BAND'][ib::5],SDSS_outcr['MAGTYPE'][ib::5],SDSS_outcr['MAG'][ib::5],SDSS_outcr['MAGERR'][ib::5],SDSS_outcr['FLAG'][ib::5]=DBID,'SDSS',SDSStid,SDSSobjid,SDSSra,SDSSdec,SDSSmjd,stripe,b,'PSF',SDSSmagdict[b],SDSSmagerrdict[b],0
        outcr=np.append(outcr,SDSS_outcr)
    else:
        gBHy,gBHs=np.zeros(0),np.zeros(0)
    os.system('mkdir -p %s/%s'%(DB_path,DBID))
    if len(curDBIDs)>1:
        for curDBID in curDBIDs[1:]:
            os.chdir(DB_path)
            os.system('ln -sf %s %s'%(DBID,curDBID))
    np.savetxt('%s/%s/LC.tab'%(DB_path,DBID),outcr,fmt=('%20s %20s %20s %20s %f %f %f %20s %12s %12s %f %f %i'),header=('DatabaseID Survey SurveyCoaddID SurveyObjectID RA DEC MJD TAG BAND MAGTYPE MAG MAGERR FLAG'),comments='')

    np.savetxt('%s/%s/DES_data.tab'%(DB_path,DBID),des_outcr,fmt='%f %i %i %i %f %f %f %f %f %f %s',header=('MJD IMAGEID OBJECTID COADD_OBJECTS_ID RA DEC MAG_AUTO MAGERR_AUTO MAG_PSF MAGERR_PSF BAND'),comments='')

    #print DBID, curid

    for curDBID in curDBIDs: dbi_out=np.append(dbi_out,np.array([[curDBID,cid,tid,cur_dr7,MQrn,SPrn,SDSSNAME]]),axis=0)
#f=open('/home/rumbaugh/var_database/Y3A1/database_index.dat','ab')
np.savetxt(f,dbi_out,fmt='%s %s %s %s %s %s %s',header='DatabaseID Y3A1_COADD_OBJECTS_ID SDSS_DR13_thingid SDR7ID MQ_ROWNUM SP_ROWNUM DR7_BH_SDSSNAME')
#f.close()
