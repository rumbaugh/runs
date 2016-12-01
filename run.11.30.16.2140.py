import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

good_dbids=np.array([20458,18172,20977,1053,3866])

DB_path='/home/rumbaugh/var_database'
psfpdf=bpdf.PdfPages('/home/rumbaugh/var_database/plots/changinglookAGNcandidates_plots.12.1.16.pdf')
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'%s_SDSS'%b for b in SDSSbands}
POSSbands=np.array(['g','r','i'])

def plot_band(ax,mjd,mag,magerr,cbands,band,connectpoints=True,nolabels=False):
    gband=np.where(cbands==band)[0]
    magplot=mag[gband]
    magploterr=magerr[gband]
    g100=np.where(magplot<100)[0]
    try:
        curcol=coldict[band]
    except KeyError:
        print '%s is not a valid band'%band
        return
    if connectpoints:
        gsort=np.argsort(mjd[gband][g100])
        ax.plot(mjd[gband][g100][gsort],magplot[g100][gsort],color=curcol,lw=2)
    ax.errorbar(mjd[gband][g100],magplot[g100],yerr=magploterr[g100],color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    if nolabels:
        ax.scatter(mjd[gband][g100],magplot[g100],color=curcol)
    else:
        ax.scatter(mjd[gband][g100],magplot[g100],color=curcol,label=band)
    #return


def plot_lightcurve(dbid,mjd,mag,magerr,bands,gdes,plotSDSS=False,fname=None,connectpoints=True):
    fig=plt.figure(1)
    fig.clf()
    ax=fig.add_subplot(2,1,2)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    for b in ['g','r','i','z','Y']:
        plot_band(ax,mjd[gdes],mag[gdes],magerr[gdes],bands[gdes],b,connectpoints=connectpoints)
    xlim=plt.xlim()
    plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
    ylim=plt.ylim()
    plt.ylim(ylim[1],ylim[0])
    ax.legend()
    ax=fig.add_subplot(2,1,1)
    for b in ['g','r','i','z','Y']:
        plot_band(ax,mjd,mag,magerr,bands,b,connectpoints=connectpoints,nolabels=True)
    xlim=plt.xlim()
    plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
    ylim=plt.ylim()
    plt.ylim(ylim[1],ylim[0])
    ax.legend()
    ax.set_xlabel('MJD')
    ax.set_ylabel('Mag_PSF')
    ax.set_title(dbid)
    plt.savefig(psfpdf,format='pdf')
    return

outputdir='/home/rumbaugh/var_database'

#cr=np.loadtxt('SDSSPOSS_lightcurve_entries.tab',dtype={'names':('cid','SP_ROWNUM','ra_y1a1','dec_y1a1','sdr7id','mjd_SDSS','EPOCHG','EPOCHR','EPOCHI','ra','dec','G_POSS','R_POSS','I_POSS','G_POSS_err','R_POSS_err','I_POSS_err','G_SDSS','R_SDSS','I_SDSS','G_SDSS_err','R_SDSS_err','I_SDSS_err'),'formats':('i8','i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
#cry=np.loadtxt('SDSSPOSS_lightcurve_entries_Y1A1.tab',skiprows=1,dtype={'names':('mjd','imageid','cid','SPid','ra','dec','mag','magerr','band','exp'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','|S12','f8')})

for DBID in good_dbids:
    cr=np.loadtxt('%s/%i/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    gdes=np.where(cr['Survey']=='DES')[0]
    gsdss=np.where(cr['Survey']=='SDSS')[0]
    curid=int(cr['SurveyCoaddID'][gdes[0]])
    mjd,mag,magerr,bands=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND']
    plot_lightcurve(DBID,mjd,mag,magerr,bands,gdes,plotSDSS=False)

psfpdf.close()
