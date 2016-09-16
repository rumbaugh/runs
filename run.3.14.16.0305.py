import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/diffhist.supercolors_vs_rfU-B.appcor.3.14.16.pdf')
date='3.12.16'

ierrmax=99999999

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

adamnames={'cl0023': 'sg0023+0423_v0.1.7','rxj1716': 'rxj1716+6708_v0.0.5'}
#acatloaddict={'names':('id','z_spec','x','y','ra','dec','fluxaper_B','erraper_B','fluxaper_V','erraper_V','fluxaper_Rplus','erraper_Rplus','fluxaper_Iplus','erraper_Iplus','fluxaper_r','erraper_r','fluxaper_i','erraper_i','fluxaper_z','erraper_z','fluxaper_J','erraper_J','fluxaper_K','erraper_K','fluxcolor_ch1','errcolor_ch1','fluxcolor_ch2','errcolor_ch2','fluxauto_B','errauto_B','fluxauto_V','errauto_V','fluxauto_Rplus','errauto_Rplus','fluxauto_Iplus','errauto_Iplus','fluxauto_r','errauto_r','fluxauto_i','errauto_i','fluxauto_z','errauto_z','fluxauto_J','errauto_J','fluxauto_K','errauto_K','weight_B','weight_V','weight_Rplus','weight_Iplus','weight_r','weight_i','weight_z','weight_J','weight_K','weight_ch1','weight_ch2','wmin','star','saturation','badfit','use'),'formats':('i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8','i8','i8','i8')}
acatloaddict={'names':('id','z_spec','x','y','ra','dec'),'formats':('i8','f8','f8','f8','f8','f8')}
aRFloaddict={'names':('id','z','DM','RF_NUV','RF_U','RF_B','RF_V'),'formats':('i8','f8','f8','f8','f8','f8','f8')}

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]
zarr=np.linspace(0.1,2,1000)
ARed,ABlue=0.424*(1-1.794*(zarr-0.628)),0.45*(1-1.824*(zarr-0.679))
BRed,BBlue=0.576*(1.794*(zarr-0.628)),0.55*(1.824*(zarr-0.679))
ARed[zarr>1/1.794+0.628]=0
BRed[zarr<0.628]=0
ABlue[zarr>1/1.824+0.679]=0
BBlue[zarr<0.679]=0
param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr}
fig=figure(1)
for field in ['cl0023','rxj1716']:
    pcat = '/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    scat='%s/%s'%(spec_dict['basepath'],spec_dict[field]['file'])
    refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
    crp=np.loadtxt(pcat,dtype=refdict)
    useoldid=True
    if field=='cl1604':
        crs=np.loadtxt(scat,dtype=ACSspecloaddictwnotes)
        FILES1.write('# ID mask slit ra dec magR magI magZ z zerr Q OLDIDs PHOT_FLAGS ACS_RA ACS_DEC ACS_ID F606W F814W notes\n')
        FILES2.write('# ID mask slit ra dec magR magI magZ z zerr Q OLDIDs PHOT_FLAGS ACS_RA ACS_DEC ACS_ID F606W F814W notes\n')
    else:
        try:
            crs=np.loadtxt(scat,dtype=specloaddictwnotes)
        except:
            crs=np.loadtxt(scat,dtype=specloaddictwnotes2)
            useoldid=False
    r,i,redshift,q=crs['magR'],crs['magI'],crs['z'],crs['Q']
    rerr,ierr,zerr=np.zeros(len(r)),np.zeros(len(i)),np.zeros(len(i))
    for ipr in range(0,np.shape(crs)[0]):
        gp=np.where(((np.abs(crs['ra'][ipr]-crp['ra'])<0.2/3600)&(np.abs(crs['dec'][ipr]-crp['dec'])<0.2/3600)&(np.abs(r[ipr]-crp['magR'])<0.1)&(np.abs(i[ipr]-crp['magI'])<0.1)))[0]
        if len(gp)==0:
            rerr[ipr],ierr[ipr]=99,99
        else:
            gp=gp[0]
            rerr[ipr],ierr[ipr],zerr[ipr]=crp['dmagR'][gp],crp['dmagI'][gp],crp['dmagZ'][gp]
    rerrorig,ierrorig,zerrorig=np.copy(rerr),np.copy(ierr),np.copy(zerr)
    r,i,rerr,ierr=calc_param_mags(r,i,crs['magZ'],rerr,ierr,zerr,redshift,param_dict=param_dict)
    rerrinit,ierrinit=np.copy(rerr),np.copy(ierr)    
    r,i,redshift,rerr,ierr,gCMD=r[q>2.5],i[q>2.5],redshift[q>2.5],rerr[q>2.5],ierr[q>2.5],np.arange(len(q))[q>2.5]

    g40=np.where((r<40)&(i<40)&(crs['magZ'][q>2.5]<40))[0]
    r,i,rerr,ierr,redshift,gCMD=r[g40],i[g40],rerr[g40],ierr[g40],redshift[g40],gCMD[g40]      
    r,i,rerr,ierr,redshift,gCMD=r[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))],i[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))],rerr[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))],ierr[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))],redshift[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))],gCMD[((redshift>spec_dict[field]['z'][1])&(redshift<spec_dict[field]['z'][2]))]
    r,i,rerr,ierr,redshift,gCMD=r[ierr<ierrmax],i[ierr<ierrmax],rerr[ierr<ierrmax],ierr[ierr<ierrmax],redshift[ierr<ierrmax],gCMD[ierr<ierrmax]
    crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
    D_L=crcc[:,13]*3.086E22
    DM=crcc[:,15]
    cc_z=crcc[:,0]
    gdls=np.zeros(len(redshift),dtype='i8')
    for igdl in range(0,len(gdls)):
        gdl=np.argsort(np.abs(redshift[igdl]-cc_z))[0]
        gdls[igdl]=gdl
    r,i=r-DM[gdls]-2.5*np.log10(1+redshift),i-DM[gdls]-2.5*np.log10(1+redshift)
    gcut=np.where(i<=-22)[0]

    adampath='/home/rumbaugh/git/ORELSE/Catalogs/tomczak_catalogs'
    adamname=adamnames[field]
    acat='%s/%s/%s.cat'%(adampath,adamname,adamname)
    amagcat='%s/%s/%s.mag'%(adampath,adamname,adamname)
    aRFcat='%s/%s/%s.restframe'%(adampath,adamname,adamname)
    cra=np.loadtxt(acat,dtype=acatloaddict)
    crarf=np.loadtxt(aRFcat,dtype=aRFloaddict)
    crmag=np.loadtxt(amagcat,usecols=(26,27))
    crmag=crmag[:,0]
    ga=np.zeros(len(gCMD),dtype='i8')
    for j in range(0,len(gCMD)):
        gatmp=np.where((np.abs(cra['ra']-crs['ra'][gCMD[j]])<1./3600)&(np.abs(cra['dec']-crs['dec'][gCMD[j]])<1./3600))[0]
        gasrt=np.argsort((np.abs(cra['ra']-crs['ra'][gCMD[j]]))**2+(np.abs(cra['dec']-crs['dec'][gCMD[j]]))**2)
        ga[j]=gasrt[0]
    RFU,RFB=crarf['RF_U'][ga],crarf['RF_B'][ga]
    mRFU,mRFB=np.ones(len(RFU))*99,np.ones(len(RFU))*99
    mRFU[RFU>0],mRFB[RFB>0]=-2.5*np.log10(RFU[RFU>0])+25-crmag[ga][RFU>0]-DM[gdls]-2.5*np.log10(1+redshift),-2.5*np.log10(RFB[RFB>0])+25-crmag[ga][RFB>0]-DM[gdls]-2.5*np.log10(1+redshift)
    #mRFU[RFU>0],mRFB[RFB>0]=-2.5*np.log10(RFU[RFU>0])+25-DM[gdls]-2.5*np.log10(1+redshift),-2.5*np.log10(RFB[RFB>0])+25-DM[gdls]-2.5*np.log10(1+redshift)
    print crmag[ga][RFU>0]
    coldiff=r-i-(mRFU-mRFB)
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.hist(coldiff,color='r',range=(-1,1),bins=20)
    ax.set_xlabel("Color Difference")
    ax.set_ylabel("Number of Sources")
    ax.set_title('%s (m_blue-m_red vs rest-frame U-B)'%field)
    ax.set_xlim(-1,1)
    #ax.set_ylim(0,1)
    fig.savefig(psfpdf,format='pdf')
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.hist(r-mRFU,color='r',range=(-6,6),bins=120)
    ax.set_xlabel("Magnitude Difference")
    ax.set_ylabel("Number of Sources")
    ax.set_title('%s (m_blue - restframe U)'%field)
    ax.set_xlim(-2,2)
    #ax.set_ylim(0,1)
    fig.savefig(psfpdf,format='pdf')
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.hist(i-mRFB,color='r',range=(-6,6),bins=120)
    ax.set_xlabel("Magnitude Difference")
    ax.set_ylabel("Number of Sources")
    ax.set_title('%s (m_red - restframe B)'%field)
    ax.set_xlim(-2,2)
    #ax.set_ylim(0,1)
    fig.savefig(psfpdf,format='pdf')
    
psfpdf.close()
