import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
import pandas as pd
import pydl.pydlutils.spheregroup


hdu=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
data=hdu[1].data
#data=data.byteswap().newbyteorder()
data=data[(data['EW_OIII_5007']>0)&(data['EW_BROAD_HB']!=0)&(data['EW_FE_HB_4434_4684']!=0)&(data['FWHM_BROAD_HB']>0)]
data=data[(np.log10(data['EW_OIII_5007'])>0.001)&(np.log10(data['EW_OIII_5007'])<3)&(data['FWHM_BROAD_HB']<15000)]

plt.figure(1)
plt.clf()
EWOIII,EWHB,EWFeII,FWHMHB=data['EW_OIII_5007'],data['EW_BROAD_HB'],data['EW_FE_HB_4434_4684'],data['FWHM_BROAD_HB']#/(1+data['REDSHIFT'])
RFe=EWFeII/EWHB
gFe=np.where((RFe<3)&(RFe>0.001))[0]
EWOIII,FWHMHB,RFe=EWOIII[gFe],FWHMHB[gFe],RFe[gFe]
try:
    smOIII
except NameError:
    smOIII=np.zeros(len(RFe))

    for RFetmp,HBtmp,i in zip(RFe,FWHMHB,np.arange(len(RFe))):
        smOIII[i]=np.mean(EWOIII[(np.abs(RFetmp-RFe)<0.2)&(np.abs(HBtmp-FWHMHB)<1000)])

    logEWOIII=np.log10(smOIII)
cmap = plt.cm.get_cmap('gist_rainbow_r')


sc = plt.scatter(RFe,FWHMHB, c=logEWOIII, vmin=0.7, vmax=1.6, s=2, edgecolor='None', cmap=cmap)
plt.axvline(0,c='gray')
plt.axvline(0.6,c='gray')
plt.axvline(1.5,c='gray')

plt.axhline(5000,c='gray')
plt.axhline(8000,c='gray')
plt.axhline(3000,c='gray')
plt.xlim(-0.2,3)
plt.ylim(0,15000)
plt.xlabel(r'R$_{FeII}$')
plt.ylabel(r'FHWM$_{H\beta}$ (km/s)')
clb=plt.colorbar(sc)
clb.set_label('log EW(OIII)')#, labelpad=-40, y=1.05, rotation=0)
plt.savefig('/home/rumbaugh/DR7_RFe-FHMWHB-OIII.png')

data=data[gFe]

DBdf=pd.read_csv('/home/rumbaugh/DB_QSO_S82.dat',delim_whitespace=True,names=['DBID','ra','dec','SDR5ID','Mi','Micorr','redshift','massBH','Lbol','u','g','r','i','z','Au'],skiprows=2)

drwname='/home/rumbaugh/s82drw_g.dat'
drwdict={'names':('SDR5ID','ra','dec','redshift','M_i','mass_BH','chi2_pdf','ltau','lsig','ltau_lim_lo','ltau_lim_hi','lsig_lim_lo','lsig_lim_hi','edge_flag','Plike','Pnoise','Pinf','mu','npts'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i4','f8','f8','f8','f8','i8')}
crdrw=np.loadtxt(drwname,dtype=drwdict)

drwdf=pd.DataFrame({name:crdrw[name] for name in ['SDR5ID','ra','dec','redshift','ltau','lsig','ltau_lim_lo','ltau_lim_hi','lsig_lim_lo','lsig_lim_hi','edge_flag','Plike','Pnoise','Pinf']})
drwdf=pd.merge(DBdf,drwdf,left_index=True,right_index=True,on=['ra','dec','redshift','SDR5ID'])

gkeep=np.in1d(drwdf.lsig.values,[  -0.8,  -10.0,  -0.95, -0.975, -0.675,   -0.9, -0.775,  -0.85,
                -1.0, -0.575,   -0.5, -1.175, -0.875, -0.925, -0.725, -0.625,
               -0.65, -1.025,   -0.6,   -1.1, -1.225,   -1.3,   -4.0,-1.475000],invert=True)

vct=drwdf.ltau.value_counts()
tau_cut=vct.index[vct.values>5]
vcs=drwdf.lsig.value_counts()
sig_cut=vcs.index[vcs.values>5]
P_cut=(drwdf.edge_flag.values==0)&(drwdf.Plike.values-drwdf.Pnoise.values>2)&(drwdf.Plike.values-drwdf.Pinf.values>.05)

gkeeptau,gkeepsig=np.in1d(drwdf.ltau.values,tau_cut,invert=True),np.in1d(drwdf.lsig.values,sig_cut,invert=True)
gkeep=gkeeptau*gkeepsig*P_cut

drwdf=drwdf[gkeep]

fitdf=pd.read_csv('/home/rumbaugh/QSO_S82_CAR1_fits_wlik.csv')
#fitdf['sigma']=np.sqrt(0.5*fitdf.sigma.values**2*fitdf.tau.values)

df=pd.merge(fitdf,drwdf,on='DBID')

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
try:
    sm_dict
except NameError:
    sm_dict={}

for mapper,mappername in zip([np.log10(fulldf.sigma.values*np.sqrt(365)),fulldf.lsig.values,np.log10(fulldf.tau.values),df.ltau.values],['lsig','lsig(Mac)','ltau','ltau(Mac)']):

    plt.figure(1)
    plt.clf()

    try:
        sm_dict[mappername]
    except KeyError:
        sm=np.zeros(len(mapper))

        for RFetmp,HBtmp,i in zip(fulldf.RFe.values,fulldf.FWHM_BROAD_HB.values,np.arange(len(mapper))):
            sm[i]=np.mean(10**mapper[(np.abs(RFetmp-fulldf.RFe.values)<0.2)&(np.abs(HBtmp-fulldf.FWHM_BROAD_HB.values)<1000)])

        sm_dict[mappername]=np.log10(sm)
    sm=sm_dict[mappername]
    cmap = plt.cm.get_cmap('gist_rainbow_r')
    sc = plt.scatter(fulldf.RFe.values,fulldf.FWHM_BROAD_HB.values, c=sm, vmin=0.7, vmax=1.6, s=2, edgecolor='None', cmap=cmap)
    plt.axvline(0,c='gray')
    plt.axvline(0.6,c='gray')
    plt.axvline(1.5,c='gray')

    plt.axhline(5000,c='gray')
    plt.axhline(8000,c='gray')
    plt.axhline(3000,c='gray')
    plt.xlim(-0.2,3)
    plt.ylim(0,15000)
    plt.xlabel(r'R$_{FeII}$')
    plt.ylabel(r'FHWM$_{H\beta}$ (km/s)')
    clb=plt.colorbar(sc)
    clb.set_label(mappername)#, labelpad=-40, y=1.05, rotation=0)
    plt.savefig('/home/rumbaugh/DR7_RFe-FHMWHB-{}.png'.format(mappername))
