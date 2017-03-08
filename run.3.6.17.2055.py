import numpy as np
import pydl
pydl.test()

fname='/home/rumbaugh/master_QSO_S82.dat'
mdict={'names':('DR5ID','RA','DEC','Redshift','umag','umagerr','gmag','gmagerr','rmag','rmagerr','imag','imagerr','zmag','zmagerr','Au','lohHI','20mag','F-SN','S-Fsep','F1Flag','F2Flag','logX','X-SN','S-XSep','Jmag','Jmagerr','Hmag','Hmagerr','Kmag','Kmagerr','S-2Sep','iMag','D(g-i)','Morph','SPFlag','SMFlag','UTSFlag','B-TSFlag','Blowz','Bhiz','BFFlag','BRFlag','BSFlag','B-*Flag','BGFlag','RNum','PMJD','SMJD','SPNum','SFNum','rerun','CCol','Frame','ONum','TTsFlag','Tlowz','Thiz','TFFlag','TRFlag','TSFlag','T-*Flag','TGFlag','T-umag','T-umagerr','T-gmag','T-gmagerr','T-rmag','T-rmagerr','T-imag','T-imagerr','T-zmag','T-zmagerr','SpOID','OName'),'formats':('|S20','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','|S28')}
delims=(19,11,11,7,7,6,7,6,7,6,7,6,7,6,7,7,7,8,7,3,3,8,7,7,7,6,7,6,7,6,7,8,7,3,3,3,3,12,3,3,3,3,3,3,3,6,6,6,5,5,4,3,5,5,12,3,3,3,3,3,3,3,7,6,7,6,7,6,7,6,7,6,21,26)
cr82=np.genfromtxt(fname,dtype=mdict,delimiter=delims)

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SP_rownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})
crmi=np.loadtxt('/home/rumbaugh/var_database/Y3A1/match_index.dat',dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('i8','i8','|S32','f8','f8','i8','i8','|S32')},skiprows=1)
gs=np.where(crmi['SDSS_NAME']!='-1')[0]

sout=pydl.pydlutils.spheregroup.spherematch(crmi['RA'][gs],crmi['DEC'][gs],cr82['RA'],cr82['DEC'],0.3/3600)
print len(sout[0])
gm=np.where(crmi['COADD_OBJECTS_ID'][gs[sout[0]]]>0)[0]
print len(gm)
gm=np.where(crmi['TILENAME'][gs[sout[0]]]!='None')[0]
print len(gm)
gm=np.where((crmi['COADD_OBJECTS_ID'][gs[sout[0]]]>0)&(crmi['TILENAME'][gs[sout[0]]]=='None'))[0]
print len(gm)
gm=np.where((crmi['COADD_OBJECTS_ID'][gs[sout[0]]]==0)&(crmi['TILENAME'][gs[sout[0]]]!='None'))[0]
print len(gm)
gm=np.where((crmi['COADD_OBJECTS_ID'][gs[sout[0]]]>=0)&(crmi['TILENAME'][gs[sout[0]]]!='None'))[0]
print len(gm)
