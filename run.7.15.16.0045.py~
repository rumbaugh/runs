import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/SphDist.py")
execfile("/home/rumbaugh/set_spec_dict.py")
execfile('/home/rumbaugh/setup_adam_cats.py')

date='6.7.16'
cmloaddict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','specID','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigs','sigh','sigf'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S48','|S24','|S24','f8','f8','f8','f8','f8','f8')}

adamcorrval=-1.3975614258700002
ierrmax=99999999
numsig=3
crRS=np.loadtxt('/home/rumbaugh/final_RS_values_supercolors.notes',dtype={'names':('field','y0','m','sig'),'formats':('|S32','f8','f8','f8')})

crRS_ACS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets.cl1604_ACS.3.6.16.dat',dtype={'names':('field','number','RA','Dec','RSoffset','F606W','F814W'),'formats':('|S24','i8','f8','f8','f8','f8','f8')})

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604","RXJ1821":"rxj1821","RXJ1757":"rxj1757"}

for i in range(0,len(crRS['field'])): crRS['field'][i]=target_dir[crRS['field'][i]]


cmcat='/home/rumbaugh/combined_match_catalog.5.9.16.dat'
crcm=np.loadtxt(cmcat,cmloaddict)
testfield=np.zeros(np.shape(crcm)[0],dtype='|S24')
for i in range(0,len(testfield)):
    testfield[i]=crcm['field'][i].lower()
testfield[((testfield=='cl1324_south')|(testfield=='cl1324_north'))]='cl1324'
crx=crcm
crxl=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.4.17.16.dat',dtype={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','sig_soft','sig_hard','sig_full'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S64','|S24','f8','f8','f8')})
sigma=np.zeros((np.shape(crxl)[0],3))
sigma[:,0],sigma[:,1],sigma[:,2]=crxl['sig_soft'],crxl['sig_hard'],crxl['sig_full']
sigma=np.max(sigma,axis=1)

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

FILES1=open('/home/rumbaugh/Chandra/coadd_cats/spectra_AGN.Region1.%s.dat'%(date),'w')
FILES2=open('/home/rumbaugh/Chandra/coadd_cats/spectra_AGN.Region2.%s.dat'%(date),'w')
FILES3=open('/home/rumbaugh/Chandra/coadd_cats/spectra_AGN.Region3.%s.dat'%(date),'w')
FILES4=open('/home/rumbaugh/Chandra/coadd_cats/spectra_AGN.Region4.%s.dat'%(date),'w')
FILES1.write('# field ID mask slit ra dec magR magI magZ z zerr Q OLDIDs PHOT_FLAGS ACS_RA ACS_DEC ACS_ID F606W F814W notes\n')
FILES2.write('# field ID mask slit ra dec magR magI magZ z zerr Q OLDIDs PHOT_FLAGS ACS_RA ACS_DEC ACS_ID F606W F814W notes\n')
FILES3.write('# field ID mask slit ra dec magR magI magZ z zerr Q OLDIDs PHOT_FLAGS ACS_RA ACS_DEC ACS_ID F606W F814W notes\n')
FILES4.write('# field ID mask slit ra dec magR magI magZ z zerr Q OLDIDs PHOT_FLAGS ACS_RA ACS_DEC ACS_ID F606W F814W notes\n')


