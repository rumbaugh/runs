import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/SphDist.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/KStest.py')
execfile('/home/rumbaugh/set_spec_dict.py')
date='3.12.16'

rbounds=(-0.5,10)
nbins=(rbounds[1]-rbounds[0])*2


cr2=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','ra','dec','z','sig0.5mpc','sig0.5mpcerr','n0.5mpc','sig1mpc','sig1mpcerr','n1mpc','logMvir','LMVerr','nh'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','i8','f8','f8','i8','f8','f8','f8')})
cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_Xray.dat',dtype={'names':('field','cluster','ra','dec','z','nh'),'formats':('|S24','|S24','f8','f8','f8','f8')})
testfield,testclus=np.zeros(np.shape(cr)[0],dtype='|S24'),np.zeros(np.shape(cr)[0],dtype='|S24')
for i in range(0,len(testclus)):
    testfield[i]=cr['field'][i].lower()
    testclus[i]=cr['cluster'][i].lower()
testfield2,testclus2=np.zeros(np.shape(cr2)[0],dtype='|S24'),np.zeros(np.shape(cr2)[0],dtype='|S24')
for i in range(0,len(testclus2)):
    testfield2[i]=cr2['field'][i].lower()
    testclus2[i]=cr2['cluster'][i].lower()

cfields,ras,decs,zs,clus_sig=np.append(testfield2,testfield[-4:]),np.append(cr2['ra'],cr['ra'][-4:]),np.append(cr2['dec'],cr['dec'][-4:]),np.append(cr2['z'],cr['z'][-4:]),np.append(cr2['sig0.5mpc'],np.ones(4)*1000.)
#gcs=np.where(clus_sig==0)[0]
#clus_sig[gcs]=cr2['sig0.5mpc'][gcs]


infile='/home/rumbaugh/combined_match_catalog.1.19.16.dat'

indict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','bcnts_soft','bcnts_hard','bcnts_full'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8')}

crx=np.loadtxt(infile,dtype=indict)

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

spacedist=np.ones(len(crx['RA']))*-1
veldist=np.ones(len(crx['RA']))*-1
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])
specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}
allspacedist=np.zeros(0)
allveldist=np.zeros(0)
AGN_CKP_arr=np.zeros(len(crx['RA']),dtype='bool')
all_CKP_arr=np.zeros(0,dtype='bool')
for i in range(0,len(crx['RA'])):
    field=crx['field'][i]
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)  
    gq=np.where((crs['Q']>2.5)&(crs['z']>spec_dict[field]['z'][1])&(crs['z']<spec_dict[field]['z'][2]))[0]
    zs=crs['z']
    zx=crx['redshift'][i]
    gnoz=np.where((np.abs(crx['RA'][i]-crs['ra'][gq])*np.cos(crx['Dec'][i]*np.pi/180)<20./3600)&(np.abs(crx['Dec'][i]-crs['dec'][gq])<20./3600))[0]
    if ((len(gnoz)>0)&(zx>0.01)):
        tmpdist=60*SphDist(crx['RA'][i],crx['Dec'][i],crs['ra'][gq][gnoz],crs['dec'][gq][gnoz])*kpc[gdls[i]]
        tmpzdist=np.abs(((1+zx)**2-(1+zs[gq][gnoz])**2)/((1+zx)**2+(1+zs[gq][gnoz])**2))*3.*10.**5
        print np.sort(tmpdist)[0:5],np.sort(tmpzdist)[0:5]
        gCKP=np.where((tmpdist<70)&(tmpzdist<350))[0]
        if len(gCKP)>1: AGN_CKP_arr[i]=1

for field in targets: 
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    gq=np.where((crs['Q']>2.5)&(crs['z']>spec_dict[field]['z'][1])&(crs['z']<spec_dict[field]['z'][2]))[0]
    tmpall_CKP_arr=np.zeros(len(crs['z']),dtype='bool')
    zs=crs['z'][gq]
    for i in range(0,len(gq)):
        zx=crs['z'][gq[i]]
        gnoz=np.where((np.abs(crs['ra'][gq[i]]-crs['ra'][gq])*np.cos(crs['dec'][gq[i]]*np.pi/180)<20./3600)&(np.abs(crs['dec'][gq[i]]-crs['dec'][gq])<20./3600)&(gq!=i))[0]
        gdl=np.argsort(np.abs(zx-cc_z))[0]
        tmpzdist=np.abs(((1+zx)**2-(1+zs[gnoz])**2)/((1+zx)**2+(1+zs[gnoz])**2))*3.*10.**5
        tmpdistnoz=60*SphDist(crs['ra'][gq[i]],crs['dec'][gq[i]],crs['ra'][gq[gnoz]],crs['dec'][gq[gnoz]])*kpc[gdl]
        gKDC=np.where((tmpzdist<350)&(tmpdistnoz<70))[0]
        if len(gKDC)>0: tmpall_CKP_arr[i]=1
    all_CKP_arr=np.append(all_CKP_arr,tmpall_CKP_arr)

AGN_CKPs,all_CKPs=np.sum(AGN_CKP_arr),np.sum(all_CKP_arr)/2
print AGN_CKPs,all_CKPs
print AGN_CKPs*1./len(crx['RA']),all_CKPs*1./len(all_CKP_arr)
