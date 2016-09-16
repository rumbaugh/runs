import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/SphDist.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/KStest.py')
execfile('/home/rumbaugh/set_spec_dict.py')
date='4.17.16'


group_dict={'Passive':['rcs0224','rxj1221','cl1350','rxj1757','rxj1821'],'Intermediate':['cl1324','cl1324_north','cl1324_south','rxj1716'],'Cl0023+Cl1604':['cl0023','cl1604'],'High-z':['cl0849','rxj1053','rxj0910']}
groups=group_dict.keys()

truetargets=["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324","rxj1821","rxj1716","rxj1053","cl1604"]

PS_out_dict={}
for t in np.append(groups,truetargets):
    PS_out_dict[t]={'clusdist_all':np.zeros(0),'veldist_all':np.zeros(0),'PS_all':np.zeros(0),'num_all':0,'clusdist_AGN':np.zeros(0),'veldist_AGN':np.zeros(0),'PS_AGN':np.zeros(0),'num_AGN':0}


rbounds=(-0.5,10)
nbins=(rbounds[1]-rbounds[0])*2

crRS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets.AGN.3.9.16.dat',dtype={'names':('field','number','RA','Dec','RSoffset','magR','magI','magZ','SCmagRed','SCmagBlue'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8')})
crRS_ACS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets.cl1604_ACS.3.6.16.dat',dtype={'names':('field','number','RA','Dec','RSoffset','F606W','F814W'),'formats':('|S24','i8','f8','f8','f8','f8','f8')})


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
sig=np.concatenate((crx['sigS'].reshape((len(crx['sigS']),1)),crx['sigH'].reshape((len(crx['sigH']),1)),crx['sigF'].reshape((len(crx['sigF']),1))),axis=1)
sig=np.max(sig,axis=1)

gsig=np.where(sig>2)[0]

linfile='/home/rumbaugh/X-ray_lum_cat.4.17.16.dat'

lindict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8','f8','f8','f8')}

crl=np.loadtxt(linfile,dtype=lindict)

cosmocalc(zs,outfile='/home/rumbaugh/cc_out_clus.2.9.16.dat',ids=cfields)

crcc=np.loadtxt('/home/rumbaugh/cc_out_clus.2.9.16.dat',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
kpc = crcc[:,12]
Hz = crcc[:,16]*70.
Mpc = kpc/1000.

legposdict={"rcs0224":'upper left',"cl0849":'upper left',"rxj0910":'lower right',"rxj1221":'upper left',"cl1350":'lower right',"rxj1757":'upper right',"cl0023":'upper right',"cl1324_north":'upper left',"cl1324_south":'upper left',"rxj1821":'upper left',"cl1137":'lower left',"rxj1716":'lower left',"rxj1053":'lower center',"cl1604":'upper left'}

clusdist=np.ones(len(crx['RA'][gsig]))*-1
veldist=np.ones(len(crx['RA'][gsig]))*-1
PSdist=np.ones(len(crx['RA'][gsig]))*-1

gAGN=np.zeros(len(crRS['RA']-2),dtype='i8')
gnot1604=np.where(crRS['field']!='cl1604')[0]
RSO=np.zeros(len(gAGN))
for i in range(0,len(crRS['RA'][gnot1604])):
    tmpdist=np.sqrt((crRS['RA'][gnot1604][i]-crx['RA'][gsig])**2+(crRS['Dec'][gnot1604][i]-crx['Dec'][gsig])**2)
    gAGN[i]=np.argsort(tmpdist)[0]
    if tmpdist[gAGN[i]]>1./3600: print 'Too big! %f'%(tmpdist[gAGN[i]]*3600)
    RSO[i]=-crRS['RSoffset'][gnot1604][i]
for i in range(0,len(crRS_ACS['RA'])):
    tmpdist=np.sqrt((crRS_ACS['RA'][i]-crx['RA'][gsig])**2+(crRS_ACS['Dec'][i]-crx['Dec'][gsig])**2)
    gAGN[i+len(gnot1604)]=np.argsort(tmpdist)[0]
    if tmpdist[gAGN[i+len(gnot1604)]]>1./3600: print 'Too big! %f'%(tmpdist[gAGN[i+len(gnot1604)]]*3600)
    RSO[i+len(gnot1604)]=-crRS_ACS['RSoffset'][i]

crd=np.loadtxt('/home/rumbaugh/Chandra/clustocentric_dists.dat',usecols=(1,2,3,4,5,6))
crdf=np.loadtxt('/home/rumbaugh/Chandra/clustocentric_dists.dat',usecols=(0,),dtype='|S24')

ccd=crd[:,3]
vd=crd[:,4]
psd=crd[:,5]

for target in truetargets:
    if target=='cl1324':
        gcrd=np.where((crdf=='cl1324_north')|(crdf=='cl1324_south')|(crdf=='cl1324'))[0]
    else:
        gcrd=np.where(crdf==target)[0]
    PS_out_dict[target]['clusdist_AGN'],PS_out_dict[target]['veldist_AGN']=ccd[gcrd],vd[gcrd]
    PS_out_dict[target]['PS_AGN'],PS_out_dict[target]['num_AGN']=psd[gcrd],len(gcrd)
    for group in groups:
        if target in group_dict[group]: 
            PS_out_dict[group]['clusdist_AGN'],PS_out_dict[group]['veldist_AGN']=np.append(ccd[gcrd],PS_out_dict[group]['clusdist_AGN']),np.append(vd[gcrd],PS_out_dict[group]['veldist_AGN'])
            PS_out_dict[group]['PS_AGN'],PS_out_dict[group]['num_AGN']=np.append(psd[gcrd],PS_out_dict[group]['PS_AGN']),PS_out_dict[group]['num_AGN']+len(gcrd)

fig=plt.figure(2)
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])
allclusdist=np.zeros(0)
allveldist=np.zeros(0)
allPSdist=np.zeros(0)


