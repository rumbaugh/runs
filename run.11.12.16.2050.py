import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/SphDist.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/KStest.py')
execfile('/home/rumbaugh/set_spec_dict.py')
date='11.12.16'

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


infile='/home/rumbaugh/combined_match_catalog.6.21.16.dat'

indict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','ID','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','|S32','f8','f8','f8','f8','f8','f8')}

crx=np.loadtxt(infile,dtype=indict)
sig=np.concatenate((crx['sigS'].reshape((len(crx['sigS']),1)),crx['sigH'].reshape((len(crx['sigH']),1)),crx['sigF'].reshape((len(crx['sigF']),1))),axis=1)
sig=np.max(sig,axis=1)

gsig=np.where(sig>2)[0]

linfile='/home/rumbaugh/X-ray_lum_cat.6.21.16.dat'

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
FILE=open('/home/rumbaugh/Chandra/clustocentric_dists.dat','w')
FILE.write('# field number RA Dec clusdist veldist PhaseSpaceDist\n')
for i in range(0,len(crx['RA'][gsig])):
    gnoz=np.where(((cfields==crx['field'][gsig][i].lower())|(cfields==crx['field'][gsig][i][:6].lower())))[0]
    zx=crx['redshift'][gsig][i]
    tmpzdist=np.abs(((1+zx)**2-(1+zs[gnoz])**2)/((1+zx)**2+(1+zs[gnoz])**2))*3.*10.**5/clus_sig[gnoz]
    tmpdistnoz=60*SphDist(crx['RA'][gsig][i],crx['Dec'][gsig][i],ras[gnoz],decs[gnoz])
    tmpr200 = 2*clus_sig[gnoz]/(np.sqrt(200)*Hz[gnoz])
    tmpclusdistnoz=tmpdistnoz*Mpc[gnoz]/tmpr200
    tmpPSdist=tmpzdist*tmpclusdistnoz
    gPS=np.argsort(tmpPSdist)[0]
    clusdist[i],veldist[i],PSdist[i]=tmpclusdistnoz[gPS],tmpzdist[gPS],tmpPSdist[gPS]
    FILE.write('%12s %2i %9.5f %9.5f %f %f %f\n'%(crx['field'][gsig][i],crx['number'][gsig][i],crx['RA'][gsig][i],crx['Dec'][gsig][i],clusdist[i],veldist[i],PSdist[i]))
FILE.close()

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

fig=plt.figure(2)
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","rxj1716","rxj1053","cl1604"])
allclusdist=np.zeros(0)
allveldist=np.zeros(0)
allPSdist=np.zeros(0)
allPS2dist=np.zeros(0)

