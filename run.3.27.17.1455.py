import numpy as np
execfile('/home/rumbaugh/pythonscripts/StructureFunction.py')
outputdir='/home/rumbaugh/var_database/Y3A1'
nbins=10


hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data 

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]
crm=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)
crm=crm[gdr]

crmd=crm[np.abs(crm['drop'])>1]

hduc=py.open('/home/rumbaugh/dr7_control.fits')
cdata=hduc[1].data
cz,cname,cL=cdata['REDSHIFT'],cdata['SDSS_NAME'],cdata['LOGLBOL']

gc=np.zeros(len(cdata),dtype='i8')
for i in range(0,len(gc)): 
    try:
        gc[i]=np.where(crdb['SDSSNAME']==cname[i])[0][0]
    except IndexError:
        gc[i]=-1
gc=gc[gc>-1]


DBIDs=crdb['DatabaseID'][gc]
np.savetxt('/home/rumbaugh/dr7_control_dbids.dat',DBIDs,fmt='%s')
for DBID in np.intersect1d(DBIDs,crdb['DatabaseID'][np.abs(crm['drop'])>1]):
    gmf=np.where(data['DatabaseID']==DBID)[0][0]
    redshift=data['Redshift'][gmf]
    cr=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    crout=np.loadtxt('%s/%s/outliers.tab'%(DBdir,DBID),dtype='i8')
    try:
        crmac=np.loadtxt('%s/%s/Macleod_LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('|S24','f8','f8','f8','|S4','f8','f8','i8')})
        croutmac=np.loadtxt('%s/%s/outliers_Macleod.tab'%(DBdir,DBID),dtype='i8')
        crmac=crmac[croutmac>-1]
        croutmac=croutmac[croutmac>-1]
        outlier_arr=np.array(np.append(crout,croutmac),dtype='bool')
    except:
        crmac=None
        outlier_arr=np.array(crout,dtype='bool')
    if crmac!=None:
        newcr=np.zeros((len(cr),),dtype={'names':('DatabaseID','Survey','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('|S24','|S4','f8','f8','f8','|S4','f8','f8','i8')})
        newcr['DatabaseID'],newcr['Survey'],newcr['RA'],newcr['DEC'],newcr['MJD'],newcr['BAND'],newcr['MAG'],newcr['MAGERR'],newcr['FLAG']=cr['DatabaseID'],cr['Survey'],cr['RA'],cr['DEC'],cr['MJD'],cr['BAND'],cr['MAG'],cr['MAGERR'],cr['FLAG']
        newcrmac=np.zeros((len(crmac),),dtype={'names':('DatabaseID','Survey','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('|S24','|S4','f8','f8','f8','|S4','f8','f8','i8')})
        newcrmac['DatabaseID'],newcrmac['Survey'],newcrmac['RA'],newcrmac['DEC'],newcrmac['MJD'],newcrmac['BAND'],newcrmac['MAG'],newcrmac['MAGERR'],newcrmac['FLAG']=crmac['DatabaseID'],np.full(len(crmac),'SDSS',dtype='|S4'),crmac['RA'],crmac['DEC'],crmac['MJD'],crmac['BAND'],crmac['MAG'],crmac['MAGERR'],crmac['FLAG']
        cr=np.append(newcr,newcrmac)
    gorig=np.arange(len(cr))[(cr['MAG']>14)&(cr['MAG']<30)&(cr['MAGERR']<5)]
    cr=cr[(cr['MAG']>14)&(cr['MAG']<30)&(cr['MAGERR']<5)]
    outlier_arr=outlier_arr[gorig]
    cr=cr[outlier_arr==0]
    mjd,mag,magerr=cr['MJD'],cr['MAG'],cr['MAGERR']
    flux=10**(mag/-2.5+10)
    fluxerr=np.log(10)/-2.5*flux*magerr
    mjdmin=np.min(mjd)
    mjd=mjdmin+(mjd-mjdmin)/(1+redshift)
    SF1,SF2,SF3,SF4,SF5=CalcStructureFunction_eq14(flux,mjd,nbins=nbins),CalcStructureFunction_eq15(flux,mjd,fluxerr,nbins=nbins),CalcStructureFunction_eq16(flux,mjd,fluxerr,nbins=nbins),CalcStructureFunction_eq17(flux,mjd,nbins=nbins),CalcStructureFunction_eq18(flux,mjd,fluxerr,nbins=nbins)
    outcr=np.zeros((nbins,),dtype={'names':('tau','SF1','SF2','SF3','SF4','SF5'),'formats':('f8','f8','f8','f8','f8','f8')})
    outcr['tau'],outcr['SF1'],outcr['SF2'],outcr['SF3'],outcr['SF4'],outcr['SF5']=SF1[0],SF1[1],SF2[1],SF3[1],SF4[1],SF5[1]
    np.savetxt('%s/%s/SF.tab'%(outputdir,DBID),outcr,fmt='%f %f %f %f %f %f')
