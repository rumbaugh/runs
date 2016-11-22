import numpy as np
import pyfits as py
DB_path='/home/rumbaugh/var_database'

crsp=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EpochG','EpochR','EpochI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_r_SDSS','g_SDSS','g_ERR','r_SDSS','r_ERR','i_SDSS','i_ERR'),'formats':('f8','f8','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','f8','f8','|S12','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8')})

inDES_SPs=np.array([18615,18644,32529,32528,32526,32534,18463,18322,18416])

double_count_indexes=np.zeros(0,dtype='|S30')

crdb=np.loadtxt('/home/rumbaugh/var_database/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id'),'formats':('i8','i8','i8','i8')})
#crdb=crdb[:100]

dblen=len(crdb)

Survey=np.zeros(dblen,dtype='|S20')
Survey[:]='DES'
Survey[crdb['thingid']>0]='DES;SDSS'
Survey[(crdb['CID']>0)&(crdb['sdr7id']!=0)]='DES;SDSS;POSS'
Survey[(crdb['CID']<=0)&(crdb['sdr7id']!=0)]='SDSS;POSS'
CIDout=np.copy(crdb['CID'])
MJDrange,redshifts,s82=np.zeros(dblen),np.zeros(dblen),np.zeros(dblen,dtype='i8')
raDES,decDES,raSDSS,decSDSS,raPOSS,decPOSS=np.zeros(dblen),np.zeros(dblen),np.zeros(dblen),np.zeros(dblen),np.zeros(dblen),np.zeros(dblen)
numDES_g,numDES_r,numDES_i,numDES_z,numDES_Y,numSDSS_g,numSDSS_r,numSDSS_i,numSDSS_z,numSDSS_u=np.zeros(dblen,dtype='i8'),np.zeros(dblen,dtype='i8'),np.zeros(dblen,dtype='i8'),np.zeros(dblen,dtype='i8'),np.zeros(dblen,dtype='i8'),np.zeros(dblen,dtype='i8'),np.zeros(dblen,dtype='i8'),np.zeros(dblen,dtype='i8'),np.zeros(dblen,dtype='i8'),np.zeros(dblen,dtype='i8')
medDES_g,medDES_r,medDES_i,medDES_z,medDES_Y,medSDSS_g,medSDSS_r,medSDSS_i,medSDSS_z,medSDSS_u=np.zeros(dblen),np.zeros(dblen),np.zeros(dblen),np.zeros(dblen),np.zeros(dblen),np.zeros(dblen),np.zeros(dblen),np.zeros(dblen),np.zeros(dblen),np.zeros(dblen)
medPOSS_g,medPOSS_r,medPOSS_i=np.zeros(dblen),np.zeros(dblen),np.zeros(dblen)
for DBID in crdb['DBID']:
    db_cr=np.loadtxt('%s/%i/LC.tab'%(DB_path,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    MJDrange[DBID]=np.max(db_cr['MJD'])-np.min(db_cr['MJD'])
    gdes=np.where(db_cr['Survey']=='DES')[0]
    try:
        numDES_g[DBID],numDES_r[DBID],numDES_i[DBID],numDES_z[DBID],numDES_Y[DBID]=len(gdes[db_cr['BAND'][gdes]=='g']),len(gdes[db_cr['BAND'][gdes]=='r']),len(gdes[db_cr['BAND'][gdes]=='i']),len(gdes[db_cr['BAND'][gdes]=='z']),len(gdes[db_cr['BAND'][gdes]=='Y'])
        medDES_g[DBID],medDES_r[DBID],medDES_i[DBID],medDES_z[DBID],medDES_Y[DBID]=np.median(db_cr['MAG'][gdes][db_cr['BAND'][gdes]=='g']),np.median(db_cr['MAG'][gdes][db_cr['BAND'][gdes]=='r']),np.median(db_cr['MAG'][gdes][db_cr['BAND'][gdes]=='i']),np.median(db_cr['MAG'][gdes][db_cr['BAND'][gdes]=='z']),np.median(db_cr['MAG'][gdes][db_cr['BAND'][gdes]=='Y'])
        raDES[DBID],decDES[DBID]=np.mean(db_cr['RA'][gdes]),np.mean(db_cr['DEC'][gdes])
    except IndexError:
        numDES_g[DBID],numDES_r[DBID],numDES_i[DBID],numDES_z[DBID],numDES_Y[DBID]=len(gdes[np.array([db_cr['BAND']])[gdes]=='g']),len(gdes[np.array([db_cr['BAND']])[gdes]=='r']),len(gdes[np.array([db_cr['BAND']])[gdes]=='i']),len(gdes[np.array([db_cr['BAND']])[gdes]=='z']),len(gdes[np.array([db_cr['BAND']])[gdes]=='Y'])
        medDES_g[DBID],medDES_r[DBID],medDES_i[DBID],medDES_z[DBID],medDES_Y[DBID]=np.median(np.array([db_cr['MAG']])[gdes][np.array([db_cr['BAND']])[gdes]=='g']),np.median(np.array([db_cr['MAG']])[gdes][np.array([db_cr['BAND']])[gdes]=='r']),np.median(np.array([db_cr['MAG']])[gdes][np.array([db_cr['BAND']])[gdes]=='i']),np.median(np.array([db_cr['MAG']])[gdes][np.array([db_cr['BAND']])[gdes]=='z']),np.median(np.array([db_cr['MAG']])[gdes][np.array([db_cr['BAND']])[gdes]=='Y'])
        raDES[DBID],decDES[DBID]=np.mean(np.array([db_cr['RA']])[gdes]),np.mean(np.array([db_cr['DEC']])[gdes])
        
    if crdb['thingid'][DBID]>0:
        gsdss=np.where(db_cr['Survey']=='SDSS')[0]
        numSDSS_g[DBID],numSDSS_r[DBID],numSDSS_i[DBID],numSDSS_z[DBID],numSDSS_u[DBID]=len(gsdss[db_cr['BAND'][gsdss]=='g']),len(gsdss[db_cr['BAND'][gsdss]=='r']),len(gsdss[db_cr['BAND'][gsdss]=='i']),len(gsdss[db_cr['BAND'][gsdss]=='z']),len(gsdss[db_cr['BAND'][gsdss]=='u'])
        medSDSS_g[DBID],medSDSS_r[DBID],medSDSS_i[DBID],medSDSS_z[DBID],medSDSS_u[DBID]=np.median(db_cr['MAG'][gsdss][db_cr['BAND'][gsdss]=='g']),np.median(db_cr['MAG'][gsdss][db_cr['BAND'][gsdss]=='r']),np.median(db_cr['MAG'][gsdss][db_cr['BAND'][gsdss]=='i']),np.median(db_cr['MAG'][gsdss][db_cr['BAND'][gsdss]=='z']),np.median(db_cr['MAG'][gsdss][db_cr['BAND'][gsdss]=='u'])
        crsdss=np.loadtxt('%s/%i/SDSS_data.tab'%(DB_path,DBID),dtype={'names':('MJD','RA','DEC','OBJID','NUMROW','PSFMAG_U','PSFMAG_G','PSFMAG_R','PSFMAG_I','PSFMAG_Z','PSFMAGERR_U','PSFMAGERR_G','PSFMAGERR_R','PSFMAGERR_I','PSFMAGERR_Z','RUN','STRIPE','THINGID','MQ_ROWNUM','COADD_OBJECTS_ID','HPIX'),'formats':('f8','f8','f8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','i8','i8','i8','i8','i8')},skiprows=1)
        if 82 in crsdss['STRIPE']: s82[DBID]=1
        raSDSS[DBID],decSDSS[DBID]=np.mean(db_cr['RA'][gsdss]),np.mean(db_cr['DEC'][gsdss])
    if crdb['sdr7id'][DBID]!=0:
        gsp=np.where(crsp['SDR7ID']==crdb['sdr7id'][DBID])[0]
        if len(gsp)>1:
            if crsp['SDR7ID'][gsp][0] in double_count_indexes:
                curcnt=len(double_count_indexes[double_count_indexes==crsp['SDR7ID'][gsp][0]])
                gsp=gsp[curcnt]
                double_count_indexes=np.append(double_count_indexes,crsp['SDR7ID'][gsp])
            else:
                gsp=gsp[0]
                double_count_indexes=np.append(double_count_indexes,crsp['SDR7ID'][gsp])
        else:
            gsp=gsp[0]
        if gsp in inDES_SPs: CIDout[DBID]=-1
        gsdss=np.where(db_cr['Survey']=='SDSS')[0]
        gposs=np.where(db_cr['Survey']=='POSS')[0]
        if crdb['thingid'][DBID]<=0: 
            numSDSS_g[DBID],numSDSS_r[DBID],numSDSS_i[DBID]=1,1,1
            medSDSS_g,medSDSS_r,medSDSS_i=db_cr['MAG'][gsdss][db_cr['BAND'][gsdss]=='g'][0],db_cr['MAG'][gsdss][db_cr['BAND'][gsdss]=='r'][0],db_cr['MAG'][gsdss][db_cr['BAND'][gsdss]=='i'][0]
            medPOSS_g[DBID],medPOSS_r[DBID],medPOSS_i[DBID]=db_cr['MAG'][gposs][db_cr['BAND'][gposs]=='g'][0],db_cr['MAG'][gposs][db_cr['BAND'][gposs]=='r'][0],db_cr['MAG'][gposs][db_cr['BAND'][gposs]=='i'][0]
            s82[DBID]=crdb['s82flag'][gsp][0]
        if crdb['cid']<=0:
            redshifts[DBID]=crsp['redshift'][gsp][0]
        raPOSS[DBID],decPOSS[DBID]=crsp['ra'][gsp][0],crsp['dec'][gsp][0]
colDBID,colSurvey,colCID,coltid,colsdr7id,colMJDrange,colredshifts,cols82,colraDES,coldecDES,colraSDSS,coldecSDSS,colraPOSS,coldecPOSS,colnumDES_g,colnumDES_r,colnumDES_i,colnumDES_z,colnumDES_Y,colnumSDSS_g,colnumSDSS_r,colnumSDSS_i,colnumSDSS_z,colnumSDSS_u,colmedDES_g,colmedDES_r,colmedDES_i,colmedDES_z,colmedDES_Y,colmedSDSS_g,colmedSDSS_r,colmedSDSS_i,colmedSDSS_z,colmedSDSS_u=py.Column(name='DatabaseID',format='I',array=crdb['DBID']),py.Column(name='Survey',format='A20',array=Survey),py.Column(name='Y1A1_CoaddObjectsID',format='I',array=CIDout),py.Column(name='DR13_thingid',format='I',array=crdb['thingid']),py.Column(name='sdr7id',format='I',array=crdb['sdr7id']),py.Column(name='MaxBaseline',format='D',array=MJDrange),py.Column(name='Redshift',format='E',array=redshifts),py.Column(name='Stripe82',format='I',array=s82),py.Column(name='RA_DES',format='E',array=raDES),py.Column(name='Dec_DES',format='E',array=decDES),py.Column(name='RA_SDSS',format='E',array=raSDSS),py.Column(name='Dec_SDSS',format='E',array=decSDSS),py.Column(name='RA_POSS',format='E',array=raPOSS),py.Column(name='Dec_POSS',format='E',array=decPOSS),py.Column(name='Epochs_DES_g',format='D',array=numDES_g),py.Column(name='Epochs_DES_r',format='D',array=numDES_r),py.Column(name='Epochs_DES_i',format='D',array=numDES_i),py.Column(name='Epochs_DES_z',format='D',array=numDES_z),py.Column(name='Epochs_DES_Y',format='D',array=numDES_Y),py.Column(name='Epochs_SDSS_g',format='D',array=numSDSS_g),py.Column(name='Epochs_SDSS_r',format='D',array=numSDSS_r),py.Column(name='Epochs_SDSS_i',format='D',array=numSDSS_i),py.Column(name='Epochs_SDSS_z',format='D',array=numSDSS_z),py.Column(name='Epochs_SDSS_u',format='D',array=numSDSS_u),py.Column(name='med_DES_g',format='D',array=medDES_g),py.Column(name='med_DES_r',format='D',array=medDES_r),py.Column(name='med_DES_i',format='D',array=medDES_i),py.Column(name='med_DES_z',format='D',array=medDES_z),py.Column(name='med_DES_Y',format='D',array=medDES_Y),py.Column(name='med_SDSS_g',format='D',array=medSDSS_g),py.Column(name='med_SDSS_r',format='D',array=medSDSS_r),py.Column(name='med_SDSS_i',format='D',array=medSDSS_i),py.Column(name='med_SDSS_z',format='D',array=medSDSS_z),py.Column(name='med_SDSS_u',format='D',array=medSDSS_u)
cols=py.ColDefs([colDBID,colSurvey,colCID,coltid,colsdr7id,colMJDrange,colredshifts,cols82,colraDES,coldecDES,colraSDSS,coldecSDSS,colraPOSS,coldecPOSS,colnumDES_g,colnumDES_r,colnumDES_i,colnumDES_z,colnumDES_Y,colnumSDSS_u,colnumSDSS_g,colnumSDSS_r,colnumSDSS_i,colnumSDSS_z,colmedDES_g,colmedDES_r,colmedDES_i,colmedDES_z,colmedDES_Y,colmedSDSS_u,colmedSDSS_g,colmedSDSS_r,colmedSDSS_i,colmedSDSS_z])
tbhdu=py.BinTableHDU.from_columns(cols)
tbhdu.writeto('/home/rumbaugh/var_database/masterfile.fits',clobber=True)