coeff=[0.1,0.4,2]
tc=(0,)
for itc in range(1,len(specloaddict['names'])): tc=tc+(itc,)
for field in targets: 
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict,usecols=tc)
    g=np.where(((cfields==field)|(cfields==field[:6].lower())))[0]
    print field,len(g)
    gq=np.where((crs['Q']>2.5)&(crs['z']>spec_dict[field]['z'][1])&(crs['z']<spec_dict[field]['z'][2]))[0]
    tmpallclusdist=np.ones(len(gq))*-1
    tmpallveldist=np.ones(len(gq))*-1
    tmpallPSdist=np.ones(len(gq))*-1
    tmpallPS2dist=np.ones(len(gq))*-1
    nearclus=np.ones(len(gq),dtype='i8')*-1
    for i in range(0,len(gq)):
        zx=crs['z'][gq[i]]
        tmpzdist=np.abs(((1+zx)**2-(1+zs[g])**2)/((1+zx)**2+(1+zs[g])**2))*3.*10.**5/clus_sig[g]
        r200 = 2*clus_sig[g]/(np.sqrt(200)*Hz[g])
        tmpdistnoz=60*SphDist(crs['ra'][gq[i]],crs['dec'][gq[i]],ras[g],decs[g])*Mpc[g]/r200
        tmpPSdist=tmpzdist*tmpdistnoz
        gPS=np.argsort(tmpPSdist)[0]
        tmpallclusdist[i],tmpallveldist[i],tmpallPSdist[i]=tmpdistnoz[gPS],tmpzdist[gPS],tmpPSdist[gPS]
        nearclus[i]=gPS
        if len(g)>1: 
            tmpallPS2dist[i]=tmpPSdist[np.argsort(tmpPSdist)[1]]
    allclusdist=np.append(allclusdist,tmpallclusdist)
    allveldist=np.append(allveldist,tmpallveldist)
    allPSdist=np.append(allPSdist,tmpallPSdist)
    allPS2dist=np.append(allPS2dist,tmpallPS2dist)
    g1,g2,g3,g4=np.where(tmpallPSdist<coeff[0])[0],np.where((tmpallPSdist>coeff[0])&(tmpallPSdist<coeff[1]))[0],np.where((tmpallPSdist>coeff[1])&(tmpallPSdist<coeff[2]))[0],np.where(tmpallPSdist>coeff[2])[0]
    r200 = 2*clus_sig/(np.sqrt(200)*Hz)
    r500 = 2*clus_sig/(np.sqrt(500)*Hz)
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    #tmpallclusdist[tmpIRflag==0]=-0.24
    for ia in range(0,len(gq)): plt.arrow(crs['ra'][gq[ia]],crs['dec'][gq[ia]],ras[g][nearclus[ia]]-crs['ra'][gq[ia]],decs[g][nearclus[ia]]-crs['dec'][gq[ia]],color='r',lw=0.4,width=0.000005,head_length=0.00001)
    ax.scatter(crs['ra'][gq[g1]],crs['dec'][gq[g1]],color='magenta',label='PS<0.1')
    ax.scatter(crs['ra'][gq[g2]],crs['dec'][gq[g2]],color='orange',label='0.1<PS<0.4')
    ax.scatter(crs['ra'][gq[g3]],crs['dec'][gq[g3]],color='green',label='0.4<PS<2')
    ax.scatter(crs['ra'][gq[g4]],crs['dec'][gq[g4]],color='blue',label='PS>2')
    ax.scatter(crd[:,1][crdf==field],crd[:,2][crdf==field],marker='s',facecolors='none',edgecolors='red')
    phidummy=np.linspace(0,2*np.pi,1000)
    xdummy,ydummy=np.cos(phidummy),np.sin(phidummy)
    for ic in g:
        xcen,ycen=ras[ic],decs[ic]
        ax.scatter(np.array([xcen]),np.array([ycen]),marker='x',s=48,color='k')
        ax.plot(xdummy*0.5/Mpc[ic]/3600.+xcen,ydummy*0.5/Mpc[ic]/3600.+ycen,lw=2,ls='--',color='k')
        ax.plot(xdummy*r200[ic]/Mpc[ic]/3600.+xcen,ydummy*r200[ic]/Mpc[ic]/3600.+ycen,lw=2,ls='dotted',color='k')
        ax.plot(xdummy*r500[ic]/Mpc[ic]/3600.+xcen,ydummy*r500[ic]/Mpc[ic]/3600.+ycen,lw=2,ls='dotted',color='k')
        plt.text(xcen+10./3600,ycen+10./3600/np.cos(xcen*np.pi/180.),'%s, z=%.3f'%(cr['cluster'][ic],zs[ic]),color='teal')
    ax.set_xlabel('RA')
    ax.set_ylabel('Dec')
    ax.set_title('%s'%field)
    plt.legend(loc=legposdict[field])
    xlim=plt.xlim()
    ylim=plt.ylim()
    ax.set_ylim(ylim[1],ylim[0])
    #ax.set_ylim(0,10)
    #ax.set_xlim(-0.5,10)
    #fig.savefig(psfpdf,format='pdf')
#psfpdf.close()


plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(allclusdist,allveldist,color='k',s=1)
plt.scatter(ccd,veldist,color='r',s=16)
plt.xlabel('Clustocentric Distance (R/R_200)')
plt.ylabel('Velocity Distance del V/vel_disp')
plt.title('Phase Space Diagram')
dumx=np.linspace(0.01,100,10000)
#for coeff in [0.1,0.4,1,2,5,7.5,10,15,20]:
carr=['cyan','orange','green']
lwarr=['solid','dashed','dotted']
for coeff,c,clw in zip([0.1,0.4,2],carr,lwarr):
    dumy=coeff*1./dumx
    plt.plot(dumx,dumy,label='%.1f'%coeff,color=c,lw=2,ls=clw)
