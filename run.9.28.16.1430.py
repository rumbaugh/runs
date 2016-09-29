import numpy as np
import healpy as hp
nside=16384

cr=np.loadtxt("Downloads/milliquas.txt",usecols=(0,1))

crout=np.zeros((np.shape(cr)[0],4))

crout[:,0]=np.arange(np.shape(cr)[0])
crout[:,1:3]=cr
crout[:,3]=hp.ang2pix(nside,(90-cr[:,1])*np.pi/180.,cr[:,0]*np.pi/180,True)

np.savetxt('/home/rumbaugh/milliquas+healpix.txt',crout,fmt='%i %f %f %i')
np.savetxt('/home/rumbaugh/MILLIQUAS_HPIX.csv',crout,fmt='%i,%f,%f,%i',header='MQ_ROWNUM,RA,DEC,HPIX')
