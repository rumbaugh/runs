import numpy as np
import pyfits as py
import matplotlib.pyplot as plt
import easyaccess as ea
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/var_database/plots/eric_LC_comp_test.2.10.17.pdf')

con=ea.connect()

bands=['g','r','i','z']
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}

N=10

hdu=py.open('Downloads/C1_lc.fits')
data=hdu[1].data

Eric_cids=np.array(np.unique(data['COADD_OBJECT_ID']),dtype='i8')
cid_list=Eric_cids[100:100+N]

cidstr='%i'%cid_list[0]
for cid in cid_list[1:]: cidstr='%s,%i'%(cidstr,cid)

query="SELECT y.COADD_OBJECT_ID,e.mjd_obs,o.RA,o.DEC,o.expnum,o.filename,o.object_number,z.mag_zero-2.5*log(10,o.flux_psf) as mag_psf,SQRT(POWER(z.SIGMA_MAG_ZERO, 2)+ POWER(o.FLUXERR_PSF / o.FLUX_PSF, 2)) as MAGERR_PSF,z.mag_zero-2.5*log(10,o.flux_auto) as mag_auto,SQRT(POWER(z.SIGMA_MAG_ZERO,2) + POWER(o.FLUXERR_AUTO / o.FLUX_AUTO, 2)) as MAGERR_AUTO,o.band,o.flags,o.flags_detmodel,o.flags_model,o.flags_weight FROM des_admin.Y3A1_COADD_OBJECT_SUMMARY y, des_admin.y3a1_finalcut_object o,des_admin.y3a1_exposure e,des_admin.y3a1_wavg_oclink l,des_admin.y3a1_zeropoint z where o.expnum=e.expnum and y.coadd_object_id=l.coadd_object_id and o.filename=l.se_object_filename and o.object_number=l.se_object_number and e.expnum=z.expnum and z.source='FGCM' and z.version='v2.0' and z.CATALOGNAME=o.FILENAME and y.coadd_object_id in (%s);"%(cidstr)

DF=con.query_to_pandas(query)

for cid in cid_list:
    gdf=np.where(np.array(DF['COADD_OBJECT_ID'])==cid)[0]
    geric=np.where(data['COADD_OBJECT_ID']==cid)[0]
    plt.figure()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.locator_params(nbins=4)
    mjd,magplot,magploterr=DF['MJD_OBS'][gdf],DF['MAG_PSF'][gdf],DF['MAGERR_PSF'][gdf]
    for b in bands:
        curcol=coldict[b]
        gb=np.where(DF['BAND'][gdf]==b)[0]
        plt.plot(mjd[gb],magplot[gb],color=curcol,lw=2)
        plt.errorbar(mjd[gb],magplot[gb],yerr=magploterr[gb],color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
        plt.scatter(mjd[gb],magplot[gb],color=curcol,label=b)
    plt.xlabel('MJD')
    plt.ylabel('Mag. PSF')
    #plt.legend()
    plt.savefig(psfpdf,format='pdf')
    plt.figure()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.locator_params(nbins=4)
    mjd,magplot,magploterr=DF['MJD_OBS'][gdf],DF['MAG_PSF'][gdf],DF['MAGERR_PSF'][gdf]
    for b in bands:
        curcol=coldict[b]
        mjdE,magplotE,magploterrE=data['LC_MJD_%s'%b.upper()][geric],data['LC_MAG_PSF_%s'%b.upper()][geric],data['LC_MAGERR_PSF_%s'%b.upper()][geric]
        for j in np.arange(np.shape(mjdE)[0]):
            ggood=np.where(magplotE[j]>0.1)[0]
            plt.plot(mjdE[j][ggood],magplotE[j][ggood],color=curcol,lw=2)
            plt.errorbar(mjdE[j][ggood],magplotE[j][ggood],yerr=magploterrE[j][ggood],color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
            plt.scatter(mjdE[j][ggood],magplotE[j][ggood],color=curcol)
    plt.xlabel('MJD')
    plt.ylabel('Mag. PSF')
    #plt.legend()
    plt.savefig(psfpdf,format='pdf')
psfpdf.close()
        
