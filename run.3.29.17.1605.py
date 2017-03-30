import numpy as np
import pyfits as py
import easyaccess as ea
con=ea.connect()
outputdir,DBdir='/home/rumbaugh/var_database/Y3A1','/home/rumbaugh/var_database/Y3A1'

crm=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)
crm2=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.28.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
np.savetxt('/home/rumbaugh/databaseIDs.csv',crdb,fmt='%s,%s,%i,%i,%s,%i,%s,%i,%s',header='DatabaseID,DBIDS,MQrownum,SP_rownum,sdr7id,thingid,SDSSNAME,CID,TILENAME',comments='')
crm=crm[crdb['SDSSNAME']!='-1']
crm2=crm2[crdb['SDSSNAME']!='-1']
crdb=crdb[crdb['SDSSNAME']!='-1']

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data

cr=np.loadtxt('/home/rumbaugh/gemini_target',dtype={'names':('DR7ID','SDSSNAME','ra','dec','z','FIRST','lastgmjd','gmag','lastimjd','imag','S82ID','DBID'),'formats':('i8','|S24','f8','f8','f8','i8','i8','f8','i8','f8','i8','|S24')})

outcr=np.zeros((len(cr),),dtype={'names':('ra','dec','SDSSNAME'),'formats':('f8','f8','|S24')})
outcr['ra'],outcr['dec'],outcr['SDSSNAME']=cr['ra'],cr['dec'],cr['SDSSNAME']
np.savetxt('/home/rumbaugh/radecname_forcutouts.gemini.tab',outcr,fmt='%f,%f,%s')

outcr=np.zeros((len(cr),),dtype={'names':('ra','dec'),'formats':('f8','f8')})
outcr['ra'],outcr['dec']=cr['ra'],cr['dec']
np.savetxt('/home/rumbaugh/radec_forcutouts.gemini.tab',outcr,fmt='%f,%f')

crmac=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_Macleod_S82_match.dat',dtype={'names':('DBID','MCID'),'formats':('|S24','|S24')},skiprows=1)

outcr=np.zeros((len(cr),),dtype={'names':('DR7ID','SDSSNAME','ra','dec','z','FIRST','lastgmjd','gmag','lastimjd','imag','S82ID','DBID'),'formats':('|S16','|S24','f8','f8','f8','i8','i8','f8','i8','f8','i8','|S24')})
for i in range(0,len(outcr)):
    DBID=cr['DBID'][i]
    crlc=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    gg,gi=np.where(crlc['BAND']=='g')[0],np.where(crlc['BAND']=='i')[0]
    gsort,isort=np.argsort(crlc['MJD'][gg]),np.argsort(crlc['MJD'][gi])
    gmac=np.where(crmac['DBID']==DBID)[0][0]
    gmf=np.where(data['DatabaseID']==DBID)[0][0]
    gdb=np.where(crdb['DatabaseID']==DBID)[0][0]
    outcr['DR7ID'][i],outcr['SDSSNAME'][i],outcr['ra'][i],outcr['dec'][i],outcr['z'][i],outcr['FIRST'][i],outcr['lastgmjd'][i],outcr['gmag'][i],outcr['lastimjd'][i],outcr['imag'][i],outcr['S82ID'][i]=crdb['sdr7id'][gdb],crdb['SDSSNAME'][gdb],data['RA_SDSS'][gmf],data['Dec_SDSS'][gmf],data['Redshift'][gmf],0,crlc['MJD'][gg[gsort[-1]]],crlc['MAG'][gg[gsort[-1]]],crlc['MJD'][gi[isort[-1]]],crlc['MAG'][gi[isort[-1]]],crmac['MCID'][gmac]
    
np.savetxt('/home/rumbaugh/gemcheck.dat',outcr,fmt='%7s %24s %10.6f %10.6f %7.5f %2i %5i %6.3f %5i %6.3f %8i %10s',header='DR7ID SDSSNAME ra dec z FIRST lastgmjd gmag lastimjd imag S82ID DBID')



qry='SELECT g.DR7ID,g.SDSS_NAME,g.DBID,y.SPREAD_MODEL_G,y.SPREADERR_MODEL_G,y.SPREAD_MODEL_R,y.SPREADERR_MODEL_R,y.SPREAD_MODEL_I,y.SPREADERR_MODEL_I,y.SPREAD_MODEL_Z,y.SPREADERR_MODEL_Z,y.SPREAD_MODEL_Y,y.SPREADERR_MODEL_Y FROM RUMBAUGH.GEMINI_TARGET g,DES_ADMIN.Y3A1_COADD_OBJECT_SUMMARY y,RUMBAUGH.DATABASEIDS d WHERE y.COADD_OBJECT_ID=d.CID AND d.DATABASEID=g.DBID'
DF=con.query_to_pandas(qry)
DF=np.array(DF,dtype={'names':('DR7ID','SDSS_NAME','DBID','SPREAD_MODEL_G','SPREAD_MODEL_G_ERR','SPREAD_MODEL_R','SPREAD_MODEL_R_ERR','SPREAD_MODEL_I','SPREAD_MODEL_I_ERR','SPREAD_MODEL_Z','SPREAD_MODEL_Z_ERR','SPREAD_MODEL_Y','SPREAD_MODEL_Y_ERR'),'formats':('i8','|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
gs=np.argsort(DF['DR7ID'])
outcr=DF[gs]
np.savetxt('/home/rumbaugh/gemini.spread_model.dat',outcr,fmt='%i %s %s %f %f %f %f %f %f %f %f %f %f',header='DR7ID SDSS_NAME DBID SPREAD_MODEL_G SPREAD_MODEL_G_ERR SPREAD_MODEL_R SPREAD_MODEL_R_ERR SPREAD_MODEL_I SPREAD_MODEL_I_ERR SPREAD_MODEL_Z SPREAD_MODEL_Z_ERR SPREAD_MODEL_Y SPREAD_MODEL_Y_ERR')
