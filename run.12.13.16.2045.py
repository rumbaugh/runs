import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
execfile('/home/rumbaugh/pythonscripts/angconvert.py')
import matplotlib.backends.backend_pdf as bpdf
import pyfits as py
hdu=py.open('/home/rumbaugh/var_database/masterfile.fits')
data=hdu[1].data
outputdir='/home/rumbaugh/var_database'
psfpdf=bpdf.PdfPages('/home/rumbaugh/var_database/plots/changinglookAGNcandidates_fluxplots.12.13.16.pdf')
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
crdescutout=np.loadtxt('/home/rumbaugh/descuts/results/12-5-16/matched_12-5-16.csv',skiprows=1,delimiter=',',dtype={'names':('ra','dec','tile','fname'),'formats':('f8','f8','|S12','|S25')})


#lsras,lsdecs=hms2deg(crls['rah'],crls['ram'],crls['ras']),dms2deg(crls['decd'],crls['decm'],crls['decs'])


crids=np.loadtxt('/home/rumbaugh/var_database/maxdiffs_DBID.12.1.16.txt',dtype={'names':('DBID','maxdiff'),'formats':('i8','f8')})

good_dbids=crids['DBID'][crids['maxdiff']>2]

cr_rids=np.loadtxt('/home/rumbaugh/changinglookAGNcandidates_index.12.6.16.dat',dtype={'names':('DBID','CID','tid','sdr7id','ra','dec','IntFlag'),'formats':('i8','i8','i8','i8','f8','f8','i8')})

good_dbids=cr_rids['DBID'][cr_rids['IntFlag']==1]

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
    if label==None:
        ax.scatter(cens,fluxes,color=curcol,s=36)
    else:
        ax.scatter(cens,fluxes,color=curcol,s=36,label=label)

def calc_flux(ax,mjd,mag,magerr,cbands,band,connectpoints=True):
    gband=np.where(cbands==band)[0]
    magplot=mag[gband]
    magploterr=magerr[gband]
    g100=np.where((magplot<100)&(np.isnan(magplot)==False))[0]
    if len(g100)>1:
        medmag=np.median(magplot[g100])
        
        #medmagerr=np.mean(
    else:
        medmag=magplot[g100]
    if np.shape(medmag)!=(): 
        if len(medmag)==0:
            return 0
        medmag=medmag[0]
    return 10**(medmag/-2.5)


