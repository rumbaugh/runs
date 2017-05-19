import numpy as np
import pyfits as py
import os
execfile('/home/rumbaugh/pythonscripts/angconvert.py')
execfile('/home/rumbaugh/pythonscripts/SphDist.py')
DB_path='/home/rumbaugh/var_database/Y3A1'
os.chdir(DB_path) 
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
POSSbands=np.array(['g','r','i'])
execfile('/home/rumbaugh/pythonscripts/SphDist.py')

mac_thresh=5.

def make_cid_dict(incr,col='cid'):
    tdict={}
    for i,cid in zip(np.arange(0,len(incr)),incr[col]):
        try:
            tdict[cid]=np.append(tdict[cid],i)
        except KeyError:
            tdict[cid]=np.array([i])
    return tdict

fmt_dict={'i8': 'K','<i': 'D','i4': 'D','f8': 'E', '|S': 'A', 'int64': 'K', 'int32':'D','float64': 'E'}
def make_hdu(arr):
    colarr=[]
    for name in arr.dtype.names: 
        dfmt=np.str(arr.dtype[name])
        try:
            fmt=fmt_dict[dfmt]
        except KeyError:
            fmt=fmt_dict[dfmt[:2]]
        if fmt=='A': fmt='A%s'%dfmt[2:]
        colarr+=[py.Column(name=name,format=fmt,array=arr[name])]
    cols=py.ColDefs(colarr)
    tbhdu=py.BinTableHDU.from_columns(cols)
    return tbhdu

try:
    doload
except NameError:
    doload=True
if doload:
    hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
    bhdata=hdubh[1].data
    bhz,bhname=bhdata['REDSHIFT'],bhdata['SDSS_NAME']
    gbh_dict={bhname[x]: x for x in range(0,len(bhname))}

    bhRAdict,bhDECdict={bhname[x]: bhdata['RA'][x] for x in range(len(bhdata))},{bhname[x]: bhdata['DEC'][x] for x in range(len(bhdata))}

    fname='/home/rumbaugh/Downloads/milliquas.txt'
    mdict={'names':('RA','DEC','Name','Descrip','Rmag','Bmag','Comment','R','B','Z','Cite','Zcite','Qpct','Xname','Rname','Lobe1','Lobe2'),'formats':('f8','f8','|S27','|S5','f8','f8','|S4','|S2','|S2','f8','|S7','|S7','f8','|S24','|S24','|S24','|S24')}
    delims=(11,12,27,5,5,5,4,2,2,7,7,7,4,23,23,23,23)
    crmq=np.genfromtxt(fname,dtype=mdict,delimiter=delims)
    mqRAdict,mqDECdict={x: crmq['RA'][x] for x in range(len(crmq))},{x: crmq['DEC'][x] for x in range(len(crmq))}

    crch=np.loadtxt('/home/rumbaugh/dr7_bh_y3a1_match_closechanges.csv',dtype={'names':('SDSSNAME','RA','DEC','HPIX','CID'),'formats':('|S24','f8','f8','i8','i8')},skiprows=1,delimiter=',')
    for i in range(0,len(crch)): crch['SDSSNAME'][i]=crch['SDSSNAME'][i].strip()

    double_count_indexes=np.zeros(0,dtype='|S30')

    crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SPrownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})

    crsp=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EpochG','EpochR','EpochI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_r_SDSS','g_SDSS','g_ERR','r_SDSS','r_ERR','i_SDSS','i_ERR'),'formats':('f8','f8','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S12','f8','f8','|S12','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8')})
    spRAdict,spDECdict={crsp['SDR7ID'][x]: crsp['ra'][x] for x in range(0,len(crsp))},{crsp['SDR7ID'][x]: crsp['dec'][x] for x in range(0,len(crsp))}


    crmi=np.loadtxt('/home/rumbaugh/var_database/Y3A1/match_index.dat',dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('i8','i8','|S32','f8','f8','i8','i8','|S32')},skiprows=1)
    gcrmi_match=np.where(crmi['COADD_OBJECTS_ID']>0)[0]
    crmim=crmi[gcrmi_match]
    mihdu=make_hdu(crmi)

