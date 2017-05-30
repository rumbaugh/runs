import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/pythonscripts/KStest.py')

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
data=hdubh[1].data


hduc=py.open('/home/rumbaugh/dr7_control.fits')
cdata=hduc[1].data


crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.28.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24')})
drop=np.abs(crd['glo']-crd['ghi'])
crd=crd[drop>1]


crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)

inids=np.in1d(crdb['DatabaseID'],crd['DBID'])
crdb=crdb[inids]

dataid=np.in1d(data['SDSS_NAME'],crdb['SDSSNAME'])
data=data[dataid]


plt.figure(1)
plt.clf()
plt.hist(np.log10(data['EW_OIII_4959']),range=(0.5,3),bins=25,normed=True,facecolor='None',edgecolor='k',lw=2)
plt.hist(np.log10(cdata['EW_OIII_4959']),range=(0.5,3),bins=25,normed=True,facecolor='None',edgecolor='green',lw=2)
plt.xlabel(r'H$\beta$')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/spectral_plots.OIII_4959.5.29.17.png')

print 'OIII_4959'
print KStest(data['EW_OIII_4959'][(np.log10(data['EW_OIII_4959'])>=0.5)&(np.log10(data['EW_OIII_4959'])<=3)],cdata['EW_OIII_4959'][(np.log10(cdata['EW_OIII_4959'])>=0.5)&(np.log10(cdata['EW_OIII_4959'])<=3)])


plt.figure(1)
plt.clf()
plt.hist(np.log10(data['EW_OIII_5007']),range=(0.5,3),bins=25,normed=True,facecolor='None',edgecolor='k',lw=2)
plt.hist(np.log10(cdata['EW_OIII_5007']),range=(0.5,3),bins=25,normed=True,facecolor='None',edgecolor='green',lw=2)
plt.xlabel(r'H$\beta$')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/spectral_plots.OIII_5007.5.29.17.png')

print 'OIII_5007'
print KStest(data['EW_OIII_5007'][(np.log10(data['EW_OIII_5007'])>=0.5)&(np.log10(data['EW_OIII_5007'])<=3)],cdata['EW_OIII_5007'][(np.log10(cdata['EW_OIII_5007'])>=0.5)&(np.log10(cdata['EW_OIII_5007'])<=3)])

plt.figure(1)
plt.clf()
plt.hist(np.log10(data['EW_BROAD_HB']),range=(0.5,3),bins=25,normed=True,facecolor='None',edgecolor='k',lw=2)
plt.hist(np.log10(cdata['EW_BROAD_HB']),range=(0.5,3),bins=25,normed=True,facecolor='None',edgecolor='green',lw=2)
plt.xlabel(r'H$\beta$')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/spectral_plots.HB.5.29.17.png')

print 'Hbeta'
print KStest(data['EW_BROAD_HB'][(np.log10(data['EW_BROAD_HB'])>=0.5)&(np.log10(data['EW_BROAD_HB'])<=3)],cdata['EW_BROAD_HB'][(np.log10(cdata['EW_BROAD_HB'])>=0.5)&(np.log10(cdata['EW_BROAD_HB'])<=3)])

plt.figure(1)
plt.clf()
plt.hist(np.log10(data['EW_MGII']),range=(0.5,3.5),bins=30,normed=True,facecolor='None',edgecolor='k',lw=2)
plt.hist(np.log10(cdata['EW_MGII']),range=(0.5,3.5),bins=30,normed=True,facecolor='None',edgecolor='green',lw=2)
plt.xlabel('MgII')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/spectral_plots.MgII.5.29.17.png')

print 'MgII'
print KStest(data['EW_MGII'][(np.log10(data['EW_MGII'])>=0.5)&(np.log10(data['EW_MGII'])<=3.5)],cdata['EW_MGII'][(np.log10(cdata['EW_MGII'])>=0.5)&(np.log10(cdata['EW_MGII'])<=3.5)])

plt.figure(1)
plt.clf()
plt.hist(np.log10(data['EW_CIV']),range=(0,4),bins=40,normed=True,facecolor='None',edgecolor='k',lw=2)
plt.hist(np.log10(cdata['EW_CIV']),range=(0,4),bins=40,normed=True,facecolor='None',edgecolor='green',lw=2)
plt.xlabel('CIV')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/spectral_plots.CIV.5.29.17.png')

print 'CIV'
print KStest(data['EW_CIV'][(np.log10(data['EW_CIV'])>=0)&(np.log10(data['EW_CIV'])<=4)],cdata['EW_CIV'][(np.log10(cdata['EW_CIV'])>=0)&(np.log10(cdata['EW_CIV'])<=4)])

plt.figure(1)
plt.clf()
plt.hist(data['LOGEDD_RATIO'],range=(-3,1),bins=40,normed=True,facecolor='None',edgecolor='k',lw=2)
plt.hist(cdata['LOGEDD_RATIO'],range=(-3,1),bins=40,normed=True,facecolor='None',edgecolor='green',lw=2)
plt.xlabel(r'log $L/L_{edd}$')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/spectral_plots.Ledd.5.29.17.png')

print 'Ledd'
print KStest(data['LOGEDD_RATIO'][(data['LOGEDD_RATIO']>=-3)&(data['LOGEDD_RATIO']<=1)],cdata['LOGEDD_RATIO'][(cdata['LOGEDD_RATIO']>=-3)&(cdata['LOGEDD_RATIO']<=1)])
