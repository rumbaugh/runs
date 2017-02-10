import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
execfile('/home/rumbaugh/pythonscripts/angconvert.py')
import matplotlib.backends.backend_pdf as bpdf
outputdir='/home/rumbaugh/var_database'
psfpdf=bpdf.PdfPages('/home/rumbaugh/var_database/plots/CLQ_candidate_lightcurves_cut.MQ.2.10.17.pdf')
DB_path='/home/rumbaugh/var_database'
maxdb=None
WavLL,WavUL=3000,10500

bands=np.array(['g','r','i','z'])
#bcens={'u': 387.663943790537, 'g': 484.183358196563, 'r': 643.8534828217, 'i': 782.099282740933, 'z': 917.234266385718, 'Y': 987.780238651117}
bcens={'u': 3876.63943790537, 'g': 4841.83358196563, 'r': 6438/534828217, 'i': 7820.99282740933, 'z': 9172.34266385718, 'Y': 9877.80238651117}
crv=np.loadtxt('/home/rumbaugh/Downloads/VanderBerk_datafile1.txt',skiprows=23)

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DatabaseID','Y3A1_COADD_OBJECTS_ID','SDSS_DR13_thingid','SDR7ID'),'formats':('|S64','|S64','|S64','|S64')})

crf=np.loadtxt('/home/rumbaugh/CLQ_candidate_list.MQ.2.9.17.dat',dtype={'names':('DatabaseID','cid','thingid','ra','dec','Flag'),'formats':('|S64','|S64','i8','f8','f8','i8')})

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

#cr_rids=np.loadtxt('/home/rumbaugh/changinglookAGNcandidates_index.12.6.16.dat',dtype={'names':('DBID','CID','tid','thingid','ra','dec','IntFlag'),'formats':('i8','i8','i8','i8','f8','f8','i8')})

#good_dbids=cr_rids['DBID'][cr_rids['IntFlag']==1]

coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'%s_SDSS'%b for b in SDSSbands}
POSSbands=np.array(['g','r','i'])

