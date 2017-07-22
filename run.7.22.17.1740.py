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


hdu=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
data=hdu[1].data
#data=data.byteswap().newbyteorder()
data=data[(data['EW_OIII_5007']>0)&(data['EW_BROAD_HB']!=0)&(data['EW_FE_HB_4434_4684']!=0)&(data['FWHM_BROAD_HB']>0)]
data=data[(np.log10(data['EW_OIII_5007'])>0.001)&(np.log10(data['EW_OIII_5007'])<3)&(data['FWHM_BROAD_HB']<15000)]
EWOIII,EWHB,EWFeII,FWHMHB=data['EW_OIII_5007'],data['EW_BROAD_HB'],data['EW_FE_HB_4434_4684'],data['FWHM_BROAD_HB']#/(1+data['REDSHIFT'])
RFe=EWFeII/EWHB

nums=10
RFedict={x: {'lb':0.5*x, 'ub': 0.5*(x+1), 'badinds':np.zeros(0,dtype='i8')} for x in np.arange(0,4)}
totrandinds=np.zeros(0,dtype='i8')
for x in range(0,4):
    g=np.where((RFe>RFedict[x]['lb'])&(RFe<RFedict[x]['ub']))[0]
    RFedict[x]['g']=g
    RFedict[x]['randinds']=np.random.choice(g,nums,replace=False)
    totrandinds=np.append(totrandinds,RFedict[x]['randinds'])



outdf=pd.DataFrame({x: np.zeros(nums*4) for x in ['p','q']})
outdf['group']=np.repeat(np.arange(4),nums)
for i in np.arange(nums*4):
    ind=totrandinds[i]
    x=i/nums
    len_lc=np.count_nonzero(data[ind]['LC_MJD_G'])
    DBID=data['COADD_OBJECT_ID'][ind]
    while len_lc<10:
        RFedict[x]['badinds']=np.append(RFedict[x]['badinds'],ind)
        gtmp=np.in1d(RFedict[x]['g'],RFedict[x]['badinds'])
        possinds=RFedict[x]['g'][gtmp]
        ind=np.random.choice(possinds)
        RFedict['randinds'][i%nums]=ind
        totrandsinds[i]=ind
        DBID=data['COADD_OBJECT_ID'][ind]
        len_lc=np.count_nonzero(data[ind]['LC_MJD_G'])
    mjd,mag,magerr=np.zeros(len_lc),np.zeros(len_lc),np.zeros(len_lc)
    mjd[:],mag[:],magerr[:]=data[ind]['LC_MJD_G'][:len_lc],data[ind]['LC_MAG_PSF_G'][:len_lc],data[ind]['LC_MAGERR_PSF_G'][:len_lc]
    inf_or_nan=np.ones(len(mjd),dtype='bool')
    for arr in [mjd,mag,magerr]:
        for func in [np.isnan,np.isinf]:
            inf_or_nan*=np.invert(func(arr))
    mjd,mag,magerr=mjd[inf_or_nan],mag[inf_or_nan],magerr[inf_or_nan]
    len_lc=len(mjd)
    outlier_arr= np.zeros(len_lc,dtype='bool')
    for ipt in np.arange(len(outlier_arr)):
        gthresh=np.where(np.abs(mjd-mjd[ipt])<outlier_window)[0]
        if len(gthresh)>1:
            outlier_arr[ipt]= np.abs(np.median(mag[gthresh])-mag[ipt]) > outlier_thresh
    mjd,mag,magerr=mjd[outlier_arr==False],mag[outlier_arr==False],magerr[outlier_arr==False]
    DRWmodel=cm.CarmaModel(mjd,mag,magerr,p=4,q=0)
    try:
        DRWmodel.choose_order(4)
        DRWsample=DRWmodel.run_mcmc(nsamples)
        pickle.dump(DRWsample,open('/home/rumbaugh/CARpickles/%i.DRWsample_OR_chooseorder.pickle'%DBID,'wb'))
        outdf['p'][i],outdf['q'][i]=DRWmodel.p,DRWmodel.q
    except:
        print '%i failed'%DBID
        outdf['p'][i],outdf['q'][i]=0,0
outdf['cid']=data['COADD_OBJECT_ID'][totrandinds]
outdf['DBID']=totrandsinds
outdf.to_csv('/home/rumbaugh/S82.downsample.choose_order.csv',index=False)
