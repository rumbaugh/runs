import numpy as np
import pyfits as py
import matplotlib.pyplot as plt

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
plt.hist(data['EW_BROAD_HB'],range=(0.5,3),bins=25,normed=True,facecolor='None',edgecolor='k',lw=2)
plt.hist(cdata['EW_BROAD_HB'],range=(0.5,3),bins=25,normed=True,facecolor='None',edgecolor='green',lw=2)
plt.xlabel(r'H$\beta$')
plt.savefig('/home/rumbaugh/var_database/Y3A1/spectral_plots.HB.5.29.17.png')


plt.figure(1)
plt.clf()
plt.hist(data['EW_MGII']/100.,range=(0.5,3.5),bins=30,normed=True,facecolor='None',edgecolor='k',lw=2)
plt.hist(cdata['EW_MGII']/100.,range=(0.5,3.5),bins=30,normed=True,facecolor='None',edgecolor='green',lw=2)
plt.xlabel('MgII')
plt.savefig('/home/rumbaugh/var_database/Y3A1/spectral_plots.MgII.5.29.17.png')


plt.figure(1)
plt.clf()
plt.hist(data['EW_CIV'],range=(0,4),bins=40,normed=True,facecolor='None',edgecolor='k',lw=2)
plt.hist(cdata['EW_CIV'],range=(0,4),bins=40,normed=True,facecolor='None',edgecolor='green',lw=2)
plt.xlabel('CIV')
plt.savefig('/home/rumbaugh/var_database/Y3A1/spectral_plots.CIV.5.29.17.png')


plt.figure(1)
plt.clf()
plt.hist(data['LOGEDD_RATIO'],range=(-3,1),bins=40,normed=True,facecolor='None',edgecolor='k',lw=2)
plt.hist(cdata['LOGEDD_RATIO'],range=(-3,1),bins=40,normed=True,facecolor='None',edgecolor='green',lw=2)
plt.xlabel(r'log $L/L_{edd}$')
plt.savefig('/home/rumbaugh/var_database/Y3A1/spectral_plots.Ledd.5.29.17.png')
