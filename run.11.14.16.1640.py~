import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
import pyfits as py
#nside=16384
nside=64
sdict={16:16,64:4}
        
DESbands=np.array(['g','r','i','z','Y'])
SDSSbands=np.array(['u','g','r','i','z'])

hdu=py.open('/home/rumbaugh/Downloads/OzDES_QSO_20160627.fits')
cro=hdu[1].data
plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.hist(cro['REDSHIFT'])
plt.savefig('/home/rumbaugh/DBplots/zhist_plot.ozdes.png')
for band in DESbands:
    plt.figure(1)
    plt.clf()
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    plt.hist(cro['DES coadd %s'%band][(cro['DES coadd %s'%band]>0)&(cro['DES coadd %s'%band]<40)],range=(15,25),bins=20)
    plt.savefig('/home/rumbaugh/DBplots/maghist_plot_%s.ozdes.png'%band)


cr=np.loadtxt('/home/rumbaugh/milliquas_y1a1_coadd_mags.tab',skiprows=1,dtype={'names':('cid','magY','magg','magr','magi','magz'),'formats':('i8','f8','f8','f8','f8','f8')})
for band in DESbands:
    plt.figure(1)
    plt.clf()
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    plt.hist(cr['mag%s'%band][(cr['mag%s'%band]>0)&(cr['mag%s'%band]<40)],range=(15,25),bins=20)
    plt.savefig('/home/rumbaugh/DBplots/maghist_plot_%s.MQ_Y1A1.png'%band)

cr=np.loadtxt('/home/rumbaugh/milliquas_lightcurve_entries_SDSS.tab',skiprows=1,dtype={'names':('numrow','cid','MQrownum','magu','magg','magr','magi','magz'),'formats':('i8','i8','i8','f8','f8','f8','f8','f8')},usecols=(0,1,2,13,14,15,16,16))
cids=np.unique(cr['cid'])
medmags={b: np.zeros(len(cids)) for b in SDSSbands}
for cid,i in zip(cids,np.arange(len(cids))):
    g=np.where(cr['cid']==cid)[0]
    if len(g)==1:
        for b in SDSSbands: medmags[b][i]=cr['mag%s'%b][g]
    else:
        for b in SDSSbands: medmags[b][i]=np.median(cr['mag%s'%b][g])
for band in SDSSbands:
    plt.figure(1)
    plt.clf()
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    plt.hist(medmags[band][(medmags[band]>0)&(medmags[band]<40)],range=(15,25),bins=20)
    plt.savefig('/home/rumbaugh/DBplots/maghist_plot_%s.MQ_SDSS.png'%band)

cr=np.loadtxt('/home/rumbaugh/sdssposs_y1a1_coadd_mags.tab',skiprows=1,dtype={'names':('cid','magY','magg','magr','magi','magz'),'formats':('i8','f8','f8','f8','f8','f8')})
for band in DESbands:
    plt.figure(1)
    plt.clf()
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    plt.hist(cr['mag%s'%band][(cr['mag%s'%band]>0)&(cr['mag%s'%band]<40)],range=(15,25),bins=20)
    plt.savefig('/home/rumbaugh/DBplots/maghist_plot_%s.POSS_Y1A1.png'%band)

cr=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EpochG','EpochR','EpochI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_r_SDSS','g_SDSS','g_ERR','r_SDSS','r_ERR','i_SDSS','i_ERR'),'formats':('f8','f8','|S2','|S2','|S2','|S2','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S2','f8','f8','|S2','|S2','|S2','|S2','|S2','f8','f8','f8','f8','f8','f8','f8')})
for sdssband,possband in zip(['g','r','i'],['G','R','I']):
    plt.figure(1)
    plt.clf()
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    plt.hist(cr['%s_POSS'%possband][(cr['%s_POSS'%possband]>0)&(cr['%s_POSS'%possband]<40)],range=(15,25),bins=20,label='POSS %s'%possband)
    plt.hist(cr['%s_SDSS'%sdssband][(cr['%s_SDSS'%sdssband]>0)&(cr['%s_SDSS'%sdssband]<40)],range=(15,25),bins=20,label='SDSS %s'%sdssband,facecolor='None',lw=4,edgecolor='k')
    plt.legend()
    plt.savefig('/home/rumbaugh/DBplots/maghist_plot_%s.SDSS-POSS.png'%sdssband)
plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.hist(cr['redshift'])
plt.savefig('/home/rumbaugh/DBplots/zhist_plot.SDSS-POSS.png')
    
fname='/home/rumbaugh/Downloads/milliquas.txt'
mdict={'names':('RA','DEC','Name','Descrip','Rmag','Bmag','Comment','R','B','Z','Cite','Zcite','Qpct','Xname','Rname','Lobe1','Lobe2'),'formats':('f8','f8','|S27','|S5','f8','f8','|S4','|S2','|S2','f8','|S7','|S7','f8','|S24','|S24','|S24','|S24')}
delims=(11,12,27,5,5,5,4,2,2,7,7,7,4,23,23,23,23)
cr=np.genfromtxt(fname,dtype=mdict,delimiter=delims)
for band in ['R','B']:
    plt.figure(1)
    plt.clf()
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    plt.hist(cr['%smag'%band][(cr['%smag'%band]>0)&(cr['%smag'%band]<40)],range=(15,25),bins=20)
    plt.savefig('/home/rumbaugh/DBplots/maghist_plot_%s.milliquas_full.png'%band)
plt.figure(1)
plt.clf()
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
plt.hist(cr['Z'][np.isnan(cr['Z'])==False])
plt.savefig('/home/rumbaugh/DBplots/zhist_plot.milliquas_full.png')
