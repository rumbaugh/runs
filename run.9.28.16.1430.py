import numpy as np
import healpy as hp
nside=16384

cr=np.loadtxt("Downloads/milliquas.txt",usecols=(0,1))

crout=np.zeros((np.shape(cr)[0],3))

crout[:,:2]=cr
crout[:,2]=hp.ang2pix(nside,(90-cr[:,2])*np.pi/180.,cr[:,1]*np.pi/180,True)

np.savetxt('/home/rumbaugh/milliquas+healpix.txt',crout,fmt='%f %f %i')
