import numpy as np
import pyfits as py
import pandas as pd

crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
drops=np.abs(crd['glo']-crd['ghi'])

maxg=np.zeros(len(drops))


hdubh=py.open('dr7_bh_Nov19_2013.fits')
data=hdubh[1].data

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

try:
    SN2DR7
except:
    DBID2SN={crdb['DatabaseID'][x]:crdb['SDSSNAME'][x] for x in np.arange(len(crdb))[crdb['SDSSNAME']!='-1']}

    SN2DR7={data['SDSS_NAME'][x]:x for x in np.arange(0,len(data))}

    sdssname=np.array([DBID2SN[x] for x in crd['DBID']])
    DR7ID=np.array([SN2DR7[x] for x in sdssname],dtype='i8')

gsort=np.argsort(DR7ID)
DR7ID,sdssname,crd=DR7ID[gsort],sdssname[gsort],crd[gsort]

for i in range(0,len(DR7ID)):
    df=pd.read_csv('/home/rumbaugh/EVQ_DB/{}_g'.format(DR7ID[i]))
    df=df[df.FLAG.values>=0]
    if len(df)>1:
        maxg[i]=df.MAG.max()-df.MAG.min()

print len(maxg[maxg>2])
print len(maxg[maxg>1.5])
print len(maxg[maxg>1])

        
