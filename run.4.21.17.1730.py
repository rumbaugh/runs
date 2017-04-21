import numpy as np
import matplotlib.pyplot as plt
cry=np.loadtxt('/home/rumbaugh/DR7_BH_Y3A1_MATCH_COADD_PARAMS.tab',dtype={'names':('SDSSNAME','CID','RA','DEC','mag_g','mag_r','mag_i','mag_z','mag_y','magerr_g','magerr_r','magerr_i','magerr_z','magerr_y','class_star'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
crs=np.loadtxt('/home/rumbaugh/Y3A1_star_magsample.tab',dtype={'names':('class_star','CID','RA','DEC','mag_g','mag_r','mag_i','mag_z','mag_y'),'formats':('f8','i8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)


matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=14

plt.figure(1)
plt.clf()
plt.hist(cry['mag_g'],range=(15,25),bins=20)
plt.xlim(15,25)
plt.xlabel('g-band Magnitude')
plt.ylabel('Number of Object')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magdist_DR7.hist.4.21.17.png')


plt.figure(1)
plt.clf()
plt.hist(crs['mag_g'],range=(15,25),bins=20)
plt.xlim(15,25)
plt.xlabel('g-band Magnitude')
plt.ylabel('Number of Object')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magdist_Y3A1_stars.hist.4.21.17.png')
