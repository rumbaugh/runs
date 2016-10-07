import numpy as np

cr=np.loadtxt('/home/rumbaugh/milliquas_y1a1_match.csv',delimiter=',',skiprows=1,dtype={'names':('MQ','RA','Dec','Hpix','cid'),'formats':('i8','f8','f8','i8','i8')})
outcr=np.zeros((len(cr),3))
outcr[:,0],outcr[:,1],outcr[:,2]=np.arange(1,len(cr)+1),cr['RA'],cr['Dec']
np.savetxt('/home/rumbaugh/milliquas_radec.tab',outcr,fmt='%i %f %f',comments='',header='NUMROW RA DEC')
