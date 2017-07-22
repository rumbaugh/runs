import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1=pd.read_csv('/home/rumbaugh/SN_fields.S1.AUTO_CAR1fits.csv')
df1['field']='S1'
df2=pd.read_csv('/home/rumbaugh/SN_fields.S2.AUTO_CAR1fits.csv')
df2['field']='S2'
df=df1.append(df2)

try:
    df.sigma_hat
except AttributeError:
    df['sigma_hat']=df.sig.values
    df['sigma']=0.5*(df.sigma_hat.values**2)*df.tau.values
    df['sigma_err']=0.5*np.sqrt(4*(df.sigma_hat.values*df.tau.values)**2*(0.5*(df.sigub.values-df.siglb.values))**2+df.sigma_hat.values**4*(0.5*(df.tauub.values-df.taulb.values))**2)


plt.figure(1)
plt.clf()
plt.errorbar(df.tau.values,df.sigma.values,xerr=[df.tau.values-df.taulb.values,df.tauub.values-df.tau.values],yerr=df.sigma_err.values,fmt='o',capsize=2,mew=0,ms=3,alpha=0.5)
plt.xlim(0,2200)
plt.ylim(0,0.75)
plt.xlabel(r'$\sigma^2$')
plt.ylabel(r'$\tau$ (days)')

plt.savefig('/home/rumbaugh/SN_fields.tau_vs_sigma.AUTO.CAR1fits.png')

plt.figure(1)
plt.clf()
plt.hist(df.sigma.values,color='k',alpha=0.5,label='All',range=(0,0.75),bins=12)
plt.hist(df[df.field.values=='S1'].sigma.values,color='r',alpha=0.5,label='S1',range=(0,0.75),bins=12))
plt.hist(df[df.field.values=='S2'].sigma.values,color='b',alpha=0.5,label='S2',range=(0,0.75),bins=12))
plt.xlabel(r'$\sigma^2$')
plt.ylabel('Number of Objects')
plt.legend()
plt.savefig('/home/rumbaugh/SN_fields.sigma_hist.AUTO.CAR1fits.png')
