import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/SphDist.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/KStest.py')
execfile('/home/rumbaugh/set_spec_dict.py')

rbounds=(-0.5,10)
nbins=(rbounds[1]-rbounds[0])*2
infile0='/home/rumbaugh/combined_match_catalog.4.17.16.dat'

indict0={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8','f8','f8','f8')}

crx0=np.loadtxt(infile0,dtype=indict0)


infile='/home/rumbaugh/combined_match_catalog.all_sources.5.31.16.dat'

indict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','ID','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','|S32','f8','f8','f8','f8','f8','f8')}

crx=np.loadtxt(infile,dtype=indict)

linfile='/home/rumbaugh/X-ray_lum_cat.all_sources.5.31.16.dat'

lindict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8')}

crl=np.loadtxt(linfile,dtype=lindict)

sig=np.concatenate((crx['sigS'].reshape((len(crx['sigS']),1)),crx['sigH'].reshape((len(crx['sigH']),1)),crx['sigF'].reshape((len(crx['sigF']),1))),axis=1)
sig=np.max(sig,axis=1)

linfile0='/home/rumbaugh/X-ray_lum_cat.4.17.16.dat'
lindict0={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8')}

crl0=np.loadtxt(linfile0,dtype=lindict0)

sig0=np.concatenate((crx0['sigS'].reshape((len(crx0['sigS']),1)),crx0['sigH'].reshape((len(crx0['sigH']),1)),crx0['sigF'].reshape((len(crx0['sigF']),1))),axis=1)
sig0=np.max(sig0,axis=1)

crx=crx[sig>2]
crl=crl[sig>2]

crx0=crx0[sig0>2]
crl0=crl0[sig0>2]


crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
kpc=crcc[:,12]
DM=crcc[:,15]
cc_z=crcc[:,0]
gdls=np.zeros(len(crx['redshift']),dtype='i8')
for igdl in range(0,len(gdls)):
    gdl=np.argsort(np.abs(crx['redshift'][igdl]-cc_z))[0]
    gdls[igdl]=gdl

legposdict={"rcs0224":'upper left',"cl0849":'upper left',"rxj0910":'lower right',"rxj1221":'upper left',"cl1350":'lower right',"rxj1757":'upper right',"cl0023":'upper right',"cl1324_north":'upper left',"cl1324_south":'upper left',"rxj1821":'upper left',"cl1137":'lower left',"rxj1716":'lower left',"rxj1053":'lower center',"cl1604":'upper left'}


CKPgrouparr=np.zeros((4,5),dtype='object')
groups=['All','z<0.8','0.8<z<0.96','z>0.96']
gfAGN_arr=np.zeros(len(crx['RA']),dtype='bool')
for i in range(0,len(groups)): CKPgrouparr[i]=np.array(['Field,%s'%groups[i],0,0,0,0])
for i in range(0,len(crx['RA'])):
    field=crx['field'][i]
    if field in targets[-2:]: 
        field='cl1324'
        crx['field'][i]='cl1324'
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)  
    gq=np.where((crs['Q']>2.5)&((crs['z']<spec_dict[field]['z'][1])|(crs['z']>spec_dict[field]['z'][2]))&(crs['z']>0.68)&(crs['z']<1.11))[0]
    zs=crs['z']
    zx=crx['redshift'][i]
    if (((zx<spec_dict[field]['z'][1])|(zx>spec_dict[field]['z'][2]))&(zx>0.68)&(zx<1.11)):
        gfAGN_arr[i]=True


fig=plt.figure()

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
lxA,lxB,lxC,lxD=np.log10(crl0['lum_full'][(((crl0['field']=='cl1350')|(crl0['field']=='rxj1221')|(crl0['field']=='rxj1757')|(crl0['field']=='rxj1821')|(crl0['field']=='rcs0224')))]),np.log10(crl0['lum_full'][(((crl0['field']=='cl1324')|(crl0['field']=='cl1324_north')|(crl0['field']=='cl1324_south')|(crl0['field']=='rxj1716')))]),np.log10(crl0['lum_full'][(((crl0['field']=='cl0023')|(crl0['field']=='cl1604')))]),np.log10(crl0['lum_full'][(((crl0['field']=='rxj1053')|(crl0['field']=='cl0849')|(crl0['field']=='rxj0910')))])
plt.hist((lxA,lxB,lxC,lxD),range=(42.5,44.5),bins=4,color=('r','green','blue','purple'),label=('Passive','Intermediate','Cl0023 & Cl1604','High-z'))
plt.xlabel('X-ray Luminosity')
plt.ylabel('Number of Sources')
plt.legend()
#plt.savefig('/home/rumbaugh/Chandra/plots/lum_hist.group_comps.6.15.16.png')

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

lA,lB,lC,lD=np.log10(crl['lum_full'][((gfAGN_arr==True))]),np.log10(crl['lum_full'][((gfAGN_arr==True)&(crl['redshift']<0.8))]),np.log10(crl['lum_full'][((gfAGN_arr==True)&(crl['redshift']>=0.8)&(crl['redshift']<=0.96))]),np.log10(crl['lum_full'][((gfAGN_arr==True)&(crl['redshift']>0.96))])

plt.hist((lA,lB,lC,lD),range=(42.5,44.5),bins=4,color=('r','green','blue','purple'),label=('All','z<0.8','0.8<z<0.96','z>0.96'))
plt.xlabel('X-ray Luminosity')
plt.ylabel('Number of Sources')
plt.legend()
#plt.savefig('/home/rumbaugh/Chandra/plots/lum_hist.field_comp.6.15.16.png')

groupnames=['Passive','Intermediate','Cl0023 & Cl1604','High-z']
fieldnames=['All','z<0.8','0.8<z<0.96','z>0.96']

for ig,group,lg in zip(np.arange(0,4),groupnames,[lxA,lxB,lxC,lxD]):
    for field,ifld,lf in zip(fieldnames,np.arange(0,4),[lA,lB,lC,lD]):
        print '%s - %s: '%(group,field),KStest(lg,lf)