crpmf=np.loadtxt('/home/rumbaugh/MQ_SDSS_y3a1_tidplatemjdfiber.csv',delimiter=',',skiprows=1,dtype={'names':('tid','plate','mjd','fiber'),'formats':('i8','i8','i8','i8')})

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
        gb=np.where(bands==b)[0]
        if len(gb)>1:
            combis=np.array(list(it.combinations(np.arange(len(mag[gb])),2)))
            i1,i2=combis[:,0],combis[:,1]
            sigma=np.abs((mag[gb][i1]-mag[gb][i2])/np.sqrt(magerr[gb][i1]**2+magerr[gb][i2]**2))
            totdiffstmp=np.abs(mag[gb][i1]-mag[gb][i2])
            ggooddiff=np.where((sigma>=3)&(mag[gb][i1]>1)&(mag[gb][i1]<30)&(mag[gb][i2]>1)&(mag[gb][i2]<30))[0]
            if len(ggooddiff)>0:
                bestdiff[b]['diff']=np.max(totdiffstmp[ggooddiff])
                gsort=np.argsort(totdiffstmp[ggooddiff])
                gsortis=np.argsort([mag[gb][i1][ggooddiff][gsort[-1]],mag[gb][i2][ggooddiff][gsort[-1]]])
                imax,imin=[i1,i2][gsortis[0]][ggooddiff][gsort[-1]],[i1,i2][gsortis[1]][ggooddiff][gsort[-1]]
                bestdiff[b]['ihi'],bestdiff[b]['ilo']=imax,imin
    fig=plt.figure(1)
    fig.clf()
    ax3=plt.subplot2grid((2,10),(1,0),colspan=6)
    totdiffs=np.zeros(4)
    for ib,b in zip(np.arange(4),['g','r','i','z']):
        totdiffs[ib]=bestdiff[b]['diff']
    ibest=np.argsort(totdiffs)[-1]
    bbest=['g','r','i','z'][ibest]
    gbbest=np.where(bands==bbest)[0]
    imax,imin=bestdiff[bbest]['ihi'],bestdiff[bbest]['ilo']
    maxfluxes,minfluxes=np.zeros(4),np.zeros(4)
    maxfluxerrs,minfluxerrs=np.zeros(4),np.zeros(4)
    for ib,b in zip(np.arange(4),['g','r','i','z']):
        gbt=np.where(bands==b)[0]
        maxfluxes[ib],maxfluxerrs[ib]=calc_flux(mjd,mag,magerr,bands,b,mjd[gbbest][imax])
        minfluxes[ib],minfluxerrs[ib]=calc_flux(mjd,mag,magerr,bands,b,mjd[gbbest][imin])
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.locator_params(nbins=4)
    if specfile!=None:
        shdu=py.open(specfile)
        specdata=shdu[1].data
        sflux,swav=specdata['flux'],10**(specdata['loglam'])
        s_closei=np.where(np.abs(swav-bcens['i'])<20)[0]
        smwid=10
        swav=swav[smwid:-smwid]
        normflux=sflux/np.mean(sflux[s_closei])
        smoothflux=[np.mean(normflux[x-smwid:x+smwid+1]) for x in np.arange(smwid,len(normflux)-smwid)]
        ax3.plot(swav,smoothflux,lw=1,color='magenta',zorder=1)
    v_closei=np.where(np.abs(crv[:,0]*(1.+redshift)-bcens['i'])<20)[0]
    gvrange=np.where((crv[:,0]*(1.+redshift)>WavLL)&(crv[:,0]*(1.+redshift)<WavUL))[0]
    if len(gvrange)>0:
        vmax=np.max(crv[:,1][gvrange]/np.mean(crv[:,1][v_closei]))
    else:
        vmax=np.max(crv[:,1])
    if trueredshift>0:ax3.plot(crv[:,0]*(1.+redshift),crv[:,1]/np.mean(crv[:,1][v_closei]),color='k',lw=1,zorder=2)
    plot_flux(ax3,maxfluxes,maxfluxerrs,label='Max',curcol='r')
    maxplot=np.max(maxfluxes)
    plot_flux(ax3,minfluxes,minfluxerrs,label='Min',curcol='b')
    if np.max(minfluxes)>maxplot:maxplot=np.max(minfluxes)
    ax3.set_xlabel('Wavelength (A)')
    ax3.set_ylabel('Flux (Arb. Units)')
    survmax,survmin=survey[gbbest][imax],survey[gbbest][imin]
    if ((not('DES' in [survmax,survmin]))&('DES' in survey[bands==bbest])):
        sortmjdcens=np.argsort([mjd[gbbest][imax],mjd[gbbest][imin]])
        iDESex=np.argsort(mag[(bands==bbest)&(survey=='DES')])[-sortmjdcens[0]]
        DESexfluxes,DESexfluxerrs=np.zeros(4),np.zeros(4)
        for ib,b in zip(np.arange(4),['g','r','i','z']):
            gbt=np.where(bands==b)[0]
            DESexfluxes[ib],DESexfluxerrs[ib]=calc_flux(mjd,mag,magerr,bands,b,mjd[(bands==bbest)&(survey=='DES')][iDESex])
        plot_flux(ax3,DESexfluxes,DESexfluxerrs,label='DES %s'%['Max','Min'][-sortmjdcens[0]],curcol='cyan')
        if np.max(DESexfluxes)>maxplot:maxplot=np.max(DESexfluxes)
    #ax3.legend(loc='lower right')
    plt.xlim(WavLL,WavUL)
    plt.ylim(-0.05,vmax*1.05)
    if trueredshift<=0: 
        plt.ylim(-0.05,1.15*maxplot)
    ax1=plt.subplot2grid((2,10),(0,0),colspan=6)
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.locator_params(nbins=4)
    for b in ['g','r','i','z','Y']:
        plot_band(ax1,mjd,mag,magerr,bands,b,connectpoints=connectpoints,nolabels=False)
    xlim=plt.xlim()
    plt.xlim(xlim[0],xlim[1]+0.33*(xlim[1]-xlim[0]))
    ylim=plt.ylim()
    plt.axvline(mjd[gbbest][imax],ls='dashed',lw=1,color='r')
    plt.axvline(mjd[gbbest][imin],ls='dashed',lw=1,color='b')
    if ((not('DES' in [survmax,survmin]))&('DES' in survey[bands==bbest])):plt.axvline(mjd[gbbest][iDESex],ls='dashed',lw=1,color='cyan')
    if ylim[1]>30:
        ylim=(ylim[0],np.max(mag)+0.1)
    if ylim[1]>30: ylim=(ylim[0],30)
    if ylim[0]<15:
        ylim=(np.min(mag)-0.1,ylim[1])
    if ylim[0]<15: ylim=(15,ylim[1])
    plt.ylim(ylim[1],ylim[0])
    ax1.legend()
    ax1.set_xlabel('MJD')
    ax1.set_ylabel('Mag_PSF')
    if redshift>0:
        ax1.set_title('%s, z=%.4f'%(dbid,trueredshift))
    else:
        ax1.set_title(dbid)
    if len(gdes)>999999990:
        gdc=np.where(crdescutin['DBID']==DBID)[0]
        if len(gdc)>0:
            if crdescutout['fname'][gdc[0]]!='False':
                DESfname='%s.tif'%(crdescutout['fname'][gdc[0]])
                ax4=plt.subplot2grid((2,10),(1,6),colspan=4,xticks=[],yticks=[])
                img4=mpimg.imread('/home/rumbaugh/descuts/results/12-18-16/%s'%(DESfname))
                ax4.imshow(img4)
    if len(gsdss)>0:
        ax3=plt.subplot2grid((2,10),(0,6),colspan=4,xticks=[],yticks=[])
        SDSSfname='/home/rumbaugh/var_database/plots/%s_SDSScutout.jpeg'%(dbid)
        img3=mpimg.imread(SDSSfname)
        ax3.imshow(img3)
    plt.savefig(psfpdf,format='pdf')
    return

good_dbids=crf['DatabaseID'][crf['Flag']==1]
outcr=np.zeros((len(good_dbids),),dtype={'names':('DatabaseID','cid','thingid','ra','dec','flag'),'formats':('|S24','i8','i8','f8','f8','i8')})
outcr['flag'],outcr['DatabaseID']=0,good_dbids
for DBID,idb in zip(good_dbids,np.arange(len(good_dbids))):
    cr=np.loadtxt('%s/Y3A1/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
    gdb=np.where(crdb['DatabaseID']==DBID)[0][0]
    plot_lightcurve(DBID,mjd,mag,magerr,bands,survey,plotSDSS=False)
    outcr['cid'][idb],outcr['thingid'][idb],outcr['ra'][idb],outcr['dec'][idb]=crdb['Y3A1_COADD_OBJECTS_ID'][gdb],crdb['SDSS_DR13_thingid'][gdb],np.mean(cr['RA']),np.mean(cr['DEC'])
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
        #print band,magdiffs
        if len(gsig)>0: candidate_flag[idb]=True
psfpdf.close()