mastercr=np.zeros((len(crmim),),dtype={'names':('DatabaseID','Survey','Y3A1_CoaddObjectsID','DR13_thingid','sdr7id','SDSSNAME','MQ_ROWNUM','SP_ROWNUM','MaxBaseline','Redshift','Stripe82','RA_DES','Dec_DES','RA_SDSS','Dec_SDSS','RA_POSS','Dec_POSS','Epochs_DES_g','Epochs_DES_r','Epochs_DES_i','Epochs_DES_z','Epochs_DES_Y','Epochs_SDSS_g','Epochs_SDSS_r','Epochs_SDSS_i','Epochs_SDSS_z','Epochs_SDSS_u','med_DES_g','med_DES_r','med_DES_i','med_DES_z','med_DES_Y','med_SDSS_g','med_SDSS_r','med_SDSS_i','med_SDSS_z','med_SDSS_u','med_POSS_g','med_POSS_r','med_POSS_i','MQ_Descrip','MQ_QPct','Y3A1TILE','OldDatabaseID'),'formats':('|S40','|S20','i8','i8','|S20','|S40','i8','i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','<i4','<i4','<i4','<i4','<i4','<i4','<i4','<i4','<i4','<i4','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S6','f8','|S40','|S40')})
mastercr['sdr7id'],mastercr['SDSSNAME'],mastercr['MQ_ROWNUM'],mastercr['SP_ROWNUM']=-1,'-1',-1,-1

