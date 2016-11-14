import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
import numpy.random as rand
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

crcf=np.loadtxt('/home/rumbaugh/Chandra/X-ray_completeness.MC_sim_true.z_clus.7.10.16.dat',dtype={'names':('field','42-42.5','42.5-43','43-43.5','43.5-44','44-44.5'),'formats':('|S24','f8','f8','f8','f8','f8')})
crfcf=np.loadtxt('/home/rumbaugh/Chandra/X-ray_completeness.MC_sim_true.z_range.7.10.16.dat',dtype={'names':('field','z_range','42-42.5','42.5-43','43-43.5','43.5-44','44-44.5'),'formats':('|S24','|S24','f8','f8','f8','f8','f8')})

lxA,lxB,lxC,lxD=np.log10(crl0['lum_full'][(((crl0['field']=='cl1350')|(crl0['field']=='rxj1221')|(crl0['field']=='rxj1757')|(crl0['field']=='rxj1821')|(crl0['field']=='rcs0224')))]),np.log10(crl0['lum_full'][(((crl0['field']=='cl1324')|(crl0['field']=='cl1324_north')|(crl0['field']=='cl1324_south')|(crl0['field']=='rxj1716')))]),np.log10(crl0['lum_full'][(((crl0['field']=='cl0023')|(crl0['field']=='cl1604')))]),np.log10(crl0['lum_full'][(((crl0['field']=='rxj1053')|(crl0['field']=='cl0849')|(crl0['field']=='rxj0910')))])

fig=plt.figure()
wA,wB,wC,wD=1/crcf['42.5-43'][crcf['field']=='Passive']*np.ones(len(lxA)),1/crcf['42.5-43'][crcf['field']=='Intermediate']*np.ones(len(lxB)),1/crcf['42.5-43'][crcf['field']=='Cl0023+Cl1604']*np.ones(len(lxC)),1/crcf['42.5-43'][crcf['field']=='High-z']*np.ones(len(lxD))
wxA,wxB,wxC,wxD=np.array([wA,np.ones(len(wA))]),np.array([wB,np.ones(len(wB))]),np.array([wC,np.ones(len(wC))]),np.array([wD,np.ones(len(wD))])
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist((lxA,lxB,lxC,lxD),range=(42.5,43),bins=1,color=('r','green','blue','purple'),alpha=0.3,weights=(wA,wB,wC,wD))
plt.hist((lxA,lxB,lxC,lxD),range=(42.5,44.5),bins=4,color=('r','green','blue','purple'),label=('Passive','Intermediate','SG0023 & SC1604','High-z'))
plt.xlabel('X-ray Luminosity')
plt.ylabel('Number of Sources')
plt.legend()
plt.savefig('/home/rumbaugh/Chandra/plots/lum_hist.group_comps.6.15.16.png')

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

lA,lB,lC,lD=np.log10(crl['lum_full'][((gfAGN_arr==True))]),np.log10(crl['lum_full'][((gfAGN_arr==True)&(crl['redshift']<0.8))]),np.log10(crl['lum_full'][((gfAGN_arr==True)&(crl['redshift']>=0.8)&(crl['redshift']<=0.96))]),np.log10(crl['lum_full'][((gfAGN_arr==True)&(crl['redshift']>0.96))])
wA,wB,wC,wD=1/crfcf['42.5-43'][((crfcf['field']=='Combined')&(crfcf['z_range']=='All'))]*np.ones(len(lA)),1/crfcf['42.5-43'][((crfcf['field']=='Combined')&(crfcf['z_range']=='z<0.8'))]*np.ones(len(lB)),1/crfcf['42.5-43'][((crfcf['field']=='Combined')&(crfcf['z_range']=='0.8<z<0.96'))]*np.ones(len(lC)),1/crfcf['42.5-43'][((crfcf['field']=='Combined')&(crfcf['z_range']=='z>0.96'))]*np.ones(len(lD))
wA2,wB2,wC2,wD2=1/crfcf['43-43.5'][((crfcf['field']=='Combined')&(crfcf['z_range']=='All'))]*np.ones(len(lA)),1/crfcf['43-43.5'][((crfcf['field']=='Combined')&(crfcf['z_range']=='z<0.8'))]*np.ones(len(lB)),1/crfcf['43-43.5'][((crfcf['field']=='Combined')&(crfcf['z_range']=='0.8<z<0.96'))]*np.ones(len(lC)),1/crfcf['43-43.5'][((crfcf['field']=='Combined')&(crfcf['z_range']=='z>0.96'))]*np.ones(len(lD))

