import numpy as np
import os
import pyfits as py
DB_path='/home/rumbaugh/var_database/Y3A1'
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
POSSbands=np.array(['g','r','i'])
execfile('/home/rumbaugh/pythonscripts/SphDist.py')

crch=np.loadtxt('/home/rumbaugh/dr7_bh_y3a1_match_closechanges.csv',dtype={'names':('SDSSNAME','RA','DEC','HPIX','CID'),'formats':('|S24','f8','f8','i8','i8')},skiprows=1,delimiter=',')

double_count_indexes=np.zeros(0,dtype='|S30')

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SPrownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})

crdbs=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

crybh=np.loadtxt('/home/rumbaugh/dr7_bh_lightcurve_entries_y3a1_closechanges.tab',dtype={'names':('SDSSNAME','cid','mjd','ra','dec','imageid','ofilename','OBJECT_ID','mag','magerr','mag_auto','mag_auto_err','band','flags','flags_detmodel','flags_model','flags_weight'),'formats':('|S24','i8','f8','f8','f8','i8','|S64','i8','f8','f8','f8','f8','|S12','i8','i8','i8','i8')},skiprows=1)

#crybh=np.loadtxt('/home/rumbaugh/dr7_bh_lightcurve_entries_y3a1.tab',dtype={'names':('SDSSNAME','cid','mjd','ra','dec','imageid','ofilename','OBJECT_ID','mag','magerr','mag_auto','mag_auto_err','band','flags','flags_detmodel','flags_model','flags_weight'),'formats':('|S24','i8','f8','f8','f8','i8','|S64','i8','f8','f8','f8','f8','|S12','i8','i8','i8','i8')},skiprows=1)
crbh=np.loadtxt('/home/rumbaugh/dr7_bh_lightcurve_entries_SDSS.y3a1.tab',skiprows=1,dtype={'names':('numrow','cid','SDSSNAME','ray3a1','decy3a1','objid','thingid','mjd_g','ra','dec','run','rerun','stripe','psfmag_u','psfmag_g','psfmag_r','psfmag_i','psfmag_z','psfmagerr_u','psfmagerr_g','psfmagerr_r','psfmagerr_i','psfmagerr_z'),'formats':('i8','i8','|S24','f8','f8','i8','i8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crbhSN=np.loadtxt('/home/rumbaugh/dr7_bh_lightcurve_entries_y3a1_SN.tab',dtype={'names':('SDSSNAME','cid','mjd','ra','dec','mag','magerr','band','flags',),'formats':('|S64','i8','f8','f8','f8','f8','f8','|S12','i8')},skiprows=1)

crmi=np.loadtxt('/home/rumbaugh/var_database/Y3A1/match_index.dat',dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('i8','i8','|S32','f8','f8','i8','i8','|S32')},skiprows=1)

dbids,gdbs,gdb,gmi=np.zeros(len(crch),dtype='|S24'),np.zeros(len(crch),dtype='i8'),np.zeros(len(crch),dtype='object'),np.zeros(len(crch),dtype='i8')
for i in range(0,len(crch)):
    SDSSNAME=crch['SDSSNAME'][i].strip()
    gdb[i]=np.where(crdb['SDSSNAME']==SDSSNAME)[0]
    gdbs[i]=np.where(crdbs['SDSSNAME']==SDSSNAME)[0][0]
    dbids[i]=crdbs['DatabaseID'][gdbs[i]]
    gmi[i]=np.where(crmi['SDSS_NAME']==SDSSNAME)[0][0]

dbi_out=np.zeros((0,7),dtype='object')
for cid,SDSSNAME,ich in zip(crch['CID'],crch['SDSSNAME'],np.arange(len(crch))):
    SDSSNAME=SDSSNAME.strip()
    inSN=False
    outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    Y3A1outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    DR13outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    cur_dr7,tid='None',0
    curDBIDs=np.zeros(0,dtype='|S64')
    gMQSN,gSPSN,gBHSN=np.zeros(0),np.zeros(0),np.zeros(0)
    #if MQrn!=-1:
    #    gMQSN=np.where(crmqSN['cid']==cid)[0]
    #    if len(gMQSN)>0:inSN=True
    #if SPrn!=-1:
    #    gSPSN=np.where(crspSN['cid']==cid)[0]
    #    if len(gSPSN)>0:inSN=True
    #if SDSSNAME!='-1':
    #    gBHSN=np.where(crbhSN['SDSSNAME']==SDSSNAME)[0]
    #    if len(gBHSN)>0:inSN=True
    #if not(inSN): continue
    gMQy,gMQs,gMQSN=np.zeros(0),np.zeros(0),np.zeros(0)
    gSPy,gSPs=np.zeros(0),np.zeros(0)
    if SDSSNAME!='-1':
        gBHy=np.where(crybh['SDSSNAME']==SDSSNAME)[0]
        gBHs=np.where(crbh['SDSSNAME']==SDSSNAME)[0]
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
        maxdist=SphDist(maxra,maxdec,minra,mindec)*60
        if maxdist>100: print 'Maxdist of %.1f for %s,%f,%f,%f,%f'%(maxdist,DBID,maxra,maxdec,minra,mindec)
    for idb in np.arange(len(gdb[ich])):
        crdb[gdb[ich][idb]]['CID']=cid
    crdbs[gdbs]['CID']=cid
    crmi[gmi]['COADD_OBJECTS_ID']=cid
#    for curDBID in curDBIDs: dbi_out=np.append(dbi_out,np.array([[curDBID,cid,tid,cur_dr7,MQrn,SPrn,SDSSNAME]]),axis=0)
#f='/home/rumbaugh/var_database/Y3A1/database_index.dat'
np.savetxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',crdb,fmt='%s %s %s %s %s %s %s',header='DatabaseID Y3A1_COADD_OBJECTS_ID SDSS_DR13_thingid SDR7ID MQ_ROWNUM SP_ROWNUM DR7_BH_SDSSNAME')
np.savetxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.csv',crdbs,fmt='%s,%s,%i,%i,%s,%i,%s,%i,%s',header='DatabaseID,DBIDS,MQrownum,SP_rownum,sdr7id,thingid,SDSSNAME,CID,TILENAME',comments='')
np.savetxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',crdbs,header=('PrimaryDatabaseID AllDatabaseIDs MQ_ROWNUM SP_ROWNUM SDR7ID THINGID SDSSNAME COADD_OBJECTS_ID TILENAME'),fmt='%32s %128s %i %i %s %i %s %i %s',comments='') 
np.savetxt('/home/rumbaugh/var_database/Y3A1/match_index.dat',crmi,fmt='%32s %32s %32s %f %f %i %i %32s',header='MQ_ROWNUM SP_ROWNUM SDSS_NAME RA DEC HPIX COADD_OBJECTS_ID TILENAME',comments='')

#f.close()
#np.savetxt('/home/rumbaugh/database_maxdists_test.dat',maxdists)
#maxsortdists=np.sort(maxsortdists)
#print maxsortdists[-100:]
