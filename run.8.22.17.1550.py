import numpy as np
import pyfits as py
import pandas as pd

DBdir='/home/rumbaugh/var_database/Y3A1'
crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
drops=np.abs(crd['glo']-crd['ghi'])

hdubh=py.open('dr7_bh_Nov19_2013.fits')
data=hdubh[1].data

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

DBID2SN={crdb['DatabaseID'][x]:crdb['SDSSNAME'][x] for x in np.arange(len(crdb))[crdb['SDSSNAME']!='-1']}

SN2DR7={data['SDSS_NAME'][x]:x for x in np.arange(0,len(data))}

sdssname=np.array([DBID2SN[x] for x in crd['DBID']])
DR7ID=np.array([SN2DR7[x] for x in sdssname],dtype='i8')

gsort=np.argsort(DR7ID)
DR7ID,sdssname,crd=DR7ID[gsort],sdssname[gsort],crd[gsort]

for i in range(0,len(DR7ID)):
    DBID=crd['DBID'][i]
    
    cr=np.loadtxt('%s/%s/LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    crout=np.loadtxt('%s/%s/outliers.tab'%(DBdir,DBID),dtype='i8')
    try:
        crmac=np.loadtxt('%s/%s/Macleod_LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('i8','f8','f8','f8','|S4','f8','f8','i8')})
        try:
            croutmac=np.loadtxt('%s/%s/outliers_Macleod.tab'%(DBdir,DBID),dtype='i8')
        except IOError:
            pass
    except IOError:
        crmac=None
    badbands={x:0 for x in ['g','r','i']}
    for band in ['g','r','i']:
        badbands[x]=len(cr[(cr['BAND']==band)&(crout<0)])
    print DBID,badbands