crmim=crmim[:10]
for cid,MQrn,SPrn,SDSSNAME,imi,TILENAME in zip(crmim['COADD_OBJECTS_ID'],crmim['MQ_ROWNUM'],crmim['SP_ROWNUM'],crmim['SDSS_NAME'],np.arange(len(crmim)),crmim['TILENAME']):
    inSN=False
    outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','SPREAD','SPREADERR'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','f8','f8')})
    Y3A1outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','SPREAD','SPREADERR'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','f8','f8')})
    DR13outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','SPREAD','SPREADERR'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','f8','f8')})
    oldDBID=None
    DBID=None
    if MQrn!=-1:
        try:
            MQRA,MQDEC=mqRAdict[MQrn],mqDECdict[MQrn]
            mqrah,mqram,mqras=deg2hms(MQRA)
            mqdecd,mqdecm,mqdecs=deg2dms(MQDEC)
            DBID='%02i%02i%02i%+03i%02i%02i'%(mqrah,mqram,mqras,mqdecd,mqdecm,int(mqdecs))
            if oldDBID==None:oldDBID='MQ%i'%MQrn
        except KeyError:
            MQRA,MQDEC=0,0
    if SDSSNAME!='-1':
        gbh=gbh_dict[SDSSNAME]
        try:
            BHRA,BHDEC=bhRAdict[BHrn],bhDECdict[BHrn]
            bhrah,bhram,bhras=deg2hms(BHRA)
            bhdecd,bhdecm,bhdecs=deg2dms(BHDEC)
            DBID='%02i%02i%02i%+03i%02i%02i'%(bhrah,bhram,bhras,bhdecd,bhdecm,int(bhdecs))
            if oldDBID==None:oldDBID='BH%i'%BHrn
        except KeyError:
            BHRA,BHDEC=0,0
    if SPrn!=-1:
        curdr7=crsp['SDR7ID'][SPrn]
        try:
            SPRA,SPDEC=spRAdict[curdr7],spDECdict[curdr7]
            sprah,spram,spras=deg2hms(SPRA)
            spdecd,spdecm,spdecs=deg2dms(SPDEC)
            if DBID==None:DBID='%02i%02i%02i%+03i%02i%02i'%(sprah,spram,spras,spdecd,spdecm,int(spdecs))
            if oldDBID==None:oldDBID='SDSSPOSS%i'%SPrn
        except KeyError:
            SPRA,SPDEC=0,0
    os.system('ln -sf %s %s'%(oldDBID,DBID))
    cr=np.loadtxt('%s/%s/LC.tab'%(DB_path,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    if np.shape(cr)==():
        mjd,mag,magerr,bands,survey=np.array([cr['MJD']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['BAND']]),np.array([cr['Survey']])
        outcr=np.zeros((1,),dtype={'names':('Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','OUTLIER'),'formats':('|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','i8')})
        outcr['Survey'],outcr['SurveyCoaddID'],outcr['SurveyObjectID'],outcr['RA'],outcr['DEC'],outcr['MJD'],outcr['TAG'],outcr['BAND'],outcr['MAGTYPE'],outcr['MAG'],outcr['MAGERR'],outcr['FLAG']=np.array([cr['Survey']]),np.array([cr['SurveyCoaddID']]),np.array([cr['SurveyObjectID']]),np.array([cr['RA']]),np.array([cr['DEC']]),np.array([cr['MJD']]),np.array([cr['TAG']]),np.array([cr['BAND']]),np.array([cr['MAGTYPE']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['FLAG']])
    else:
        outcr=np.zeros((len(cr),),dtype={'names':('Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','OUTLIER'),'formats':('|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','i8')})
        outcr['Survey'],outcr['SurveyCoaddID'],outcr['SurveyObjectID'],outcr['RA'],outcr['DEC'],outcr['MJD'],outcr['TAG'],outcr['BAND'],outcr['MAGTYPE'],outcr['MAG'],outcr['MAGERR'],outcr['FLAG']=cr['Survey'],cr['SurveyCoaddID'],cr['SurveyObjectID'],cr['RA'],cr['DEC'],cr['MJD'],cr['TAG'],cr['BAND'],cr['MAGTYPE'],cr['MAG'],cr['MAGERR'],cr['FLAG']
        mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
    outcr['TAG'][outcr['SurveyObjectID']==0]='SN'
    try:
        crout=np.loadtxt('%s/%s/outliers.tab'%(DB_path,DBID),dtype='i8')
        outcr['OUTLIER']=crout
        outcr['OUTLIER'][(crout==0)&(outcr['BAND']=='g')]=-1
    except IOError:
        crout=np.zeros(len(cr))
    try:
        crmac=np.loadtxt('%s/%s/Macleod_LC.tab'%(DB_path,DBID),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('|S24','f8','f8','f8','|S4','f8','f8','i8')})
        outcrmac['Survey'],outcrmac['SurveyCoaddID'],outcrmac['SurveyObjectID'],outcrmac['RA'],outcrmac['DEC'],outcrmac['MJD'],outcrmac['TAG'],outcrmac['BAND'],outcrmac['MAGTYPE'],outcrmac['MAG'],outcrmac['MAGERR'],outcrmac['FLAG']=crmac['Survey'],crmac['SurveyCoaddID'],crmac['SurveyObjectID'],crmac['RA'],crmac['DEC'],crmac['MJD'],crmac['TAG'],crmac['BAND'],crmac['MAGTYPE'],crmac['MAG'],crmac['MAGERR'],crmac['FLAG']
        try:
            croutmac=np.loadtxt('%s/%s/outliers_Macleod.tab'%(DB_path,DBID),dtype='i8')
            outcrmac['OUTLIER']=croutmac
        except IOError:
            croutmac=np.zeros(0)
            outcrmac['OUTLIER'][(croutmac==0)&(outcrmac['BAND']=='g')]=-1
            outcrmac=np.zeros((len(crmac),),dtype={'names':('Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','OUTLIER'),'formats':('|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','i8')})
        appmac_dict={}
        mac=True
        for b in ['g','r','i','z','u']:
            gb=np.where(bands==b)[0]
            gbmac=np.where(crmac['BAND']==b)[0]
            if len(gb)>0:
                gb0=np.where((cr['BAND']==b)&(cr['MJD']>np.min(crmac['MJD'])-30)&(cr['MJD']<np.max(crmac['MJD'])+30))[0]
                if ((len(gb0)>0)&(len(gbmac)>0)):
                    mjd0,mjdmac=cr['MJD'][gb0],crmac['MJD'][gbmac]
                mjddists=np.abs(mjdmac.reshape((len(mjdmac),1))-mjd0.reshape((1,len(mjd0)))*np.ones((len(mjdmac),1)))
                mindists=np.min(mjddists,axis=1)
                gmac2=np.where(mindists>mac_thresh)[0]
            else:
                gmac2=np.arange(len(gbmac))
            crappmac=np.zeros((len(gmac2),),dtype={'names':('Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','OUTLIER'),'formats':('|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','i8')})
            crappmac['Survey'],crappmac['SurveyCoaddID'],crappmac['RA'],crappmac['DEC'],crappmac['MJD'],crappmac['TAG'],crappmac['BAND'],crappmac['MAGTYPE'],crappmac['MAG'],crappmac['MAGERR'],crappmac['OUTLIER']='SDSS',crmac['DatabaseID'][gbmac[gmac2]],crmac['RA'][gbmac[gmac2]],crmac['DEC'][gbmac[gmac2]],crmac['MJD'][gbmac[gmac2]],'MACLEOD',b,'PSF',crmac['MAG'][gbmac[gmac2]],crmac['MAGERR'][gbmac[gmac2]],croutmac[gbmac[gmac2]]
            appmac_dict[b]=crappmac
        crappmac=np.concatenate((crappmac['u'],crappmac['g'],crappmac['r'],crappmac['i'],crappmac['z']))
        crappmac['OUTLIER'][(crappmac['OUTLIER']==0)&(crappmac['BAND']=='g')]=-1
        outcr=np.concatenate((outcr,crappmac))
    except IOError:
        crmac=np.zeros(0)
        mac=False
    try:
        crdes=np.loadtxt('%s/%s/DES_data.tab'%(DB_path,DBID),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')},skiprows=1)
        if np.shape(crdes)==():
            crdestmp=np.zeros((1,),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
            crdestmp['MJD'],crdestmp['IMAGEID'],crdestmp['OBJECTID'],crdestmp['COADD_OBJECTS_ID'],crdestmp['RA'],crdestmp['DEC'],crdestmp['MAG_AUTO'],crdestmp['MAGERR_AUTO'],crdestmp['MAG_PSF'],crdestmp['MAGERR_PSF'],crdestmp['BAND']=np.array([crdestmp['MJD']]),np.array([crdestmp['IMAGEID']]),np.array([crdestmp['OBJECTID']]),np.array([crdestmp['COADD_OBJECTS_ID']]),np.array([crdestmp['RA']]),np.array([crdestmp['DEC']]),np.array([crdestmp['MAG_AUTO']]),np.array([crdestmp['MAGERR_AUTO']]),np.array([crdestmp['MAG_PSF']]),np.array([crdestmp['MAGERR_PSF']]),np.array([crdestmp['BAND']])
            crdes=crdestmp
    except IOError:
        crdes=np.zeros(0)
    prihdr = py.Header()
    prihdr['DatabaseID']=DBID
    prihdr['OldDatabaseID']=oldDBID
    prihdu = py.PrimaryHDU(header=prihdr)
    lchdu=make_hdu(outcr)
    hdulistarr=[prihdu,lchdu]
    macind,desind=99,99
    curind=2
    if mac:
        machdu=make_hdu(outcrmac)
        hdulistarr+=[outcrmac]
        macind=curind
        curind+=1
    if len(crdes)>0:
        deshdu=make_hdu(crdes)
        hdulistarr+=[deshdu]
        desind=curind
        curind+=1
    thdulist = py.HDUList(hdulistarr)
    if desind<99:
        thdulist[desind].header['COADD_OBJECT_ID']=cid
    thdulist.writeto('%s/%s/LC.fits'%(DB_path,DBID))
    for surv in np.unique(outcr['Survey']):
        mastercr['RA_%s'%surv][imi]=np.median(outcr['RA'][outcr['Survey']==surv])
        mastercr['Dec_%s'%surv][imi]=np.median(outcr['DEC'][outcr['Survey']==surv])
        tdists=SphDist(mastercr['RA_%s'%surv][imi],mastercr['Dec_%s'%surv][imi],outcr['RA'][outcr['Survey']==surv],outcr['DEC'][outcr['Survey']==surv])/60.
        if np.sort(tdists)[0]>1:
            if mastercr['RA_%s'%surv][imi]>180: 
                mastercr['RA_%s'%surv][imi]-=180
            else:
                mastercr['RA_%s'%surv][imi]+=180
            tdists=SphDist(mastercr['RA_%s'%surv][imi],mastercr['Dec_%s'%surv][imi],outcr['RA'][outcr['Survey']==surv],outcr['DEC'][outcr['Survey']==surv])/60.
            if np.sort(tdists)[0]>1: print 'median coords for %s,%s still messed up'%(DBID,surv)
        if mastercr['Survey'][imi]=='':
            mastercr['Survey'][imi]=surv
        else:
            mastercr['Survey'][imi]='%s,%s'%(mastercr['Survey'][imi],surv)
    if MQrn>-1:
        mastercr['Redshift'][imi]=bhz[MQrn]
        mastercr['MQ_Descrip'][imi], mastercr['MQ_QP'][imi]=crmq['Descrip'][MQrn].replace(' ',''),crmq['Qpct'][MQrn]
    if SPrn!=-1:
        mastercr['Redshift'][imi]=crsp['redshift'][SPrn]
    if SDSSNAME!='-1':
        master['Redshift'][imi]=bhz[gbh]
    mastercr['MaxBaseline'][imi]=np.max(outcr['MJD'])-np.min(outcr['MJD'])
    for b in np.unique(outcr['BAND'][outcr['Survey']=='DES']):
        mastercr['numDES_%s'%b][imi]=len(outcr[(outcr['Survey']=='DES')&(outcr['BAND']==b)])
        mastercr['medDES_%s'%b][imi]=np.median(outcr[(outcr['Survey']=='DES')&(outcr['BAND']==b)&(outcr['OUTLIER']<1)])
    for b in np.unique(outcr['BAND'][outcr['Survey']=='SDSS']):
        mastercr['numSDSS_%s'%b][imi]=len(outcr[(outcr['Survey']=='SDSS')&(outcr['BAND']==b)])
        mastercr['medSDSS_%s'%b][imi]=np.median(outcr[(outcr['Survey']=='SDSS')&(outcr['BAND']==b)&(outcr['OUTLIER']<1)])
    if 'SDSS' in outcr['Survey']:
        mastercr['DR13_thingid'][imi]=np.max(outcr['SurveyCoaddID'][outcr['Survey']=='SDSS'])
    if 'POSS' in outcr['Survey']:mastercr['sdr7id'][imi]=crsp['SDR7ID'][SPrn]
    mastercr['DatabaseID'][imi],mastercr['OldDatabaseID'][imi],mastercr['Y3A1_CoaddObjectsID'][imi],mastercr['SDSSNAME'][imi],mastercr['MQ_ROWNUM'][imi],mastercr['SP_ROWNUM'][imi],mastercr['Y3A1TILE'][imi]=DBID,oldDBID,cid,SDSSNAME,MQrn,SPrn,TILENAME
    if 'S82' in outcr['TAG']: mastercr['S82'][imi]=1

masterhdu=make_hdu(mastercr)

prihdu = py.PrimaryHDU()
hdulistarr=[prihdu,masterhdu,mihdu]
thdulist = py.HDUList(hdulistarr)
thdulist.writeto('%s/masterfile.fits'%(DB_path))
