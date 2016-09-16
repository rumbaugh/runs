import numpy as np
import matplotlib.pyplot as plt


cr=np.loadtxt('/home/rumbaugh/Chandra/coadds.allORELSE.mostly.magcut.EWnD4000.winfillcorrHd.cat',dtype={'names':('field','file','z','OII','OIIerr','Hd','Hderr','D4000','D4000err','Hdcorr'),'formats':('|S12','|S64','f8','f8','f8','f8','f8','f8','f8','f8')})

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604"}

meanUmag=np.zeros(len(cr['z']))
for i in range(0,len(cr['z'])):
    field=target_dir[cr['field'][i]]
    crSC=np.loadtxt('/home/rumbaugh/Chandra/coadd_cats/supercolors_cut-20.9.%s.4.11.16.dat'%field,dtype={'names':('ID','RA','Dec','magR','magI','magZ','dmagR','dmagI','dmagZ','SCmagRed','SCmagBlue','dRed','dBlue'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
    crSC['dBlue'][crSC['dBlue']<=0]=999999.
    meanUmag[i]=np.sum(crSC['SCmagBlue']/(crSC['dBlue']**2))/np.sum(1/(crSC['dBlue']**2))

coeff0=3E10/(3543.0E-8)**2
SFR_OII=-2.51*10.**(-(48.6+meanUmag)/2.5-10.)*coeff0*cr['OII']



plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(SFR_OII,cr['Hd'],color='r',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
#plt.xlim(xlim[1],xlim[0])
for i in range(0,len(cr['OII'])): plt.text(SFR_OII[i]+xrng/50.,cr['Hd'][i],cr['field'][i],color='b')
#plt.axvline(-4,lw=2,color='k',ls='dashed')
plt.xlabel('SFR(L(OII))')
plt.ylabel(r'EW(H$\delta$) (angstroms)')
plt.savefig('/home/rumbaugh/Chandra/plots/coadds.SFR_OII_vs_Hd.png')

