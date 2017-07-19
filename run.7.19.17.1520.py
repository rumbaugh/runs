import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

specdf=pd.read_csv('/home/rumbaugh/SNfields_S2_cen_30122_spec.csv')

fitdf=pd.read_csv('/home/rumbaugh/SN_fields.S2.cen_{}.CAR1fits.csv'.format(ri))

autormsdf=pd.read_csv('/home/rumbaugh/SN_fields.S2.cen_{}.AUTO_RMS.csv'.format(ri))

rmsdf=pd.read_csv('/home/rumbaugh/SN_fields.S2.cen_{}.RMS.csv'.format(ri))

fulldf=pd.merge(fitdf,specdf,left_on=['DataID','cid'],right_on=['dataid','coadd_object_id'],suffixes=('_DR7','_DR13'))
fulldf=pd.merge(fulldf,rmsdf,on=['DataID','cid'],suffixes=('','_RMS'))
fulldf=pd.merge(fulldf,autormsdf,on=['DataID','cid'],suffixes=('','_AUTO'))
fulldf=fulldf[fulldf.numepoch.values>5]

try:
    fulldf.sigma_hat
except AttributeError:
    fulldf['sigma_hat']=fulldf.sig.values
    fulldf['sigma']=0.5*(fulldf.sigma_hat.values**2)*fulldf.tau.values
    fulldf['sigma_err']=0.5*np.sqrt(4*(fulldf.sigma_hat.values*fulldf.tau.values)**2*(0.5*(fulldf.sigub.values-fulldf.siglb.values))**2+fulldf.sigma_hat.values**4*(0.5*(fulldf.tauub.values-fulldf.taulb.values))**2)

cdict={x:y for x,y in zip(['STAR','QSO','GALAXY'],['red','cyan','green'])}

plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
for objclass in ['STAR','QSO','GALAXY']:
    tmpdf=fulldf[fulldf['class'].values==objclass]
    plt.hist(tmpdf.RMS.values,color=cdict[objclass],alpha=0.4,range=(0,4),bins=20)
plt.xlabel('RMS variability (mags)')
plt.ylabel('Number of objects')
plt.savefig('/home/rumbaugh/RMS_hist.SN_fields.S2.cen_{}.RMS.png'.format(ri))

plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
for objclass in ['STAR','QSO','GALAXY']:
    tmpdf=fulldf[fulldf['class'].values==objclass]
    plt.hist(tmpdf.RMS_AUTO.values,color=cdict[objclass],alpha=0.4,range=(0,4),bins=20)
plt.xlabel('RMS variability (mags)')
plt.ylabel('Number of objects')
plt.savefig('/home/rumbaugh/RMS_hist_AUTO.SN_fields.S2.cen_{}.RMS.png'.format(ri))
