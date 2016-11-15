import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
import pyfits as py
#nside=16384
nside=64
sdict={16:16,64:4}
        
DESbands=np.array(['g','r','i','z','Y'])
SDSSbands=np.array(['u','g','r','i','z'])
POSSbands=np.array(['g','r','i'])

jbands=np.array(['g','r','i','z'])

coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}

hdu=py.open('/home/rumbaugh/Downloads/OzDES_QSO_20160627.fits')
cro=hdu[1].data
gm=np.arange(len(cro['DES coadd g']),dtype='i8')
for band in jbands: 
    gmtmp=np.where((cro['DES coadd %s'%band]>0)&(cro['DES coadd %s'%band]<40))[0]
    gm=np.intersect1d(gm,gmtmp)
plt.figure(1)
plt.clf()
DEShists=np.zeros(4,dtype='object')
for ib,band in zip(np.arange(4),jbands):
    DEShists[ib]=cro['DES coadd %s'%band][gm]
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.hist((DEShists[0],DEShists[1],DEShists[2],DEShists[3]),range=(16,24),bins=8,color=('green','red','magenta','blue'),label=('g','r','i','z'),normed=True)
plt.legend()

plt.xlim(16,24)
plt.savefig('/home/rumbaugh/DBplots/maghist_plot_griz.ozdes.png')


plt.figure(2)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.scatter(DEShists[0]-DEShists[1],DEShists[2]-DEShists[3],s=2,edgecolor='None',color='r')
plt.xlabel('g-r')
plt.ylabel('i-z')
plt.axvline(0.6,ls='dashed',lw=2,color='k')
plt.axhline(0.55,ls='dashed',lw=2,color='k')
plt.xlim(-1,3)
plt.ylim(-1.5,2)
plt.savefig('/home/rumbaugh/DBplots/colplot_g-r_i-z.ozdes.png')

plt.figure(2)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.scatter(DEShists[1]-DEShists[2],DEShists[2]-DEShists[3],s=2,edgecolor='None',color='r')
plt.xlabel('r-i')
plt.ylabel('i-z')
plt.axvline(0.45,ls='dashed',lw=2,color='k')
plt.axhline(0.55,ls='dashed',lw=2,color='k')
plt.xlim(-1,3)
plt.ylim(-1.5,2)
plt.savefig('/home/rumbaugh/DBplots/colplot_r-i_i-z.ozdes.png')


cr=np.loadtxt('/home/rumbaugh/milliquas_y1a1_coadd_mags.tab',skiprows=1,dtype={'names':('cid','magY','magg','magr','magi','magz'),'formats':('i8','f8','f8','f8','f8','f8')})
gm=np.arange(len(cr),dtype='i8')
for band in jbands: 
    gmtmp=np.where((cr['mag%s'%band]>0)&(cr['mag%s'%band]<40))[0]
    gm=np.intersect1d(gm,gmtmp)
plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
DEShists=np.zeros(4,dtype='object')
for ib,band in zip(np.arange(4),jbands):
    #DEShists[ib]=cr['mag%s'%band][(cr['mag%s'%band]>0)&(cr['mag%s'%band]<40)]
    DEShists[ib]=cr['mag%s'%band][gm]
plt.hist((DEShists[0],DEShists[1],DEShists[2],DEShists[3]),range=(16,24),bins=8,color=('green','red','magenta','blue'),label=('g','r','i','z'),normed=True)

cr=np.loadtxt('/home/rumbaugh/milliquas_lightcurve_entries_SDSS.tab',skiprows=1,dtype={'names':('numrow','cid','MQrownum','magu','magg','magr','magi','magz'),'formats':('i8','i8','i8','f8','f8','f8','f8','f8')},usecols=(0,1,2,13,14,15,16,17))
cids=np.unique(cr['cid'])
medmags={b: np.zeros(len(cids)) for b in SDSSbands}
for cid,i in zip(cids,np.arange(len(cids))):
    g=np.where(cr['cid']==cid)[0]
    if len(g)==1:
        for b in SDSSbands: medmags[b][i]=cr['mag%s'%b][g]
    else:
        for b in SDSSbands: medmags[b][i]=np.median(cr['mag%s'%b][g])
SDSShists=np.zeros(4,dtype='object')
for ib,band in zip(np.arange(4),jbands):
    SDSShists[ib]=medmags[band][(medmags[band]>0)&(medmags[band]<40)]
plt.hist((SDSShists[0],SDSShists[1],SDSShists[2],SDSShists[3]),range=(16,24),bins=8,color=('k','k','k','k'),facecolor='None',lw=4,edgecolor='k',normed=True)
plt.legend()

plt.xlim(16,24)
plt.savefig('/home/rumbaugh/DBplots/maghist_plot_griz.MQ_DES+SDSS.png')

