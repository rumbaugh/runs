import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
DB_path='/home/rumbaugh/var_database'
cre=np.loadtxt('/home/rumbaugh/milliquas_num_epochs.dat',dtype='i8')
IDs,exps=cre[:,0],cre[:,1]
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])

ge=np.argsort(exps)[::-1]

con=ea.connect()

outputdir='/home/rumbaugh/var_database'
IDsteplen=10

curIDstep=0
laststep=len(IDs)
steps_arr=np.arange(0,laststep,IDsteplen,dtype='i8')
for curIDstep in steps_arr:
    idsstr=''
    if curIDstep!=steps_arr[-1]:
        for s in IDs[curIDstep:curIDstep+10]: idsstr='%s, %i'%(idsstr,s)
        curIDs=IDs[curIDstep:curIDstep+10]
    else:
        for s in IDs[curIDstep:laststep]: idsstr='%s, %i'%(idsstr,s)
        curIDs=IDs[curIDstep:laststep]
    idsstr=idsstr[1:]

    query='SELECT e.mjd_obs,o.imageid,o.object_id,y.COADD_OBJECTS_ID,y.RA,y.DEC,o.mag_auto+i.zeropoint as magauto,o.magerr_auto+i.sigma_zeropoint as magerr_auto,o.mag_psf+i.zeropoint as magpsf,o.magerr_psf+i.sigma_zeropoint as magerr_psf,o.band,i.exptime FROM des_admin.Y1A1_COADD_OBJECTS y, des_admin.y1a1_objects o, des_admin.y1a1_image i,des_admin.y1a1_exposure e where o.imageid=i.id and i.exposureid=e.id and y.coadd_objects_id=o.coadd_objects_id and y.coadd_objects_id in (%s)'%idsstr

    DF=con.query_to_pandas(query)

    SDSSquery='SELECT s.mjd_g as mjd,s.ra,s.dec,s.objid,s.numrow,s.psfmag_u,s.psfmag_g,s.psfmag_r,s.psfmag_i,s.psfmag_z,s.psfmagerr_u,s.psfmagerr_g,s.psfmagerr_r,s.psfmagerr_i,s.psfmagerr_z,s.run,s.rerun,s.stripe,s.thingid,m.mq_rownum,m.coadd_objects_id as cid,m.hpix FROM RUMBAUGH.MQ_SDSS_DR13_MATCH s, RUMBAUGH.MILLIQUAS_Y1A1_MATCH_ONLY m WHERE m.numrow=s.numrow and m.coadd_objects_id in (%s)'%idsstr

    SDF=con.query_to_pandas(SDSSquery)
    stags=np.zeros(len(SDF['RA']),dtype='|S12')
    stags[:]='NONE'
    stags[np.array(SDF['STRIPE'])==82]='Stripe82'

    #cr=np.loadtxt('/home/rumbaugh/milliquas_lightcurve_entries_y1a1.tab',skiprows=1,dtype={'names':('mjd','imageid','cid','MGid','ra','dec','mag','magerr','band','exp'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','|S12','f8')})
    mjd,mag,magerr,cID,bands,yra,ydec=np.array(DF['MJD_OBS']),np.array(DF['MAGPSF']),np.array(DF['MAGERR_PSF']),np.array(DF['COADD_OBJECTS_ID']),np.array(DF['BAND']),np.array(DF['RA']),np.array(DF['DEC'])
    SDSSmjd,SDSScid=np.array(SDF['MJD']),np.array(SDF['CID'])
    SDSSra,SDSSdec=np.array(SDF['RA']),np.array(SDF['DEC'])
    SDSSmagdict,SDSSmagerrdict={b: np.array(SDF['PSFMAG_%s'%(b.upper())]) for b in SDSSbands},{b: np.array(SDF['PSFMAGERR_%s'%(b.upper())]) for b in SDSSbands}


    for idcur,iid in zip(curIDs,np.arange(len(curIDs))):
        #print idcur
        DBID=curIDstep+iid
        os.system('rm -rf %s/%i'%(DB_path,DBID))
        os.mkdir('%s/%i'%(DB_path,DBID))
        gci=np.where(idcur==cID)[0]
        db_outcr=np.zeros((len(gci),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
        db_outcr['DatabaseID'],db_outcr['Survey'],db_outcr['SurveyCoaddID'],db_outcr['SurveyObjectID'],db_outcr['RA'],db_outcr['DEC'],db_outcr['MJD'],db_outcr['TAG'],db_outcr['BAND'],db_outcr['MAGTYPE'],db_outcr['MAG'],db_outcr['MAGERR'],db_outcr['FLAG']=DBID,'DES',idcur,np.array(DF['OBJECT_ID'])[gci],yra[gci],ydec[gci],mjd[gci],'NONE',bands[gci],'PSF',mag[gci],magerr[gci],0
        gsci=np.where(idcur==SDSScid)[0]
        SDSS_outcr=np.zeros((len(gsci)*5,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
        for b,ib in zip(SDSSbands,np.arange(len(SDSSbands))):
            SDSS_outcr['DatabaseID'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['Survey'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['SurveyCoaddID'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['SurveyObjectID'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['RA'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['DEC'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['MJD'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['TAG'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['BAND'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['MAGTYPE'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['MAG'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['MAGERR'][len(gsci)*ib:len(gsci)*(ib+1)],SDSS_outcr['FLAG'][len(gsci)*ib:len(gsci)*(ib+1)]=DBID,'SDSS',np.array(SDF['THINGID'])[gsci],np.array(SDF['OBJID'])[gsci],SDSSra[gsci],SDSSdec[gsci],SDSSmjd[gsci],stags[gsci],b,'PSF',SDSSmagdict[b][gsci],SDSSmagerrdict[b][gsci],0
        outcr=np.append(db_outcr,SDSS_outcr)
        np.savetxt('%s/%i/LC.tab'%(DB_path,DBID),outcr,fmt=('%12i %20s %20s %20s %f %f %f %20s %12s %12s %f %f %i'),header=('DatabaseID Survey SurveyCoaddID SurveyObjectID RA DEC MJD TAG BAND MAGTYPE MAG MAGERR FLAG'),comments='')
        np.savetxt('%s/%i/DES_data.tab'%(DB_path,DBID),np.array(DF)[gci],fmt='%f %i %i %i %f %f %f %f %f %f %s %f',header=('MJD IMAGEID OBJECTID COADD_OBJECTS_ID RA DEC MAG_AUTO MAGERR_AUTO MAG_PSF MAGERR_PSF BAND EXPTIME'),comments='')
        np.savetxt('%s/%i/SDSS_data.tab'%(DB_path,DBID),np.array(SDF)[gsci],fmt=('%f %f %f %i %i %f %f %f %f %f %f %f %f %f %f%i %i %i %i %i %i %i'),header=('MJD RA DEC OBJID NUMROW PSFMAG_U  PSFMAG_G  PSFMAG_R  PSFMAG_I  PSFMAG_Z  PSFMAGERR_U  PSFMAGERR_G  PSFMAGERR_R  PSFMAGERR_I  PSFMAGERR_Z RUN RERUN STRIPE THINGID MQ_ROWNUM COADD_OBJECTS_UD HPIX'),comments='')
