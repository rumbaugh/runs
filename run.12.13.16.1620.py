import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
execfile('/home/rumbaugh/pythonscripts/angconvert.py')
import matplotlib.backends.backend_pdf as bpdf
outputdir='/home/rumbaugh/var_database'
psfpdf=bpdf.PdfPages('/home/rumbaugh/var_database/plots/changinglookAGNcandidates_colplots.12.13.16.pdf')
DB_path='/home/rumbaugh/var_database'
maxdb=None

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

def plot_band(ax,mjd,mag,magerr,cbands,band,band2,survey,connectpoints=True,nolabels=False):
    gbands=np.where((cbands==band)|(cbands==band2))[0]
    gisort=gbands[np.argsort(mjd[gbands])]
    gband=np.where(cbands[gisort]==band)[0]
    gdes,gndes=np.where(survey[gisort][gband]=='DES')[0],np.where(survey[gisort][gband]!='DES')[0]
    if (len(gdes)>0)&(len(gndes)>0):
        magplot,magploterr=np.zeros(len(gisort)),np.zeros(len(gisort))
        gallndes,galldes=np.where(survey[gisort]!='DES')[0],np.where(survey[gisort]=='DES')[0]
        magplot[gallndes]=np.interp(mjd[gisort][gallndes],mjd[gisort][gband][gndes],mag[gisort][gband][gndes])
        magploterr[gallndes]=np.interp(mjd[gisort][gallndes],mjd[gisort][gband][gndes],magerr[gisort][gband][gndes])
        magplot[galldes]=np.interp(mjd[gisort][galldes],mjd[gisort][gband][gdes],mag[gisort][gband][gdes])
        magploterr[galldes]=np.interp(mjd[gisort][galldes],mjd[gisort][gband][gdes],magerr[gisort][gband][gdes])
    else:
        magplot=np.interp(mjd[gisort],mjd[gisort][gband],mag[gisort][gband])
        magploterr=np.interp(mjd[gisort],mjd[gisort][gband],magerr[gisort][gband])
    g100_1=np.where(magplot<100)[0]

    gband2=np.where(cbands[gisort]==band2)[0]
    gdes,gndes=np.where(survey[gisort][gband2]=='DES')[0],np.where(survey[gisort][gband2]!='DES')[0]
    if (len(gdes)>0)&(len(gndes)>0):
        magplot2,magplot2err=np.zeros(len(gisort)),np.zeros(len(gisort))
        gallndes,galldes=np.where(survey[gisort]!='DES')[0],np.where(survey[gisort]=='DES')[0]
        #print len(gisort),len(gallndes),len(gband2),len(gndes)
        #print mjd[gisort][gallndes]
        #print mjd[gisort][gband2][gndes]
        #print mag[gisort][gband2][gndes]
        #print magplot2[gisort[gallndes]]
        magplot2[gallndes]=np.interp(mjd[gisort][gallndes],mjd[gisort][gband2][gndes],mag[gisort][gband2][gndes])
        magplot2err[gallndes]=np.interp(mjd[gisort][gallndes],mjd[gisort][gband2][gndes],magerr[gisort][gband2][gndes])
        magplot2[galldes]=np.interp(mjd[gisort][galldes],mjd[gisort][gband2][gdes],mag[gisort][gband2][gdes])
        magplot2err[galldes]=np.interp(mjd[gisort][galldes],mjd[gisort][gband2][gdes],magerr[gisort][gband2][gdes])
    else:
        magplot2=np.interp(mjd[gisort],mjd[gisort][gband2],mag[gisort][gband2])
        magplot2err=np.interp(mjd[gisort],mjd[gisort][gband2],magerr[gisort][gband2])
    g100_2=np.where(magplot2<100)[0]
    g100=np.intersect1d(g100_1,g100_2)
    colplot,colploterr=magplot-magplot2,np.sqrt(magploterr**2+magplot2err**2)
    try:
        curcol=coldict[band]
    except KeyError:
        print '%s is not a valid band'%band
        return
    if connectpoints:
        #gsort=np.argsort(mjd[gband][g100])
        ax.plot(mjd[gisort][g100],colplot[g100],color=curcol,lw=2)
    ax.errorbar(mjd[gisort][g100],colplot[g100],yerr=colploterr[g100],color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    if nolabels:
        ax.scatter(mjd[gisort][g100],colplot[g100],color=curcol)
    else:
        ax.scatter(mjd[gisort][g100],colplot[g100],color=curcol,label='%s-%s'%(band,band2))
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
    if len(gdes)>0:
        ax3=plt.subplot2grid((2,10),(1,0),colspan=6)
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        plt.locator_params(nbins=4)
        for b,b2 in zip(['g','r','i'],['r','i','z']):
            if (b in bands[gdes])&(b2 in bands[gdes]):plot_band(ax3,mjd[gdes],mag[gdes],magerr[gdes],bands[gdes],b,b2,survey,connectpoints=connectpoints)
        xlim=plt.xlim()
        plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
        ylim=plt.ylim()
        #if ylim[1]>30:
        #    ylim=(ylim[0],np.max(mag)+0.1)
        #if ylim[1]>30: ylim=(ylim[0],30)
        #if ylim[0]<15:
        #    ylim=(np.min(mag)-0.1,ylim[1])
        #if ylim[0]<15: ylim=(15,ylim[1])
        plt.ylim(ylim[1],ylim[0])
        ax3.set_ylabel('Color')
        ax3.set_xlabel('MJD')
        ax3.legend()
    ax1=plt.subplot2grid((2,10),(0,0),colspan=6)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.locator_params(nbins=4)
    for b,b2 in zip(['g','r','i'],['r','i','z']):
        if (b in bands)&(b2 in bands):
            if len(gdes)>0:
                plot_band(ax1,mjd,mag,magerr,bands,b,b2,survey,connectpoints=connectpoints,nolabels=True)
            else:
                plot_band(ax1,mjd,mag,magerr,bands,b,b2,survey,connectpoints=connectpoints,nolabels=False)
    xlim=plt.xlim()
    plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
    ylim=plt.ylim()
    #if ylim[1]>30:
    #    ylim=(ylim[0],np.max(mag)+0.1)
    #if ylim[1]>30: ylim=(ylim[0],30)
    #if ylim[0]<15:
    #    ylim=(np.min(mag)-0.1,ylim[1])
    #if ylim[0]<15: ylim=(15,ylim[1])
    plt.ylim(ylim[1],ylim[0])
    ax1.legend()
    #ax1.set_xlabel('MJD')
    ax1.set_ylabel('Color')
    ax1.set_title(dbid)
    if len(gdes==0):ax1.legend()
    if len(gdes)>0:
        gdc=np.where(crdescutin['DBID']==DBID)[0]
        if len(gdc)>0:
            if crdescutout['fname'][gdc[0]]!='False':
                DESfname='%s.tif'%(crdescutout['fname'][gdc[0]])
                ax4=plt.subplot2grid((2,10),(1,6),colspan=4,xticks=[],yticks=[])
                img4=mpimg.imread('/home/rumbaugh/descuts/results/12-5-16/%s'%(DESfname))
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
    plot_lightcurve(DBID,mjd,mag,magerr,bands,survey,plotSDSS=False)

psfpdf.close()
