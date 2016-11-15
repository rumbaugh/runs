import easyaccess as ea
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
DB_path='/home/rumbaugh/var_database'
psfpdf=bpdf.PdfPages('/home/rumbaugh/var_database/plots/SDSS+POSS_plots_inY1A1.pdf')
cre=np.loadtxt('/home/rumbaugh/SDSSPOSS_Y1A1_num_epochs.dat',dtype='i8')
IDs,exps=cre[:,0],cre[:,1]
IDs=np.sort(np.random.choice(IDs,100,False))
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'%s_SDSS'%b for b in SDSSbands}
POSSbands=np.array(['g','r','i'])

ge=np.argsort(exps)[::-1]


def plot_POSS(ax,band,bandname=None,connectpoints=False):
    POSS_cols={'g': '#003300', 'r': '#ffb3ff', 'i': '#cccc00'}
    if bandname==None: bandname=band
    POSSmag,POSSmagerr=POSSmagdict[band],POSSmagerrdict[band]
    POSSmjd=POSSmjddict[band]
    curcol=POSS_cols[band]
    if connectpoints:
        gsort=np.argsort(POSSmjd)
        ax.plot(POSSmjd[gsort],POSSmag[gsort],color=curcol,lw=2)
    ax.errorbar(POSSmjd,POSSmag,yerr=POSSmagerr,color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    ax.scatter(POSSmjd,POSSmag,color=curcol,label='POSS %s'%band,marker='d')
    
def plot_SDSS(ax,band,bandname=None,connectpoints=False):
    SDSS_cols={'g': '#66ff66','u': 'purple', 'r': 'pink', 'i': 'brown', 'z': 'silver'}
    if bandname==None: bandname=band
    SDSSmag,SDSSmagerr=SDSSmagdict[band],SDSSmagerrdict[band]
    curcol=SDSS_cols[band]
    if connectpoints:
        gsort=np.argsort(SDSSmjd)
        ax.plot(SDSSmjd[gsort],SDSSmag[gsort],color=curcol,lw=2)
    ax.errorbar(SDSSmjd,SDSSmag,yerr=SDSSmagerr,color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    ax.scatter(SDSSmjd,SDSSmag,color=curcol,label='SDSS %s'%band,marker='d')
    

def plot_band(ax,gid,band,connectpoints=True,nolabels=False):
    gband=np.where(bands[gid]==band)[0]
    magplot=mag[gid][gband]
    magploterr=magerr[gid][gband]
    g100=np.where(magplot<100)[0]
    try:
        curcol=coldict[band]
    except KeyError:
        print '%s is not a valid band'%band
        return
    if connectpoints:
        gsort=np.argsort(mjd[gid][gband][g100])
        ax.plot(mjd[gid][gband][g100][gsort],magplot[g100][gsort],color=curcol,lw=2)
    ax.errorbar(mjd[gid][gband][g100],magplot[g100],yerr=magploterr[g100],color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    if nolabels:
        ax.scatter(mjd[gid][gband][g100],magplot[g100],color=curcol)
    else:
        ax.scatter(mjd[gid][gband][g100],magplot[g100],color=curcol,label=band)
    #return


def plot_lightcurve(cid,band='all',plotSDSS=False,fname=None,connectpoints=True):
    band=band.lower()
    #g=np.where(cID==cid)[0]
    #if len(g)==0:
    #    print 'No matches for %i'%cid
    #    return
    fig=plt.figure(1)
    fig.clf()
    #ax=fig.add_subplot(2,1,2)
    ax=fig.add_subplot(1,1,1)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    #if band=='all':
    #    for b in coldict.keys():
    #        plot_band(ax,g,b,connectpoints=connectpoints)
    #    xlim=plt.xlim()
    #    plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
    #    ax.legend()
    #ax=fig.add_subplot(2,1,1)
    if band=='all':
        #for b in coldict.keys():
        #    plot_band(ax,g,b,connectpoints=connectpoints,nolabels=True)
        if plotSDSS==True:
            for b in POSSbands:
                plot_SDSS(ax,b,bandname=SDSS_colnames[b],connectpoints=connectpoints)
                plot_POSS(ax,b,bandname=SDSS_colnames[b],connectpoints=connectpoints)
        xlim=plt.xlim()
        plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
        ax.legend()
    else:
        plot_band(ax,g,band,connectpoints=connectpoints)
    ax.set_xlabel('MJD')
    ax.set_ylabel('Mag_PSF')
    ax.set_title(cid)
    if fname!=None: plt.savefig(psfpdf,format='pdf')
    return
  

outputdir='/home/rumbaugh/var_database'
crt=np.loadtxt('/home/rumbaugh/SDSSPOSS_INY1A1TILE.tab',dtype={'names':('SP_ROWNUM','RA','DEC','TILENAME'),'formats':('i8','f8','f8','|S30')},skiprows=1)
cr=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EPOCHG','EPOCHR','EPOCHI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_SDSS','G_SDSS','G_SDSS_ERR','R_SDSS','R_SDSS_ERR','I_SDSS','I_SDSS_ERR'),'formats':('f8','f8','|S2','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S2','f8','f8','|S2','|S2','|S2','|S2','|S2','f8','f8','f8','f8','f8','f8','f8')})
#cr=np.loadtxt('SDSSPOSS_lightcurve_entries.tab',dtype={'names':('cid','SP_ROWNUM','ra_y1a1','dec_y1a1','sdr7id','mjd_SDSS','EPOCHG','EPOCHR','EPOCHI','ra','dec','G_POSS','R_POSS','I_POSS','G_POSS_err','R_POSS_err','I_POSS_err','G_SDSS','R_SDSS','I_SDSS','G_SDSS_err','R_SDSS_err','I_SDSS_err'),'formats':('i8','i8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
cry=np.loadtxt('SDSSPOSS_lightcurve_entries_Y1A1.tab',skiprows=1,dtype={'names':('mjd','imageid','cid','SPid','ra','dec','mag','magerr','band','exp'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','|S12','f8')})
for curid in crt['SP_ROWNUM']:
    gid=np.array([curid])
    #gid=np.where(cr['SP_ROWNUM']==curid)[0]
    SDSSmjd=cr['mjd_SDSS'][gid]
    SDSSra,SDSSdec=cr['ra'][gid],cr['dec'][gid]
    SDSSmagdict,SDSSmagerrdict={b: cr['%s_SDSS'%(b.upper())][gid] for b in POSSbands},{b: cr['%s_SDSS_ERR'%(b.upper())][gid] for b in POSSbands}
    POSSra,POSSdec=cr['ra'][gid],cr['dec'][gid]
    POSSmagdict,POSSmagerrdict,POSSmjddict={b: cr['%s_POSS'%(b.upper())][gid] for b in POSSbands},{b: cr['%s_ERR'%(b.upper())][gid] for b in POSSbands},{b: 50448.+365.25*(cr['EPOCH%s'%(b.upper())][gid]-1997) for b in POSSbands}


    plot_lightcurve(curid,plotSDSS=True,fname='/home/rumbaugh/var_database/plots/SDSS+POSS_lightcurve_%s.png'%curid)
psfpdf.close()
