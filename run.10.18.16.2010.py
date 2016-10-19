import numpy as np
cr=np.loadtxt('milliquas_y1a1_match_pass2.tab',dtype={'names':('MQ','ra','dec','hpix','cid'),'formats':('i8','f8','f8','i8','i8')},skiprows=1)
outcr=cr[cr['cid']!=0]
np.savetxt('/home/rumbaugh/milliquas_y1a1_match_only.tab',outcr,fmt='%i %f %f %i %i',header='MQ_ROWNUM RA DEC HPIX COADD_OBJECTS_ID',comments='')
outcr2=np.zeros((len(outcr),3))
outcr2[:,0],outcr2[:,1],outcr2[:,2]=np.arange(len(outcr)),outcr['ra'],outcr['dec']
np.savetxt('/home/rumbaugh/MQ_radec_monly.tab',outcr2,fmt='%i %f %f',header='NUMROW RA DEC',comments='')