coeff=[0.1,0.4,2]
for field in targets: 
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    g=np.where(((cfields==field)|(cfields==field[:6].lower())))[0]
    gq=np.where((crs['Q']>2.5)&(crs['z']>spec_dict[field]['z'][1])&(crs['z']<spec_dict[field]['z'][2]))[0]
    tmpallclusdist=np.ones(len(gq))*-1
    tmpallveldist=np.ones(len(gq))*-1
    tmpallPSdist=np.ones(len(gq))*-1
    for i in range(0,len(gq)):
        zx=crs['z'][gq[i]]
        tmpzdist=np.abs(((1+zx)**2-(1+zs[g])**2)/((1+zx)**2+(1+zs[g])**2))*3.*10.**5/clus_sig[g]
        r200 = 2*clus_sig[g]/(np.sqrt(200)*Hz[g])
        tmpdistnoz=60*SphDist(crs['ra'][gq[i]],crs['dec'][gq[i]],ras[g],decs[g])*Mpc[g]/r200
        tmpPSdist=tmpzdist*tmpdistnoz
        gPS=np.argsort(tmpPSdist)[0]
        tmpallclusdist[i],tmpallveldist[i],tmpallPSdist[i]=tmpdistnoz[gPS],tmpzdist[gPS],tmpPSdist[gPS]
    allclusdist=np.append(allclusdist,tmpallclusdist)
    allveldist=np.append(allveldist,tmpallveldist)
    allPSdist=np.append(allPSdist,tmpallPSdist)
    if field[:6]=='cl1324':
        PS_out_dict['cl1324']['PS_all']=np.append(PS_out_dict['cl1324']['PS_all'],tmpallPSdist)
        PS_out_dict['cl1324']['clusdist_all']=np.append(PS_out_dict['cl1324']['clusdist_all'],tmpallclusdist)
        PS_out_dict['cl1324']['veldist_all']=np.append(PS_out_dict['cl1324']['veldist_all'],tmpallveldist)
        PS_out_dict['cl1324']['num_all']+=len(tmpallPSdist)
    elif field!='cl1137':
        PS_out_dict[field]['PS_all'],PS_out_dict[field]['num_all']=tmpallPSdist,len(tmpallPSdist)
        PS_out_dict[field]['clusdist_all'],PS_out_dict[field]['veldist_all']=tmpallclusdist,tmpallveldist
    for group in groups:
        if field in group_dict[group]: 
            PS_out_dict[group]['clusdist_all'],PS_out_dict[group]['veldist_all']=np.append(tmpallclusdist,PS_out_dict[group]['clusdist_all']),np.append(tmpallveldist,PS_out_dict[group]['veldist_all'])
            PS_out_dict[group]['PS_all'],PS_out_dict[group]['num_all']=np.append(tmpallPSdist,PS_out_dict[group]['PS_all']),PS_out_dict[group]['num_all']+len(tmpallPSdist)
            
    g1,g2,g3,g4=np.where(tmpallPSdist<coeff[0])[0],np.where((tmpallPSdist>coeff[0])&(tmpallPSdist<coeff[1]))[0],np.where((tmpallPSdist>coeff[1])&(tmpallPSdist<coeff[2]))[0],np.where(tmpallPSdist>coeff[2])[0]
    r200 = 2*clus_sig/(np.sqrt(200)*Hz)
    r500 = 2*clus_sig/(np.sqrt(500)*Hz)

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for t in PS_out_dict.keys():
    plt.scatter([np.median(PS_out_dict[t]['clusdist_AGN'])],[np.median(PS_out_dict[t]['veldist_AGN'])],color='r',s=16)
    plt.text(np.median(PS_out_dict[t]['clusdist_AGN']),np.median(PS_out_dict[t]['veldist_AGN']),t,color='b')
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$R/R_{200}$',size=15)
plt.ylabel(r'$\left|\Delta v\right|/\sigma_v$',size=15)
dumx=np.linspace(0.01,100,10000)
#for coeff in [0.1,0.4,1,2,5,7.5,10,15,20]:
carr=['cyan','orange','green']
for coeff,c in zip([0.1,0.4,2],carr):
    dumy=coeff*1./dumx
    plt.loglog(dumx,dumy,label=r'$p=$%.1f'%coeff,color=c,lw=2)
