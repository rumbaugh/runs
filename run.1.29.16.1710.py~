import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
execfile('/home/rumbaugh/setup_adam_cats.py')
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/CMDs_wACS.9.26.16.pdf')

cmloaddict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','specID','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigs','sigh','sigf'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S48','|S24','|S24','f8','f8','f8','f8','f8','f8')}

adamcorrval=-1.3975614258700002
ierrmax=99999999
numsig=3
crRS=np.loadtxt('/home/rumbaugh/final_RS_values_supercolors.notes',dtype={'names':('field','y0','m','sig'),'formats':('|S32','f8','f8','f8')})
crRS_ACS=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.cl1604_ACS.nofit.3.6.16.dat',dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604","RXJ1821":"rxj1821","RXJ1757":"rxj1757"}

for i in range(0,len(crRS['field'])): crRS['field'][i]=target_dir[crRS['field'][i]]

cmcat='/home/rumbaugh/combined_match_catalog.5.9.16.dat'
crcm=np.loadtxt(cmcat,cmloaddict)
testfield=np.zeros(np.shape(crcm)[0],dtype='|S24')
for i in range(0,len(testfield)):
    testfield[i]=crcm['field'][i].lower()
testfield[((testfield=='cl1324_south')|(testfield=='cl1324_north'))]='cl1324'
        
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

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
#FILERS=open('/home/rumbaugh/Chandra/RS_offsets_wACS.6.13.16.dat','w')
#FILERS.write('# field AGNnumber specID RA Dec RSoffset magR magI magZ SCmagRed SCmagBlue\n')
FILEall=open('/home/rumbaugh/Chandra/CMD_info_all.9.26.16.dat','w')
FILEAGN=open('/home/rumbaugh/Chandra/CMD_info_AGN.9.26.16.dat','w')
FILEall.write('# Mag Color Field\n')
FILEAGN.write('# Mag Color Field\n')
for field in targets[np.argsort(zlist)]:
    pcat = '/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    scat='%s/%s'%(spec_dict['basepath'],spec_dict[field]['file'])
    refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
    useoldid=True
    if field=='cl1604':
        pcat = '/home/rumbaugh/git/ORELSE/Catalogs/ACS/Cl1604/merged.F606W_F814W_deep.all.coll.hdat'
        crp=np.loadtxt(pcat,dtype={'names':('ra','dec','magR','magI','dmagR','dmagI'),'formats':('f8','f8','f8','f8','f8','f8')})
        crs=np.loadtxt(scat,dtype=ACSspecloaddict,usecols=ACStc)
    else:
        crs=np.loadtxt(scat,dtype=specloaddict,usecols=tc)
        crp=np.loadtxt(pcat,dtype=refdict,usecols=ptc)
    r,i,redshift,q=crs['magR'],crs['magI'],crs['z'],crs['Q']
    rerr,ierr,zerr=np.zeros(len(r)),np.zeros(len(i)),np.zeros(len(i))
    for ipr in range(0,np.shape(crs)[0]):
        gp=np.where(((np.abs(crs['ra'][ipr]-crp['ra'])<0.2/3600)&(np.abs(crs['dec'][ipr]-crp['dec'])<0.2/3600)&(np.abs(r[ipr]-crp['magR'])<0.1)&(np.abs(i[ipr]-crp['magI'])<0.1)))[0]
        if ((len(gp)==0)|(field=='cl1604')):
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
    
    r,i=r-adamcorrval,i-adamcorrval
    gcut=np.where(i<=-20.9)[0]
    
    gAGN=np.zeros(0,dtype='i8')
    gAGN2=np.zeros(0,dtype='i8')
    gf=np.where(field==testfield)[0]

    for igf in range(0,len(gf)):
        gsm=np.where((np.abs(crcm['RA'][gf[igf]]-crs['ra'])<20/3600.)&(np.abs(crcm['Dec'][gf[igf]]-crs['dec'])<20/3600.)&(np.abs(crcm['redshift'][gf[igf]]-crs['z'])<0.01)&(crcm['mask'][gf[igf]]==crs['mask'])&(crcm['slit'][gf[igf]]==crs['slit']))[0]
        if len(gsm)==0:
            print 'No match for source %s %i'%(field,crcm['number'][gf[igf]])
        else:
            if len(gsm)>1:
                print 'More than one match for source %s %i'%(field,crcm['number'][gf[igf]])
                print crs['mask'][gsm],crs['slit'][gsm]
            if ((crcm['sigs'][gf[igf]]>2)|(crcm['sigh'][gf[igf]]>2)|(crcm['sigf'][gf[igf]]>2)):
                gAGN=np.append(gAGN,gsm[0])
                gAGN2=np.append(gAGN2,gf[igf])
    AGNr,AGNi,AGNrerr,AGNierr=calc_param_mags(crs['magR'][gAGN],crs['magI'][gAGN],crs['magZ'][gAGN],rerrorig[gAGN],ierrorig[gAGN],zerrorig[gAGN],crs['z'][gAGN],param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr})
    crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
    D_L=crcc[:,13]*3.086E22
    DM=crcc[:,15]
    cc_z=crcc[:,0]
    gdls=np.zeros(len(gAGN),dtype='i8')
    for igdl in range(0,len(gdls)):
        gdl=np.argsort(np.abs(crs['z'][gAGN][igdl]-cc_z))[0]
        gdls[igdl]=gdl
    AGNr,AGNi=AGNr-DM[gdls]-2.5*np.log10(1+crs['z'][gAGN]),AGNi-DM[gdls]-2.5*np.log10(1+crs['z'][gAGN])
    AGNr,AGNi=AGNr-adamcorrval,AGNi-adamcorrval
    if field=='cl1604':
        AGNr,AGNi=crs['F606W'][gAGN],crs['F814W'][gAGN]
        r,i=crs['F606W'][gCMD],crs['F814W'][gCMD]

    gf=np.where(crRS['field']==field)[0][0]
    y0,m,sig=crRS['y0'][gf],crRS['m'][gf],crRS['sig'][gf]
    if field=='cl1604':y0,m,sig=crRS_ACS['y0']+0,crRS_ACS['m']+0,crRS_ACS['sig']+0
    width=2*numsig*sig

    rso=(y0+m*AGNi-(AGNr-AGNi))/(0.5*width)
    rso_all=(y0+m*i-(r-i))/(0.5*width)
    #for iw in range(0,len(AGNr)):
    #    #FILERS.write('%12s %2i %16s %9.5f %9.5f %6.3f %f %f %f %f %f\n'%(field,crcm['number'][gAGN2[iw]],crs['ID'][gAGN[iw]],crcm['RA'][gAGN2[iw]],crcm['Dec'][gAGN2[iw]],rso[iw],crs['magR'][gAGN[iw]],crs['magI'][gAGN[iw]],crs['magZ'][gAGN[iw]],AGNi[iw],AGNr[iw]))
    #for iw in range(0,len(gCMD)):
    #    if iw not in gAGN: #FILERS.write('%12s -1 %16s %9.5f %9.5f %6.3f %f %f %f %f %f\n'%(field,crs['ID'][gCMD[iw]],crs['ra'][gCMD[iw]],crs['dec'][gCMD[iw]],rso_all[iw],crs['magR'][gCMD[iw]],crs['magI'][gCMD[iw]],crs['magZ'][gCMD[iw]],i[iw],r[iw]))


    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 20
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.scatter(i,r-i)
    for n in range(0,len(i)): FILEall.write('%f %f %s\n'%(i[n],r[n]-i[n],field))
    ax.scatter(AGNi,AGNr-AGNi,color='magenta',marker='d',s=96)
    for n in range(0,len(AGNi)): FILEAGN.write('%f %f %s\n'%(AGNi[n],AGNr[n]-AGNi[n],field))
    ax.set_title(field)
    if field == 'cl1604':
        ax.set_xlim(20.5,25.5)
        ax.set_ylim(-0.5,2.6)
        ax.set_xlabel('F814W',fontsize='large')
        ax.set_ylabel('F606W-F814W',fontsize='large')
    else:
        ax.set_xlim(-27,-19.5)
        ax.set_ylim(-0.5,1.72)
        ax.set_xlabel(r'$M_{red}$',fontsize='large')
        ax.set_ylabel(r'$M_{blue} - M_{red}$',fontsize='large')
    xlim=plt.xlim()
    ylim=plt.ylim()
    xspace=np.linspace(xlim[0],xlim[1],1000)
    ydummy=m*(xspace)+y0
    ax.plot(xspace,ydummy+0.5*width,ls='--',lw=2,color='r')
    ax.plot(xspace,ydummy-0.5*width,ls='--',lw=2,color='r')
    if field == 'cl1604':
        ax.set_xlim(20.5,25)
        ax.set_ylim(0,2.1)
    else:
        ax.set_xlim(-25.7,-19.5)
        ax.axvline(-20.9,color='k',ls='dotted',lw=2)
        ax.set_ylim(0,1.72)
    fig.savefig(psfpdf,format='pdf')
    
psfpdf.close()
#FILERS.close()
FILEall.close()
FILEAGN.close()
