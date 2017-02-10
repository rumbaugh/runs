import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
execfile('/home/rumbaugh/pythonscripts/angconvert.py')
import matplotlib.backends.backend_pdf as bpdf
outputdir='/home/rumbaugh/var_database'
psfpdf=bpdf.PdfPages('/home/rumbaugh/var_database/plots/CLQ_candidate_lightcurves.MQ.2.9.17.pdf')
DB_path='/home/rumbaugh/var_database'
maxdb=None
WavLL,WavUL=3000,10500

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DatabaseID','Y3A1_COADD_OBJECTS_ID','SDSS_DR13_thingid','SDR7ID'),'formats':('|S64','|S64','|S64','|S64')})

crf=np.loadtxt('/home/rumbaugh/var_database/CLQ_candidate_flags_MQ.dat',dtype={'names':('DatabaseID','Flag'),'formats':('|S64','i8')},skiprows=1)

#lsdict={'names':('DESJ','rah','ram','ras','decd','decm','decs','tif'),'formats':
#('|S4','i8','i8','f8','i8','i8','f8','|S4')}
#delims=(4,2,2,4,3,2,4,4)
#crls=np.genfromtxt('',dtype=lsdict,delimiter=delims)
#lsfilenames=np.loadtxt('',dtype='|S30')

#crdescutin=np.loadtxt('/home/rumbaugh/radecname_forDEScutouts.csv',delimiter=',DEScutout_DBID_',dtype={'names':('radec','DBID'),'formats':('|S20','i8')})
#crdescutout=np.loadtxt('/home/rumbaugh/descuts/results/12-5-16/matched_12-5-16.csv',skiprows=1,delimiter=',',dtype={'names':('ra','dec','tile','fname'),'formats':('f8','f8','|S12','|S25')})


#lsras,lsdecs=hms2deg(crls['rah'],crls['ram'],crls['ras']),dms2deg(crls['decd'],crls['decm'],crls['decs'])


#crids=np.loadtxt('/home/rumbaugh/var_database/maxdiffs_DBID.12.1.16.txt',dtype={'names':('DBID','maxdiff'),'formats':('i8','f8')})

#good_dbids=crids['DBID'][crids['maxdiff']>2]

#cr_rids=np.loadtxt('/home/rumbaugh/changinglookAGNcandidates_index.12.6.16.dat',dtype={'names':('DBID','CID','tid','sdr7id','ra','dec','IntFlag'),'formats':('i8','i8','i8','i8','f8','f8','i8')})

#good_dbids=cr_rids['DBID'][cr_rids['IntFlag']==1]

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
    if len(gdes)>0:
        ax3=plt.subplot2grid((2,10),(1,0),colspan=6)
        plt.rc('axes',linewidth=2)
        plt.fontsize = 14
        plt.tick_params(which='major',length=8,width=2,labelsize=14)
        plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
        plt.locator_params(nbins=4)
        for b in ['g','r','i','z','Y']:
            plot_band(ax3,mjd[gdes],mag[gdes],magerr[gdes],bands[gdes],b,connectpoints=connectpoints)
        xlim=plt.xlim()
        plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
        ylim=plt.ylim()
        if ylim[1]>30:
            ylim=(ylim[0],np.max(mag)+0.1)
        if ylim[1]>30: ylim=(ylim[0],30)
        if ylim[0]<15:
            ylim=(np.min(mag)-0.1,ylim[1])
        if ylim[0]<15: ylim=(15,ylim[1])
        plt.ylim(ylim[1],ylim[0])
        ax3.set_ylabel('Mag_PSF')
        ax3.set_xlabel('MJD')
        ax3.legend()
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
    ax1.set_title(dbid)
    if len(gdes==0):ax1.legend()
    if len(gdes)>999999999999999999999990:
        gdc=np.where(crdescutin['DBID']==DBID)[0]
        if len(gdc)>0:
            if crdescutout['fname'][gdc[0]]!='False':
                DESfname='%s.tif'%(crdescutout['fname'][gdc[0]])
                ax4=plt.subplot2grid((2,10),(1,6),colspan=4,xticks=[],yticks=[])
                img4=mpimg.imread('/home/rumbaugh/descuts/results/12-5-16/%s'%(DESfname))
                ax4.imshow(img4)
    if len(gsdss)>9999999999999999990:
        ax3=plt.subplot2grid((2,10),(0,6),colspan=4,xticks=[],yticks=[])
        SDSSfname='/home/rumbaugh/var_database/plots/%s_SDSScutout.jpeg'%(dbid)
        img3=mpimg.imread(SDSSfname)
        ax3.imshow(img3)
    plt.savefig(psfpdf,format='pdf')
    return

good_dbids=crf['DatabaseID'][crf['Flag']==1]
outcr=np.zeros((len(good_dbids),),dtype={'names':('DatabaseID','cid','sdr7id','ra','dec','flag'),'formats':('|S24','i8','i8','f8','f8','i8')})
outcr['flag'],outcr['DatabaseID']=0,good_dbids
for DBID,idb in zip(good_dbids,np.arange(len(good_dbids))):
    cr=np.loadtxt('%s/Y3A1/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
    gdb=np.where(crdb['DatabaseID']==DBID)[0][0]
    plot_lightcurve(DBID,mjd,mag,magerr,bands,survey,plotSDSS=False)
    outcr['cid'][idb],outcr['sdr7id'][idb],outcr['ra'][idb],outcr['dec'][idb]=crdb['Y3A1_COADD_OBJECTS_ID'][gdb],crdb['SDR7ID'][gdb],np.mean(cr['RA']),np.mean(cr['DEC'])
    ggood=np.where((cr['MAG']>15)&(cr['MAG']<30))[0]#&(cr['FLAG']<16))[0]
    cr=cr[ggood]
    mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
    for band in ['g','r','i','z']:
        gSDSS,gDES=np.where(survey[bands==band]=='SDSS')[0],np.where(survey[bands==band]=='DES')[0]
        if ((len(gSDSS)==0)|(len(gDES)==0)): continue
        SDSSmags,DESmags=mag[bands==band][gSDSS],mag[bands==band][gDES]
        SDSSmagerrs,DESmagerrs=magerr[bands==band][gSDSS],magerr[bands==band][gDES]
        magpairs=np.zeros([len(SDSSmags)*len(DESmags),2])
        magpairs[:,1],magpairs[:,0]=np.repeat(SDSSmags,len(DESmags)),np.tile(DESmags,len(SDSSmags))
        magerrpairs=np.zeros([len(SDSSmagerrs)*len(DESmagerrs),2])
        magerrpairs[:,1],magerrpairs[:,0]=np.repeat(SDSSmagerrs,len(DESmagerrs)),np.tile(DESmagerrs,len(SDSSmagerrs))
        magdiffs,differrs=magpairs[:,0]-magpairs[:,1],np.sqrt(np.sum(magerrpairs**2,axis=1))
        diffsigs=magdiffs/differrs
        gsig=np.where((magdiffs>2)&(diffsigs>3))[0]
        print band,magdiffs
        if len(gsig)>0: candidate_flag[idb]=True
psfpdf.close()
