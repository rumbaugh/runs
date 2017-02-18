import numpy as np
cr=np.loadtxt('/home/rumbaugh/dr7_bh_y3a1_match.csv',dtype={'names':('SDSSNAME','ra','dec','hpix','cid'),'formats':('|S24','f8','f8','i8','i8')},skiprows=1,delimiter=',')
for i in np.arange(len(cr)):cr['SDSSNAME'][i]=cr['SDSSNAME'][i].strip()
cr=cr[np.argsort(cr['SDSSNAME'])]
hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
bhz,bhname=bhdata['REDSHIFT'],bhdata['SDSS_NAME']
numrow=np.argsort(bhname)

outcr['numrow'],outcr['SDSSNAME'],outcr['ra'],outcr['dec']=numrow,cr['SDSSNAME'],cr['ra'],cr['dec']
np.savetxt('/home/rumbaugh/dr7_bh_radec.csv',outcr,fmt='%i,%s,%f,%f',header='NUMROW,SDSSNAME,RA,DEC',comments='')

gcr=np.where(cr['cid']!=0)[0]
cr,numrow=cr[gcr],numrow[gcr]
outcr['numrow'],outcr['SDSSNAME'],outcr['ra'],outcr['dec'],outcr['cid']=numrow,cr['SDSSNAME'],cr['ra'],cr['dec'],cr['cid']
np.savetxt('/home/rumbaugh/dr7_bh_match_only.csv',outcr,fmt='%i,%s,%f,%f,%i',header='NUMROW,SDSSNAME,RA,DEC,COADD_OBJECT_ID',comments='')
