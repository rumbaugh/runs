import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv('/home/rumbaugh/SN_fields.S1.AUTO_CAR1fits.csv')
df1['field']='S1'
df2=pd.read_csv('/home/rumbaugh/SN_fields.S2.AUTO_CAR1fits.csv')
df2['field']='S2'
df=df1.append(df2)

try:
    fulldf.sigma_hat
except AttributeError:
    fulldf['sigma_hat']=fulldf.sig.values
    fulldf['sigma']=0.5*(fulldf.sigma_hat.values**2)*fulldf.tau.values
    fulldf['sigma_err']=0.5*np.sqrt(4*(fulldf.sigma_hat.values*fulldf.tau.values)**2*(0.5*(fulldf.sigub.values-fulldf.siglb.values))**2+fulldf.sigma_hat.values**4*(0.5*(fulldf.tauub.values-fulldf.taulb.values))**2)


plt.figure(1)
plt.clf()
plt.errorbar(fulldf.tau.values,fulldf.sigma.values,xerr=[fulldf.tau.values-fulldf.taulb.values,fulldf.tauub.values-fulldf.tau.values],yerr=df.sigma_err.values,fmt='o',capsize=2,mew=0,ms=3,alpha=0.5)
plt.xlabel(r'$\sigma**2$')
plt.ylabel(r'$\tau$ (days)')

plt.savefig('/home/rumbaugh/SN_fields.tau_vs_sigma.AUTO.CAR1fits.png')

plt.figure(1)
plt.clf()
plt.hist(fulldf.sigma.values,color='k',alpha=0.5,label='All')
plt.hist(fulldf[fulldf.field.values=='S1'].sigma.values,color='r',alpha=0.5,label='S1')
plt.hist(fulldf[fulldf.field.values=='S2'].sigma.values,color='b',alpha=0.5,label='S2')
plt.xlabel(r'$\sigma**2$')
plt.ylabel(r'$\tau$ (days)')
plt.legend()
plt.savefig('/home/rumbaugh/SN_fields.sigma_hist.AUTO.CAR1fits.png')
