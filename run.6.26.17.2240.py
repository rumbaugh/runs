import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.test_compiled.6.26.17.csv')

df=df.set_index(df.cluster)
df=df[(df.cluster!='Cl0849')&(df.cluster!='0225-0019')]

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

df=df.astype({x: float for x in ['perc_code','sigdiff_code']})
df.set_value('RXJ1221B','sigdiff_code',np.nan)
df.set_value('RXJ1221B','perc_code',np.nan)

df['total_SR_offset']=df[['mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig']].sum(axis=1)
df['mean_SR_offset']=df[['mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig']].mean(axis=1,skipna=True)

df['total_code']=df[['perc_code','sigdiff_code','P_DS_code','P3_code','dist_code','BCGvel_code']].sum(axis=1)
df['mean_code']=df[['perc_code','sigdiff_code','P_DS_code','P3_code','dist_code','BCGvel_code']].mean(axis=1,skipna=True)

dfcode=df[['field','cluster','perc_code','sigdiff_code','P_DS_code','P3_code','dist_code','BCGvel_code','total_SR_offset','mean_SR_offset','total_code','mean_code']]
dfcode.to_csv('/home/rumbaugh/Chandra/ORELSE.test_codes.6.26.17.csv',index=False)
plt.figure(1)
plt.clf()
plt.scatter(df.total_code,df.total_SR_offset)
plt.xlabel('Composite Virialization Metric')
plt.ylabel(r'Total Scaling Relation Offset $\left(\sigma\right)$')
plt.savefig('/home/rumbaugh/Chandra/plots/code_vs_SROff.6.26.17.png')
plt.clf()
plt.scatter(df.mean_code,df.mean_SR_offset)
dftmp=df[np.isfinite(df.mean_SR_offset)]
for i in range(0,len(dftmp)):
    if dftmp.index.values[i]=='RXJ1716A':
        plt.text(dftmp.mean_code[i],dftmp.mean_SR_offset[i],'RXJ1716B')
    else:
        plt.text(dftmp.mean_code[i],dftmp.mean_SR_offset[i],dftmp.index.values[i])
plt.xlabel('Mean Composite Virialization Metric')
plt.ylabel(r'Mean Scaling Relation Offset $\left(\sigma\right)$')
plt.savefig('/home/rumbaugh/Chandra/plots/code_vs_SROff.mean.6.26.17.png')
