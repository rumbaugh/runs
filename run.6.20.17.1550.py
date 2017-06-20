import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/S82_CAR1_fits.posteriors.pdf')

try:
    numrands
except NameError:
    numrands=200

DBdf=pd.read_csv('/home/rumbaugh/DB_QSO_S82.dat',delim_whitespace=True,names=['DBID','ra','dec','SDR5ID','Mi','Micorr','redshift','massBH','Lbol','u','g','r','i','z','Au'],skiprows=2)

drwname='/home/rumbaugh/s82drw_g.dat'
drwdict={'names':('SDR5ID','ra','dec','redshift','M_i','mass_BH','chi2_pdf','ltau','lsig','ltau_lim_lo','ltau_lim_hi','lsig_lim_lo','lsig_lim_hi','edge_flag','Plike','Pnoise','Pinf','mu','npts'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i4','f8','f8','f8','f8','i8')}
crdrw=np.loadtxt(drwname,dtype=drwdict)

drwdf=pd.DataFrame({name:crdrw[name] for name in ['SDR5ID','ra','dec','redshift','ltau','lsig','ltau_lim_lo','ltau_lim_hi','lsig_lim_lo','lsig_lim_hi']})
drwdf=pd.merge(DBdf,drwdf,left_index=True,right_index=True,on=['ra','dec','redshift','SDR5ID'])

gkeep=np.in1d(drwdf.lsig.values,[  -0.8,  -10.0,  -0.95, -0.975, -0.675,   -0.9, -0.775,  -0.85,
                -1.0, -0.575,   -0.5, -1.175, -0.875, -0.925, -0.725, -0.625,
               -0.65, -1.025,   -0.6,   -1.1, -1.225,   -1.3,   -4.0,-1.475000],invert=True)

vct=drwdf.ltau.value_counts()
tau_cut=vct.index[vct.values>5]
vcs=drwdf.lsig.value_counts()
sig_cut=vcs.index[vcs.values>5]

gkeeptau,gkeepsig=np.in1d(drwdf.ltau.values,tau_cut,invert=True),np.in1d(drwdf.lsig.values,sig_cut,invert=True)
gkeep=gkeeptau*gkeepsig

drwdf=drwdf[gkeep]

fitdf=pd.read_csv('/home/rumbaugh/QSO_S82_CAR1_fits.csv')
#fitdf['sigma']=np.sqrt(0.5*fitdf.sigma.values**2*fitdf.tau.values)

df=pd.merge(fitdf,drwdf,on='DBID')

grand=np.random.choice(np.arange(len(df)),numrands,replace=False)
gsort=grand[np.argsort(fitdf.tau.values[grand])]
for i,DBID in zip(gsort,df.DBID.values[gsort]):
    sample=pickle.load(open("/home/rumbaugh/CARpickles/{}.DRWsample.pickle".format(DBID),'rb'))
    sample.plot_2dkde('log_omega','sigma',doPlotStragglers=False)
    fig=plt.gcf()
    ax0=fig.get_axes()[0]
    macltau,maclsig,macltauLB,macltauUB,maclsigLB,maclsigUB=df.ltau[i],df.lsig[i],df.ltau_lim_lo[i],df.ltau_lim_hi[i],df.lsig_lim_lo[i],df.lsig_lim_hi[i]
    maclomega,maclomegaUB,maclomegaLB=-macltau,-macltauLB,-macltauUB
    lomerrl,lomerru,sigerrl,sigerru=np.log(np.exp(maclomega)-np.exp(maclomegaLB)),np.log(np.exp(maclomegaUB)-np.exp(maclomega)),np.exp(maclsig)-np.exp(maclsigLB),np.exp(maclsigUB)-np.exp(maclsig)
    ax0.errorbar([maclomega],[np.exp(maclsig)],xerr=[[lomerrl],[lomerru]],yerr=[[sigerrl],[sigerru]],color='r',fmt='ro',lw=2,capsize=3,mew=1)
    ax0.text(0.5,0.9,'%i:ltau=%.1f(%.1f),lsig=%.1f'%(DBID,np.log10(df.tau[i]),-np.log(df.tau[i]),np.log10(df.sigma[i])),fotnsize=20,transform=ax0.transAxes,horizontalalignment='center')
    fig.savefig(psfpdf,format='pdf')
    plt.clf()
    plt.close('all')
psfpdf.close()