#for xval in [0.5,1,1.5]:
#    plt.axvline(xval,color='b',lw=2,ls='--')
plt.ylim(-0,10)
plt.xlim(-0,10)
plt.legend()
plt.savefig('/home/rumbaugh/Chandra/plots/phase_space_diagram.%s.png'%(date))

plt.figure(2)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
print KStest(ccd*veldist,allclusdist*allveldist)
PS_AGN,PS_all=ccd*veldist,allclusdist*allveldist
PS_AGN[PS_AGN<=10**-1.75]=1.001*10**-1.75
PS_AGN[PS_AGN>=100]=99.9
PS_all[PS_all<=10**-1.75]=1.001*10**-1.75
PS_all[PS_all>=100]=99.9

newPSdist=np.copy(allPS2dist)
newPSdist[newPSdist<0]=allPSdist[newPSdist<0]
newPSdist[newPSdist<=10**-1.75]=1.001*10**-1.75
newPSdist[newPSdist>=100]=99.9

a=plt.hist(np.log10(PS_all),color='r',bins=[-1.75,-1,np.log10(0.4),np.log10(2),2],weights=np.ones(len(PS_all))*1./len(PS_all))
b=plt.hist(np.log10(newPSdist),color='b',bins=[-1.75,-1,np.log10(0.4),np.log10(2),2],weights=np.ones(len(newPSdist))*1./len(newPSdist),edgecolor='k',facecolor='None',lw=4)#weights=25*np.ones(len(allclusdist))*1./len(allclusdist),)
#plt.scatter(ccd,veldist,color='r',s=16)
#for coeff in [0.1,0.4,2]:
#    plt.axvline(np.log10(coeff),lw=2,ls='--',color='k')
plt.xlabel(r'log$[(R/R_{200}) \times (\left|\Delta v\right|/\sigma_v)]$',size=15)
plt.ylabel('Fraction of Sources')
plt.title('Phase Space Histogram')
#plt.ylim(-0,20)
plt.xlim(-1.75,1)
#plt.savefig('/home/rumbaugh/Chandra/plots/phase_space_hist.2nd_p.%s.png'%(date))

KStest(ccd*veldist,allclusdist*allveldist)

plt.figure(2)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(np.log10(PS_AGN),color='r',bins=[-1.75,-1,np.log10(0.4),np.log10(2),2],weights=np.ones(len(PS_AGN))*1./len(PS_AGN))
plt.hist(np.log10(PS_all),color='b',bins=[-1.75,-1,np.log10(0.4),np.log10(2),2],weights=np.ones(len(PS_all))*1./len(PS_all),edgecolor='k',facecolor='None',lw=4)#weights=25*np.ones(len(allclusdist))*1./len(allclusdist),)
#plt.scatter(ccd,veldist,color='r',s=16)
#for coeff in [0.1,0.4,2]:
#    plt.axvline(np.log10(coeff),lw=2,ls='--',color='k')
plt.xlabel(r'log$[(R/R_{200}) \times (\left|\Delta v\right|/\sigma_v)]$',size=15)
plt.ylabel('Fraction of Sources')
plt.title('Phase Space Histogram')
#plt.ylim(-0,20)
plt.xlim(-1.75,1)
#plt.savefig('/home/rumbaugh/Chandra/plots/phase_space_hist.%s.png'%(date))

highb=20
veldist[veldist>highb]=highb
allveldist[allveldist>highb]=highb

#veldist[veldist<0.001]=0.001
#allveldist[allveldist<0]=0.0001
lowb=0.01
veldist[veldist<lowb]=lowb
allveldist[allveldist<lowb]=lowb

g_points=np.where((veldist>lowb)&(veldist<highb))[0]
g_lowb=np.where((veldist==lowb))[0]
g_highb=np.where((veldist==highb))[0]
g_allpoints=np.where((allveldist>lowb)&(allveldist<highb))[0]
g_alllowb=np.where((allveldist==lowb))[0]
g_allhighb=np.where((allveldist==highb))[0]

