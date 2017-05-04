import numpy as np
import os
DB_path='/home/rumbaugh/var_database/Y3A1'
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
POSSbands=np.array(['g','r','i'])
execfile('/home/rumbaugh/pythonscripts/SphDist.py')

double_count_indexes=np.zeros(0,dtype='|S30')

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SPrownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})

crsp=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EpochG','EpochR','EpochI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_r_SDSS','g_SDSS','g_ERR','r_SDSS','r_ERR','i_SDSS','i_ERR'),'formats':('f8','f8','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S12','f8','f8','|S12','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8')})
crse=np.loadtxt('/home/rumbaugh/SDSSPOSS_lightcurve_entries.tab',dtype={'names':('cid','SP_ROWNUM','ra_y1a1','dec_y1a1','sdr7id','mjd_SDSS','EPOCHG','EPOCHR','EPOCHI','ra','dec','G_POSS','R_POSS','I_POSS','G_POSS_err','R_POSS_err','I_POSS_err','G_SDSS','R_SDSS','I_SDSS','G_SDSS_err','R_SDSS_err','I_SDSS_err'),'formats':('i8','i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
cryse=np.loadtxt('/home/rumbaugh/SDSSPOSS_lightcurve_entries_y3a1.tab',skiprows=1,dtype={'names':('SPid','cid','mjd','ra','dec','imageid','ofile','OBJECT_ID','mag','magerr','mag_auto','mag_auto_err','band','flags','flags_detmodel','flags_model','flags_weight'),'formats':('i8','i8','f8','f8','f8','i8','|S64','i8','f8','f8','f8','f8','|S12','i8','i8','i8','i8')})
crspSN=np.loadtxt('/home/rumbaugh/sdssposs_lightcurve_entries_y3a1_SN_abridged.tab',dtype={'names':('SPrownum','cid','mjd','ra','dec','mag','magerr','band','flags',),'formats':('i8','i8','f8','f8','f8','f8','f8','|S12','i8')},skiprows=1)

crybh=np.loadtxt('/home/rumbaugh/dr7_bh_lightcurve_entries_y3a1.tab',dtype={'names':('SDSSNAME','cid','mjd','ra','dec','imageid','ofilename','OBJECT_ID','mag','magerr','mag_auto','mag_auto_err','band','flags','flags_detmodel','flags_model','flags_weight'),'formats':('|S24','i8','f8','f8','f8','i8','|S64','i8','f8','f8','f8','f8','|S12','i8','i8','i8','i8')},skiprows=1)
crbh=np.loadtxt('/home/rumbaugh/dr7_bh_lightcurve_entries_SDSS.y3a1.tab',skiprows=1,dtype={'names':('numrow','cid','SDSSNAME','ray3a1','decy3a1','objid','thingid','mjd_g','ra','dec','run','rerun','stripe','psfmag_u','psfmag_g','psfmag_r','psfmag_i','psfmag_z','psfmagerr_u','psfmagerr_g','psfmagerr_r','psfmagerr_i','psfmagerr_z'),'formats':('i8','i8','|S24','f8','f8','i8','i8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crbhSN=np.loadtxt('/home/rumbaugh/dr7_bh_lightcurve_entries_y3a1_SN.tab',dtype={'names':('SDSSNAME','cid','mjd','ra','dec','mag','magerr','band','flags',),'formats':('|S64','i8','f8','f8','f8','f8','f8','|S12','i8')},skiprows=1)

crmqy=np.loadtxt('/home/rumbaugh/milliquas_lightcurve_entries_y3a1.tab',dtype={'names':('MQrownum','cid','mjd','ra','dec','imageid','ofilename','OBJECT_ID','mag','magerr','mag_auto','mag_auto_err','band','flags','flags_detmodel','flags_model','flags_weight'),'formats':('i8','i8','f8','f8','f8','i8','|S64','i8','f8','f8','f8','f8','|S12','i8','i8','i8','i8')},skiprows=1)
crmqs=np.loadtxt('/home/rumbaugh/milliquas_lightcurve_entries_SDSS.y3a1.tab',skiprows=1,dtype={'names':('numrow','cid','MQ','ray3a1','decy3a1','objid','thingid','mjd_g','ra','dec','run','rerun','stripe','psfmag_u','psfmag_g','psfmag_r','psfmag_i','psfmag_z','psfmagerr_u','psfmagerr_g','psfmagerr_r','psfmagerr_i','psfmagerr_z'),'formats':('i8','i8','i8','f8','f8','i8','i8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crmqSN=np.loadtxt('/home/rumbaugh/milliquas_lightcurve_entries_y3a1_SN_abridged.tab',dtype={'names':('MQrownum','cid','mjd','ra','dec','mag','magerr','band','flags',),'formats':('i8','i8','f8','f8','f8','f8','f8','|S12','i8')},skiprows=1)

crmi=np.loadtxt('/home/rumbaugh/var_database/Y3A1/match_index.dat',dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('i8','i8','|S32','f8','f8','i8','i8','|S32')},skiprows=1)
#gcrmi_match=np.where(crmi['COADD_OBJECTS_ID']>0)[0]
gdbids=np.array(['MQ206171','MQ208717','MQ213230','MQ209259','MQ212075','MQ211918','MQ214934','MQ214802','MQ214532','MQ215548','MQ216346'])
gcids=crdb['CID'][np.in1d(crdb['DBID'],gdbids)]
gcrmi_match=np.in1d(crmi['COADD_OBJECTS_ID'],gcids)
crmim=crmi[gcrmi_match]

dbi_out=np.zeros((0,7),dtype='object')
maxdists=np.zeros(len(crmim))
for cid,MQrn,SPrn,SDSSNAME,imi in zip(crmim['COADD_OBJECTS_ID'],crmim['MQ_ROWNUM'],crmim['SP_ROWNUM'],crmim['SDSS_NAME'],np.arange(len(crmim))):
    inSN=False
    outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    Y3A1outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    DR13outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    cur_dr7,tid='None',0
    curDBIDs=np.zeros(0,dtype='|S64')
    gMQSN,gSPSN=np.zeros(0),np.zeros(0)
    #if MQrn!=-1:
    #    gMQSN=np.where(crmqSN['cid']==cid)[0]
    #    if len(gMQSN)>0:inSN=True
    #if SPrn!=-1:
    #    gSPSN=np.where(crspSN['cid']==cid)[0]
    #    if len(gSPSN)>0:inSN=True
    if SDSSNAME!='-1':
        gBHSN=np.where(crbhSN['cid']==cid)[0]
        if len(gBHSN)>0:inSN=True
    #if not(inSN): continue
    if MQrn!=-1:
        gMQy=np.where(crmqy['cid']==cid)[0]
        gMQs=np.where(crmqs['cid']==cid)[0]
        curMQ=MQrn
        curDBIDs=np.append(curDBIDs,'MQ%i'%curMQ)
        DBID=curDBIDs[0]
        des_outcr=np.zeros((len(gMQy),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
        if len(gMQy)>0:
            mjd,mag,magerr,magauto,magautoerr,cIDs,bands,yra,ydec,flags=crmqy['mjd'][gMQy],crmqy['mag'][gMQy],crmqy['magerr'][gMQy],crmqy['mag_auto'][gMQy],crmqy['mag_auto_err'][gMQy],crmqy['cid'][gMQy],crmqy['band'][gMQy],crmqy['ra'][gMQy],crmqy['dec'][gMQy],crmqy['flags'][gMQy]
            Y3A1outcr=np.zeros((len(gMQy),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
            Y3A1outcr['DatabaseID'],Y3A1outcr['Survey'],Y3A1outcr['SurveyCoaddID'],Y3A1outcr['SurveyObjectID'],Y3A1outcr['RA'],Y3A1outcr['DEC'],Y3A1outcr['MJD'],Y3A1outcr['TAG'],Y3A1outcr['BAND'],Y3A1outcr['MAGTYPE'],Y3A1outcr['MAG'],Y3A1outcr['MAGERR'],Y3A1outcr['FLAG']=DBID,'DES',cid,np.array(crmqy['OBJECT_ID'])[gMQy],yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
            outcr=np.append(outcr,Y3A1outcr)
            des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,crmqy['imageid'][gMQy],crmqy['OBJECT_ID'][gMQy],cid,yra,ydec,magauto,magautoerr,mag,magerr,bands
        if len(gMQSN)>0:
            mjd,mag,magerr,cIDs,bands,yra,ydec,flags=crmqSN['mjd'][gMQSN],crmqSN['mag'][gMQSN],crmqSN['magerr'][gMQSN],crmqSN['cid'][gMQSN],crmqSN['band'][gMQSN],crmqSN['ra'][gMQSN],crmqSN['dec'][gMQSN],crmqSN['flags'][gMQSN]
            Y3A1outcr=np.zeros((len(gMQSN),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
            Y3A1outcr['DatabaseID'],Y3A1outcr['Survey'],Y3A1outcr['SurveyCoaddID'],Y3A1outcr['SurveyObjectID'],Y3A1outcr['RA'],Y3A1outcr['DEC'],Y3A1outcr['MJD'],Y3A1outcr['TAG'],Y3A1outcr['BAND'],Y3A1outcr['MAGTYPE'],Y3A1outcr['MAG'],Y3A1outcr['MAGERR'],Y3A1outcr['FLAG']=DBID,'DES',cid,0,yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
            outcr=np.append(outcr,Y3A1outcr)
            if len(des_outcr)==0: 
                des_outcr=np.zeros((len(mjd),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
                des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,0,0,cid,yra,ydec,0,0,mag,magerr,bands
        if len(gMQs)>0:
            SDSSmjd,SDSScid=crmqs['mjd_g'][gMQs],crmqs['cid'][gMQs]
            SDSSra,SDSSdec=crmqs['ra'][gMQs],crmqs['dec'][gMQs]
            SDSStid,SDSSobjid,stripe=crmqs['thingid'][gMQs],crmqs['objid'][gMQs],crmqs['stripe'][gMQs]
            tid=SDSStid[0]
            SDSSmagdict,SDSSmagerrdict={b: crmqs['psfmag_%s'%(b.lower())][gMQs] for b in SDSSbands},{b: crmqs['psfmagerr_%s'%(b.lower())][gMQs] for b in SDSSbands}
            DR13outcr=np.zeros((5*len(gMQs),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
            for b,ib in zip(SDSSbands,np.arange(len(SDSSbands))):
                DR13outcr['DatabaseID'][ib::5],DR13outcr['Survey'][ib::5],DR13outcr['SurveyCoaddID'][ib::5],DR13outcr['SurveyObjectID'][ib::5],DR13outcr['RA'][ib::5],DR13outcr['DEC'][ib::5],DR13outcr['MJD'][ib::5],DR13outcr['TAG'][ib::5],DR13outcr['BAND'][ib::5],DR13outcr['MAGTYPE'][ib::5],DR13outcr['MAG'][ib::5],DR13outcr['MAGERR'][ib::5],DR13outcr['FLAG'][ib::5]=DBID,'SDSS',SDSStid,SDSSobjid,SDSSra,SDSSdec,SDSSmjd,stripe,b,'PSF',SDSSmagdict[b],SDSSmagerrdict[b],0
            outcr=np.append(outcr,DR13outcr)
    else:
        gMQy,gMQs,gMQSN=np.zeros(0),np.zeros(0),np.zeros(0)
    if SPrn!=-1:
        gSPy=np.where(cryse['cid']==cid)[0]
        gSPs=np.where(crse['cid']==cid)[0]
        cur_dr7=crse['sdr7id'][gSPs[0]]
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
        sp_outcr=np.append(p_outcr,SDSS_outcr)
        outcr=np.append(outcr,sp_outcr)
        if len(Y3A1outcr)==0:
            mjd,mag,magerr,magauto,magautoerr,cIDs,bands,yra,ydec,flags=cryse['mjd'][gSPy],cryse['mag'][gSPy],cryse['magerr'][gSPy],cryse['mag_auto'][gSPy],cryse['mag_auto_err'][gSPy],cryse['cid'][gSPy],cryse['band'][gSPy],cryse['ra'][gSPy],cryse['dec'][gSPy],cryse['flags'][gSPy]
            Y3A1outcr=np.zeros((len(gSPy),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
            Y3A1outcr['DatabaseID'],Y3A1outcr['Survey'],Y3A1outcr['SurveyCoaddID'],Y3A1outcr['SurveyObjectID'],Y3A1outcr['RA'],Y3A1outcr['DEC'],Y3A1outcr['MJD'],Y3A1outcr['TAG'],Y3A1outcr['BAND'],Y3A1outcr['MAGTYPE'],Y3A1outcr['MAG'],Y3A1outcr['MAGERR'],Y3A1outcr['FLAG']=DBID,'DES',cid,np.array(cryse['OBJECT_ID'])[gSPy],yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
            outcr=np.append(outcr,Y3A1outcr)
            des_outcr=np.zeros((len(gSPy),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
            des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,cryse['imageid'][gSPy],cryse['OBJECT_ID'][gSPy],cid,yra,ydec,magauto,magautoerr,mag,magerr,bands
            if len(gSPSN)>0:
                mjd,mag,magerr,cIDs,bands,yra,ydec,flags=crspSN['mjd'][gSPSN],crspSN['mag'][gSPSN],crspSN['magerr'][gSPSN],crspSN['cid'][gSPSN],crspSN['band'][gSPSN],crspSN['ra'][gSPSN],crspSN['dec'][gSPSN],crspSN['flags'][gSPSN]
                Y3A1outcr=np.zeros((len(gSPSN),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
                Y3A1outcr['DatabaseID'],Y3A1outcr['Survey'],Y3A1outcr['SurveyCoaddID'],Y3A1outcr['SurveyObjectID'],Y3A1outcr['RA'],Y3A1outcr['DEC'],Y3A1outcr['MJD'],Y3A1outcr['TAG'],Y3A1outcr['BAND'],Y3A1outcr['MAGTYPE'],Y3A1outcr['MAG'],Y3A1outcr['MAGERR'],Y3A1outcr['FLAG']=DBID,'DES',cid,0,yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
                outcr=np.append(outcr,Y3A1outcr)
                if len(des_outcr)==0:
                    des_outcr=np.zeros((len(mjd),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
                    des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,0,0,cid,yra,ydec,0,0,mag,magerr,bands

    else:
        gSPy,gSPs=np.zeros(0),np.zeros(0)
    if SDSSNAME!='-1':
        gBHy=np.where(crybh['cid']==cid)[0]
        gBHs=np.where(crbh['cid']==cid)[0]
        curSN=SDSSNAME
        curDBIDs=np.append(curDBIDs,'DR7BH%s'%curSN)
        DBID=curDBIDs[0]
        des_outcr=np.zeros((len(gBHy),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
        mjd,mag,magerr,magauto,magautoerr,cIDs,bands,yra,ydec,flags=crybh['mjd'][gBHy],crybh['mag'][gBHy],crybh['magerr'][gBHy],crybh['mag_auto'][gBHy],crybh['mag_auto_err'][gBHy],crybh['cid'][gBHy],crybh['band'][gBHy],crybh['ra'][gBHy],crybh['dec'][gBHy],crybh['flags'][gBHy]
        if len(Y3A1outcr)==0:
            Y3A1outcr=np.zeros((len(gBHy),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
            Y3A1outcr['DatabaseID'],Y3A1outcr['Survey'],Y3A1outcr['SurveyCoaddID'],Y3A1outcr['SurveyObjectID'],Y3A1outcr['RA'],Y3A1outcr['DEC'],Y3A1outcr['MJD'],Y3A1outcr['TAG'],Y3A1outcr['BAND'],Y3A1outcr['MAGTYPE'],Y3A1outcr['MAG'],Y3A1outcr['MAGERR'],Y3A1outcr['FLAG']=DBID,'DES',cid,np.array(crybh['OBJECT_ID'])[gBHy],yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
            outcr=np.append(outcr,Y3A1outcr)
            des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,crybh['imageid'][gBHy],crybh['OBJECT_ID'][gBHy],cid,yra,ydec,magauto,magautoerr,mag,magerr,bands
            if len(gBHSN)>0:
                mjd,mag,magerr,cIDs,bands,yra,ydec,flags=crbhSN['mjd'][gBHSN],crbhSN['mag'][gBHSN],crbhSN['magerr'][gBHSN],crbhSN['cid'][gBHSN],crbhSN['band'][gBHSN],crbhSN['ra'][gBHSN],crbhSN['dec'][gBHSN],crbhSN['flags'][gBHSN]
                Y3A1outcr=np.zeros((len(gBHSN),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
                Y3A1outcr['DatabaseID'],Y3A1outcr['Survey'],Y3A1outcr['SurveyCoaddID'],Y3A1outcr['SurveyObjectID'],Y3A1outcr['RA'],Y3A1outcr['DEC'],Y3A1outcr['MJD'],Y3A1outcr['TAG'],Y3A1outcr['BAND'],Y3A1outcr['MAGTYPE'],Y3A1outcr['MAG'],Y3A1outcr['MAGERR'],Y3A1outcr['FLAG']=DBID,'DES',cid,0,yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
                outcr=np.append(outcr,Y3A1outcr)
                if len(des_outcr)==0: 
                    des_outcr=np.zeros((len(mjd),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
                    des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,0,0,cid,yra,ydec,0,0,mag,magerr,bands
        elif len(gBHSN)>0:
            mjd,mag,magerr,cIDs,bands,yra,ydec,flags=crbhSN['mjd'][gBHSN],crbhSN['mag'][gBHSN],crbhSN['magerr'][gBHSN],crbhSN['cid'][gBHSN],crbhSN['band'][gBHSN],crbhSN['ra'][gBHSN],crbhSN['dec'][gBHSN],crbhSN['flags'][gBHSN]
            Y3A1outcr=np.zeros((len(gBHSN),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
            Y3A1outcr['DatabaseID'],Y3A1outcr['Survey'],Y3A1outcr['SurveyCoaddID'],Y3A1outcr['SurveyObjectID'],Y3A1outcr['RA'],Y3A1outcr['DEC'],Y3A1outcr['MJD'],Y3A1outcr['TAG'],Y3A1outcr['BAND'],Y3A1outcr['MAGTYPE'],Y3A1outcr['MAG'],Y3A1outcr['MAGERR'],Y3A1outcr['FLAG']=DBID,'DES',cid,0,yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
            outcr=np.append(outcr,Y3A1outcr)
            if len(des_outcr)==0: 
                des_outcr=np.zeros((len(mjd),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
                des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,0,0,cid,yra,ydec,0,0,mag,magerr,bands

        if ((len(gBHs)>0)&(len(DR13outcr)==0)):
            SDSSmjd,SDSScid=crbh['mjd_g'][gBHs],crbh['cid'][gBHs]
            SDSSra,SDSSdec=crbh['ra'][gBHs],crbh['dec'][gBHs]
            SDSStid,SDSSobjid,stripe=crbh['thingid'][gBHs],crbh['objid'][gBHs],crbh['stripe'][gBHs]
            if tid==0:tid=SDSStid[0]
            SDSSmagdict,SDSSmagerrdict={b: crbh['psfmag_%s'%(b.lower())][gBHs] for b in SDSSbands},{b: crbh['psfmagerr_%s'%(b.lower())][gBHs] for b in SDSSbands}
            DR13outcr=np.zeros((5*len(gBHs),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
            for b,ib in zip(SDSSbands,np.arange(len(SDSSbands))):
                DR13outcr['DatabaseID'][ib::5],DR13outcr['Survey'][ib::5],DR13outcr['SurveyCoaddID'][ib::5],DR13outcr['SurveyObjectID'][ib::5],DR13outcr['RA'][ib::5],DR13outcr['DEC'][ib::5],DR13outcr['MJD'][ib::5],DR13outcr['TAG'][ib::5],DR13outcr['BAND'][ib::5],DR13outcr['MAGTYPE'][ib::5],DR13outcr['MAG'][ib::5],DR13outcr['MAGERR'][ib::5],DR13outcr['FLAG'][ib::5]=DBID,'SDSS',SDSStid,SDSSobjid,SDSSra,SDSSdec,SDSSmjd,stripe,b,'PSF',SDSSmagdict[b],SDSSmagerrdict[b],0
            outcr=np.append(outcr,DR13outcr)
        else:
            if len(gBHs)==0:print "No SDSS data for %s"%SDSSNAME
    else:
        gBHy,gBHs=np.zeros(0),np.zeros(0)
    os.system('mkdir -p %s/%s'%(DB_path,DBID))
    if len(curDBIDs)>1:
        for curDBID in curDBIDs[1:]:
            os.chdir(DB_path)
            os.system('ln -sf %s %s'%(DBID,curDBID))
    np.savetxt('%s/%s/LC.tab'%(DB_path,DBID),outcr,fmt=('%20s %20s %20s %20s %f %f %f %20s %12s %12s %f %f %i'),header=('DatabaseID Survey SurveyCoaddID SurveyObjectID RA DEC MJD TAG BAND MAGTYPE MAG MAGERR FLAG'),comments='')

    np.savetxt('%s/%s/DES_data.tab'%(DB_path,DBID),des_outcr,fmt='%f %i %i %i %f %f %f %f %f %f %s',header=('MJD IMAGEID OBJECTID COADD_OBJECTS_ID RA DEC MAG_AUTO MAGERR_AUTO MAG_PSF MAGERR_PSF BAND'),comments='')
    if len(outcr)>0:
        maxra,maxdec,minra,mindec=np.max(outcr['RA']),np.max(outcr['DEC']),np.min(outcr['RA']),np.min(outcr['DEC'])
        maxdists[imi]=SphDist(maxra,maxdec,minra,mindec)*60
        if maxdists[imi]>100: print 'Maxdist of %.1f for %s,%f,%f,%f,%f'%(maxdists[imi],DBID,maxra,maxdec,minra,mindec)
#    for curDBID in curDBIDs: dbi_out=np.append(dbi_out,np.array([[curDBID,cid,tid,cur_dr7,MQrn,SPrn,SDSSNAME]]),axis=0)
#f='/home/rumbaugh/var_database/Y3A1/database_index.dat'
#np.savetxt(f,dbi_out,fmt='%s %s %s %s %s %s %s',header='DatabaseID Y3A1_COADD_OBJECTS_ID SDSS_DR13_thingid SDR7ID MQ_ROWNUM SP_ROWNUM DR7_BH_SDSSNAME')
#f.close()
#np.savetxt('/home/rumbaugh/database_maxdists_test.dat',maxdists)
#maxsortdists=np.sort(maxsortdists)
#print maxsortdists[-100:]
