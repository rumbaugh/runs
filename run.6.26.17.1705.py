import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/S82_CAR1_fits.posteriors.6.26.17.pdf')
psfpdf2=bpdf.PdfPages('/home/rumbaugh/S82_CAR1_fits.assess_fit.6.26.17.pdf')

try:
    numrands
except NameError:
    numrands=25

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

fitdf=pd.read_csv('/home/rumbaugh/QSO_S82_CAR1_fits.csv')
#fitdf['sigma']=np.sqrt(0.5*fitdf.sigma.values**2*fitdf.tau.values)

df=pd.merge(fitdf,drwdf,on='DBID')

df['ltaudiff']=df.ltau-np.log10(df.tau)
df['group']=pd.cut(df.ltaudiff,[-np.inf,-0.6,-0.2,0.2,2,np.inf],labels=['D','C','B','A','Z'])

coldict={'A':'blue','B':'green','C':'orange','D':'magenta','Z':'red'}

grand=np.zeros(0,dtype='i8')
for group in ['A','B','C','D']:
    grand=np.append(grand,np.random.choice(df.index[df.group==group],numrands,replace=False))
grand=np.append(grand,np.random.choice(df.index[df.group=='Z'],5,replace=False))

for i,DBID in zip(grand,df.DBID.values[grand]):
    sample=pickle.load(open("/home/rumbaugh/CARpickles/{}.DRWsample.pickle".format(DBID),'rb'))
    sample.plot_2dkde('log_omega','sigma',doPlotStragglers=False)
    fig=plt.gcf()
    ax0=fig.get_axes()[0]
    macltau,maclsig,macltauLB,macltauUB,maclsigLB,maclsigUB=df.ltau[i],df.lsig[i]-np.log10(np.sqrt(365)),df.ltau_lim_lo[i],df.ltau_lim_hi[i],df.lsig_lim_lo[i]-np.log10(np.sqrt(365)),df.lsig_lim_hi[i]-np.log10(np.sqrt(365))
    maclomega,maclomegaUB,maclomegaLB=-macltau*np.log(10),-macltauLB*np.log(10),-macltauUB*np.log(10)
    lomerrl,lomerru,sigerrl,sigerru=maclomega-maclomegaLB,maclomegaUB-maclomega,10**(maclsig)-10**(maclsigLB),10**(maclsigUB)-10**(maclsig)
    ax0.errorbar([maclomega],[10**(maclsig)],xerr=[[lomerrl],[lomerru]],yerr=[[sigerrl],[sigerru]],color='r',fmt='ro',lw=2,capsize=3,mew=1)
    ax0.text(0.5,0.9,'%i:ltau=%.1f(%.1f),lsig=%.1f'%(DBID,np.log10(df.tau[i]),-np.log(df.tau[i]),np.log10(df.sigma[i])),fontsize=15,transform=ax0.transAxes,horizontalalignment='center',color=coldict[df.group[i]])
    fig.savefig(psfpdf,format='pdf')
    plt.clf()
    plt.close('all')
    plt.figure(1)
    plt.clf()
    sample.assess_fit(doShow=False)
    plt.subplots_adjust(hspace=0.25)
    plt.subplots_adjust(top=0.92)
    fig=plt.gcf()
    plt.text(0.5,0.95,'%i:ltau=%.1f(%.1f),lsig=%.1f'%(DBID,np.log10(df.tau[i]),-np.log(df.tau[i]),np.log10(df.sigma[i])),fontsize=15,transform=fig.transFigure,horizontalalignment='center',color=coldict[df.group[i]])
    fig.savefig(psfpdf2,format='pdf',dpi=400)
psfpdf.close()
psfpdf2.close()
