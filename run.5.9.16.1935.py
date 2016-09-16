import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")

date='5.9.16'
cmloaddict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','specID','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigs','sigh','sigf'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S48','|S24','|S24','f8','f8','f8','f8','f8','f8')}

adamcorrval=-1.3975614258700002
ierrmax=99999999
crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
DM=crcc[:,15]
cc_z=crcc[:,0]

crx=np.loadtxt('/home/rumbaugh/combined_match_catalog.5.9.16.dat',dtype=cmloaddict)
crxl=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.4.17.16.dat',dtype={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','sig_soft','sig_hard','sig_full'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S64','|S24','f8','f8','f8')})
sigma=np.zeros((np.shape(crx)[0],3))
sigma[:,0],sigma[:,1],sigma[:,2]=crx['sig_soft'],crx['sig_hard'],crx['sig_full']
sigma=np.max(sigma,axis=1)

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]

refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}

groups={'High-z':['rxj0910','cl0849','rxj1053'],'cl0023':['cl0023'],'cl1604':['cl1604'],'intermediate':['cl1324','rxj1716'],'quiescent':['rxj1821','rxj1757','cl1350','rcs0224','rxj1221']}

lumcut=42.5

for group in groups.keys():
    FILES1=open('/home/rumbaugh/Chandra/coadd_cats/spectra_all.%s.%s.dat'%(group,date),'w')
    FILES2=open('/home/rumbaugh/Chandra/coadd_cats/spectra_lumcut_%.1f.%s.%s.dat'%(lumcut,group,date),'w')
    if group=='cl1604':
        FILES1.write('# field ID mask slit ra dec magR magI magZ z zerr Q OLDIDs PHOT_FLAGS ACS_RA ACS_DEC ACS_ID F606W F814W notes\n')
        FILES2.write('# field ID mask slit ra dec magR magI magZ z zerr Q OLDIDs PHOT_FLAGS ACS_RA ACS_DEC ACS_ID F606W F814W notes\n')
    else:
        FILES1.write('# field ID mask slit ra dec magR magI magZ z zerr Q oldid notes\n')
        FILES2.write('# field ID mask slit ra dec magR magI magZ z zerr Q oldid notes\n')
    for field in groups[group]:
        gf=np.where(crx['field']==field)[0]
        if field=='cl1324': gf=np.where((crx['field']==field)|(crx['field']=='cl1324_north')|(crx['field']=='cl1324_south'))[0]
        pcat = '/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
        scat='%s/%s'%(spec_dict['basepath'],spec_dict[field]['file'])
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
        for i in range(0,len(gf)):
            gs=np.where(crs['ID']==crx['specID'][gf[i]])[0]
            if len(gs)>1:
                tmpdist=SphDist(crx['RA'][gf[i]],crx['Dec'][gf[i]],crs['ra'][gs],crs['dec'][gs])
                gas=np.argsort(tmpdist)
                gs=gs[gas[0]]
            elif len(gs)==1:
                gs=gs[0]
            else:
                sys.exit('no match')
            if sigma[gf[i]]>2:
                if field=='cl1604':
                    FILES1.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %16s %9.5f %9.5f %8.4f %8.4f %8.4f %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],crs['OLDIDs'][gs],crs['PHOT_FLAGS'][gs],crs['ACS_RA'][gs],crs['ACS_DEC'][gs],crs['ACS_ID'][gs],crs['F606W'][gs],crs['F814W'][gs],crs['notes'][gs]))
                    if np.log10(crxl['lum_full'][gf[i]])>=lumcut:FILES2.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %16s %9.5f %9.5f %8.4f %8.4f %8.4f %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],crs['OLDIDs'][gs],crs['PHOT_FLAGS'][gs],crs['ACS_RA'][gs],crs['ACS_DEC'][gs],crs['ACS_ID'][gs],crs['F606W'][gs],crs['F814W'][gs],crs['notes'][gs]))
                elif useoldid:
                    FILES1.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],crs['oldid'][gs],crs['notes'][gs]))
                    if np.log10(crxl['lum_full'][gf[i]])>=lumcut:FILES2.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],crs['oldid'][gs],crs['notes'][gs]))
                else:
                    FILES1.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],'NONE',crs['notes'][gs]))
                    if np.log10(crxl['lum_full'][gf[i]])>=lumcut:FILES2.write('%12s %16s %16s %8s %9.5f %9.5f %8.4f %8.4f %8.4f %11.8f %11.8f %2i %16s %s\n'%(field,crs['ID'][gs],crs['mask'][gs],crs['slit'][gs],crs['ra'][gs],crs['dec'][gs],crs['magR'][gs],crs['magI'][gs],crs['magZ'][gs],crs['z'][gs],crs['zerr'][gs],crs['Q'][gs],'NONE',crs['notes'][gs]))
    FILES1.close()
    FILES2.close()