plt.hist((lA,lB,lC,lD),range=(42.5,43),bins=1,color=('r','green','blue','purple'),alpha=0.3,weights=(wA,wB,wC,wD))
plt.hist((lA,lB,lC,lD),range=(43,43.5),bins=1,color=('r','green','blue','purple'),alpha=0.3,weights=(wA2,wB2,wC2,wD2))
plt.hist((lA,lB,lC,lD),range=(42.5,44.5),bins=4,color=('r','green','blue','purple'),label=('All','z<0.8','0.8<z<0.96','z>0.96'))
plt.xlabel('X-ray Luminosity')
plt.ylabel('Number of Sources')
plt.legend()
plt.savefig('/home/rumbaugh/Chandra/plots/lum_hist.field_comp.6.15.16.png')

groupnames=['Passive','Intermediate','Cl0023 & Cl1604','High-z']
fieldnames=['All','z<0.8','0.8<z<0.96','z>0.96']

for ig,group,lg in zip(np.arange(0,4),groupnames,[lxA,lxB,lxC,lxD]):
    for field,ifld,lf in zip(fieldnames,np.arange(0,4),[lA,lB,lC,lD]):
        print '%s - %s: '%(group,field),KStest(lg,lf)

ls=[lxA,lxB,lxC,lxD,lA,lB,lC,lD]
ws=[wxA,wxB,wxC,wxD,np.array([wA,wA2]),np.array([wB,wB2]),np.array([wC,wC2]),np.array([wD,wD2])]

def MC_KStest(arr1,arr2,w1,w2,ntrials=100):
    KS_probs=np.zeros(ntrials)
    nnew=np.zeros((2,ntrials,2))
    arrs=[arr1,arr2]
    wstmp=[w1,w2]
    for i in range(0,2):
        nnew[i,:,0]=rand.rand(ntrials)
        nnew[i,:,0][nnew[i,:,0]<wstmp[i][0][0]%1]=np.ceil((wstmp[i][0][0]-1)*len(arrs[i][((arrs[i]>42.5)&(arrs[i]<43))]))
        nnew[i,:,0][nnew[i,:,0]<1]=np.int((wstmp[i][0][0]-1)*len(arrs[i][((arrs[i]>42.5)&(arrs[i]<43))]))
        if np.median(wstmp[i][1][0])>1:
            nnew[i,:,1]=rand.rand(ntrials)
            nnew[i,:,1][nnew[i,:,0]<wstmp[i][1][0]%1]=np.ceil((wstmp[i][1][0]-1)*len(arrs[i][((arrs[i]>42.5)&(arrs[i]<43))]))
            nnew[i,:,1][nnew[i,:,0]<1]=np.int((wstmp[i][1][0]-1)*len(arrs[i][((arrs[i]>42.5)&(arrs[i]<43))]))
    for i in range(0,ntrials):
        ex1a,ex2a=rand.rand(nnew[0][i][0])*0.5+42.5,rand.rand(nnew[1][i][0])*0.5+42.5
        arr1tmp,arr2tmp=np.append(np.copy(arr1),ex1a),np.append(np.copy(arr2),ex2a)
        if np.median(wstmp[0][1])>1:
            ex1b=rand.rand(nnew[0][i][1])*0.5+42.5
            arr1tmp=np.append(arr1tmp,ex1b)
        if np.median(wstmp[1][1])>1:
            ex2b=rand.rand(nnew[1][i][1])*0.5+42.5
            arr2tmp=np.append(arr2tmp,ex2b)
        KStmp=KStest(arr1tmp,arr2tmp)
        KS_probs[i]=KStmp[1]
    return KS_probs
import time
st=time.time()
print 'Starting MC Sims...'
MCprobs=np.ones((len(ls),len(ls)))
for l1,il1 in zip(ls,np.arange(len(ls))):
    for l2,il2 in zip(ls,np.arange(len(ls))):
        if il1!=il2:
            KSprobs=MC_KStest(l1,l2,ws[il1],ws[il2],ntrials=10000)
            MCprobs[il1][il2]=round(np.median(KSprobs),4)
    ttmp=time.time()
    print '%i%% Done. %.1fs elapsed. ETA: %.1fs'%(int(100*(il1+1.)/len(ls)),ttmp-st,(len(ls)-il1-1.)*(ttmp-st)/(il1+1))
arrt=np.array(['Passive','Intermediate','Cl0023&Cl1604','High-z','Field(all)','z<0.8','0.8<z<0.96','z>0.96'])
out=np.concatenate((arrt.reshape((len(arrt),1)),MCprobs),axis=1)
np.savetxt('/home/rumbaugh/Chandra/MC_KS_probs.7.12.16.dat',out,fmt='%13s',header='                   Passive        Inter.   Cl0023&Cl1604     High-z        Field(all)     z<0.8      0.8<z<0.96      z>0.96')
