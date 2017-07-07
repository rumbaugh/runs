import carmcmc as cm
import numpy as np
import pandas as pd
import pickle
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

outlier_window=300
outlier_thresh=0.5
num=5000

normfrac=0.317310507863
nsamples=20000
iLB,iUB=int(normfrac*0.5*nsamples),int((1-0.5*normfrac)*nsamples)

df=pd.read_csv('/home/rumbaugh/Eric_LC_S2.csv',skipinitialspace=True,names=['COADD_OBJECT_ID','RA','DEC','MJD','MAG','MAGERR','BAND','FLAGS'])

df=df[df.BAND.values=='g']

df.reset_index(inplace=True)

cids=df.COADD_OBJECT_ID.unique()

cids_rand=np.random.choice(cids,num,replace=False)

df=df[np.in1d(df.COADD_OBJECT_ID.values,cids_rand)]

df.reset_index(inplace=True)
outdf=pd.DataFrame({x: np.zeros(num) for x in ['tau','taulb','tauub','sig','siglb','sigub']})
outdf['cid']=cids_rand
for ind in np.arange(len(cids_rand)):
    DBID=cids_rand[ind]
    LCdf=df[df.COADD_OBJECT_ID.values==DBID]
    try:
        outlier_arr=pickle.load(open('/home/rumbaugh/CARpickles/SN_fields/S2/%i.outliers_g.pickle'%DBID,'rb'))
    except IOError:
        outlier_arr= np.zeros(len(LCdf.MAG.values),dtype='bool')
        for ipt in np.arange(len(outlier_arr)):
            gthresh=np.where(np.abs(LCdf.MJD.values-LCdf.MJD.values[ipt])<outlier_window)[0]
            if len(gthresh)>1:
                outlier_arr[ipt]= np.abs(np.median(LCdf.MAG.values[gthresh])-LCdf.MAG.values[ipt]) > outlier_thresh
        pickle.dump(outlier_arr,open('/home/rumbaugh/CARpickles/SN_fields/S2/%i.outliers_g.pickle'%DBID,'wb'))
    LCdf=LCdf[outlier_arr==False]
    DRWmodel=cm.CarmaModel(LCdf.MJD.values,LCdf.MAG.values,LCdf.MAGERR.values,p=1,q=0)
    DRWsample=DRWmodel.run_mcmc(nsamples)

    lomega_samples,sigma_samples=np.sort(DRWsample.get_samples('log_omega').flatten()),np.sort(DRWsample.get_samples('sigma').flatten())
    lomega,sigma=np.median(lomega_samples),np.median(sigma_samples)
    lomegaLB,lomegaUB,sigmaLB,sigmaUB=lomega_samples[iLB],lomega_samples[iUB],sigma_samples[iLB],sigma_samples[iUB]
    pickle.dump(DRWsample,open('/home/rumbaugh/CARpickles/SN_fields/S2/%i.DRWsample_OR.pickle'%DBID,'wb'))
    outdf['tau'][ind],outdf['taulb'][ind],outdf['tauub'][ind],outdf['sig'][ind],outdf['siglb'][ind],outdf['sigub'][ind]=np.exp(-lomega),np.exp(-lomegaUB),np.exp(-lomegaLB),sigma,sigmaLB,sigmaUB
outdf.to_csv('/home/rumbaugh/SN_fields.S2.CAR1fits.csv',index=False)
