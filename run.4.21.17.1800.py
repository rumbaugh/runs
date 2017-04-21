import numpy as np
import matplotlib.pyplot as plt

try:
    crsl
except NameError:
    crsl=np.loadtxt('/home/rumbaugh/Y3A1_star_sample_lightcurves.tab',dtype={'names':('class_star','CID','MJD','RA','DEC','expnum','file','objnum','magpsf','magerrpsf','magauto','magerrauto','band','flag','flag_detmodel','flag_model','flag_weight'),'formats':('f8','i8','f8','f8','f8','i8','|S24','i8','f8','f8','f8','f8','|S4','i8','i8','i8','i8')},skiprows=1)
    crsl=crsl[crsl['band']=='g']
try:
    cryl
except NameError:
    cryl=np.loadtxt('/home/rumbaugh/DR7_Y3A1_lightcurves.tab',dtype={'names':('class_star','CID','MJD','RA','DEC','expnum','file','objnum','magpsf','magerrpsf','magauto','magerrauto','band','flag','flag_detmodel','flag_model','flag_weight'),'formats':('f8','i8','f8','f8','f8','i8','|S24','i8','f8','f8','f8','f8','|S4','i8','i8','i8','i8')},skiprows=1)
    cryl=cryl[cryl['band']=='g']


matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=14

plt.figure(1)
plt.clf()
a=plt.hist(cryl['magerrpsf'],range=(0,0.06),bins=30,color='k',normed=True)
b=plt.hist(crsl['magerrpsf'],range=(0,0.06),bins=30,color='r',edgecolor='r',facecolor='None',lw=3,normed=True)
plt.xlim(0,0.06)
plt.xlabel('g-band Magnitude Error')
plt.ylabel('Normalized Number of Objects')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magerrdist_stars_comp.hist.4.21.17.png')
