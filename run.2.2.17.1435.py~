import numpy as np
cr=np.loadtxt('milliquas_y1a1_match_pass2.tab',dtype={'names':('MQ','ra','dec','hpix','cid'),'formats':('i8','f8','f8','i8','i8')},skiprows=1)
#outcr=cr[cr['cid']!=0]
cr=cr[cr['cid']!=0]
outcr=np.zeros(len(cr),dtype=[('numrow', '<i8'),('MQ', '<i8'), ('ra', '<f8'), ('dec', '<f8'), ('hpix', '<i8'), ('cid', '<i8')])
outcr['numrow'],outcr['MQ'],outcr['ra'],outcr['dec'],outcr['hpix'],outcr['cid']=np.arange(len(outcr)),cr['MQ'],cr['ra'],cr['dec'],cr['hpix'],cr['cid']
np.savetxt('/home/rumbaugh/milliquas_y1a1_match_only.tab',outcr,fmt='%i %i %f %f %i %i',header='NUMROW MQ_ROWNUM RA DEC HPIX COADD_OBJECTS_ID',comments='')
np.savetxt('/home/rumbaugh/milliquas_y1a1_match_only.csv',outcr,fmt='%i,%i,%f,%f,%i,%i',header='NUMROW,MQ_ROWNUM,RA,DEC,HPIX,COADD_OBJECTS_ID',comments='')
outcr2=np.zeros((len(outcr),4))
outcr2[:,0],outcr2[:,1],outcr2[:,2],outcr2[:,3]=np.arange(len(outcr)),outcr['MQ'],outcr['ra'],outcr['dec']
np.savetxt('/home/rumbaugh/MQ_radec_monly.tab',outcr2,fmt='%i %i %f %f',header='NUMROW MQ_ROWNUM RA DEC',comments='')
np.savetxt('/home/rumbaugh/MQ_radec_monly.csv',outcr2,fmt='%i,%i,%f,%f',header='NUMROW,MQ_ROWNUM,RA,DEC',comments='')
