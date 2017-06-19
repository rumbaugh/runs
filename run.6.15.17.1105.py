import numpy as np
import pyfits as py
import pandas as pd

crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
drops=np.abs(crd['glo']-crd['ghi'])
crd=crd[drops>1]

hdubh=py.open('dr7_bh_Nov19_2013.fits')
data=hdubh[1].data

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

DBID2SN={crdb['DatabaseID'][x]:crdb['SDSSNAME'][x] for x in np.arange(len(crdb))[crdb['SDSSNAME']!='-1']}

SN2DR7={data['SDSS_NAME'][x]:x for x in np.arange(0,len(data))}

sdssname=np.array([DBID2SN[x] for x in crd['DBID']])
DR7ID=np.array([SN2DR7[x] for x in sdssname],dtype='i8')

gsort=np.argsort(DR7ID)
DR7ID,sdssname,crd=DR7ID[gsort],sdssname[gsort],crd[gsort]

FIRST=data['FIRST_FR_TYPE'][DR7ID]

outcr=np.zeros((len(FIRST),),dtype={'names':('DR7ID','RA','DEC','z','mjdlo','glo','siglo','mjdhi','ghi','sighi','FIRST'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8')})
outcr['DR7ID'],outcr['RA'],outcr['DEC'],outcr['z'],outcr['mjdlo'],outcr['glo'],outcr['siglo'],outcr['mjdhi'],outcr['ghi'],outcr['sighi'],outcr['FIRST']=DR7ID,crd['RA'],crd['DEC'],crd['z'],crd['mjdlo'],crd['glo'],crd['siglo'],crd['mjdhi'],crd['ghi'],crd['sighi'],FIRST

np.savetxt('EVQ_Table2.tab',outcr,fmt='%6i %8.5f %+9.6f %6.4f %8.2f %6.3f %6.3f %8.2f %6.3f %6.3f %2i')

outcr2=np.loadtxt('DR7_CLQ_candidates_more.tab',dtype={'names':('DR7ID','RA','DEC','z','mjdlo','glo','siglo','mjdhi','ghi','sighi','FIRST'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8')})
cr2=np.loadtxt('DR7_CLQ_candidates_more.tab',dtype={'names':('DR7ID','RA','DEC','z','mjdlo','glo','siglo','mjdhi','ghi','sighi','FIRST'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8')})
gs=[np.zeros(len(cr2),dtype='i8') for x in range(0,11)]

for name,i in zip(['DR7ID','RA','DEC','z','mjdlo','glo','siglo','mjdhi','ghi','sighi','FIRST'],np.arange(len(gs))): 
    print name,np.count_nonzero(np.round(cr2[name],2)-np.round(outcr2[name],2))
    gs[i]=np.where(np.round(cr2[name],2)-np.round(outcr2[name],2)!=0)[0]
gall=np.unique(np.concatenate(gs))
for i in gall:
    print '\n%i:\n%6i %8.5f %+9.6f %6.4f %8.2f %6.3f %6.3f %8.2f %6.3f %6.3f %2i'%(i,outcr2['DR7ID'][i],outcr2['RA'][i],outcr2['DEC'][i],outcr2['z'][i],outcr2['mjdlo'][i],outcr2['glo'][i],outcr2['siglo'][i],outcr2['mjdhi'][i],outcr2['ghi'][i],outcr2['sighi'][i],outcr2['FIRST'][i])
    print '%6i %8.5f %+9.6f %6.4f %8.2f %6.3f %6.3f %8.2f %6.3f %6.3f %2i'%(cr2['DR7ID'][i],cr2['RA'][i],cr2['DEC'][i],cr2['z'][i],cr2['mjdlo'][i],cr2['glo'][i],cr2['siglo'][i],cr2['mjdhi'][i],cr2['ghi'][i],cr2['sighi'][i],cr2['FIRST'][i])
    print '%6i %8.5f %+9.6f %6.4f %8.2f %6.3f %6.3f %8.2f %6.3f %6.3f %2i'%(cr2['DR7ID'][i]-outcr2['DR7ID'][i],cr2['RA'][i]-outcr2['RA'][i],cr2['DEC'][i]-outcr2['DEC'][i],cr2['z'][i]-outcr2['z'][i],cr2['mjdlo'][i]-outcr2['mjdlo'][i],cr2['glo'][i]-outcr2['glo'][i],cr2['siglo'][i]-outcr2['siglo'][i],cr2['mjdhi'][i]-outcr2['mjdhi'][i],cr2['ghi'][i]-outcr2['ghi'][i],cr2['sighi'][i]-outcr2['sighi'][i],cr2['FIRST'][i]-outcr2['FIRST'][i])
