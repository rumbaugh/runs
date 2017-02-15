import numpy as np
cr=np.loadtxt('dr7_bh_y3a1_match.csv',dtype={'names':('SDSSNAME','ra','dec','hpix','cid'),'formats':('|S24','f8','f8','i8','i8')},skiprows=1,delimiter=',')
#outcr=cr[cr['cid']!=0]
#cr=cr[cr['cid']!=0]
outcr=np.zeros(len(cr),dtype=[('numrow', '<i8'),('SDSSNAME', '|S24'), ('ra', '<f8'), ('dec', '<f8')])
outcr['numrow'],outcr['SDSSNAME'],outcr['ra'],outcr['dec'],outcr['cid']=np.arange(len(outcr)),cr['SDSSNAME'],cr['ra'],cr['dec'],cr['cid']
np.savetxt('/home/rumbaugh/dr7_bh_match_only.csv',outcr,fmt='%i,%s,%f,%f,%i',header='NUMROW,SDSSNAME,RA,DEC,COADD_OBJECT_ID',comments='')
