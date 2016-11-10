import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
DB_path='/home/rumbaugh/var_database'
cre=np.loadtxt('/home/rumbaugh/SDSSPOSS_Y1A1_num_epochs.dat',dtype='i8')
IDs,exps=cre[:,0],cre[:,1]
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])

ge=np.argsort(exps)[::-1]

cr=np.loadtxt('SDSSPOSS_lightcurve_entries.tab',dtype={'names':('cid','SP_ROWNUM','ra_y1a1','dec_y1a1','sdr7id','mjd_SDSS','EPOCHG','EPOCHR','EPOCHI','ra','dec','G_POSS','R_POSS','I_POSS','G_POSS_err','R_POSS_err','I_POSS_err','G_SDSS','R_SDSS','I_SDSS','G_SDSS_err','R_SDSS_err','I_SDSS_err'),'formats':('i8','i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
cry=np.loadtxt('SDSSPOSS_lightcurve_entries_Y1A1.tab',skiprows=1,dtype={'names':('mjd','imageid','cid','SPid','ra','dec','mag','magerr','band','exp'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','|S12','f8')})

crdb=np.loadtxt('/home/rumbaugh/var_database/database_index.dat')
maxdbid=len(crdb)
dbi_out=np.zeros((maxdbid,4),dtype='i8')
dbi_out[:,:3]=np.copy(crdb)
for curid in IDs[:10]:
    gid,gidy=np.where(cr['cid']==curid)[0],np.where(cry['cid']==curid)[0]
    mjd,mag,magerr,cID,bands,yra,ydec=cry['mjd'][gidy],cry['mag'][gidy],cry['magerr'][gidy],cry['cid'][gidy],cry['band'][gidy],cry['ra'][gidy],cry['dec'][gidy]
    SDSSmjd,SDSScid=cr['mjd_SDSS'][gid],cr['cid'][gid]
    SDSSra,SDSSdec=cr['ra'][gid],cr['dec'][gid]
    SDSSmagdict,SDSSmagerrdict={b: cr['%s_SDSS'%(b.upper())][gid] for b in POSSbands},{b: cr['%s_SDSS_err'%(b.upper())][gid] for b in POSSbands}
    POSScid=cr['cid'][gid]
    POSSra,POSSdec=cr['ra'][gid],cr['dec'][gid]
    POSSmagdict,POSSmagerrdict,POSSmjddict={b: cr['%s_POSS'%(b.upper())][gid] for b in POSSbands},{b: cr['%s_POSS_err'%(b.upper())][gid] for b in POSSbands},{b: 50448.+365.25*(cr['EPOCH%s'%(b.upper())][gid]-1997) for b in POSSbands}

    p_outcr=np.zeros((3,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    SDSS_outcr=np.zeros((3,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    for b,ib in zip(POSSbands,np.arange(len(POSSbands))):
        p_outcr['DatabaseID'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['Survey'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['SurveyCoaddID'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['SurveyObjectID'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['RA'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['DEC'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['MJD'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['TAG'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['BAND'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['MAGTYPE'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['MAG'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['MAGERR'][len(gid)*ib:len(gid)*(ib+1)],p_outcr['FLAG'][len(gid)*ib:len(gid)*(ib+1)]=DBID,'POSS','0','0',POSSra,POSSdec,POSSmjddict[b],'None',b,'PSF',POSSmagdict[b],POSSmagerrdict[b],0
        SDSS_outcr['DatabaseID'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['Survey'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['SurveyCoaddID'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['SurveyObjectID'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['RA'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['DEC'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['MJD'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['TAG'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['BAND'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['MAGTYPE'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['MAG'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['MAGERR'][len(gid)*ib:len(gid)*(ib+1)],SDSS_outcr['FLAG'][len(gid)*ib:len(gid)*(ib+1)]=DBID,'SDSS','0','0',SDSSra,SDSSdec,SDSSmjd,'None',b,'PSF',SDSSmagdict[b],SDSSmagerrdict[b],0
    outcr=np.append(p_outcr,SDSS_outcr)
    cur_cID=cID
    if np.shape(cur_cID)!=():
        cur_cID=cID[0]
    if cID in crdb[:,1]:
        gdb=np.where(cID==crdb[:,1])[0]
        DBID=crdb[gdb[0]]
        dbi_out[gdb[0]][3]=cr['sdr7id'][gid][0]
        crLC=np.loadtxt('%s/%i/LC.tab'%(DB_path,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S20','|S20','f8','f8','i8')},skiprows=1)
        outcr=np.append(crLC,outcr)
        np.savetxt('%s/%i/LC.tab'%(DB_path,DBID),outcr,fmt=('%12i %20s %20s %20s %f %f %f %20s %12s %12s %f %f %i'),header=('DatabaseID Survey SurveyCoaddID SurveyObjectID RA DEC MJD TAG BAND MAGTYPE MAG MAGERR FLAG'),comments='')
    else:
        DBID=maxdbid
        maxdbid+=1
        db_outcr=np.zeros((len(gidy),),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
        db_outcr['DatabaseID'],db_outcr['Survey'],db_outcr['SurveyCoaddID'],db_outcr['SurveyObjectID'],db_outcr['RA'],db_outcr['DEC'],db_outcr['MJD'],db_outcr['TAG'],db_outcr['BAND'],db_outcr['MAGTYPE'],db_outcr['MAG'],db_outcr['MAGERR'],db_outcr['FLAG']=DBID,'DES',idcur,np.array(cry['OBJECT_ID'])[gidy],yra[gidy],ydec[gidy],mjd[gidy],'NONE',bands[gidy],'PSF',mag[gidy],magerr[gidy],0
        outcr=np.append(db_outcr,outcr)
        np.savetxt('%s/%i/LC.tab'%(DB_path,DBID),outcr,fmt=('%12i %20s %20s %20s %f %f %f %20s %12s %12s %f %f %i'),header=('DatabaseID Survey SurveyCoaddID SurveyObjectID RA DEC MJD TAG BAND MAGTYPE MAG MAGERR FLAG'),comments='')
        np.savetxt('%s/%i/DES_data.tab'%(DB_path,DBID),db_outcr,fmt='%f %i %i %i %f %f %f %f %f %f %s %f',header=('MJD IMAGEID OBJECTID COADD_OBJECTS_ID RA DEC MAG_AUTO MAGERR_AUTO MAG_PSF MAGERR_PSF BAND EXPTIME'),comments='')
        #np.savetxt('%s/%i/SDSS_data.tab'%(DB_path,DBID),np.array(SDF)[gid],fmt=('%f %f %f %i %i %f %f %f %f %f %f %f %f %f %f%i %i %i %i %i %i %i'),header=('MJD RA DEC OBJID NUMROW PSFMAG_U  PSFMAG_G  PSFMAG_R  PSFMAG_I  PSFMAG_Z  PSFMAGERR_U  PSFMAGERR_G  PSFMAGERR_R  PSFMAGERR_I  PSFMAGERR_Z RUN RERUN STRIPE THINGID MQ_ROWNUM COADD_OBJECTS_UD HPIX'),comments='')
        dbi_out=np.append(dbi_out,np.array([DBID,curid,0,cr['sdr7id'][gid][0]]))
    print DBID, curid
np.savetxt('/home/rumbaugh/var_database/database_index.dat',dbi_out,fmt='%i %i %i %i',header='DatabaseID Y1A1_COADD_OBJECTS_ID SDSS_DR13_thindid SDR7ID')
