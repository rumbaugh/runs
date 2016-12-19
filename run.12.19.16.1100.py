import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
execfile('/home/rumbaugh/pythonscripts/angconvert.py')
import matplotlib.backends.backend_pdf as bpdf
import itertools as it
import pyfits as py
hdu=py.open('/home/rumbaugh/var_database/masterfile.fits')
data=hdu[1].data

outputdir='/home/rumbaugh/var_database'
psfpdf=bpdf.PdfPages('/home/rumbaugh/var_database/plots/changinglookAGNcandidates_plots.12.19.16.pdf')
DB_path='/home/rumbaugh/var_database'
maxdb=None

WavLL,WavUL=300,1050

bands=np.array(['g','r','i','z'])
bcens={'u': 387.663943790537, 'g': 484.183358196563, 'r': 643.8534828217, 'i': 782.099282740933, 'z': 917.234266385718, 'Y': 987.780238651117}
crv=np.loadtxt('/home/rumbaugh/Downloads/VanderBerk_datafile1.txt',skiprows=23)

#lsdict={'names':('DESJ','rah','ram','ras','decd','decm','decs','tif'),'formats':
#('|S4','i8','i8','f8','i8','i8','f8','|S4')}
#delims=(4,2,2,4,3,2,4,4)
#crls=np.genfromtxt('',dtype=lsdict,delimiter=delims)
#lsfilenames=np.loadtxt('',dtype='|S30')

crdescutin=np.loadtxt('/home/rumbaugh/radecname_forDEScutouts.csv',delimiter=',DEScutout_DBID_',dtype={'names':('radec','DBID'),'formats':('|S20','i8')})
crdescutout=np.loadtxt('/home/rumbaugh/descuts/results/12-18-16/matched_12-18-16.csv',skiprows=1,delimiter=',',dtype={'names':('ra','dec','tile','fname'),'formats':('f8','f8','|S12','|S25')})


#lsras,lsdecs=hms2deg(crls['rah'],crls['ram'],crls['ras']),dms2deg(crls['decd'],crls['decm'],crls['decs'])


crids=np.loadtxt('/home/rumbaugh/var_database/maxdiffs_DBID.12.18.16.txt',dtype={'names':('DBID','maxdiff'),'formats':('i8','f8')})

cr_rids=np.loadtxt('/home/rumbaugh/changinglookAGNcandidates_index.12.18.16.dat',dtype={'names':('DBID','CID','tid','sdr7id','ra','dec','IntFlag'),'formats':('i8','i8','i8','i8','f8','f8','i8')})

good_dbids=cr_rids['DBID'][cr_rids['IntFlag']==1]

crdb=np.loadtxt('/home/rumbaugh/var_database/database_index.dat',dtype={'names':('DBID','CID','tID','dr7id'),'formats':('i8','i8','i8','i8')})

crpmf=np.loadtxt('/home/rumbaugh/MQ_SDSS_tidplatemjdfiber.csv',delimiter=',',skiprows=1,dtpye={'names':('tid','plate','mjd','fiber'),'formats':('i8','i8','i8','i8')})

coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'%s_SDSS'%b for b in SDSSbands}
POSSbands=np.array(['g','r','i'])

def plot_flux(ax,fluxes,label=None,curcol='k',bands=np.array(['g','r','i','z'])):
    if len(fluxes)!=len(bands):
        print 'Lengths of fluxes and bands must be equal'
        return
    cens=np.zeros(len(bands))
    for ib,b in zip(np.arange(len(bands)),bands): cens[ib]=bcens[b] 
    if 'i' in bands:
        gi=np.where(bands=='i')[0][0]
        fluxes/=fluxes[gi]
    elif 'r' in bands:
        gi=np.where(bands=='r')[0][0]
        fluxes/=fluxes[gi]
    else:
        return
    if label==None:
        ax.scatter(cens,fluxes,color=curcol,s=36)
    else:
        ax.scatter(cens,fluxes,color=curcol,s=36,label=label)

