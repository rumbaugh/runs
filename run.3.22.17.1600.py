import numpy as np
import healpy as hp
import pydl
import pydl.pydlutils

mcdict={'names':('DBID','RA','DEC','SDR5ID','Mi','Micorr','redshift','massBH','Lbol','u','g','r','i','z','Au'),'formats':('i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
delims=(8,11,11,6,8,8,7,6,7,7,7,7,7,7,7)
crmc=np.genfromtxt('/home/rumbaugh/macleodQSOs/DB_QSO_S82.dat',dtype=mcdict,delimiter=delims)

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data

data=data[crdb['SDSSNAME']!='-1']
crdb=crdb[crdb['SDSSNAME']!='-1']

gdb,gmac,dists=pydl.pydutils.spheregroup.spherematch(data['RA_SDSS'],data['Dec_SDSS'],crmc['RA'],crmc['DEC'],0.2/3600)

outcr=np.zeros((len(data),),dtype={'names':('DBID','MCID'),'formats':('|S24','i8')})
outcr['DBID'],outcr['MCID']=data['DatabaseID'],-1
for i in range(0,len(outcr)):
    DBID=outcr['DBID'][i]
    g=np.where(DBID==outcr['DBID'][gdb])[0]
    if len(g)>0:
        outcr['MCID'][i]=crmc['DBID'][gmac[g[0]]]
        mcLCdict={'names':('MJD_u','mag_u','mag_u_err','MJD_u','mag_u','mag_u_err','MJD_u','mag_u','mag_u_err','MJD_u','mag_u','mag_u_err','MJD_u','mag_u','mag_u_err','ra','dec'),'formats':('f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
        crlc=np.loadtxt('/home/rumbaugh/QSO_S82/%i'%(crmc['DBID'][gmac[g[0]]]),dtype=mcLCdict)
        LCcr=np.zeros((len(crlc)*5,),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('i8','f8','f8','f8','|S4','f8','f8','i8')})
        LCcr['DatabaseID']=outcr['MCID'][i]
        for b,ib in zip(['u','g','r','i','z'],np.arange(5)):
            LCcr['MJD'][ib*len(crlc):(ib+1)*len(crlc)],LCcr['BAND'][ib*len(crlc):(ib+1)*len(crlc)],LCcr['MAG'][ib*len(crlc):(ib+1)*len(crlc)],LCcr['MAGERR'][ib*len(crlc):(ib+1)*len(crlc)],LCcr['RA'][ib*len(crlc):(ib+1)*len(crlc)],LCcr['DEC'][ib*len(crlc):(ib+1)*len(crlc)]=crlc['MJD_%s'%b],crlc['mag_%s'%b],crlc['mag_%s_err'%b],crlc['ra'],crlc['dec']
        np.savetxt('/home/rumbaugh/var_database/Y3A1/%s/Macleod_LC.tab'%DBID,
np.savetxt('/home/rumbaugh/var_database/Y3A1/DR7_Macleod_S82_match.dat',outcr,fmt='%24s %i',header='DatabaseID Macleod_DatabaseID',comments='')

