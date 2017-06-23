import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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


plt.figure(1)
plt.clf()
plt.scatter(df.ltau,np.log10(df.tau),s=4,edgecolor=None,facecolor='r',color='r',alpha=0.1)
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(xlim[0],xlim[1],100)
plt.plot(xdummy,xdummy,lw=2,color='k',ls='dashed')
plt.xlim(-2,xlim[1])
plt.ylim(ylim[0],ylim[1])
plt.xlabel(r'log(Macleod $\tau$ (days))')
plt.ylabel(r'log(CAR1 fit $\tau$ (days))')
plt.savefig('/home/rumbaugh/S82_CARfit_test.6.22.17.tau.png')



plt.figure(1)
plt.clf()
plt.scatter(df.lsig,np.log10(df.sigma*np.sqrt(365)),s=4,edgecolor=None,facecolor='r',color='r',alpha=0.1)
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(xlim[0],xlim[1],100)
plt.plot(xdummy,xdummy,lw=2,color='k',ls='dashed')
plt.xlim(xlim[0],xlim[1])
plt.ylim(ylim[0],ylim[1])
plt.xlabel(r'log(Macleod $\sigma$)')
plt.ylabel(r'log(CAR1 fit $\sigma$)')
plt.savefig('/home/rumbaugh/S82_CARfit_test.6.22.17.sigma.png')





plt.figure(1)
plt.clf()
plt.scatter(df.ltau-np.log10(df.tau),df.lsig-np.log10(df.sigma*np.sqrt(365)),s=4,edgecolor=None,facecolor='r',color='r',alpha=0.1)
xlim=plt.xlim()
ylim=plt.ylim()
plt.axvline(2,color='gray',lw=1,ls='dashed')
plt.axvline(0.2,color='gray',lw=1,ls='dashed')
plt.axvline(-0.2,color='gray',lw=1,ls='dashed')
plt.axvline(-0.6,color='gray',lw=1,ls='dashed')
plt.axhline(0,color='k',lw=2,ls='dashed')
plt.axvline(0,color='k',lw=2,ls='dashed')
plt.text(1,1.25,'A',color='blue',horizontalalignment='center',verticalalignment='center',fontsize=16)
plt.text(2.5,1.25,'Z',color='red',horizontalalignment='center',verticalalignment='center',fontsize=16)
plt.text(0,1.25,'B',color='green',horizontalalignment='center',verticalalignment='center',fontsize=16)
plt.text(-.4,1.25,'C',color='orange',horizontalalignment='center',verticalalignment='center',fontsize=16)
plt.text(-2,1.25,'D',color='magenta',horizontalalignment='center',verticalalignment='center',fontsize=16)
plt.xlim(-3,3)
plt.ylim(-0.5,1.5)
plt.ylabel(r'log(Macleod $\sigma$)-log(CAR1 fit $\sigma$)')
plt.xlabel(r'log(Macleod $\tau$ (days))-log(CAR1 fit $\tau$ (days))')
plt.savefig('/home/rumbaugh/S82_CARfit_test.6.22.17.tausig_diff.png')


plt.figure(1)
plt.clf()
plt.scatter(df.ltau-np.log10(df.tau),df.medtaulik-df.Plike,s=4,edgecolor=None,facecolor='r',color='r',alpha=0.1)
xlim=plt.xlim()
ylim=plt.ylim()
plt.axvline(0,color='k',lw=2,ls='dashed')
plt.xlim(-3,3)
plt.ylabel(r'log(Macleod likelihood)-log(CAR1 fit likelihood)')
plt.xlabel(r'log(Macleod $\tau$ (days))-log(CAR1 fit $\tau$ (days))')
plt.savefig('/home/rumbaugh/S82_CARfit_test.6.22.17.siglik_diff.png')




plt.figure(1)
plt.clf()
plt.scatter(df.lsig-np.log10(df.sigma*np.sqrt(365)),f.medsiglik-df.Plike,s=4,edgecolor=None,facecolor='r',color='r',alpha=0.1)
xlim=plt.xlim()
ylim=plt.ylim()
plt.axhline(0,color='k',lw=2,ls='dashed')
plt.axvline(0,color='k',lw=2,ls='dashed')
plt.xlim(-0.5,1.5)
plt.xlabel(r'log(Macleod $\sigma$)-log(CAR1 fit $\sigma$)')
plt.ylabel(r'log(Macleod likelihood)-log(CAR1 fit likelihood)')
plt.savefig('/home/rumbaugh/S82_CARfit_test.6.22.17.taulik_diff.png')



