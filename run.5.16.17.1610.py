import numpy as np
import pyfits as py
execfile('/home/rumbaugh/pythonscripts/angconvert.py')
DB_path='/home/rumbaugh/var_database/Y3A1'
try:
    doload
except NameError:
    doload=True
if doload:
    hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
    bhdata=hdubh[1].data
    bhz,bhname=bhdata['REDSHIFT'],bhdata['SDSS_NAME']


    bhRAdict,bhDECdict={bhname[x]: bhdata['RA'][x] for x in range(len(bhdata))},{bhname[x]: bhdata['DEC'][x] for x in range(len(bhdata))}

    fname='/home/rumbaugh/Downloads/milliquas.txt'
    mdict={'names':('RA','DEC','Name','Descrip','Rmag','Bmag','Comment','R','B','Z','Cite','Zcite','Qpct','Xname','Rname','Lobe1','Lobe2'),'formats':('f8','f8','|S27','|S5','f8','f8','|S4','|S2','|S2','f8','|S7','|S7','f8','|S24','|S24','|S24','|S24')}
    delims=(11,12,27,5,5,5,4,2,2,7,7,7,4,23,23,23,23)
    crmq=np.genfromtxt(fname,dtype=mdict,delimiter=delims)

    mqRAdict,mqDECdict={x: crmq['RA'][x] for x in range(len(crmq))},{x: crmq['DEC'][x] for x in range(len(crmq))}

    fname='/home/rumbaugh/Downloads/milliquas.txt'
    mdict={'names':('RA','DEC','Name','Descrip','Rmag','Bmag','Comment','R','B','Z','Cite','Zcite','Qpct','Xname','Rname','Lobe1','Lobe2'),'formats':('f8','f8','|S27','|S5','f8','f8','|S4','|S2','|S2','f8','|S7','|S7','f8','|S24','|S24','|S24','|S24')}
    delims=(11,12,27,5,5,5,4,2,2,7,7,7,4,23,23,23,23)
    crmq2=np.genfromtxt(fname,dtype=mdict,delimiter=delims,filling_values=-1)

    #crf=np.loadtxt('/home/rumbaugh/MQ_Y1A1_MATCH_WGOLDFLAGS.tab',dtype={'names':('MQ_ROWNUM','ra','dec','CID','FLAGSG','FLAGSBR'),'formats':('i8','f8','f8','i8','i8','i8')},skiprows=1)

    crsp=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EpochG','EpochR','EpochI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_r_SDSS','g_SDSS','g_ERR','r_SDSS','r_ERR','i_SDSS','i_ERR'),'formats':('f8','f8','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','f8','f8','|S12','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8')})

    crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

crdb=crdb[(crdb['MQrownum']>-1)&(crdb['SDSSNAME']!='-1')]
mqra,mqdec,bhra,bhdec,bhdbids,mqdbids=np.zeros(len(crdb)),np.zeros(len(crdb)),np.zeros(len(crdb)),np.zeros(len(crdb)),np.zeros(len(crdb),dtype='|S24'),np.zeros(len(crdb),dtype='|S24')
dbdict={}

for i in range(0,len(crdb)):
    mqra[i],mqdec[i],bhra[i],bhdec[i]=mqRAdict[crdb['MQrownum'][i]],mqDECdict[crdb['MQrownum'][i]],bhRAdict[crdb['SDSSNAME'][i]],bhDECdict[crdb['SDSSNAME'][i]]
    mqrah,mqram,mqras=deg2hms(mqra[i])
    mqdecd,mqdecm,mqdecs=deg2dms(mqdec[i])
    bhrah,bhram,bhras=deg2hms(bhra[i])
    bhdecd,bhdecm,bhdecs=deg2dms(bhdec[i])
    mqras,mqdecs=np.round(mqras),np.round(mqdecs)
    bhras,bhdecs=np.round(bhras),np.round(bhdecs)
    #mqras,mqdecs=np.round(mqras,1),np.round(mqdecs)
    #bhras,bhdecs=np.round(bhras,1),np.round(bhdecs)
    #bhdbids[i],mqdbids[i]='%02i%02i%04.1f%+03i%02i%02i'%(bhrah,bhram,bhras,bhdecd,bhdecm,int(bhdecs)),'%02i%02i%04.1f%+02i%03i%02i'%(mqrah,mqram,mqras,mqdecd,mqdecm,int(mqdecs))
    bhdbids[i],mqdbids[i]='%02i%02i%02i%+03i%02i%02i'%(bhrah,bhram,bhras,bhdecd,bhdecm,int(bhdecs)),'%02i%02i%02i%+02i%03i%02i'%(mqrah,mqram,mqras,mqdecd,mqdecm,int(mqdecs))
    try:
        dbdict[bhdbids[i]]=dbdict[bhdbids[i]]+(bhdbids[i],)
    except KeyError:
        dbdict[bhdbids[i]]=(bhdbids[i],)
    try:
        dbdict[mqdbids[i]]=dbdict[mqdbids[i]]+(mqdbids[i],)
    except KeyError:
        dbdict[mqdbids[i]]=(mqdbids[i],)
gdiff=np.where(bhdbids!=mqdbids)[0]
print 'Mismatches:'
for i in range(0,len(gdiff)):
    print '%s: %s, %s'%(crdb['DBIDS'][gdiff[i]],mqdbids[gdiff[i]],bhdbids[gdiff[i]])

print 'Collisions:'
undbids,counts=np.unique(np.append(bhdbids,mqdbids),return_counts=True)
for dbid in undbids[counts>2]:
    print '%s: '%dbid,dbdict[dbid]
