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
try:
    calcmatchlist
except NameError:
    calcmatchlist=False

def calc_tmpdist(ra1,dec1,ra2,dec2):
    return np.sqrt((ra1-ra2)**2+(dec1-dec2)**2)

nsides=16384

tol=2./3600 

crm=np.loadtxt('/home/rumbaugh/milliquas+healpix.txt',dtype={'names':('mID','ra','dec','HP'),'formats':('i8','f8','f8','i8')})

print 'loaded milliquas+healpix'

execfile('pythonscripts/find_Y1A1_tile.py')

crout=np.zeros(len(crm),dtype={'names':('mID','ra','dec','tname'),'formats':('i8','f8','f8','|S50')})
crout['mID'],crout['ra'],croit['dec']=crm['mID'],crm['ra'],crm['dec']

for i in range(0,len(crm)):
    crout['tname'][i]=find_tile(crm['ra'][i],crm['dec'][i])

np.savetxt('/home/rumbaugh/milliquas_Y1A1_tiles.csv',crout,fmt='%i,%f,%f,%s',header='MQ_ROWNUM,RA,DEC,TILENAME',comments='')
