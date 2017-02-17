import numpy as np
import pyfits as py
cr=np.loadtxt('/home/rumbaugh/dr7_bh_y3a1_match.csv',dtype={'names':('SDSSNAME','ra','dec','hpix','cid'),'formats':('|S24','f8','f8','i8','i8')},skiprows=1,delimiter=',')
cr=cr[cr['cid']!=0]
outcr=np.zeros(len(cr),dtype=[('numrow', '<i8'),('SDSSNAME', '|S24'), ('ra', '<f8'), ('dec', '<f8'), ('cid', '<i8')])

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
bhz,bhname=bhdata['REDSHIFT'],bhdata['SDSS_NAME']
numrow=np.zeros(len(outcr),dtype='i8')
for i in range(0,len(outcr)):
    gbh=np.where(bhname==cr['SDSSNAME'][i])[0][0]
    numrow[i]=gbh
outcr['numrow'],outcr['SDSSNAME'],outcr['ra'],outcr['dec'],outcr['cid']=numrow,cr['SDSSNAME'],cr['ra'],cr['dec'],cr['cid']
np.savetxt('/home/rumbaugh/dr7_bh_match_only.csv',outcr,fmt='%i,%s,%f,%f,%i',header='NUMROW,SDSSNAME,RA,DEC,COADD_OBJECT_ID',comments='')
