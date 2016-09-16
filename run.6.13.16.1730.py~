import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile("/home/rumbaugh/makeCMD.py")
execfile('/home/rumbaugh/set_spec_dict.py')
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/CMDs_param_colors.6.7.16.pdf')
adamcorrval=-1.3975614258700002

cmloaddict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigs','sigh','sigf'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')}

refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
date='3.9.16'

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]

crRS=np.loadtxt('/home/rumbaugh/final_RS_values_supercolors.notes',dtype={'names':('field','y0','m','sig'),'formats':('|S32','f8','f8','f8')})

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604","RXJ1821":"rxj1821","RXJ1757":"rxj1757"}

for i in range(0,len(crRS['field'])): crRS['field'][i]=target_dir[crRS['field'][i]]

fig=figure(1)
zarr=np.linspace(0.1,2,191)

#ARed,ABlue=0.43*(1-1.81*(zarr-0.63)),0.45*(1-1.825*(zarr-0.7))
#BRed,BBlue=0.57*(1.81*(zarr-0.63)),0.55*(1.825*(zarr-0.7))
ARed,ABlue=0.424*(1-1.794*(zarr-0.628)),0.45*(1-1.824*(zarr-0.679))
BRed,BBlue=0.576*(1.794*(zarr-0.628)),0.55*(1.824*(zarr-0.679))
ARed[zarr>1/1.794+0.628]=0
BRed[zarr<0.628]=0
ABlue[zarr>1/1.824+0.679]=0
BBlue[zarr<0.679]=0

FILERS=open('/home/rumbaugh/Chandra/RS_offsets.AGN.6.7.16.dat','w')
FILERS.write('# field number RA Dec RSoffset magR magI magZ SCmagRed SCmagBlue\n')

cols=()
for i in range(0,len(zarr)): cols=cols+(i+2,)
for field in targets[np.argsort(zlist)]:
    pcat = '/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    crp=np.loadtxt(pcat,dtype=refdict)
    scat='/home/rumbaugh/Chandra/speccats/%s_spec.cat'%field
    crs=np.loadtxt(scat,dtype=specloaddict)
    cmcat='/home/rumbaugh/combined_match_catalog.5.9.16.dat'
    crcm=np.loadtxt(cmcat,cmloaddict)
    testfield=np.zeros(np.shape(crcm)[0],dtype='|S24')
    for i in range(0,len(testfield)):
        testfield[i]=crcm['field'][i].lower()
    testfield[((testfield=='cl1324_south')|(testfield=='cl1324_north'))]='cl1324'
    #if field[:6] in ['cl1604','cl1324']:
    if field[:6] in ['aaacl1604','aaacl1324']:
        numsig=2
    else: 
        numsig=3
    rerr,ierr,zerr=np.zeros(len(crs['magR'])),np.zeros(len(crs['magR'])),np.zeros(len(crs['magR']))
    for ipr in range(0,np.shape(crs)[0]):
        gp=np.where(((np.abs(crs['ra'][ipr]-crp['ra'])<0.2/3600)&(np.abs(crs['dec'][ipr]-crp['dec'])<0.2/3600)&(np.abs(crs['magR'][ipr]-crp['magR'])<0.1)&(np.abs(crs['magI'][ipr]-crp['magI'])<0.1)))[0]
        if len(gp)==0:
            rerr[ipr],ierr[ipr]=99,99
        else:            
            gp=gp[0]
            rerr[ipr],ierr[ipr],zerr[ipr]=crp['dmagR'][gp],crp['dmagI'][gp],crp['dmagZ'][gp]
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    outfile='%s/%s_clus_CMD_nofit.%s.dat'%(curdir,field,date)
    cr=np.loadtxt(outfile,dtype={'names':('ID','mask','slit','RA','Dec','redshift','magR','magI','dmagR','dmagI','isXray'),'formats':('|S32','|S32','|S32','f8','f8','f8','f8','f8','f8','f8','bool')})
    plotfile='/home/rumbaugh/Chandra/plots/CMD_comp_color.nofit.%s_clus.%s.png'%(field,date)
    gf=np.where(crRS['field']==field)[0][0]
    y0,m,sig=crRS['y0'][gf],crRS['m'][gf],crRS['sig'][gf]
    width=2*numsig*sig
    r,i=cr['magR'][0==cr['isXray']],cr['magI'][0==cr['isXray']]
    r,i=r-adamcorrval,i-adamcorrval
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
    AGNr,AGNi,AGNrerr,AGNierr=calc_param_mags(crs['magR'][gAGN],crs['magI'][gAGN],crs['magZ'][gAGN],rerr[gAGN],ierr[gAGN],zerr[gAGN],crs['z'][gAGN],param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr})
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
    rso=(y0+m*AGNi-(AGNr-AGNi))/(0.5*width)
    for iw in range(0,len(AGNr)):
        FILERS.write('%12s %2i %9.5f %9.5f %6.3f %f %f %f %f %f\n'%(field,crcm['number'][gAGN2[iw]],crcm['RA'][gAGN2[iw]],crcm['Dec'][gAGN2[iw]],rso[iw],crs['magR'][gAGN[iw]],crs['magI'][gAGN[iw]],crs['magZ'][gAGN[iw]],AGNi[iw],AGNr[iw]))
    #print r,i
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.scatter(i,r-i)
    ax.scatter(AGNi,AGNr-AGNi,color='r',marker='x',s=64)
    ax.set_xlabel("m_red")
    ax.set_ylabel("m_blue - m_red")
    ax.set_title(field)
    ax.set_xlim(-27,-19.5)
    ax.set_ylim(-0.5,1.72)
    xlim=plt.xlim()
    ylim=plt.ylim()
    xspace=np.linspace(xlim[0],xlim[1],1000)
    ydummy=m*(xspace)+y0
    ax.plot(xspace,ydummy+0.5*width,ls='--',lw=2,color='r')
    ax.plot(xspace,ydummy-0.5*width,ls='--',lw=2,color='r')
    ax.set_xlim(-27,-19.5)
    ax.axvline(-22.3)
    #ax.set_xlim(18.5,25)
    ax.set_ylim(-0.5,1.72)
    fig.savefig(psfpdf,format='pdf')
    
    #fig.savefig(plotfile)
psfpdf.close()    
FILERS.close()
