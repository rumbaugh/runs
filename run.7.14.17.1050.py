import numpy as np
import pandas as pd
import pickle
import pyfits as py
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

outlier_window=300
outlier_thresh=0.5
num=5000

ri=30122
normfrac=0.317310507863
nsamples=20000

iLB,iUB=int(normfrac*0.5*nsamples),int((1-0.5*normfrac)*nsamples)

hdu=py.open('/home/rumbaugh/S2_lc.fits')
sndata=hdu[1].data

cenra,cendec=sndata['RA'][ri],sndata['DEC'][ri]
gri=np.sort(np.where((np.abs(cenra-sndata["RA"])<0.3)&(np.abs(cendec-sndata['DEC'])<0.3))[0])
data=sndata[gri]

specdf=pd.read_csv('/home/rumbaugh/SNfields_S2_cen_30122_spec.csv')

fitdf=pd.read_csv('/home/rumbaugh/SN_fields.S2.cen_{}.CAR1fits.csv'.format(ri))

fulldf=pd.merge(fitdf,specdf,left_on=['DataID','cid'],right_on=['dataid','coadd_object_id'],suffixes=('_DR7','_DR13'))
fulldf=fulldf[fulldf.numepoch.values>5]

try:
    fulldf.sigma_hat
except AttributeError:
    fulldf['sigma_hat']=fulldf.sig.values
    fulldf['sigma']=0.5*(fulldf.sigma_hat.values**2)*fulldf.tau.values
cdict={x:y for x,y in zip(['STAR','QSO','GALAXY'],['red','blue','green'])}

plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
for objclass in ['STAR','QSO','GALAXY']:
    tmpdf=fulldf[fulldf['class'].values==objclass]
    plt.scatter(np.log10(tmpdf.sigma.values),np.log10(tmpdf.tau.values),color=cdict[objclass],label=objclass,s=8,edgecolor='None')
plt.xlabel('log(sigma)')
plt.ylabel('log(tau)')
#plt.xlim(-0.01,.15)
plt.legend()
plt.savefig('/home/rumbaugh/specplot_SNfields_S2.cen_30122.png')
