import numpy as np
import pandas as pd
import carmcmc as cm

try:
    dotest
except NameError:
    dotest=False

nsamples=20000

DBdf=pd.read_csv('/home/rumbaugh/DB_QSO_S82.dat',delim_whitespace=True,names=['DBID','ra','dec','SDR5ID','Mi','Micorr','redshift','massBH','Lbol','u','g','r','i','z','Au'],skiprows=2)

if dotest: DBdf=DBdf[:10]

params_df=pd.DataFrame({'DBID':DBdf.DBID})
for x in ['tau','taulb','tauub','sigma','sigmalb','sigmaub']: params_df[x]=np.zeros(len(DBdf))

for i in range(0,len(DBdf)):
    LCdf=pd.read_csv('/home/rumbaugh/QSO_S82/%i'%DBdf.iloc[i]['DBID'],delim_whitespace=True,names=['MJD_u','u','u_err','MJD_g','g','g_err','MJD_r','r','r_err','MJD_i','i','i_err','MJD_z','z','z_err','ra_median','dec_median'])
    DRWmodel=cm.CarmaModel(LCdf.MJD_g.values,LCdf.g.values,LCdf.g_err.values,p=1,q=0)
    DRWsample=DRWmodel.run_mcmc(nsample)
    lomega_samples,sigma_samples=np.sort(DRWsample.get_samples('log_omega').flatten()),np.sort(DRWsample.get_samples('sigma').flatten())
    lomega,sigma=np.median(lomega_samples),np.median(sigma_samples)
    lomegaLB,lomegaUB,sigmaLB,sigmaUB=lomega_samples[iLB],lomega_samples[iUB],sigma_samples[iLB],sigma_samples[iUB]
    params_df.loc[i,'tau'],params_df.loc[i,'sigma']=np.exp(-lomega),sigma
    params_df.loc[i,'taulb'],params_df.loc[i,'tauub'],params_df.loc[i,'sigmalb'],params_df.loc[i,'sigmaub']=np.exp(-lomegaUB),np.exp(-lomegaLB),sigmaLB,sigmaUB
params_df.to_csv('/home/rumbaugh/QSO_S82_CAR1_fits.csv',index=False)
