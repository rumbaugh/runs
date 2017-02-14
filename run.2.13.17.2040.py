import numpy as np
cr=np.loadtxt('dr7_bh_y3a1_match.csv',dtype={'names':('SDSSNAME','ra','dec','hpix','cid'),'formats':('|S24','f8','f8','i8','i8')},skiprows=1,delimiter=',')
#outcr=cr[cr['cid']!=0]
#cr=cr[cr['cid']!=0]
outcr=np.zeros(len(cr),dtype=[('SDSSNAME', '|S24'),('ra', '<f8'), ('dec', '<f8')])
outcr['SDSSNAME'],outcr['ra'],outcr['dec']=cr['SDSSNAME'],cr['ra'],cr['dec']
np.savetxt('/home/rumbaugh/dr7_bh_radec.csv',outcr,fmt='%s,%f,%f',header='SDSSNAME,RA,DEC',comments='')