plt.figure(2)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.scatter(DEShists[0]-DEShists[1],DEShists[2]-DEShists[3],s=2,edgecolor='None',color='r')
plt.scatter(SDSShists[0]-SDSShists[1],SDSShists[2]-SDSShists[3],s=2,edgecolor='None',color='b')
plt.xlabel('g-r')
plt.ylabel('i-z')
plt.axvline(0.6,ls='dashed',lw=2,color='k')
plt.axhline(0.55,ls='dashed',lw=2,color='k')
plt.xlim(-1,3)
plt.ylim(-1.5,2)
plt.savefig('/home/rumbaugh/DBplots/colplot_g-r_i-z.MQ_DES+SDSS.png')
plt.figure(2)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.scatter(DEShists[1]-DEShists[2],DEShists[2]-DEShists[3],s=2,edgecolor='None',color='r')
plt.scatter(SDSShists[1]-SDSShists[2],SDSShists[2]-SDSShists[3],s=2,edgecolor='None',color='b')
plt.xlabel('r-i')
plt.ylabel('i-z')
plt.axvline(0.45,ls='dashed',lw=2,color='k')
plt.axhline(0.55,ls='dashed',lw=2,color='k')
plt.xlim(-1,3)
plt.ylim(-1.5,2)
plt.savefig('/home/rumbaugh/DBplots/colplot_r-i_i-z.MQ_DES+SDSS.png')

cr=np.loadtxt('/home/rumbaugh/sdssposs_y1a1_coadd_mags.tab',skiprows=1,dtype={'names':('cid','magY','magg','magr','magi','magz'),'formats':('i8','f8','f8','f8','f8','f8')})
crmagzcopy=np.copy(cr['magz'])
gm=np.arange(len(cr),dtype='i8')
for band in jbands: 
    gmtmp=np.where((cr['mag%s'%band]>0)&(cr['mag%s'%band]<40))[0]
    gm=np.intersect1d(gm,gmtmp)
plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
DEShists=np.zeros(3,dtype='object')
for ib,band in zip(np.arange(4),POSSbands):
    DEShists[ib]=cr['mag%s'%band][gm]
plt.hist((DEShists[0],DEShists[1],DEShists[2]),range=(16,24),bins=8,color=('green','red','magenta'),label=('g','r','i'),normed=True)

cr=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EpochG','EpochR','EpochI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_r_SDSS','g_SDSS','g_ERR','r_SDSS','r_ERR','i_SDSS','i_ERR'),'formats':('f8','f8','|S2','|S2','|S2','|S2','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S2','f8','f8','|S2','|S2','|S2','|S2','|S2','f8','f8','f8','f8','f8','f8','f8')})
SDSShists=np.zeros(3,dtype='object')
POSShists=np.zeros(3,dtype='object')
for ib,sdssband,possband in zip(np.arange(3),['g','r','i'],['G','R','I']):
    SDSShists[ib]=cr['%s_SDSS'%sdssband][(cr['%s_SDSS'%sdssband]>0)&(cr['%s_SDSS'%sdssband]<40)]
    POSShists[ib]=cr['%s_POSS'%possband][(cr['%s_POSS'%possband]>0)&(cr['%s_POSS'%possband]<40)]
plt.hist((POSShists[0],POSShists[1],POSShists[2]),range=(16,24),bins=8,color=('green','red','magenta'),normed=True,alpha=0.4)
plt.hist((SDSShists[0],SDSShists[1],SDSShists[2]),range=(16,24),bins=8,color=('k','k','k'),facecolor='None',lw=4,edgecolor='k',normed=True)
plt.legend()

plt.xlim(16,24)
plt.savefig('/home/rumbaugh/DBplots/maghist_plot_gri.SDSS-POSS+DES.png')

plt.figure(2)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.scatter(DEShists[0]-DEShists[1],DEShists[2]-crmagzcopy[gm],s=2,edgecolor='None',color='r')
plt.xlabel('g-r')
plt.ylabel('i-z')
plt.axvline(0.6,ls='dashed',lw=2,color='k')
plt.axhline(0.55,ls='dashed',lw=2,color='k')
plt.xlim(-1,3)
plt.ylim(-1.5,2)
plt.savefig('/home/rumbaugh/DBplots/colplot_g-r_i-z.SDSS-POSS_DES.png')

plt.figure(2)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.scatter(DEShists[1]-DEShists[2],DEShists[2]-crmagzcopy[gm],s=2,edgecolor='None',color='r')
plt.xlabel('r-i')
plt.ylabel('i-z')
plt.axvline(0.45,ls='dashed',lw=2,color='k')
plt.axhline(0.55,ls='dashed',lw=2,color='k')
plt.xlim(-1,3)
plt.ylim(-1.5,2)
plt.savefig('/home/rumbaugh/DBplots/colplot_r-i_i-z.SDSS-POSS_DES.png')