def calc_flux(mjd,mag,magerr,cbands,band,mjdcen):
    gband=np.where(cbands==band)[0]
    magplot=mag[gband]
    magploterr=magerr[gband]
    g100=np.where((magplot<100)&(np.isnan(magplot)==False))[0]
    if len(g100)>1:
        gcen=np.argsort(np.abs(mjd[gband][g100]-mjdcen))[0]
        medmag=(magplot[g100][gcen])
    else:
        medmag=magplot[g100]
    if np.shape(medmag)!=(): 
        if len(medmag)==0:
            return 0
        medmag=medmag[0]
    return 10**(medmag/-2.5)

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


def plot_lightcurve(dbid,mjd,mag,magerr,bands,survey,trueredshift,plotSDSS=False,fname=None,DESfname=None,connectpoints=True,specfile=None):
    redshift=np.copy(trueredshift)
    if redshift<0:redshift=0
    gdes,gsdss,gposs=np.where(survey=='DES')[0],np.where(survey=='SDSS')[0],np.where(survey=='POSS')[0]
    if len(gposs)>0:
        POSSmagdict,POSSmagerrdict,POSSmjddict={b: mag[gposs][bands[gposs]==b] for b in POSSbands},{b: np.zeros(0) for b in POSSbands},{b: np.zeros(0) for b in POSSbands}
        for band in POSSbands:
            if len(POSSmagdict[band])>0:
                POSSmagdict[band]=np.array([np.median(POSSmagdict[band])])
                POSSmagerrdict[band]=np.array([np.mean(POSSmagdict[band])])
        if (len(POSSmagdict['g'])>0)&(len(POSSmagdict['r'])>0):
            mag[gposs][bands[gposs]=='g'],mag[gposs][bands[gposs]=='r']=mag[gposs][bands[gposs]=='g']+0.392*(POSSmagdict['g']-POSSmagdict['r'])-0.28, mag[gposs][bands[gposs]=='r'] +0.127*(POSSmagdict['g']-POSSmagdict['r'])+0.1
            magerr[gposs][bands[gposs]=='g'],magerr[gposs][bands[gposs]=='r']=np.sqrt(1.392**2*magerr[gposs][bands[gposs]=='g']**2+0.392**2*magerr[gposs][bands[gposs]=='r']**2),  np.sqrt(magerr[gposs][bands[gposs]=='r']**2+0.127**2*(magerr[gposs][bands[gposs]=='g']**2+magerr[gposs][bands[gposs]=='r']**2))
        else: 
            mag[gposs][bands[gposs]=='g'],mag[gposs][bands[gposs]=='r']=np.zeros(0),np.zeros(0)
        if (len(POSSmagdict['i'])>0)&(len(POSSmagdict['r'])>0):   
            mag[gposs][bands[gposs]=='i']=mag[gposs][bands[gposs]=='i']+0.27*(POSSmagdict['r']-POSSmagdict['i'])+0.32
            magerr[gposs][bands[gposs]=='i']=np.sqrt(magerr[gposs][bands[gposs]=='i']**2+0.27**2*(magerr[gposs][bands[gposs]=='r']**2+magerr[gposs][bands[gposs]=='i']**2))
        else:
            mag[gposs][bands[gposs]=='i']=np.zeros(0)
    bestdiff={b: {'diff': 0, 'ihi': 0, 'ilo': 0} for b in ['g','r','i','z']}
    for b in ['g','r','i','z']:
        gb=np.where(bands=='b')[0]
        if len(gb)>1:
            combis=np.array(list(it.combinations(np.arange(len(mag[gb])),2)))
            i1,i2=combis[:,0],combis[:,1]
            sigma=np.abs((mag[gb][i1]-mag[gb][i2])/np.sqrt(magerr[gb][i1]**2+magerr[gb][i2]**2))
            totdiffstmp=np.abs(mag[gb][i1]-mag[gb][i2])
            ggooddiff=np.where((sigma>=3)&(mag[gb][i1]>1)&(mag[gb][i1]<30)&(mag[gb][i2]>1)&(mag[gb][i2]<30))[0]
            if len(ggooddiff)>0:
                bestdiff[b]['value']=np.max(totdiffstmp[ggooddiff])
                gsort=np.argsort(totdiffstmp[ggooddiff])
                gsortis=np.argsort([mag[gb][i1][ggooddiff][gsort[-1]],mag[gb][i2][ggooddiff][gsort[-1]]])
                imax,imin=[i1,i2][gsortis[1]][ggooddiff][gsort[-1]],[i1,i2][gsortis[0]][ggooddiff][gsort[-1]]
                bestdiff[b]['ihi'],bestdiff[b]['ilo']=imax,imin
    fig=plt.figure(1)
    fig.clf()
    ax3=plt.subplot2grid((2,10),(1,0),colspan=6)
    totdiffs=np.zeros(4)
    for ib,b in zip(np.arange(4),['g','r','i','z']):
        totdiffs[ib]=bestdiff[b]['diff']
    ibest=np.argsort(totdiffs)[-1]
    bbest=['g','r','i','z'][ibest]
    imax,imin=bestdiff[bbest]['ihi'],bestdiff[bbest]['ilo']
    maxfluxes=np.zeros(0)
    for ib,b in zip(np.arange(4),['g','r','i','z']):
        gbt=np.where(bands==b)[0]
        maxfluxes[ib]=calc_flux(mjd,mag,magerr,bands,b,mjdcen[bbest][imax])
        minfluxes[ib]=calc_flux(mjd,mag,magerr,bands,b,mjdcen[bbest][imin])
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.locator_params(nbins=4)
    if specfile!=None:
        shdu=py.open(specfile)
        specdata=shdu[1].data
        sflux,swav=specdata['flux'],10**(specdata['loglam']-1)
        s_closei=np.where(np.abs(swav-bcens['i'])<20)[0]
        ax3.plot(swav,sflux/np.mean(sflux[s_closei]),lw=1,color='magenta')
    ax3.plot(crv[:,0]/(1.+redshift),crv[:,1],color='k',lw=1)
    plot_flux(ax3,maxfluxes,label='Max',curcol='r')
    plot_flux(ax3,minfluxes,label='Min',curcol='b')
    ax3.set_ylabel('Wavelength (A)')
    ax3.set_xlabel('Flux (Arb. Units)')
    survmax,survmin=survey[bbest][imax],survey[bbest][imin]
    if not('DES' in [survmax,survmin]):
        sortmjdcens=np.argsort([mjdcen[bbest][imax],mjdcen[bbest][imin]])
        iDESex=np.argsort(mag[bands==bbest])[-sortmjdcens[0]]
        DESexfluxes=np.zeros(0)
        for ib,b in zip(np.arange(4),['g','r','i','z']):
            gbt=np.where(bands==b)[0]
            DESexfluxes[ib]=calc_flux(mjd,mag,magerr,bands,b,mjdcen[bbest][iDESex])
        plot_flux(ax3,DESexfluxes,label='DES %s'%['Max','Min'][-sortmjdcens[0]],curcol='cyan')
    ax3.legend(loc='lower right')
    plt.xlim(WavLL,WavUL)
    ax1=plt.subplot2grid((2,10),(0,0),colspan=6)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.locator_params(nbins=4)
    for b in ['g','r','i','z','Y']:
        if len(gdes)>0:
            plot_band(ax1,mjd,mag,magerr,bands,b,connectpoints=connectpoints,nolabels=True)
        else:
            plot_band(ax1,mjd,mag,magerr,bands,b,connectpoints=connectpoints,nolabels=False)
    xlim=plt.xlim()
    plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
    ylim=plt.ylim()
    plt.axvline(mjdcen[bbest][imax],ls='dashed',lw=1,color='r')
    plt.axvline(mjdcen[bbest][imin],ls='dashed',lw=1,color='b')
    if not('DES' in [survmax,survmin]):plt.axvline(mjdcen[bbest][iDESex],ls='dashed',lw=1,color='cyan')
    if ylim[1]>30:
        ylim=(ylim[0],np.max(mag)+0.1)
    if ylim[1]>30: ylim=(ylim[0],30)
    if ylim[0]<15:
        ylim=(np.min(mag)-0.1,ylim[1])
    if ylim[0]<15: ylim=(15,ylim[1])
    plt.ylim(ylim[1],ylim[0])
    ax1.legend()
    #ax1.set_xlabel('MJD')
    ax1.set_ylabel('Mag_PSF')
    if redshift>0:
        ax1.set_title('%i, z=%.4f'%(dbid,trueredshift))
    else:
        ax1.set_title(dbid)
    if len(gdes==0):ax1.legend()
    if len(gdes)>0:
        gdc=np.where(crdescutin['DBID']==DBID)[0]
        if len(gdc)>0:
            if crdescutout['fname'][gdc[0]]!='False':
                DESfname='%s.tif'%(crdescutout['fname'][gdc[0]])
                ax4=plt.subplot2grid((2,10),(1,6),colspan=4,xticks=[],yticks=[])
                img4=mpimg.imread('/home/rumbaugh/descuts/results/12-18-16/%s'%(DESfname))
                ax4.imshow(img4)
    if len(gsdss)>0:
        ax3=plt.subplot2grid((2,10),(0,6),colspan=4,xticks=[],yticks=[])
        SDSSfname='/home/rumbaugh/var_database/plots/SDSScutout_DBID_%06i.jpeg'%(dbid)
        img3=mpimg.imread(SDSSfname)
        ax3.imshow(img3)
    plt.savefig(psfpdf,format='pdf')
    return

