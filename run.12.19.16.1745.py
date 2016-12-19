import numpy as np
import pyfits as py

cr_rids=np.loadtxt('/home/rumbaugh/changinglookAGNcandidates_index.12.18.16.dat',dtype={'names':('DBID','CID','tid','sdr7id','ra','dec','IntFlag'),'formats':('i8','i8','i8','i8','f8','f8','i8')})

good_dbids=cr_rids['DBID'][cr_rids['IntFlag']==1]
crout=np.zeros((len(good_dbids),2),dtype='i8')
crout[:,0]=good_dbids
np.savetxt('/home/rumbaugh/changinglookAGNcandidates_bestindex.12.18.16.dat',crout,fmt='%12i %2i',header='DBID IntFlag')
