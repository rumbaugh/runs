import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
#psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/CMDs_param_colors.3.6.16.pdf')
execfile("/home/rumbaugh/KStest.py")


cmloaddict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigs','sigh','sigf'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')}

refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
date='3.6.16'

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]

crRS=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.composite_colors.nofit.%s.dat'%date,dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})
crRS_ACS=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.cl1604_ACS.nofit.%s.dat'%date,dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})
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

#FILERS=open('/home/rumbaugh/Chandra/RS_offsets.AGN.3.6.16.dat','w')
#FILERS.write('# field number RA Dec RSoffset magR magI magZ SCmagRed SCmagBlue\n') 
rso,rso_all=np.zeros(0),np.zeros(0)
cols=()
for i in range(0,len(zarr)): cols=cols+(i+2,)
for field in targets[np.argsort(zlist)]:
    pcat = '/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    crp=np.loadtxt(pcat,dtype=refdict)
    #scat='/home/rumbaugh/Chandra/speccats/%s_spec.cat'%field
    scat='/home/rumbaugh/git/ORELSE/Catalogs/Spec_z/%s'%spec_dict[field]['file']
    crs=np.loadtxt(scat,dtype=specloaddict)
    cmcat='/home/rumbaugh/combined_match_catalog.3.5.16.dat'
    crcm=np.loadtxt(cmcat,cmloaddict)
    if field=='cl1604':
        pcat = '/home/rumbaugh/git/ORELSE/Catalogs/ACS/Cl1604/merged.F606W_F814W_deep.all.coll.hdat'
        crp=np.loadtxt(pcat,dtype={'names':('ra','dec','magR','magI','dmagR','dmagI'),'formats':('f8','f8','f8','f8','f8','f8')})
        crs=np.loadtxt(scat,dtype=ACSspecloaddict)
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
        if ((len(gp)==0)|(field=='cl1604')):
            rerr[ipr],ierr[ipr]=99,99
        else:            
            gp=gp[0]
            rerr[ipr],ierr[ipr],zerr[ipr]=crp['dmagR'][gp],crp['dmagI'][gp],crp['dmagZ'][gp]
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    outfile='%s/%s_clus_CMD_nofit.%s.dat'%(curdir,field,date)
    if field=='cl1604':outfile='%s/%s_clus_CMD_ACS_nofit.%s.dat'%(curdir,field,date)
    cr=np.loadtxt(outfile,dtype={'names':('ID','mask','slit','RA','Dec','redshift','magR','magI','dmagR','dmagI','isXray'),'formats':('|S32','|S32','|S32','f8','f8','f8','f8','f8','f8','f8','bool')})
    gf=np.where(crRS['field']==field)[0][0]
    y0,m,sig=crRS['y0'][gf],crRS['m'][gf],crRS['sig'][gf]
    if field=='cl1604':y0,m,sig=crRS_ACS['y0']+0,crRS_ACS['m']+0,crRS_ACS['sig']+0
    width=2*numsig*sig
    r,i=cr['magR'][0==cr['isXray']],cr['magI'][0==cr['isXray']]

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
    if field=='cl1604':
        AGNr,AGNi=crs['F606W'][gAGN],crs['F814W'][gAGN]
    else:
        AGNr,AGNi,AGNrerr,AGNierr=calc_param_mags(crs['magR'][gAGN],crs['magI'][gAGN],crs['magZ'][gAGN],rerr[gAGN],ierr[gAGN],zerr[gAGN],crs['z'][gAGN],param_dict={'ARed':ARed,'ABlue':ABlue,'BRed':BRed,'BBlue':BBlue,'z':zarr})
    tmprso=(y0+m*AGNi-(AGNr-AGNi))/(0.5*width)
    tmprso_all=(y0+m*i-(r-i))/(0.5*width)
    rso,rso_all=np.append(rso,-tmprso),np.append(rso_all,-tmprso_all)
    print field
    print tmprso
    #for iw in range(0,len(AGNr)):
    #    FILERS.write('%12s %2i %9.5f %9.5f %6.3f %f %f %f %f %f\n'%(field,crcm['number'][gAGN2[iw]],crcm['RA'][gAGN2[iw]],crcm['Dec'][gAGN2[iw]],rso[iw],crs['magR'][gAGN[iw]],crs['magI'][gAGN[iw]],crs['magZ'][gAGN[iw]],AGNi[iw],AGNr[iw]))
    #print r,i
fig.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
ax=fig.add_subplot(1,1,1)
histAGN=ax.hist(rso,range=(-7,2),bins=9,color='r',cumulative=True,normed=True)
histall=ax.hist(rso_all,range=(-10,3),bins=13,color='b',alpha=0.3,cumulative=True,normed=True)#,weights=20*np.ones(len(rso_all))*1./len(rso_all))
ax.set_xlabel("RS Offset")
ax.set_ylabel("Cumulative Fraction")
ax.set_xlim(-10,3)
ax.set_ylim(0,1)
fig.savefig('/home/rumbaugh/Chandra/plots/RS_offset.cumhist.3.11.16.png')

#psfpdf.close()    
#FILERS.close()

KStest(rso,rso_all)
