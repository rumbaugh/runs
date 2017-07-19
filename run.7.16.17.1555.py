import numpy as np
import pandas as pd
import scipy.integrate
import matplotlib.pyplot as plt

def gauss(x):
    return 1/np.sqrt(2*np.pi)*np.exp(-0.5*x**2)

gtrials=10000
gsigs=np.linspace(5,0,gtrials)
try:
    gaussints
except NameError:
    gaussints=np.zeros(gtrials)
    for x,i in zip(gsigs,np.arange(gtrials)):
        gint,dum=scipy.integrate.quad(gauss,-x,x)
        gaussints[i]=1-gint


vcdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.velcenMC.csv',index_col='cluster')
vcdf=vcdf.rename(columns={'zcen':'zmed'})

df=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.test_compiled.7.16.17.csv')

df=df[(df.cluster!='Cl0849')&(df.cluster!='0225-0019')]
df=df.set_index(df.cluster)
df=pd.merge(df,vcdf,left_index=True,right_index=True)
perc_sinds=np.searchsorted(gaussints,df.perc)
df['perc_norm']=gsigs[perc_sinds]

df['sigdiff']=np.abs(df.Sig_red-df.Sig_blue)/np.sqrt(df.Sig_red_Error**2+df.Sig_blue_Error**2)

P_DS_sinds=np.searchsorted(gaussints,df.P_DS)
df['P_DS_norm']=gsigs[P_DS_sinds]

df['P3_sig']=df.P3-df.P3LB
df['P3_cat']=pd.cut(df.P3_sig,[-np.inf,0,np.inf],labels=[-1,0])
df['P3_norm']=df.P3_cat.cat.codes-1

df['P4_sig']=df.P4-df.P4LB
df['P4_cat']=pd.cut(df.P4_sig,[-np.inf,0,np.inf],labels=[-1,0])
df['P4_norm']=df.P4_cat.cat.codes-1

df_dists=df[['dist_bcg2x', 'dist_bcg2lw', 'dist_lw2x']]
df['dist_max'],df['dist_min']=df_dists.max(axis=1),df_dists.min(axis=1)
df['dist_metric']=0.5*(df.dist_max+df.dist_min)
df['dist_norm']=df.dist_metric/df.LWerr
df['dist_bcg2x_norm'],df['dist_bcg2lw_norm'],df['dist_lw2x_norm']=df['dist_bcg2x']/df.LWerr,df['dist_bcg2lw']/df.LWerr,df['dist_lw2x']/df.LWerr

df['BCGvel_norm']=(df.BCGvel-df.zmed)/df.zUB
df.BCGvel_norm[df.BCGvel_norm<1]=(df.zmed[df.BCGvel_norm<1]-df.BCGvel[df.BCGvel_norm<1])/df.zLB[df.BCGvel_norm<1]


#df.set_value('RXJ1221B','sigdiff',np.nan)
#df.set_value('RXJ1221B','perc_norm',np.nan)


df['total_SR_offset']=df[['mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig']].sum(axis=1)
df['mean_SR_offset']=df[['mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig']].mean(axis=1,skipna=True)
df['total_SR_LxTlit_offset']=df[['mindistlit_LxT','mindistfit_sigT','mindistfit_Lxsig']].sum(axis=1)
df['mean_SR_LxTlit_offset']=df[['mindistlit_LxT','mindistfit_sigT','mindistfit_Lxsig']].mean(axis=1,skipna=True)

plt.figure(1)
plt.clf()
plt.errorbar(df.mean_SR_offset.values,df.qfrac.values,yerr=df.qfracerr.values,color='r',fmt='o',capsize=3,mew=1,ms=4)
plt.xlabel(r'Mean Scaling Relation Offset ($\sigma$)')
plt.ylabel('Quiescent Fraction')
plt.savefig('/home/rumbaugh/SRoffset_vs_Qfrac.png')


plt.figure(1)
plt.clf()
plt.errorbar(df.mean_SR_LxTlit_offset.values,df.zcen.values,yerr=df.qfracerr.values,color='r',fmt='o',capsize=3,mew=1,ms=4)
plt.xlabel(r'Mean Scaling Relation Offset ($\sigma$)')
plt.ylabel('Redshift')
plt.savefig('/home/rumbaugh/SRoffset_LxTlit_vs_Zcen.png')

plt.figure(1)
plt.clf()
plt.errorbar(df.mean_SR_offset.values,df.zcen.values,yerr=df.qfracerr.values,color='r',fmt='o',capsize=3,mew=1,ms=4)
plt.xlabel(r'Mean Scaling Relation Offset ($\sigma$)')
plt.ylabel('Redsift')
plt.savefig('/home/rumbaugh/SRoffset_vs_Zcen.png')


plt.figure(1)
plt.clf()
plt.errorbar(df.mean_SR_LxTlit_offset.values,df.qfrac.values,yerr=df.qfracerr.values,color='r',fmt='o',capsize=3,mew=1,ms=4)
plt.xlabel(r'Mean Scaling Relation Offset ($\sigma$)')
plt.ylabel('Quiescent Fraction')
plt.savefig('/home/rumbaugh/SRoffset_LxTlit_vs_Qfrac.png')


plt.figure(1)
plt.clf()
plt.errorbar(df.zcen.values,df.qfrac.values,yerr=df.qfracerr.values,color='r',fmt='o',capsize=3,mew=1,ms=4)
plt.xlabel('Redshift')
plt.ylabel('Quiescent Fraction')
plt.savefig('/home/rumbaugh/Zcen_vs_Qfrac.png')
