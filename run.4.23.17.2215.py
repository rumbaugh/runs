import numpy as np
import matplotlib.pyplot as plt
try:
    crysort
except NameError:
    cry=np.loadtxt('/home/rumbaugh/DR7_BH_Y3A1_MATCH_COADD_PARAMS.tab',dtype={'names':('SDSSNAME','CID','RA','DEC','mag_g','mag_r','mag_i','mag_z','mag_y','magerr_g','magerr_r','magerr_i','magerr_z','magerr_y','class_star'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
    crysort=cry[np.argsort(cry['mag_g'])]
try:
    crssort
except NameError:
    crs=np.loadtxt('/home/rumbaugh/Y3A1_star_magsample.tab',dtype={'names':('class_star','CID','RA','DEC','mag_g','mag_r','mag_i','mag_z','mag_y'),'formats':('f8','i8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
    crssort=crs[np.argsort(crs['mag_g'])]

cdf=np.arange(len(cry))*1./len(cry)
values=np.random.rand(10000)
yrandmags=crysort['mag_g'][np.searchsorted(cdf,values)]
starinds=np.searchsorted(crssort['mag_g'],yrandmags)
srandmags=crssort['mag_g'][starinds]

matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=14

plt.figure(1)
plt.clf()
a=plt.hist(cry['mag_g'],range=(15,25),bins=20)
evqhist,bins=a[0],a[1]
plt.xlim(15,25)
plt.xlabel('g-band Magnitude')
plt.ylabel('Number of Object')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magdist_DR7.hist.4.23.17.png')

plt.figure(1)
plt.clf()
plt.hist(crssort['mag_g'],range=(15,25),bins=20)
plt.xlim(15,25)
plt.xlabel('g-band Magnitude')
plt.ylabel('Number of Object')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magdist_Y3A1_stars.hist.4.23.17.png')


plt.figure(1)
plt.clf()
plt.hist(cry['mag_g'],range=(15,25),bins=20,color='b',normed=True)
plt.hist(srandmags,range=(15,25),bins=20,color='r',edgecolor='r',facecolor='None',lw=3,normed=True)
#plt.hist(random_from_cdf,range=(15,25),bins=20,color='green',edgecolor='green',facecolor='None',lw=3,normed=True,ls='dashed')
plt.xlim(15,25)
plt.xlabel('g-band Magnitude')
plt.ylabel('Normalized Objects')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magdist_Y3A1_control_comp.hist.4.23.17.png')

outcr=crssort[starinds]
np.savetxt('Y3A1_star_control_sample.csv',outcr,header='class_star,CID,RA,DEC,mag_g,mag_r,mag_i,mag_z,mag_y',fmt='%f,%i,%f,%f,%f,%f,%f,%f,%f',comments='')
