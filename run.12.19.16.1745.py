import numpy as np
import pyfits as py

cr_rids=np.loadtxt('/home/rumbaugh/changinglookAGNcandidates_index.12.18.16.dat',dtype={'names':('DBID','CID','tid','sdr7id','ra','dec','IntFlag'),'formats':('i8','i8','i8','i8','f8','f8','i8')})

crout=np.zeros((len(cr_rids),2),dtype='i8')
crout[:,0]=cr_rids['DBID']
np.savetxt('/home/rumbaugh/changinglookAGNcandidates_bestindex.12.18.16.dat',crout,fmt='%12i %2i',header='DBID IntFlag')