for field in targets:
    gf=np.where(crx['field']==field)[0]
    if field=='cl1324': gf=np.where((crx['field']==field)|(crx['field']=='cl1324_north')|(crx['field']=='cl1324_south'))[0]
    pcat = '/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    scat='%s/%s'%(spec_dict['basepath'],spec_dict[field]['file'])
    refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
    crp=np.loadtxt(pcat,dtype=refdict)
    useoldid=True
    if field=='cl1604':
        crs=np.loadtxt(scat,dtype=ACSspecloaddictwnotes)
    else:
        try:
            crs=np.loadtxt(scat,dtype=specloaddictwnotes)
            gnotes=np.where(crs['notes']!='-')[0]
            if len(gnotes)<=1:
                crs=np.loadtxt(scat,dtype=specloaddictwnotes2)
                useoldid=False
        except:
            crs=np.loadtxt(scat,dtype=specloaddictwnotes2)
            useoldid=False
    r,i,redshift,q=crs['magR'],crs['magI'],crs['z'],crs['Q']
    rerr,ierr,zerr=np.zeros(len(r)),np.zeros(len(i)),np.zeros(len(i))
    rerrorig,ierrorig,zerrorig=np.copy(rerr),np.copy(ierr),np.copy(zerr)
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
    for ipr in range(0,np.shape(crs)[0]):
        gp=np.where(((np.abs(crs['ra'][ipr]-crp['ra'])<0.2/3600)&(np.abs(crs['dec'][ipr]-crp['dec'])<0.2/3600)&(np.abs(r[ipr]-crp['magR'])<0.1)&(np.abs(i[ipr]-crp['magI'])<0.1)))[0]
        if len(gp)==0:
            rerr[ipr],ierr[ipr]=99,99
        else:
            gp=gp[0]
            rerr[ipr],ierr[ipr],zerr[ipr]=crp['dmagR'][gp],crp['dmagI'][gp],crp['dmagZ'][gp]
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

    gfRS=np.where(crRS['field']==field)[0][0]
    y0,m,sig=crRS['y0'][gfRS],crRS['m'][gfRS],crRS['sig'][gfRS]
    width=2*numsig*sig

    rso=(y0+m*AGNi-(AGNr-AGNi))/(0.5*width)
    if field=='cl1604':
        rso=np.zeros(len(gAGN))
        for i in range(0,len(gAGN)):
            d1604=SphDist(crs['ra'][gAGN[i]],crs['dec'][gAGN[i]],crRS_ACS['RA'],crRS_ACS['Dec'])
            g0=np.argsort(d1604)[0]
            rso[i]=crRS_ACS['RSoffset'][g0]
    for i in range(0,len(gAGN)):
        gs=gAGN[i]
        #gs=np.where(crs['ID']==crx['specID'][gAGN2[i]])[0]
        #if len(gs)>1:
        #    tmpdist=SphDist(crx['RA'][gAGN2[i]],crx['Dec'][gAGN2[i]],crs['ra'][gs],crs['dec'][gs])
        #    gas=np.argsort(tmpdist)
        #    gs=gs[gas[0]]
        #elif len(gs)==1:
        #    gs=gs[0]
        #else:
        #    sys.exit('no match')
        rfile,region=None,0
        if np.log10(crxl['lum_full'][gAGN2[i]])>=43.3:
            if rso[i]>3: 
                rfile,region=FILES1,1
            elif rso[i]>1:
                rfile,region=FILES2,2
        else:
            if rso[i]<1:
                rfile,region=FILES4,4
            elif rso[i]<3:
                rfile,region=FILES3,3
        if ((sigma[gAGN2[i]]>2)&(rfile!=None)):
            print field,np.log10(crxl['lum_full'][gAGN2[i]]), rso[i], region
            if field=='cl1604':
                rfile.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %16s %9.5f %9.5f %8.4f %8.4f %8.4f %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],crs['OLDIDs'][gs],crs['PHOT_FLAGS'][gs],crs['ACS_RA'][gs],crs['ACS_DEC'][gs],crs['ACS_ID'][gs],crs['F606W'][gs],crs['F814W'][gs],crs['notes'][gs]))
                #if np.log10(crxl['lum_full'][gAGN2[i]])>=lumcut:FILES2.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %16s %9.5f %9.5f %8.4f %8.4f %8.4f %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],crs['OLDIDs'][gs],crs['PHOT_FLAGS'][gs],crs['ACS_RA'][gs],crs['ACS_DEC'][gs],crs['ACS_ID'][gs],crs['F606W'][gs],crs['F814W'][gs],crs['notes'][gs]))
            elif useoldid:
                rfile.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],crs['oldid'][gs],crs['notes'][gs]))
                #if np.log10(crxl['lum_full'][gAGN2[i]])>=lumcut:FILES2.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],crs['oldid'][gs],crs['notes'][gs]))
            else:
                rfile.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],'NONE',crs['notes'][gs]))
                #if np.log10(crxl['lum_full'][gAGN2[i]])>=lumcut:FILES2.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],'NONE',crs['notes'][gs]))egion=1

FILES1.close()
FILES2.close()
FILES3.close()
FILES4.close()
