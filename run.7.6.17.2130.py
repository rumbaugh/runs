import numpy as np
import pyfits as py
import matplotlib.pyplot as plt

hdu=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
data=hdu[1].data
data=data[(data['EW_OIII_5007']!=0)&(data['EW_BROAD_HB']!=0)&(data['EW_FE_HB_4434_4684']!=0)&(data['FWHM_BROAD_HB']!=0)]

plt.figure(1)
plt.clf()
EWOIII,EWHB,EWFeII,FWHMHB=data['EW_OIII_5007']/(1+data['REDSHIFT']),data['EW_BROAD_HB']/(1+data['REDSHIFT']),data['EW_FE_HB_4434_4684']/(1+data['REDSHIFT']),data['FWHM_BROAD_HB']#/(1+data['REDSHIFT'])
RFe=EWFeII/EWHB
try:
    smOIII
except NameError:
    smOIII=np.zeros(len(RFe))

    for RFetmp,HBtmp,i in zip(RFe,FWHMHB,np.arange(len(RFe))):
        smOIII[i]=np.mean(EWOIII[(np.abs(RFetmp-RFe)<0.2)&(np.abs(HBtmp-FWHMHB)<1000)])

    logEWOIII=np.log10(smOIII)
cmap = plt.cm.get_cmap('gist_rainbow_r')


sc = plt.scatter(RFe,FWHMHB, c=logEWOIII, vmin=0.7, vmax=1.6, s=2, edgecolor='None', cmap=cmap)
plt.axvline(0,c='gray')
plt.axvline(0.6,c='gray')
plt.axvline(1.5,c='gray')

plt.axhline(5000,c='gray')
plt.axhline(8000,c='gray')
plt.axhline(3000,c='gray')
plt.xlim(-0.2,3)
plt.ylim(0,15000)
plt.xlabel(r'R$_{FeII}$')
plt.ylabel(r'FHWM$_{H\beta}$ (km/s)')
clb=plt.colorbar(sc)
clb.set_label('log EW(OIII)')#, labelpad=-40, y=1.05, rotation=0)
plt.savefig('/home/rumbaugh/DR7_RFe-FHMWHB-OIII.png')
