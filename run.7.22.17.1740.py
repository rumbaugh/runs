import carmcmc as cm
import numpy as np
import pandas as pd
import pickle
import pyfits as py
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
import pydl.pydlutils.spheregroup

outlier_window=300
outlier_thresh=0.5
num=5000

normfrac=0.317310507863
nsamples=20000
iLB,iUB=int(normfrac*0.5*nsamples),int((1-0.5*normfrac)*nsamples)


DBdf=pd.read_csv('/home/rumbaugh/DB_QSO_S82.dat',delim_whitespace=True,names=['DBID','ra','dec','SDR5ID','Mi','Micorr','redshift','massBH','Lbol','u','g','r','i','z','Au'],skiprows=4)

drwname='/home/rumbaugh/s82drw_g.dat'
drwdict={'names':('SDR5ID','ra','dec','redshift','M_i','mass_BH','chi2_pdf','ltau','lsig','ltau_lim_lo','ltau_lim_hi','lsig_lim_lo','lsig_lim_hi','edge_flag','Plike','Pnoise','Pinf','mu','npts'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i4','f8','f8','f8','f8','i8')}
crdrw=np.loadtxt(drwname,dtype=drwdict)

drwdf=pd.DataFrame({name:crdrw[name] for name in ['SDR5ID','ra','dec','redshift','ltau','lsig','ltau_lim_lo','ltau_lim_hi','lsig_lim_lo','lsig_lim_hi','edge_flag','Plike','Pnoise','Pinf']})
drwdf=pd.merge(DBdf,drwdf,left_index=True,right_index=True,on=['ra','dec','redshift','SDR5ID'])

vct=drwdf.ltau.value_counts()
tau_cut=vct.index[vct.values>5]
vcs=drwdf.lsig.value_counts()
sig_cut=vcs.index[vcs.values>5]
P_cut=(drwdf.edge_flag.values==0)&(drwdf.Plike.values-drwdf.Pnoise.values>2)&(drwdf.Plike.values-drwdf.Pinf.values>.05)


gkeeptau,gkeepsig=np.in1d(drwdf.ltau.values,tau_cut,invert=True),np.in1d(drwdf.lsig.values,sig_cut,invert=True)
gkeep=gkeeptau*gkeepsig*P_cut

df=drwdf[gkeep]

hdu=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
data=hdu[1].data
#data=data.byteswap().newbyteorder()
data=data[(data['EW_OIII_5007']>0)&(data['EW_BROAD_HB']!=0)&(data['EW_FE_HB_4434_4684']!=0)&(data['FWHM_BROAD_HB']>0)]
data=data[(np.log10(data['EW_OIII_5007'])>0.001)&(np.log10(data['EW_OIII_5007'])<3)&(data['FWHM_BROAD_HB']<15000)]

try:
    fulldf
except NameError:
    sout=pydl.pydlutils.spheregroup.spherematch(data['RA'],data['DEC'],df.ra.values,df.dec.values,0.3/3600)

    matchdata,matchdf=data[sout[0]],df.iloc[sout[1]]
    matchdf.reset_index(inplace=True)
    data_df=pd.DataFrame({x: pd.Series(np.array(matchdata[x]).byteswap().newbyteorder()) for x in ['SDSS_NAME','RA','DEC','REDSHIFT','LOGL1350', 'LOGL1350_ERR',
       'LOGL3000', 'LOGL3000_ERR', 'LOGL5100', 'LOGL5100_ERR', 'LOGLBOL',
       'LOGLBOL_ERR', 'LOGL_BROAD_HA', 'LOGL_BROAD_HA_ERR',
       'LOGL_BROAD_HB', 'LOGL_BROAD_HB_ERR', 'LOGL_BROAD_MGII',
       'LOGL_BROAD_MGII_ERR', 'LOGL_CIV', 'LOGL_CIV_ERR', 'LOGL_MGII',
       'LOGL_MGII_ERR', 'LOGL_NARROW_HA', 'LOGL_NARROW_HA_ERR',
       'LOGL_NARROW_HB', 'LOGL_NARROW_HB_ERR', 'LOGL_NII_6585',
       'LOGL_NII_6585_ERR', 'LOGL_OIII_4959', 'LOGL_OIII_4959_ERR',
       'LOGL_OIII_5007', 'LOGL_OIII_5007_ERR', 'LOGL_SII_6718',
       'LOGL_SII_6718_ERR', 'LOGL_SII_6732', 'LOGL_SII_6732_ERR','EW_BROAD_HA',
       'EW_BROAD_HA_ERR', 'EW_BROAD_HB', 'EW_BROAD_HB_ERR',
       'EW_BROAD_MGII', 'EW_BROAD_MGII_ERR', 'EW_CIV', 'EW_CIV_ERR',
       'EW_FE_HA', 'EW_FE_HA_ERR', 'EW_FE_HB_4434_4684',
       'EW_FE_HB_4434_4684_ERR', 'EW_FE_MGII', 'EW_FE_MGII_ERR', 'EW_MGII',
       'EW_MGII_ERR', 'EW_NARROW_HA', 'EW_NARROW_HA_ERR', 'EW_NARROW_HB',
       'EW_NARROW_HB_ERR', 'EW_NII_6585', 'EW_NII_6585_ERR',
       'EW_OIII_4959', 'EW_OIII_4959_ERR', 'EW_OIII_5007',
       'EW_OIII_5007_ERR', 'EW_SII_6718', 'EW_SII_6718_ERR', 'EW_SII_6732',
       'EW_SII_6732_ERR', 'E_BV', 'FIBER', 'FINT_REST6CM_MJY_OBS',
       'FIRST_FR_TYPE', 'FWHM_BROAD_HA', 'FWHM_BROAD_HA_ERR',
       'FWHM_BROAD_HB', 'FWHM_BROAD_HB_1GAUSS', 'FWHM_BROAD_HB_ERR',
       'FWHM_BROAD_MGII', 'FWHM_BROAD_MGII_1GAUSS', 'FWHM_BROAD_MGII_ERR',
       'FWHM_CIV', 'FWHM_CIV_ERR', 'FWHM_MGII', 'FWHM_MGII_ERR',
       'FWHM_NARROW_HA', 'FWHM_NARROW_HA_ERR', 'FWHM_NARROW_HB',
       'FWHM_NARROW_HB_ERR']})


    fulldf=pd.merge(data_df,matchdf,left_index=True,right_index=True,suffixes=('','_mac'))
    fulldf['RFe']=fulldf['EW_OIII_5007'].values/fulldf['EW_BROAD_HB'].values

nums=10
RFedict={x: {'lb':0.5*x, 'ub': 0.5*(x+1), 'badinds':np.zeros(0,dtype='i8')} for x in np.arange(0,3)}
RFedict[2]['ub']=2
totrandinds=np.zeros(0,dtype='i8')
for x in range(0,3):
    g=np.where((fulldf.RFe.values>RFedict[x]['lb'])&(fulldf.RFe.values<RFedict[x]['ub']))[0]
    RFedict[x]['g']=g
    RFedict[x]['randinds']=np.random.choice(g,nums,replace=False)
    totrandinds=np.append(totrandinds,RFedict[x]['randinds'])



outdf=pd.DataFrame({x: np.zeros(nums*3) for x in ['p','q']})
outdf['group']=np.repeat(np.arange(3),nums)
for i in np.arange(nums*3):
    ind=totrandinds[i]
    x=i/nums

    LCdf=pd.read_csv('/home/rumbaugh/oldDRW/QSO_S82/%i'%fulldf.iloc[ind]['DBID'],delim_whitespace=True,names=['MJD_u','u','u_err','MJD_g','g','g_err','MJD_r','r','r_err','MJD_i','i','i_err','MJD_z','z','z_err','ra_median','dec_median'])
    LCdf=LCdf[(LCdf.g.values>0)&(LCdf.g.values<30)&(LCdf.g_err.values<3)&(LCdf.g_err.values>0)]

    len_lc=len(LCdf)

    while len_lc<10:
        RFedict[x]['badinds']=np.append(RFedict[x]['badinds'],ind)
        gtmp=np.in1d(RFedict[x]['g'],RFedict[x]['badinds'])
        possinds=RFedict[x]['g'][gtmp]
        ind=np.random.choice(possinds)
        RFedict[x]['randinds'][i%nums]=ind
        totrandsinds[i]=ind
        
        LCdf=pd.read_csv('/home/rumbaugh/oldDRW/QSO_S82/%i'%fulldf.iloc[ind]['DBID'],delim_whitespace=True,names=['MJD_u','u','u_err','MJD_g','g','g_err','MJD_r','r','r_err','MJD_i','i','i_err','MJD_z','z','z_err','ra_median','dec_median'])
        LCdf=LCdf[(LCdf.g.values>0)&(LCdf.g.values<30)&(LCdf.g_err.values<3)&(LCdf.g_err.values>0)]
        len_lc=len(LCdf)

    outlier_arr= np.zeros(len(LCdf.g.values),dtype='bool')
    for ipt in np.arange(len(outlier_arr)):
        gthresh=np.where(np.abs(LCdf.MJD_g.values-LCdf.MJD_g.values[ipt])<outlier_window)[0]
        if len(gthresh)>1:
            outlier_arr[ipt]= np.abs(np.median(LCdf.g.values[gthresh])-LCdf.g.values[ipt]) > outlier_thresh

    LCdf=LCdf[outlier_arr==False]
    mjd,mag,magerr=LCdf.MJD_g.values,LCdf.g.values,LCdf.g_err.values
    len_lc=len(mjd)
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
