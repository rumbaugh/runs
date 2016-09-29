import numpy as np
import healpy as hp
nsides=16384

crm=np.loadtxt('/home/rumbaugh/milliquas+healpix.txt',dtype={'names':('ra','dec','HP'),'formats':('f8','f8','i8')})


cr=np.loadtxt('/home/rumbaugh/y1a1_hpix.tab',dtype={'names':('cID','ra','dec','HP'),'formats':('i8','f8','f8','i8')},skiprows=1)

HPs=np.intersect1d(cr['HP'],crm['HP'])

np.savetxt('/home/rumbaugh/milliquas_distinct_HP_IDs_overlap.txt',HPs,fmt='%i')
