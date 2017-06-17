import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.test_compiled.csv')

df=df[(df.cluster!='Cl0849')&(df.cluster!='0225-0019')]
df=df.set_index(df.cluster)

df['perc_cat']=pd.cut(df.perc,[0,.003,0.05,.34,1],labels=[3,2,1,0])

df['perc_code']=3-df.perc_cat.cat.codes

df['sigdiff']=np.abs(df.Sig_red-df.Sig_blue)/np.sqrt(df.Sig_red_Error**2+df.Sig_blue_Error**2)
df['sigdiff_cat']=pd.cut(df.sigdiff,[0,1,2,3,99],labels=[0,1,2,3])
df['sigdiff_code']=df.sigdiff_cat.cat.codes

df['P_DS_cat']=pd.cut(df.P_DS,[0,.003,0.05,.34,1],labels=[3,2,1,0])
df['P_DS_code']=3-df.P_DS_cat.cat.codes

df['P3_sig']=df.P3-df.P3LB
df['P3_cat']=pd.cut(df.P3_sig,[-np.inf,0,np.inf],labels=[-1,0])
df['P3_code']=df.P3_cat.cat.codes-1

df_dists=df[['dist_bcg2x', 'dist_bcg2lw', 'dist_lw2x']]
df['dist_max'],df['dist_min']=df_dists.max(axis=1),df_dists.min(axis=1)
df['dist_metric']=0.5*(df.dist_max+df.dist_min)/60./df.rad
df['dist_cat']=pd.cut(df.dist_metric,[0,0.1,0.25,0.5,1],labels=[0,1,2,3])
df['dist_code']=df.dist_cat.cat.codes

df['BCGvel_norm']=np.abs(df.BCGvel/df.Sig_all)
df['BCGvel_cat']=pd.cut(df.BCGvel_norm,[0,0.5,1,1.5,10],labels=[0,1,2,3])
df['BCGvel_code']=df.BCGvel_cat.cat.codes

df['total_SR_offset']=df[['mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig']].sum(axis=1)
df['mean_SR_offset']=df[['mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig']].mean(axis=1,skipna=True)

df['total_code']=df[['perc_code','sigdiff_code','P_DS_code','P3_code','dist_code','BCGvel_code']].sum(axis=1)
df['mean_code']=df[['perc_code','sigdiff_code','P_DS_code','P3_code','dist_code','BCGvel_code']].mean(axis=1,skipna=True)

dfcode=df[['field','cluster','perc_code','sigdiff_code','P_DS_code','P3_code','dist_code','BCGvel_code','total_SR_offset','mean_SR_offset','total_code','mean_code']]

pca=PCA()

X=np.zeros((len(dfcode),6))
for i,code in zip(np.arange(6),['perc_code','sigdiff_code','P_DS_code','P3_code','dist_code','BCGvel_code']): X[:,i]=dfcode[code].values
pca = PCA()
X_r = pca.fit(X).transform(X)
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))
