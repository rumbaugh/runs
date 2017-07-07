import carmcmc as cm
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

normfrac=0.317310507863
nsamples=20000
iLB,iUB=int(normfrac*0.5*nsamples),int((1-0.5*normfrac)*nsamples)

hdu=py.open('/home/rumbaugh/S1_lc.fits')
data=hdu[1].data

data=data[np.random.choice(np.arange(len(data)),num,replace=False)]

outdf=pd.DataFrame({x: np.zeros(num) for x in ['tau','taulb','tauub','sig','siglb','sigub']})
cids=data['COADD_OBJECT_ID']
outdf['cid']=cids
for ind in np.arange(len(cids)):
    DBID=cids[ind]
    len_lc=np.count_nonzero(data[ind]['LC_MJD_G'])
    mjd,mag,magerr=data[ind]['LC_MJD_G'][:len_lc],data[ind]['LC_MAG_PSF_G'][:len_lc],data[ind]['LC_MAGERR_PSF_G'][:len_lc]
    try:
        outlier_arr=pickle.load(open('/home/rumbaugh/CARpickles/SN_fields/S1/%i.outliers_g.pickle'%DBID,'rb'))
    except IOError:
        outlier_arr= np.zeros(len_lc,dtype='bool')
        for ipt in np.arange(len(outlier_arr)):
            gthresh=np.where(np.abs(mjd-mjd[ipt])<outlier_window)[0]
            if len(gthresh)>1:
                outlier_arr[ipt]= np.abs(np.median(mag[gthresh])-mag[ipt]) > outlier_thresh
        pickle.dump(outlier_arr,open('/home/rumbaugh/CARpickles/SN_fields/S1/%i.outliers_g.pickle'%DBID,'wb'))
    mjd,mag,magerr=mjd[outlier_arr==False],mag[outlier_arr==False],magerr[outlier_arr==False]
    DRWmodel=cm.CarmaModel(mjd,mag,magerr,p=1,q=0)
    DRWsample=DRWmodel.run_mcmc(nsamples)

    lomega_samples,sigma_samples=np.sort(DRWsample.get_samples('log_omega').flatten()),np.sort(DRWsample.get_samples('sigma').flatten())
    lomega,sigma=np.median(lomega_samples),np.median(sigma_samples)
    lomegaLB,lomegaUB,sigmaLB,sigmaUB=lomega_samples[iLB],lomega_samples[iUB],sigma_samples[iLB],sigma_samples[iUB]
    pickle.dump(DRWsample,open('/home/rumbaugh/CARpickles/SN_fields/S1/%i.DRWsample_OR.pickle'%DBID,'wb'))
    outdf['tau'][ind],outdf['taulb'][ind],outdf['tauub'][ind],outdf['sig'][ind],outdf['siglb'][ind],outdf['sigub'][ind]=np.exp(-lomega),np.exp(-lomegaUB),np.exp(-lomegaLB),sigma,sigmaLB,sigmaUB
outdf.to_csv('/home/rumbaugh/SN_fields.S1.CAR1fits.csv',index=False)