plt.xlim(0.01,30)
lowb=0.01
highb=20
plt.ylim(lowb*0.95,highb*1.05)
plt.legend(loc='upper left')
#plt.savefig('/home/rumbaugh/Chandra/plots/phase_space_med.AGN.%s.png'%(date))

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for t in PS_out_dict.keys():
    plt.scatter([np.median(PS_out_dict[t]['clusdist_all'])],[np.median(PS_out_dict[t]['veldist_all'])],color='r',s=16)
    plt.text(np.median(PS_out_dict[t]['clusdist_all']),np.median(PS_out_dict[t]['veldist_all']),t,color='b')
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$R/R_{200}$',size=15)
plt.ylabel(r'$\left|\Delta v\right|/\sigma_v$',size=15)
dumx=np.linspace(0.01,100,10000)
#for coeff in [0.1,0.4,1,2,5,7.5,10,15,20]:
carr=['cyan','orange','green']
for coeff,c in zip([0.1,0.4,2],carr):
    dumy=coeff*1./dumx
    plt.loglog(dumx,dumy,label=r'$p=$%.1f'%coeff,color=c,lw=2)
plt.xlim(0.01,30)
lowb=0.01
highb=20
plt.ylim(lowb*0.95,highb*1.05)
plt.legend(loc='upper left')
#plt.savefig('/home/rumbaugh/Chandra/plots/phase_space_med.all.%s.png'%(date))

textarr=np.zeros((len(PS_out_dict.keys()),3),dtype='object')

for t,it in zip(groups,np.arange(0,len(groups))):
    textarr[it]=[t,np.median(PS_out_dict[t]['PS_AGN']),np.median(PS_out_dict[t]['PS_all'])]
for t,it in zip(truetargets,np.arange(0,len(truetargets))):
    textarr[it+4]=[t,np.median(PS_out_dict[t]['PS_AGN']),np.median(PS_out_dict[t]['PS_all'])]


fig=plt.figure()
ax=fig.add_subplot(111)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.table(cellText=textarr,loc='center',colLabels=('Field/Group','Median PS Metric (AGN)','Median PS Metric (all)'))
plt.savefig('/home/rumbaugh/PS_table.6.1.16.png')
