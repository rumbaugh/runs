import numpy as np
import healpy as hp

cr=np.loadtxt('/home/rumbaugh/y3a1_hpix_radec.tab',dtype={'names':('cid','ra','dec','hpix'),'formats':('i8','f8','f8','i8')},skiprows=1)

hpix_new=hp.ang2pix(1024,(90-cr['dec'])*np.pi/180.,cr['ra']*np.pi/180)
cr['hpix']=hpix_new
np.savetxt('/home/rumbaugh/y3a1_hpix_1024.tab',cr,fmt='%i %f %f %i',header='COADD_OBJECT_ID RA DEC HPIX_4194304',comments='')
