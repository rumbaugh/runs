import numpy as np
import pyfits as py

crids=np.loadtxt('/home/rumbaugh/var_database/maxdiffs_DBID.12.18.16.txt',dtype={'names':('DBID','maxdiff'),'formats':('i8','f8')})

crout=np.zeros((len(crids),2),dtype='i8')
crout[:,0]=crids['DBID']
np.savetxt('/home/rumbaugh/changinglookAGNcandidates_bestindex.12.18.16.dat',crout,fmt='%12i %2i',header='DBID IntFlag')