def plot_lightcurve(dbid,mjd,mag,magerr,bands,survey,trueredshift,plotSDSS=False,fname=None,DESfname=None,connectpoints=True):
    redshift=np.copy(trueredshift)
    if redshift<0:redshift=0
    fig=plt.figure(1)
    fig.clf()
    ax=fig.add_subplot(1,1,1)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    #plt.locator_params(nbins=4)
    ax.plot(crv[:,0]/(1.+redshift),crv[:,1],color='k',lw=1)
    gdes,gsdss,gposs,gndes=np.where(survey=='DES')[0],np.where(survey=='SDSS')[0],np.where(survey=='POSS')[0],np.where(survey!='DES')[0]
    if len(gposs)>0:
        POSSmagdict={b: mag[gposs][bands[gposs]==b] for b in POSSbands}
        for band in POSSbands:
            if len(POSSmagdict[band])>0:POSSmagdict[band]=np.array([np.median(POSSmagdict[band])])
        if (len(POSSmagdict['g'])>0)&(len(POSSmagdict['r'])>0):
            mag[gposs[bands[gposs]=='g']],mag[gposs[bands[gposs]=='r']]=mag[gposs][bands[gposs]=='g']+0.392*(POSSmagdict['g']-POSSmagdict['r'])-0.28, mag[gposs][bands[gposs]=='r'] +0.127*(POSSmagdict['g']-POSSmagdict['r'])+0.1
        else: 
            mag[gposs[bands[gposs]=='g']],mag[gposs[bands[gposs]=='r']]=np.zeros(0),np.zeros(0)
        if (len(POSSmagdict['i'])>0)&(len(POSSmagdict['r'])>0):   
            mag[gposs[bands[gposs]=='i']]=mag[gposs][bands[gposs]=='i']+0.27*(POSSmagdict['r']-POSSmagdict['i'])+0.32
        else:
            mag[gposs[bands[gposs]=='i']]=np.zeros(0)
    if len(gdes)>0:
        fluxes=np.zeros(len(['g','r','i','z']))
        for ib,b in zip(np.arange(4),['g','r','i','z']):
            fluxes[ib]=calc_flux(ax,mjd[gdes],mag[gdes],magerr[gdes],bands[gdes],b,connectpoints=connectpoints)
            if np.isnan(fluxes[ib]): fluxes[ib]=0
        if np.mean(fluxes)!=0:
            fluxes*=VBmean/np.mean(fluxes[fluxes>0])
        plot_flux(ax,fluxes,label='DES',curcol='r')
        #print 'DES',fluxes
        #xlim=plt.xlim()
        #plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
        #ylim=plt.ylim()
        #if ylim[1]>30:
        #    ylim=(ylim[0],np.max(mag)+0.1)
        #if ylim[1]>30: ylim=(ylim[0],30)
        #if ylim[0]<15:
        #    ylim=(np.min(mag)-0.1,ylim[1])
        #if ylim[0]<15: ylim=(15,ylim[1])
        #plt.ylim(ylim[1],ylim[0])
        ax.set_ylabel('Wavelength (A)')
        ax.set_xlabel('Flux (Arb. Units)')
    if len(gndes)>0:
        fluxes=np.zeros(len(['g','r','i','z']))
        for ib,b in zip(np.arange(4),['g','r','i','z']):
            fluxes[ib]=calc_flux(ax,mjd[gndes],mag[gndes],magerr[gndes],bands[gndes],b,connectpoints=connectpoints)
            if np.isnan(fluxes[ib]): fluxes[ib]=0
        if np.mean(fluxes)!=0:
            fluxes*=VBmean/np.mean(fluxes[fluxes>0])
        label='SDSS'
        if len(gposs)>0: label='SDSS+POSS'
        plot_flux(ax,fluxes,label=label,curcol='b')
        #print 'SDSS',fluxes
    #xlim=plt.xlim()
    #plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
    #ylim=plt.ylim()
    #if ylim[1]>30:
    #    ylim=(ylim[0],np.max(mag)+0.1)
    #if ylim[1]>30: ylim=(ylim[0],30)
    #if ylim[0]<15:
    #    ylim=(np.min(mag)-0.1,ylim[1])
    #if ylim[0]<15: ylim=(15,ylim[1])
    #plt.ylim(ylim[1],ylim[0])

    ax.legend(loc='lower right')
    ax.set_xlabel('Wavelength (A)')
    ax.set_ylabel('Flux (Arb. Units)')
    plt.xlim(WavLL,WavUL)
    if redshift>0:
        ax.set_title('%i, z=%.4f'%(dbid,trueredshift))
    else:
        ax.set_title(dbid)
    plt.savefig(psfpdf,format='pdf')
    return

def DES2SDSS_gr(g,r):
    return (133625*g-9375*r-218)/124250.,(69.*g+925*r)/994.+516./62125.

def DES2SDSS_iz(i,z):
    return (-89*np.sqrt(-96000*i+96000*z+181561)+8000*z+37827)/8000.,(-17*np.sqrt(-96000*i+96000*z+181561)+24000*z+6731)/24000.

wtol=50.
if maxdb!=None:
    good_dbids=good_dbids[:maxdb]
for DBID in good_dbids:
    gmf=np.where(data['DatabaseID']==DBID)[0][0]
    trueredshift=data['Redshift'][gmf]
    redshift=np.copy(trueredshift)
    if redshift<0: redshift=0
    gx=np.where((np.abs(bcens['g']-crv[:,0]/(1.+redshift))<wtol)|(np.abs(bcens['r']-crv[:,0]/(1.+redshift))<wtol)|(np.abs(bcens['i']-crv[:,0]/(1.+redshift))<wtol)|(np.abs(bcens['z']-crv[:,0]/(1.+redshift))<wtol))[0]
    if len(gx)==0:
        VBmean=np.mean(crv[:,1][(crv[:,0]/(1.+redshift)>WavLL)&(crv[:,0]/(1.+redshift)<WavUL)])
    else:
        VBmean=np.mean(crv[:,1][gx])

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
    plot_lightcurve(DBID,mjd,mag,magerr,bands,survey,trueredshift,plotSDSS=False)

psfpdf.close()
