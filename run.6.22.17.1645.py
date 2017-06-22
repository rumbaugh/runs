import numpy as np
import pandas as pd
import carmcmc as cm
import pickle

try:
    dotest
except NameError:
    dotest=False
try:
    tests
except NameError:
    tests=10

normfrac=0.317310507863
nsamples=20000
iLB,iUB=int(normfrac*0.5*nsamples),int((1-0.5*normfrac)*nsamples)

DBdf=pd.read_csv('/home/rumbaugh/DB_QSO_S82.dat',delim_whitespace=True,names=['DBID','ra','dec','SDR5ID','Mi','Micorr','redshift','massBH','Lbol','u','g','r','i','z','Au'],skiprows=2)

if dotest: DBdf=DBdf.iloc[np.random.choice(np.arange(len(DBdf)),tests,replace=False)]

params_df=pd.read_csv('/home/rumbaugh/QSO_S82_CAR1_fits.csv')
for x in ['medsiglik','medtaulik','maxlik','taumaxlik','sigmaxlik']: params_df[x]=np.zeros(len(DBdf))

for i in range(0,len(DBdf)):
    DBID=DBdf.iloc[i]['DBID']
    DRWsample=pickle.load(open('/home/rumbaugh/CARpickles/{:.2f}.DRWsample.pickle'.format(DBID),'rb'))
    tau_samples,sigma_samples,logliks=np.exp(-DRWsample.get_samples('log_omega').flatten()),DRWsample.get_samples('sigma').flatten(),DRWsample.get_samples('loglik').flatten()
    medtau,medsig=np.median(tau_samples),np.median(sigma_samples)
    gmedtau,gmedsig=np.where(medtau==tau_samples)[0],np.where(medsig==sigma_samples)[0]
    medsiglik,medtaulik=np.max(logliks[gmedsig]),np.max(logliks[gmedtau])
    maxlik=np.max(logliks)
    gmaxlik=np.where(logliks==maxlik)[0]
    if len(gmaxlik)!=():gmaxlik=gmaxlik[0]
    taumaxlik,sigmaxlik=tau_samples[gmaxlik],sigma_samples[gmaxlik]
    params_df.iloc[i]['medsiglik'],params_df.iloc[i]['medtaulik'],params_df.iloc[i]['maxlik'],params_df.iloc[i]['taumaxlik'],params_df.iloc[i]['sigmaxlik']=medsiglik,medtaulik,maxlik,taumaxlik,sigmaxlik
params_df.to_csv('/home/rumbaugh/QSO_S82_CAR1_fits_wlik.csv',index=False)
