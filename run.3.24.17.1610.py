import numpy as np
execfile('/home/rumbaugh/pythonscripts/StructureFunction.py')

nbins=10

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]
crm=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)
crm=crm[gdr]

crmd=crm[np.abs(crm['drop'])>1]

for DBID in crmd['DBID']:
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
    SF1,SF2,SF3,SF4,SF5=CalcStructureFunction_eq14(mag,mjd,nbins=nbins),CalcStructureFunction_eq15(mag,mjd,magerr,nbins=nbins),CalcStructureFunction_eq16(mag,mjd,magerr,nbins=nbins),CalcStructureFunction_eq17(mag,mjd,nbins=nbins),CalcStructureFunction_eq18(mag,mjd,magerr,nbins=nbins)
    outcr=np.zeros((nbins,),dtype={'names':('tau','SF1','SF2','SF3','SF4','SF5'),'formats':('f8','f8','f8','f8','f8','f8')})
    outcr['tau'],outcr['SF1'],outcr['SF2'],outcr['SF3'],outcr['SF4'],outcr['SF5']=SF1[:,0],SF1[:,1],SF2[:,1],SF3[:,1],SF4[:,1],SF5[:,1]
    np.savetxt('%s/%s/SF.tab'%(outputdir,DBID),outcr,fmt='%f %f %f %f %f %f')
