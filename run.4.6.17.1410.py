import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/pythonscripts/StructureFunction.py')
outputdir='/home/rumbaugh/var_database/Y3A1'
DBdir='/home/rumbaugh/var_database/Y3A1'
nbins=15

try:
    docalc
except NameError:
    docalc=True

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

if docalc:
    DBIDs=crdb['DatabaseID'][np.abs(crm['drop'])>1]
    #DBIDs=np.intersect1d(DBIDs,crdb['DatabaseID'][np.abs(crm['drop'])>1])
    #DBIDs=DBIDs[:20]
    #DBIDs=np.array(['MQ162331','MQ162879','MQ163027','MQ163865','MQ164198','MQ164285','MQ164568','MQ165055','MQ165425'])
    #print DBIDs
    #np.savetxt('/home/rumbaugh/dr7_control_dbids.dat',DBIDs,fmt='%s')
    Sarr,ltimearr=np.zeros(0,dtype='object'),np.zeros(0,dtype='object')
    #for DBID in np.intersect1d(DBIDs,crdb['DatabaseID'][np.abs(crm['drop'])>1]):
else:
    DBIDs=[]
for DBID in DBIDs:
    print DBID
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
    #flux=10**(mag/-2.5+10)
    #fluxerr=np.log(10)/-2.5*flux*magerr
    if len(mjd)==0: continue
    mjdmin=np.min(mjd)
    mjd=mjdmin+(mjd-mjdmin)/(1+redshift)
    Sarr,ltimearr=np.append(Sarr,0),np.append(ltimearr,0)
    Sarr[-1],ltimearr[-1]=mag,mjd
tauarr,Varr=EnsembleStructureFunction_IQR(Sarr,ltimearr,binwidth=0.5,calcerror=False,ntrials=1000)

outcr=np.zeros((len(Varr),),dtype={'names':('tau','SF'),'formats':('f8','f8')})
outcr['tau'],outcr['SF']=tauarr,Varr
np.savetxt('/home/rumbaugh/SF_ensemble.dat',outcr,fmt='%f %f',header='tau SF')

plt.figure(1)
plt.clf()
color_arr=['magenta','red','blue','green','cyan']
plt.loglog(tauarr,Varr,lw=2,c='orange')
plt.errorbar(tauarr,Varr,lw=2,c='orange')
plt.xlabel(r'$\Delta t$')
plt.ylabel('Structure Function')
plt.savefig('/home/rumbaugh/testplot_SF.ensemble.png')