def DES2SDSS_gr(g,r):
    return (133625*g-9375*r-218)/124250.,(69.*g+925*r)/994.+516./62125.

def DES2SDSS_iz(i,z):
    return (-89*np.sqrt(-96000*i+96000*z+181561)+8000*z+37827)/8000.,(-17*np.sqrt(-96000*i+96000*z+181561)+24000*z+6731)/24000.

if maxdb!=None:
    good_dbids=good_dbids[:maxdb]
for DBID in good_dbids:
    gmf=np.where(data['DatabaseID']==DBID)[0][0]
    trueredshift=data['Redshift'][gmf]
    redshift=np.copy(trueredshift)
    if redshift<0: redshift=0
    gdb=np.where(crdb['DBID']==DBID)[0][0]
    tid=crdb['tID'][gdb]
    plate,pmf_mjd,fiber=-1,-1,-1
    if tid!=0:
        gpmf=np.where(crpmf['tid']==tid)[0]
        if len(gpmf)>0:
            gpmf=gpmf[0]
            plate,pmf_mjd,fiber=crpmf['plate'][gpmf],crpmf['mjd'][gpmf],crpmf['fiber'][gpmf]
    if (plate>-1)&(pmf_mjd>-1)&(fiber>-1):
        specfile='/home/rumbaugh/specDL/spec-%04i-%05i-%04i.fits'%(plate,pmf_mjd,fiber)
    else:
        specfile=None
    cr=np.loadtxt('%s/%i/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('i8','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    cr=cr[(cr['MAG']>0)&(cr['MAG']<30)&(cr['MAGERR']<5)]
    gdes=np.where(cr['Survey']=='DES')[0]
    if len(gdes)>1:
        gg,gr=np.where(cr['BAND'][gdes]=='g')[0],np.where(cr['BAND'][gdes]=='r')[0]
        if (len(gg)>0)&(len(gr)>0):
            if len(gg)==1:
                medg=cr['MAG'][gdes][gg]
            else:
                medg=np.median(cr['MAG'][gdes][gg])
            if len(gr)==1:
                medr=cr['MAG'][gdes][gr]
            else:
                medr=np.median(cr['MAG'][gdes][gr])
            newg,dum1=DES2SDSS_gr(cr['MAG'][gdes][gg],medr)
            dum2,newr=DES2SDSS_gr(medg,cr['MAG'][gdes][gr])
            cr['MAG'][gdes[gg]],cr['MAG'][gdes[gr]]=newg,newr
        gi,gz=np.where(cr['BAND'][gdes]=='i')[0],np.where(cr['BAND'][gdes]=='z')[0]
        if (len(gi)>0)&(len(gz)>0):
            if len(gi)==1:
                medi=cr['MAG'][gdes][gi]
            else:
                medi=np.median(cr['MAG'][gdes][gi])
            if len(gz)==1:
                medz=cr['MAG'][gdes][gz]
            else:
                medz=np.median(cr['MAG'][gdes][gz])
            newi,dum1=DES2SDSS_iz(cr['MAG'][gdes][gi],medz)
            dum2,newz=DES2SDSS_iz(medi,cr['MAG'][gdes][gz])
            cr['MAG'][gdes[gi]],cr['MAG'][gdes[gz]]=newi,newz
    mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
    plot_lightcurve(DBID,mjd,mag,magerr,bands,survey,trueredshift,plotSDSS=False,specfile=specfile)

psfpdf.close()
