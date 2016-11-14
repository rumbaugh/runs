import numpy as np
import healpy as hp
import easyaccess as ea
import time
trst=time.time()
con=ea.connect()
try:
    istest
except NameError:
    istest=True
try:
    testruns
except NameError:
    testruns=10
try:
    testID
except NameError:
    testID=None

nsides=16384

tol=2./3600 

crm=np.loadtxt('/home/rumbaugh/sdss-poss+healpix.txt',dtype={'names':('mID','ra','dec','HP'),'formats':('i8','f8','f8','i8')})

print 'loaded sdss-poss+healpix'
#cr=np.loadtxt('/home/rumbaugh/y1a1_hpix.tab',dtype={'names':('cID','ra','dec','HP'),'formats':('f8','f8','f8','f8')},skiprows=1)
#cr['cID']=np.array(cr['cID'],dtype='i8')
#cr['HP']=np.array(cr['HP'],dtype='i8')


execfile('pythonscripts/find_Y1A1_tile.py')

crout=np.zeros(len(crm),dtype={'names':('mID','ra','dec','tname'),'formats':('i8','f8','f8','|S15')})
crout['mID'],crout['ra'],croit['dec']=crm['mID'],crm['ra'],crm['dec']

for i in range(0,len(crm)):
    crout['tname'][i]=find_tile(crm['ra'][i],crm['dec'][i])

np.savetxt('/home/rumbaugh/milliquas_Y1A1_tiles.csv',crout,fmt='%i,%f,%f,%s',header='SP_ROWNUM,RA,DEC,TILENAME',comments='')
