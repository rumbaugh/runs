import numpy as np
import pyfits as py
import matplotlib.pyplot as plt

hdu=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
data=hdu[1].data
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
