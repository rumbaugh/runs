import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
DB_path='/home/rumbaugh/var_database/Y3A1'
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
POSSbands=np.array(['g','r','i'])

double_count_indexes=np.zeros(0,dtype='|S30')

cr=np.loadtxt('milliquas_lightcurve_entries_y3a1.tab',dtype={'names':('MQrownum','cid','mjd','ra','dec','imageid','ofilename','objid','mag','magerr','magauto','magautoerr','band','flags','flags_detmodel','flags_model','flags_weight'),'formats':('i8','i8','f8','f8','f8','i8','|S64','i8','f8','f8','f8','f8','|S12','i8','i8','i8','i8')},skiprows=1)
crs=np.loadtxt('milliquas_lightcurve_entries_SDSS.y3a1.tab',skiprows=1,dtype={'names':('numrow','cid','MQ','ray3a1','decy3a1','objid','thingid','mjd_g','ra','dec','run','rerun','stripe','psfmag_u','psfmag_g','psfmag_r','psfmag_i','psfmag_z','psfmagerr_u','psfmagerr_g','psfmagerr_r','psfmagerr_i','psfmagerr_z'),'formats':('i8','i8','i8','f8','f8','i8','i8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

dbi_out=np.zeros((0,4),dtype='i8')

IDs=np.unique(cr['cid'])

for curid in IDs:
    gid,gidy=np.where(cr['cid']==curid)[0],np.where(cry['cid']==curid)[0]
    cur_MQ=cr['MQ'][gid]
    if np.shape(cur_MQ)!=(): cur_MQ=cur_MQ[0]
    mjd,mag,magerr,magauto,magautoerr,cID,bands,yra,ydec,flags=cry['mjd'][gidy],cry['mag'][gidy],cry['magerr'][gidy],cry['mag_auto'][gidy],cry['mag_auto_err'][gidy],cry['cid'][gidy],cry['band'][gidy],cry['ra'][gidy],cry['dec'][gidy],cry['flags'][gidy]
    SDSSmjd,SDSScid=cr['mjd_SDSS'][gid],cr['cid'][gid]
    SDSSra,SDSSdec=cr['ra'][gid],cr['dec'][gid]
    SDSSmagdict,SDSSmagerrdict={b: cr['%s_SDSS'%(b.upper())][gid] for b in POSSbands},{b: cr['%s_SDSS_err'%(b.upper())][gid] for b in POSSbands}

    SDSS_outcr=np.zeros((3,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    for b,ib in zip(POSSbands,np.arange(len(POSSbands))):
        SDSS_outcr['DatabaseID'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['Survey'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['SurveyCoaddID'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['SurveyObjectID'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['RA'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['DEC'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['MJD'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['TAG'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['BAND'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['MAGTYPE'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['MAG'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['MAGERR'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['FLAG'][len(gid)*ib:len(gid)*(ib+1)]='0','SDSS','0','0',SDSSra,SDSSdec,SDSSmjd,'None',b,'PSF',SDSSmagdict[b],SDSSmagerrdict[b],0
    DBID='MQ%i'%cur_MQ
    outcr['DatabaseID']=DBID
    os.system('mkdir -p %s/%s'%(DB_path,DBID))
    db_outcr=np.zeros((len(gidy),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    db_outcr['DatabaseID'],db_outcr['Survey'],db_outcr['SurveyCoaddID'],db_outcr['SurveyObjectID'],db_outcr['RA'],db_outcr['DEC'],db_outcr['MJD'],db_outcr['TAG'],db_outcr['BAND'],db_outcr['MAGTYPE'],db_outcr['MAG'],db_outcr['MAGERR'],db_outcr['FLAG']=DBID,'DES',curid,np.array(cry['OBJECT_ID'])[gidy],yra,ydec,mjd,'NONE',bands,'PSF',mag,magerr,flags
    outcr=np.append(db_outcr,SDSS_outcr)
    des_outcr=np.zeros((len(gidy),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
    des_outcr['MJD'],des_outcr['IMAGEID'],des_outcr['OBJECTID'],des_outcr['COADD_OBJECTS_ID'],des_outcr['RA'],des_outcr['DEC'],des_outcr['MAG_AUTO'],des_outcr['MAGERR_AUTO'],des_outcr['MAG_PSF'],des_outcr['MAGERR_PSF'],des_outcr['BAND']=mjd,cry['imageid'][gidy],cry['OBJECT_ID'][gidy],curid,yra,ydec,magauto,magautoerr,mag,magerr,bands
    np.savetxt('%s/%s/LC.tab'%(DB_path,DBID),outcr,fmt=('%20s %20s %20s %20s %f %f %f %20s %12s %12s %f %f %i'),header=('DatabaseID Survey SurveyCoaddID SurveyObjectID RA DEC MJD TAG BAND MAGTYPE MAG MAGERR FLAG'),comments='')
    np.savetxt('%s/%s/DES_data.tab'%(DB_path,DBID),des_outcr,fmt='%f %i %i %i %f %f %f %f %f %f %s',header=('MJD IMAGEID OBJECTID COADD_OBJECTS_ID RA DEC MAG_AUTO MAGERR_AUTO MAG_PSF MAGERR_PSF BAND'),comments='')
    #np.savetxt('%s/%s/SDSS_data.tab'%(DB_path,DBID),np.array(SDF)[gid],fmt=('%f %f %f %i %i %f %f %f %f %f %f %f %f %f %f%i %i %i %i %i %i %i'),header=('MJD RA DEC OBJID NUMROW PSFMAG_U  PSFMAG_G  PSFMAG_R  PSFMAG_I  PSFMAG_Z  PSFMAGERR_U  PSFMAGERR_G  PSFMAGERR_R  PSFMAGERR_I  PSFMAGERR_Z RUN RERUN STRIPE THINGID MQ_ROWNUM COADD_OBJECTS_UD HPIX'),comments='')
    dbi_out=np.append(dbi_out,np.array([[DBID,curid,0,cr['sdr7id'][gid][0]]]),axis=0)
    #print DBID, curid

f=open('/home/rumbaugh/var_database/Y3A1/database_index.dat','ab')
np.savetxt(f,dbi_out,fmt='%s %s %s %s',header='DatabaseID Y3A1_COADD_OBJECTS_ID SDSS_DR13_thingid SDR7ID')
f.close()
