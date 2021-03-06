import numpy as np
import pydl
import pydl.pydlutils
import pydl.pydlutils.spheregroup
import pyfits as py

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data

try:
    arcsrch
except NameError:
    arcsrch=0.3
#fname='/home/rumbaugh/master_QSO_S82.dat'
#mdict={'names':('DR5ID','RA','DEC','Redshift','umag','umagerr','gmag','gmagerr','rmag','rmagerr','imag','imagerr','zmag','zmagerr','Au','lohHI','20mag','F-SN','S-Fsep','F1Flag','F2Flag','logX','X-SN','S-XSep','Jmag','Jmagerr','Hmag','Hmagerr','Kmag','Kmagerr','S-2Sep','iMag','D(g-i)','Morph','SPFlag','SMFlag','UTSFlag','B-TSFlag','Blowz','Bhiz','BFFlag','BRFlag','BSFlag','B-*Flag','BGFlag','RNum','PMJD','SMJD','SPNum','SFNum','rerun','CCol','Frame','ONum','TTsFlag','Tlowz','Thiz','TFFlag','TRFlag','TSFlag','T-*Flag','TGFlag','T-umag','T-umagerr','T-gmag','T-gmagerr','T-rmag','T-rmagerr','T-imag','T-imagerr','T-zmag','T-zmagerr','SpOID','OName'),'formats':('|S20','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','|S28')}
#delims=(19,11,11,7,7,6,7,6,7,6,7,6,7,6,7,7,7,8,7,3,3,8,7,7,7,6,7,6,7,6,7,8,7,3,3,3,3,12,3,3,3,3,3,3,3,6,6,6,5,5,4,3,5,5,12,3,3,3,3,3,3,3,7,6,7,6,7,6,7,6,7,6,21,26)
#cr82=np.genfromtxt(fname,dtype=mdict,delimiter=delims)

mcdict={'names':('DBID','RA','DEC','SDR5ID','Mi','Micorr','redshift','massBH','Lbol','u','g','r','i','z','Au'),'formats':('i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
delims=(8,11,11,6,8,8,7,6,7,7,7,7,7,7,7)
cr82=np.genfromtxt('/home/rumbaugh/macleodQSOs/DB_QSO_S82.dat',dtype=mcdict,delimiter=delims)

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SP_rownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})

cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})

bhSN2FIRST={bhdata['SDSS_NAME'][x]: bhdata['FIRST_FR_TYPE'][x] for x in np.arange(len(bhdata))}
db2SN={crdb['DBID'][x]: crdb['SDSSNAME'][x] for x in np.arange(len(crdb))}
FIRST=np.array([bhSN2FIRST[db2SN[cr['DBID'][x]]] for x in np.arange(len(cr))])

drop=np.abs(cr['glo']-cr['ghi'])
print "Total DR7: %i"%len(bhdata)
print "Dr7+DES: %i"%(len(drop))
print "DR7 g>1: %i"%(len(drop[drop>1]))
print "DR7 g>1.5: %i"%(len(drop[drop>1.5]))
print "DR7 g>2: %i"%(len(drop[drop>2]))

crmF=cr[FIRST>0]
dropF=np.abs(crmF['glo']-crmF['ghi'])
print "Total DR7F: %i"%len(bhdata[bhdata['FIRST_FR_TYPE']>0])
print "Dr7F+DES: %i"%(len(dropF))
print "DR7F g>1: %i"%(len(dropF[dropF>1]))
print "DR7F g>1.5: %i"%(len(dropF[dropF>1.5]))
print "DR7F g>2: %i"%(len(dropF[dropF>2]))

sout=pydl.pydlutils.spheregroup.spherematch(cr['RA'],cr['DEC'],cr82['RA'],cr82['DEC'],arcsrch/3600.)

print "Total S82: %i"%(len(cr82))
sout82=pydl.pydlutils.spheregroup.spherematch(bhdata['RA'],bhdata['DEC'],cr82['RA'],cr82['DEC'],arcsrch/3600.)
crm82=cr[sout[0]]
drop82=np.abs(crm82['glo']-crm82['ghi'])
print "S82 in DES: %i"%(len(crm82))
print len(sout82[0])
print "S82 with g>1: %i"%(len(drop82[drop82>1]))
print "S82 with g>1.5: %i"%(len(drop82[drop82>1.5]))
print "S82 with g>2: %i"%(len(drop82[drop82>2]))

crmF82=cr[sout[0]][FIRST[sout[0]]>0]
dropF82=np.abs(crmF82['glo']-crmF82['ghi'])
print "Total DR7F82: %i"%len(sout82[0][bhdata['FIRST_FR_TYPE'][sout82[0]]>0])
print "Dr7F82+DES: %i"%(len(dropF82))
print "DR7F82 g>1: %i"%(len(dropF82[dropF82>1]))
print "DR7F82 g>1.5: %i"%(len(dropF82[dropF82>1.5]))
print "DR7F82 g>2: %i"%(len(dropF82[dropF82>2]))
