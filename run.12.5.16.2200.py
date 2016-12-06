import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
execfile('/home/rumbaug/pythonscripts/angconvert.py')
execfile('/home/rumbaug/pythonscripts/SphDist.py')
import matplotlib.backends.backend_pdf as bpdf

psfpdf=bpdf.PdfPages('/home/rumbaugh/var_database/plots/changinglookAGNcandidates_plots.12.5.16.pdf')
DB_path='/home/rumbaugh/var_database'

lsdict={'names':('DESJ','rah','ram','ras','decd','decm','decs','tif'),'formats':
('|S4','i8','i8','f8','i8','i8','f8','|S4')}
delims=(4,2,2,4,3,2,4,4)
crls=np.genfromtxt('',dtype=lsdict,delimiter=delims)
lsfilenames=np.loadtxt('',dtype='|S30')

lsras,lsdecs=hms2deg(crls['rah'],crls['ram'],crls['ras']),dms2deg(crls['decd'],crls['decm'],crls['decs'])


crids=np.loadtxt('/home/rumbaugh/var_database/maxdiffs_DBID.12.1.16.txt',dtype={'names':('DBID','maxdiff'),'formats':('i8','f8')})

good_dbids=crids['DBID'][crids['maxdiff']>2]

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


def plot_lightcurve(dbid,mjd,mag,magerr,bands,survey,plotSDSS=False,fname=None,DESfname=None,connectpoints=True):
    gdes,gsdss,gposs=np.where(survey=='DES')[0],np.where(survey=='SDSS')[0],np.where(survey=='POSS')[0]
    if len(gposs)>0:
        POSSmagdict={b: mag[gposs][bands[gposs]==b] for b in POSSbands}
        for band in POSSbands:
            if len(POSSmagdict[band])>0:POSSmagdict[band]=np.array([np.median(POSSmagdict[band])])
        if (len(POSSmagdict['g'])>0)&(len(POSSmagdict['r'])>0):
            mag[gposs][bands[gposs]=='g'],mag[gposs][bands[gposs]=='r']=mag[gposs][bands[gposs]=='g']+0.392*(POSSmagdict['g']-POSSmagdict['r'])-0.28, mag[gposs][bands[gposs]=='r'] +0.127*(POSSmagdict['g']-POSSmagdict['r'])+0.1
        else: 
            mag[gposs][bands[gposs]=='g'],mag[gposs][bands[gposs]=='r']=np.zeros(0),np.zeros(0)
        if (len(POSSmagdict['i'])>0)&(len(POSSmagdict['r'])>0):   
            mag[gposs][bands[gposs]=='i']=mag[gposs][bands[gposs]=='i']+0.27*(POSSmagdict['r']-POSSmagdict['i'])+0.32
        else:
            mag[gposs][bands[gposs]=='i']=np.zeros(0)
    fig=plt.figure(1)
    fig.clf()
    ax3=subplot2grid((2,10),(1,0),colspan=6)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    for b in ['g','r','i','z','Y']:
        plot_band(ax3,mjd[gdes],mag[gdes],magerr[gdes],bands[gdes],b,connectpoints=connectpoints)
    xlim=plt.xlim()
    plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
    ylim=plt.ylim()
    plt.ylim(ylim[1],ylim[0])
    ax3.legend()
    ax1=subplot2grid((2,10),(0,0),colspan=6)
    for b in ['g','r','i','z','Y']:
        plot_band(ax1,mjd,mag,magerr,bands,b,connectpoints=connectpoints,nolabels=True)
    xlim=plt.xlim()
    plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
    ylim=plt.ylim()
    plt.ylim(ylim[1],ylim[0])
    ax1.legend()
    ax1.set_xlabel('MJD')
    ax1.set_ylabel('Mag_PSF')
    ax.set_title(dbid)
    if len(gsdss)>0:
        ax3=subplot2grid((2,10),(1,6),colspan=4,xticks=[],yticks=[])
        SDSSfname='%s/SDSScutout_DBID_%06i'%(,dbid)
        ax3.imshow(SDSSfname)
    if DESfname!=None:
        ax4=subplot2grid((2,10),(1,6),colspan=4,xticks=[],yticks=[])
        ax4.imshow('%s/%s'%(,DESfname))
    plt.savefig(psfpdf,format='pdf')
    return


for DBID in good_dbids:
    cr=np.loadtxt('%s/%i/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    curid=int(cr['SurveyCoaddID'][gdes[0]])
    mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
    gdes=np.where(survey=='DES')
    if len(gdes)>0:
        mRA,mDec=np.mean(np.array([cr['RA'][gdes]])),np.mean(np.array([cr['Dec'][gdes]]))
        glsinit=np.where(np.abs(lsdecs-mDec)<.3/3600.)[0]
        DES_imagestamp_fname=None
        if len(glsinit)>0:
            tdists=SphDist(mRa,mDec,lsras[glsinit],lsras[glsinit])/60.
            gclose=np.argsort(tdists)
            if ((tdists[gclose[0]]<.3/3600.)|(tdist[gclose[0]]<0.000417*3*np.cos(mDec*np.pi/180.))):
                gls=glsinit[gclose[0]]
                DES_imagestamp_fname=lsfilenames[gls]
    plot_lightcurve(DBID,mjd,mag,magerr,bands,survey,plotSDSS=False,DESfname=DES_imagestamp_fname)

psfpdf.close()
