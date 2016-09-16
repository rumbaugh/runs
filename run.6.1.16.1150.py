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


infile='/home/rumbaugh/combined_match_catalog.4.17.16.dat'

indict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8','f8','f8','f8')}

crx=np.loadtxt(infile,dtype=indict)

linfile='/home/rumbaugh/X-ray_lum_cat.4.17.16.dat'

lindict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8','f8','f8','f8')}

crl=np.loadtxt(linfile,dtype=lindict)

sig=np.concatenate((crx['sigS'].reshape((len(crx['sigS']),1)),crx['sigH'].reshape((len(crx['sigH']),1)),crx['sigF'].reshape((len(crx['sigF']),1))),axis=1)
sig=np.max(sig,axis=1)

crx=crx[sig>2]
crl=crl[sig>2]

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
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023",'cl1324',"rxj1821","cl1137","rxj1716","rxj1053","cl1604","cl1324_north","cl1324_south"])
specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}
allspacedist=np.zeros(0)
allveldist=np.zeros(0)
AGN_CKP_arr=np.zeros(len(crx['RA']),dtype='bool')
all_CKP_arr=np.zeros(0,dtype='bool')
for i in range(0,len(crx['RA'])):
    field=crx['field'][i]
    if field in targets[-2:]: 
        field='cl1324'
        crx['field'][i]='cl1324'
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)  
    gq=np.where((crs['Q']>2.5)&(crs['z']>spec_dict[field]['z'][1])&(crs['z']<spec_dict[field]['z'][2]))[0]
    zs=crs['z']
    zx=crx['redshift'][i]
    gnoz=np.where((np.abs(crx['RA'][i]-crs['ra'][gq])*np.cos(crx['Dec'][i]*np.pi/180)<20./3600)&(np.abs(crx['Dec'][i]-crs['dec'][gq])<20./3600))[0]
    if ((len(gnoz)>0)&(zx>0.01)):
        tmpdist=60*SphDist(crx['RA'][i],crx['Dec'][i],crs['ra'][gq][gnoz],crs['dec'][gq][gnoz])*kpc[gdls[i]]
        tmpzdist=np.abs(((1+zx)**2-(1+zs[gq][gnoz])**2)/((1+zx)**2+(1+zs[gq][gnoz])**2))*3.*10.**5
        #print np.sort(tmpdist)[0:5],np.sort(tmpzdist)[0:5]
        gCKP=np.where((tmpdist<70)&(tmpzdist<350))[0]
        if len(gCKP)>1: AGN_CKP_arr[i]=1

group_dict={'Passive':['rcs0224','rxj1221','cl1350','rxj1757','rxj1821'],'Intermediate':['cl1324','rxj1716'],'Cl0023+Cl1604':['cl0023','cl1604'],'High-z':['cl0849','rxj1053','rxj0910']}
groups=group_dict.keys()
CKPgrouparr=np.zeros((4,5),dtype='object')
dum=np.zeros(0)
for i in range(0,4): CKPgrouparr[i]=np.array([groups[i],len(dum),len(dum),len(dum),len(dum)])
CKParr=np.zeros((len(targets[:-2]),5),dtype='object')
CKPallarr=np.zeros((len(targets[:-2]),2),dtype='object')
zlist=np.zeros(len(targets[:-2]))
for i in range(0,len(zlist)): zlist[i]=spec_dict[targets[i]]['z'][0]
gzlist=np.argsort(zlist)
for field,ifld in zip(targets[gzlist],np.arange(len(gzlist))): 
    #gAGN=np.where((field==crx['field'])&(sig>2))[0]
    gAGN=np.where((field==crx['field']))[0]
    numAGN=len(gAGN)
    numAGN_CKP=np.sum(AGN_CKP_arr[gAGN])
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    gq=np.where((crs['Q']>2.5)&(crs['z']>spec_dict[field]['z'][1])&(crs['z']<spec_dict[field]['z'][2]))[0]
    tmpall_CKP_arr=np.zeros(len(crs['z'][gq]),dtype='bool')
    zs=crs['z'][gq]
    for i in range(0,len(gq)):
        zx=crs['z'][gq[i]]
        gnoz=np.where((np.abs(crs['ra'][gq[i]]-crs['ra'][gq])*np.cos(crs['dec'][gq[i]]*np.pi/180)<100./3600)&(np.abs(crs['dec'][gq[i]]-crs['dec'][gq])<100./3600)&(gq!=i))[0]
        gdl=np.argsort(np.abs(zx-cc_z))[0]
        tmpzdist=np.abs(((1+zx)**2-(1+zs[gnoz])**2)/((1+zx)**2+(1+zs[gnoz])**2))*3.*10.**5
        tmpdistnoz=60*SphDist(crs['ra'][gq[i]],crs['dec'][gq[i]],crs['ra'][gq[gnoz]],crs['dec'][gq[gnoz]])*kpc[gdl]
        gKDC=np.where((tmpzdist<350)&(tmpdistnoz<70))[0]
        if len(gKDC)>1: tmpall_CKP_arr[i]=1
    all_CKP_arr=np.append(all_CKP_arr,tmpall_CKP_arr)
    print '%s - \n\nNum. of AGN with CKP: %i\nNum. of total AGN: %i\nPercentage with CKP: %.1f%%\nPercentage for all galaxies: %.1f%%\n'%(field,numAGN_CKP,numAGN,numAGN_CKP*100./numAGN,np.sum(tmpall_CKP_arr)*100./len(gq))
    CKParr[ifld]=np.array([field,numAGN_CKP,numAGN,np.round(numAGN_CKP*100./numAGN,2),np.round(np.sum(tmpall_CKP_arr)*100./len(gq),2)])
    CKPallarr[ifld]=np.array([np.sum(tmpall_CKP_arr),len(gq)])

