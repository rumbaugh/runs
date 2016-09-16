import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/optical_matching.py')

crx=np.loadtxt('/home/rumbaugh/Chandra/548/photometry/548.xray_phot.soft_hard_full.dat',dtype={'names':('raX','decX','fluxX_soft','fluxX_hard','fluxX_full','netcnts_corrX_soft','netcnts_corrX_hard','netcnts_corrX_full','sigX_soft','sigX_hard','sigX_full','dummy1','dummy2','dummy3','wflagX'),'formats':('f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i4')})
cropt=np.loadtxt('/home/rumbaugh/Chandra/photcats/rxj1716_rizdata.corr.gz',dtype={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
raX,decX=crx['raX'],crx['decX']
ra_opt,dec_opt=cropt['ra'],cropt['dec']


ra_cen, dec_cen=259.27833,67.242314
tol=100.
tolx = tol/np.cos(dec_cen*np.pi/180.0)
g_xray=np.where((np.abs(ra_cen-raX)<tolx/3600.)&(np.abs(dec_cen-decX)<tol/3600.))[0]
g_opt=np.where((np.abs(ra_cen-ra_opt)<tolx*2/3600.)&(np.abs(dec_cen-dec_opt)<tol*2/3600.))[0]
FILEX=open('/home/rumbaugh/git/cosmo_code_review/rumbaugh/2015_12_2/example_xray.cat','w')
FILEopt=open('/home/rumbaugh/git/cosmo_code_review/rumbaugh/2015_12_2/example_opt.cat','w')
FILEX.write('# raX decX fluxX_soft fluxX_hard fluxX_full netcnts_corrX_soft netcnts_corrX_hard netcnts_corrX_full sigX_soft sigX_hard sigX_full wavdetect_sig_soft wavdetect_sig_hard wavdetect_sig_full wflagX\n')
FILEopt.write('# ra dec magI ID\n')
for i in range(0,len(g_xray)):
    FILEX.write('%9.5f %9.5f %12E %12E %12E %9.5f %9.5f %9.5f %9.2f %9.2f %9.2f %9.2f %9.2f %9.2f %i\n'%(crx['raX'][g_xray[i]],crx['decX'][g_xray[i]],crx['fluxX_soft'][g_xray[i]],crx['fluxX_hard'][g_xray[i]],crx['fluxX_full'][g_xray[i]],crx['netcnts_corrX_soft'][g_xray[i]],crx['netcnts_corrX_hard'][g_xray[i]],crx['netcnts_corrX_full'][g_xray[i]],crx['sigX_soft'][g_xray[i]],crx['sigX_hard'][g_xray[i]],crx['sigX_full'][g_xray[i]],crx['dummy1'][g_xray[i]],crx['dummy2'][g_xray[i]],crx['dummy3'][g_xray[i]],crx['wflagX'][g_xray[i]]))
for i in range(0,len(g_opt)):
    FILEopt.write('%9.5f %9.5f %10.5f %s\n'%(ra_opt[g_opt[i]],dec_opt[g_opt[i]],cropt['magI'][g_opt[i]],cropt['ID'][g_opt[i]]))
FILEX.close()
FILEopt.close()

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(ra_opt,dec_opt,color='k',s=1)
plt.scatter(raX,decX,color='red',s=24)
plt.xlim(259.6,259.1)
plt.ylim(67.14,67.28)
plt.xlabel('Right Ascension')
plt.ylabel('Declination')
plt.savefig('/home/rumbaugh/Chandra/plots/548.catalogs.png')

figsize(8,8)
plt.figure(2)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter([0],[0],color='k',s=200,marker='x',lw=3)
plt.scatter([-0.65],[0.1],s=800,color='cyan')
plt.scatter([-0.1,0.9,0.3],[-0.15,0.15,1.1],s=250,color='red')
dum=np.arange(0,360,0.1)
plt.plot(np.cos(np.pi*dum/180.),np.sin(np.pi*dum/180.),color='k',lw=2)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.tick_params(axis='both',which='both',bottom='off',top='off',left='off',right='off',labelbottom='off',labeltop='off',labelleft='off',labelright='off')
plt.savefig('/home/rumbaugh/Chandra/plots/matching_illustration.png')
