import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
import matplotlib.backends.backend_pdf as bpdf
psfpdf=bpdf.PdfPages('/home/rumbaugh/Chandra/plots/testCMDs.3.14.16.pdf')

ierrmax=99999999

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
for field in targets[np.argsort(zlist)]:
    FILES1=open('/home/rumbaugh/Chandra/coadd_cats/spectra_all.%s.3.14.16.dat'%field,'w')
    FILES2=open('/home/rumbaugh/Chandra/coadd_cats/spectra_cut-22.3.%s.3.14.16.dat'%field,'w')
    FILERS1=open('/home/rumbaugh/Chandra/coadd_cats/supercolors_all.%s.3.14.16.dat'%field,'w')
    FILERS1.write('# ID RA Dec magR magI magZ dmagR dmagI dmagZ SCmagRed SCmagBlue dRed dBlue\n')
    FILERS2=open('/home/rumbaugh/Chandra/coadd_cats/supercolors_cut-22.3.%s.3.14.16.dat'%field,'w')
    FILERS2.write('# ID RA Dec magR magI magZ dmagR dmagI dmagZ SCmagRed SCmagBlue dRed dBlue\n') 
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
            FILES1.write('# ID mask slit ra dec magR magI magZ z zerr Q oldid notes\n')
            FILES2.write('# ID mask slit ra dec magR magI magZ z zerr Q oldid notes\n')
        except:
            crs=np.loadtxt(scat,dtype=specloaddictwnotes2)
            FILES1.write('# ID mask slit ra dec magR magI magZ z zerr Q notes\n')
            FILES2.write('# ID mask slit ra dec magR magI magZ z zerr Q notes\n')
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
    gcut=np.where(i<=-22.3)[0]
    for j in range(0,len(gCMD)):
        FILERS1.write('%12s %9.5f %9.5f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f\n'%(crs['ID'][gCMD[j]],crs['ra'][gCMD[j]],crs['dec'][gCMD[j]],crs['magR'][gCMD[j]],crs['magI'][gCMD[j]],crs['magZ'][gCMD[j]],rerrorig[gCMD[j]],ierrorig[gCMD[j]],zerrorig[gCMD[j]],i[j],r[j],ierr[j],rerr[j]))
        if j in gcut: FILERS2.write('%12s %9.5f %9.5f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f\n'%(crs['ID'][gCMD[j]],crs['ra'][gCMD[j]],crs['dec'][gCMD[j]],crs['magR'][gCMD[j]],crs['magI'][gCMD[j]],crs['magZ'][gCMD[j]],rerrorig[gCMD[j]],ierrorig[gCMD[j]],zerrorig[gCMD[j]],i[j],r[j],ierr[j],rerr[j]))
    if field=='cl1604':
        FILES1.write('%16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %16s %9.5f %9.5f %8.4f %8.4f %8.4f %s\n'%(crs['ID'][gCMD[j]],crs['mask'][gCMD[j]],crs['slit'][gCMD[j]],crs['ra'][gCMD[j]],crs['dec'][gCMD[j]],crs['magR'][gCMD[j]],crs['magI'][gCMD[j]],crs['magZ'][gCMD[j]],crs['z'][gCMD[j]],crs['zerr'][gCMD[j]],crs['Q'][gCMD[j]],crs['OLDIDs'][gCMD[j]],crs['PHOT_FLAGS'][gCMD[j]],crs['ACS_RA'][gCMD[j]],crs['ACS_DEC'][gCMD[j]],crs['ACS_ID'][gCMD[j]],crs['F606W'][gCMD[j]],crs['F814W'][gCMD[j]],crs['notes'][gCMD[j]]))
        if j in gcut:FILES2.write('%16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %16s %9.5f %9.5f %8.4f %8.4f %8.4f %s\n'%(crs['ID'][gCMD[j]],crs['mask'][gCMD[j]],crs['slit'][gCMD[j]],crs['ra'][gCMD[j]],crs['dec'][gCMD[j]],crs['magR'][gCMD[j]],crs['magI'][gCMD[j]],crs['magZ'][gCMD[j]],crs['z'][gCMD[j]],crs['zerr'][gCMD[j]],crs['Q'][gCMD[j]],crs['OLDIDs'][gCMD[j]],crs['PHOT_FLAGS'][gCMD[j]],crs['ACS_RA'][gCMD[j]],crs['ACS_DEC'][gCMD[j]],crs['ACS_ID'][gCMD[j]],crs['F606W'][gCMD[j]],crs['F814W'][gCMD[j]],crs['notes'][gCMD[j]]))
    elif useoldid:
        FILES1.write('%16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %s\n'%(crs['ID'][gCMD[j]],crs['mask'][gCMD[j]],crs['slit'][gCMD[j]],crs['ra'][gCMD[j]],crs['dec'][gCMD[j]],crs['magR'][gCMD[j]],crs['magI'][gCMD[j]],crs['magZ'][gCMD[j]],crs['z'][gCMD[j]],crs['zerr'][gCMD[j]],crs['Q'][gCMD[j]],crs['oldid'][gCMD[j]],crs['notes'][gCMD[j]]))
        if j in gcut:FILES2.write('%16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %s\n'%(crs['ID'][gCMD[j]],crs['mask'][gCMD[j]],crs['slit'][gCMD[j]],crs['ra'][gCMD[j]],crs['dec'][gCMD[j]],crs['magR'][gCMD[j]],crs['magI'][gCMD[j]],crs['magZ'][gCMD[j]],crs['z'][gCMD[j]],crs['zerr'][gCMD[j]],crs['Q'][gCMD[j]],crs['oldid'][gCMD[j]],crs['notes'][gCMD[j]]))
    else:
        FILES1.write('%16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %s\n'%(crs['ID'][gCMD[j]],crs['mask'][gCMD[j]],crs['slit'][gCMD[j]],crs['ra'][gCMD[j]],crs['dec'][gCMD[j]],crs['magR'][gCMD[j]],crs['magI'][gCMD[j]],crs['magZ'][gCMD[j]],crs['z'][gCMD[j]],crs['zerr'][gCMD[j]],crs['Q'][gCMD[j]],crs['notes'][gCMD[j]]))
        if j in gcut:FILES2.write('%16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %s\n'%(crs['ID'][gCMD[j]],crs['mask'][gCMD[j]],crs['slit'][gCMD[j]],crs['ra'][gCMD[j]],crs['dec'][gCMD[j]],crs['magR'][gCMD[j]],crs['magI'][gCMD[j]],crs['magZ'][gCMD[j]],crs['z'][gCMD[j]],crs['zerr'][gCMD[j]],crs['Q'][gCMD[j]],crs['notes'][gCMD[j]]))
    FILERS1.close()
    FILERS2.close()
    FILES1.close()
    FILES2.close()

    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.scatter(i,r-i)
    ax.set_xlabel("m_red")
    ax.set_ylabel("m_blue - m_red")
    ax.set_title(field)
    fig.savefig(psfpdf,format='pdf')

    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    ax.scatter(i[gcut],r[gcut]-i[gcut])
    ax.set_xlabel("m_red")
    ax.set_ylabel("m_blue - m_red")
    ax.set_title('%s - with cuts'%field)
    fig.savefig(psfpdf,format='pdf')
psfpdf.close()