for i in range(0,4):
    group=groups[i]
    print group
    for j in range(0,len(group_dict[group])):
        field=group_dict[group][j]
        g=np.where(targets[gzlist]==field)[0][0]
        CKPgrouparr[i][1:]=np.array(CKPgrouparr[i][1:],dtype='i8')+[int(CKParr[g][1]),int(CKParr[g][2]),int(CKPallarr[g][0]),int(CKPallarr[g][1])]
    CKPgrouparr[i][4]=np.round(int(CKPgrouparr[i][3])*100./int(CKPgrouparr[i][4]),2)
    CKPgrouparr[i][3]=np.round(int(CKPgrouparr[i][1])*100./int(CKPgrouparr[i][2]),2)

AGN_CKPs,all_CKPs=np.sum(AGN_CKP_arr),np.sum(all_CKP_arr)
print AGN_CKPs,all_CKPs
print AGN_CKPs*1./len(crx['RA']),all_CKPs*1./len(all_CKP_arr)

cra=np.loadtxt('/home/rumbaugh/Chandra/field_CKP_stat.dat',dtype={'names':('group','num_AGN_CKP','num_AGN','num_all_CKP','num_all'),'formats':('|S24','i8','i8','i8','i8')})

CKP_GPF_arr=np.zeros((8,5),dtype='object')
CKP_GPF_arr[:4]=CKPgrouparr
for i in range(0,4):
    CKP_GPF_arr[i+4]=np.array([cra['group'][i],cra['num_AGN_CKP'][i],cra['num_AGN'][i],np.round(cra['num_AGN_CKP'][i]*100./cra['num_AGN'][i],2),np.round(cra['num_all_CKP'][i]*100./cra['num_all'][i],2)])

fig=plt.figure()
ax=fig.add_subplot(111)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.table(cellText=CKParr,loc='center',colLabels=('Field','AGN with CKP','Total AGN','AGN with CKP (%)','CKP, all gal. (%)'))
plt.savefig('/home/rumbaugh/CKP_table.5.31.16.png')

plt.clf()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.table(cellText=CKPgrouparr,loc='center',colLabels=('Group','AGN with CKP','Total AGN','AGN with CKP (%)','CKP, all gal. (%)'))
plt.savefig('/home/rumbaugh/CKP_groups_table.5.31.16.png')

plt.clf()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.table(cellText=CKP_GPF_arr,loc='center',colLabels=('Group','AGN with CKP','Total AGN','AGN with CKP (%)','CKP, all gal. (%)'))
plt.savefig('/home/rumbaugh/CKP_groups+field_table.5.31.16.png')

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(np.log10(crl['lum_full'][((crl['field']=='cl0023')|(crl['field']=='cl1604'))]),range=(42,44.5),bins=5,color='r',label='Cl0023 & Cl1604')
plt.hist(np.log10(crl['lum_full'][((crl['field']!='cl0023')&(crl['field']!='cl1604'))]),range=(42,44.5),bins=5,color='b',alpha=0.3,label='Other AGN')
plt.xlabel('X-ray Luminosity')
plt.ylabel('Number of Sources')
plt.legend()
plt.savefig('/home/rumbaugh/Chandra/plots/lum_hist.cl0023+cl1604_comp_other.5.31.16.png')

print ' '
a,b=KStest(np.log10(crl['lum_full'][AGN_CKP_arr==1]),np.log10(crl['lum_full']))
print a,b
a,b=KStest(np.log10(crl['lum_full'][((crl['field']=='cl0023')|(crl['field']=='cl1604'))]),np.log10(crl['lum_full']))
print a,b
a,b=KStest(np.log10(crl['lum_full'][((crl['field']=='cl0023')|(crl['field']=='cl1604'))]),np.log10(crl['lum_full'][((crl['field']!='cl0023')&(crl['field']!='cl1604'))]))
print a,b