plt.figure(4)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(allclusdist[g_allpoints],allveldist[g_allpoints],color='k',s=1)
plt.scatter(ccd[g_points],veldist[g_points],color='r',s=16)
plt.scatter(allclusdist[g_alllowb],allveldist[g_alllowb]*30./29,color='k',s=18,marker=matplotlib.markers.CARETDOWN,facecolor="None")
plt.scatter(ccd[g_lowb],veldist[g_lowb]*30./29,color='r',s=48,marker='v')
plt.scatter(allclusdist[g_allhighb],allveldist[g_allhighb],color='k',s=18,marker=matplotlib.markers.CARETUP,facecolor="None")
plt.scatter(ccd[g_highb],veldist[g_highb],color='r',s=48,marker='^')
plt.xlabel(r'$R/R_{200}$',size=15)
plt.ylabel(r'$\left|\Delta v\right|/\sigma_v$',size=15)
plt.title('Phase Space Diagram')
dumx=np.linspace(0.01,100,10000)
#for coeff in [0.1,0.4,1,2,5,7.5,10,15,20]:
carr=['cyan','orange','green']
lsarr=['solid','dashed','dotted']
for coeff,c,cls in zip([0.1,0.4,2],carr,lsarr):
    dumy=coeff*1./dumx
    plt.loglog(dumx,dumy,label=r'$p=$%.1f'%coeff,color=c,lw=2,ls=cls)
#for xval in [0.5,1,1.5]:
#    plt.axvline(xval,color='b',lw=2,ls='--')
plt.xlim(0.01,30)
plt.ylim(lowb*0.95,highb*1.05)
#xlim=plt.xlim()
#ylim=plt.ylim()
#xdummy=np.linspace(xlim[0],xlim[1],1000)
#plt.plot(xdummy,xdummy,lw=1,ls='--',color='k')
#plt.xlim(xlim)
#plt.ylim(ylim)
plt.legend(loc=3)
plt.savefig('/home/rumbaugh/Chandra/plots/phase_space_diagram_logplot.%s.png'%(date))



plt.figure(5)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(allPSdist[g_allpoints],allPS2dist[g_allpoints],color='k',s=1)
plt.scatter(allPSdist[g_alllowb]*30./29,allPS2dist[g_alllowb],color='k',s=18,marker=matplotlib.markers.CARETDOWN,facecolor="None")
plt.xlabel(r'$p$ (lowest)',size=15)
plt.ylabel(r'$p$ (second lowest)',size=15)
plt.title('Phase Space Diagram, Choice Comparison')
dumx=np.linspace(0.01,100,10000)
#for coeff in [0.1,0.4,1,2,5,7.5,10,15,20]:
carr=['cyan','orange','green']
#for xval in [0.5,1,1.5]:
#    plt.axvline(xval,color='b',lw=2,ls='--')
plt.loglog([1,2],[999999,999999])
plt.xlim(0.01,200)
plt.ylim(0.01,200)
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(xlim[0],xlim[1],1000)
plt.plot(xdummy,xdummy,lw=1,ls='--',color='r')
carr=['cyan','orange','green']
for coeff,ccur in zip([0.1,0.4,2],carr):
    plt.axvline(coeff,lw=2,color=ccur,ls='dashed')
    plt.axhline(coeff,lw=2,color=ccur,ls='dashed')
plt.xlim(xlim)
plt.ylim(ylim)
#plt.savefig('/home/rumbaugh/Chandra/plots/phase_space_diagram_choicecomp.%s.png'%(date))

percdif=(allPS2dist-allPSdist)/allPSdist*100
logdif=np.log10(percdif)

plt.figure(5)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(logdif,range=(0,5),bins=20,weights=np.ones(len(logdif))*1./len(logdif[(logdif>0)&(logdif<5)]))
plt.ylabel('Fraction of sources')
plt.xlabel('log(Percent difference between second and lowest p value)')
#plt.savefig('/home/rumbaugh/Chandra/plots/phase_space_hist_choicecomp.%s.png'%(date))

print len(allPS2dist[allPS2dist<0]),len(allPS2dist)
