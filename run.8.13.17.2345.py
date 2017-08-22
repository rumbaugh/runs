import numpy as np
import matplotlib.pyplot as plt
import scipy.odr as odr


dummypoints=10000

name_dict={'Cluster_A': 'SC1604A','Cluster_B': 'SC1604B','Cluster_D': 'SC1604D','0848+4451': 'Lynx E','Lynx_W':'Lynx W','Cluster_I': 'SC1324I', '1324+3011':'SC1324A','1324+3013':'SC1324B','0910+5419':'SC0910A','0910+5422':'SC0910B'}

crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
fourpiDL2=crcc[:,18]
Ez=crcc[:,16]
cc_z=crcc[:,0]
cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','RA','Dec','z','sig0.5','sig0.5err','n0.5','sig','sigerr','nsig'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

crl=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_lums.dat',dtype={'names':('field','cluster','ls','lh','lf','ls500','lh500','lf500','lbol','lserr','lherr','lferr','ls500err','lh500err','lf500err','lbolerr'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

crf=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_fits.dat',dtype={'names':('cluster','r0','r0-','r0+','blg','bkg-','blg+','r500','r500NC','NC'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

crx=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_Xray.dat',dtype={'names':('field','cluster','ra','dec','z','nh','kt','lb','ub','rsn'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8')})
testclus=np.zeros(np.shape(crx)[0],dtype='|S128')
for i in range(0,len(testclus)): testclus[i]=crx['cluster'][i].lower()

lums=crl['lbol']
lumerrs=crl['lbolerr']
names=crl['cluster']

delinds=np.zeros(0,dtype='i8')
for i in range(np.shape(crl)[0]):
    tmpsum=0
    g=np.where(cr['cluster']==crl['cluster'][i])[0]
    for j in range(2,len(crl[i])):
        tmpsum+=np.isnan(crl[i][j])
    if tmpsum>=1: 
        delinds=np.append(delinds,i)
    elif len(g)==0:
        delinds=np.append(delinds,i)


gdo=np.delete(np.arange(np.shape(crl)[0]),delinds)
temps,tubs,tlbs,Ezs,sigs,sigerrs,r0,r500=np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo))
fields,clusters=np.zeros(len(gdo),dtype='|S24'),np.zeros(len(gdo),dtype='|S24')
for i,i0 in zip(gdo,np.arange(len(gdo))):
    g=np.where(crx['cluster']==crl['cluster'][i])[0][0]
    gf=np.where(crf['cluster']==crl['cluster'][i])[0][0]
    gc=np.where(cr['cluster']==crl['cluster'][i])[0][0]
    gcc=np.argsort(np.abs(cr['z'][gc]-cc_z))[0]
    Ezs[i0]=Ez[gcc]
    temps[i0],tubs[i0],tlbs[i0]=crx['kt'][g],crx['ub'][g],crx['lb'][g]
    sigs[i0],sigerrs[i0]=cr['sig'][gc],cr['sigerr'][gc]
    r0[i0],r500[i0]=np.abs(crf['r0'][gf]),crf['r500'][gf]
    fields[i0],clusters[i0]=crl['field'][i],crl['cluster'][i]
    print crl['cluster'][i],clusters[i0],fields[i0]

def customerr(message):
    try:
        raise ValueError
    except ValueError as err:
        err.message(message)
        raise

def calc_SR_dists(xdummy,ydummy,X,Y,Xerr,Yerr,Xerrlo=None,Yerrlo=None):
    dummypoints=len(xdummy)
    if len(xdummy)!=len(ydummy): customerr('calc_SR_Dists: xdummy and ydummy must have the same length')
    if len(X)!=len(Y): customerr('calc_SR_Dists: X and Y must have the same length')
    if len(Xerr)!=len(Yerr): customerr('calc_SR_Dists: Xerr and Yerr must have the same length')
    if len(X)!=len(Xerr): customerr('calc_SR_Dists: X and Xerr must have the same length')
    xarr=X.reshape((len(X),1))*np.ones(dummypoints)
    yarr=Y.reshape((len(Y),1))*np.ones(dummypoints)
    xdumarr=np.ones(len(X)).reshape((len(X),1))*xdummy.reshape((1,dummypoints))
    ydumarr=np.ones(len(X)).reshape((len(X),1))*ydummy.reshape((1,dummypoints))
    Xerrarr=Xerr.reshape((len(X),1))*np.ones(dummypoints)
    Yerrarr=Yerr.reshape((len(X),1))*np.ones(dummypoints)
    if (Xerrlo==None)&(Yerrlo==None):
        xnorm,ynorm=Xerrarr,Yerrarr
    else:
        xnorm,ynorm=Xerrarr,Yerrarr
        if Xerrlo!=None: 
            Xerrloarr=Xerrlo.reshape((len(X),1))*np.ones(dummypoints)
            xnorm[xarr>xdumarr]=Xerrloarr[xarr>xdumarr]
        if Yerrlo!=None: 
            Yerrloarr=Yerrloz.reshape((len(X),1))*np.ones(dummypoints)
            ynorm[yarr>ydumarr]=Yerrlo[yarr>ydumarr]
    dist=np.sqrt(((xarr-xdumarr)/xnorm)**2+((yarr-ydumarr)/ynorm)**2)
    mindist=np.min(dist,axis=1)
    return mindist

outcr=np.zeros((len(temps),),dtype={'names':('field','cluster','mindistlit_LxT','mindistfit_LxT','mindistlit_sigT','mindistfit_sigT','mindistlit_Lxsig','mindistfit_Lxsig'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8')})

def f_LxT(B,T):
    #Remember, this function is in log-log form, and Lx is divided by E(z)
    return B[0]*T+B[1]
linearLxT=odr.Model(f_LxT)
LxTdata=odr.Data(np.log(temps),np.log(lums[gdo]/Ezs),wd=(0.5*(tubs-tlbs)/temps)**-2,we=(lumerrs[gdo]/lums[gdo])**-2)
odrLxT=odr.ODR(LxTdata,linearLxT,beta0=[2.6,np.log(0.1)])
LxTout=odrLxT.run()

lumsEz=lums[gdo]/Ezs
lumEzerrs=lumerrs[gdo]/Ezs
#terrlo,terrhi=temps-tlbs,tubs-temps
terrlo,terrhi=tlbs,tubs
for i in range(0,len(terrlo)): print fields[i],clusters[i],temps[i],tlbs[i],tubs[i],lums[gdo[i]]/Ezs[i],terrlo[i],terrhi[i]


text_dict={clusters[x]: [temps[x],lumsEz[x],'left','bottom'] for x in np.arange(len(clusters))}

for i in np.arange(len(clusters)): 
    try:
        name_dict[clusters[i]]
    except KeyError:
        name_dict[clusters[i]]=clusters[i]

fig=plt.figure(1,figsize=(8,18),dpi=400)
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.clf()
plt.subplot(3,1,1)
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(temps,lums[gdo]/Ezs,xerr=[terrlo,terrhi],yerr=lumerrs[gdo]/Ezs,color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(temps,lums[gdo]/Ezs,s=32,color='r')
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(np.max([xlim[0],0.7]),xlim[1],dummypoints)
ydummy_lit0=0.112*xdummy**2.53*10**44
ydummy_lit=0.079*xdummy**2.7*10**44
ydummy_lit_4func=0.079*xdummy**2.7
ydummy_lit2=10**44.05*(xdummy/5.)**2.9
ydummy_fit=np.e**LxTout.beta[1]*xdummy**LxTout.beta[0]
plt.loglog(xdummy,ydummy_lit,lw=2,color='cyan',ls='dashed',label='Pratt et al. (2009)')
plt.loglog(xdummy,ydummy_lit2,lw=2,color='purple',ls='-.',label='Andersson et al. (2011)')
plt.loglog(xdummy,ydummy_lit0,lw=2,color='b',label='Reichert et al. (2011)')
plt.loglog(xdummy,ydummy_fit,lw=2,color='magenta',ls='dotted',label='Linear Fit')

offsetfracx,offsetfracy=1.045,1.025
for i in np.arange(len(clusters)): 
    x,y,HA,VA=text_dict[clusters[i]][0]*offsetfracx,text_dict[clusters[i]][1]*offsetfracy,text_dict[clusters[i]][2],text_dict[clusters[i]][3]
    if clusters[i]=='RCS0224B': x,y,VA,HA=4.8,1.35*10**44,'top','right'
    if name_dict[clusters[i]]=='SC0910B': x,y,VA=4,1.22*10**44,'top'
    if clusters[i]=='Cluster_D': x,HA=0.835,'right'
    if clusters[i]=='Cluster_A': x,HA=3.5,'right'
    if clusters[i]=='Cluster_I': x,y,VA,HA=2.8,0.84*10**44,'top','right'
    if name_dict[clusters[i]]=='SC0910A': y,VA=text_dict[clusters[i]][1],'center'
    if name_dict[clusters[i]]=='SC1324A': x*=offsetfracx
    if name_dict[clusters[i]]=='RXJ1716A': x,y,VA,HA=text_dict[clusters[i]][0],7*10**44,'top','center'
    if name_dict[clusters[i]]=='Lynx E': x,y,VA,HA=text_dict[clusters[i]][0],1.1*10**44,'top','center'
    plt.text(x,y,name_dict[clusters[i]],horizontalalignment=HA,verticalalignment=VA,color='k')
plt.xlim(xlim[0],xlim[1])
plt.ylim(3E43,ylim[1])
plt.xlabel('Temperature (keV)')
plt.ylabel(r'$L_x\ E(z)^{-1}$ ergs s$^{-1}$')
plt.legend(frameon=False,loc='upper left')
#plt.savefig('/home/rumbaugh/Chandra/plots/scaling_relations.Lx-T.6.4.17.png')

mindistlit,mindistfit=calc_SR_dists(xdummy,ydummy_lit_4func,temps,lumsEz*10**(-44),terrhi,lumEzerrs*10**(-44),Xerrlo=terrlo),calc_SR_dists(xdummy,ydummy_fit,temps,lumsEz,terrhi,lumEzerrs,Xerrlo=terrlo)

outcr['mindistlit_LxT'],outcr['mindistfit_LxT']=mindistlit,mindistfit

def f_sigT(B,sig):
    #Remember, this function is in log-log form, and Lx is divided by E(z)
    return B[0]*sig+B[1]
linearsigT=odr.Model(f_sigT)
sigTdata=odr.Data(np.log(temps),np.log(sigs),we=(sigerrs/sigs)**-2,wd=(0.5*(tubs-tlbs)/temps)**-2)
odrsigT=odr.ODR(sigTdata,linearsigT,beta0=[0.65,np.log(10**2.49)])
sigTout=odrsigT.run()

text_dict={clusters[x]: [temps[x],sigs[x],'left','bottom'] for x in np.arange(len(clusters))}

offsetfracx,offsetfracy=1.045,1.01
plt.subplot(3,1,2)
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(temps,sigs,xerr=[terrlo,terrhi],yerr=sigerrs,color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(temps,sigs,s=32,color='r')
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(np.max([xlim[0],0.48]),xlim[1],dummypoints)
ydummy_lit=10**2.49*xdummy**0.65
ydummy_fit=np.e**sigTout.beta[1]*xdummy**sigTout.beta[0]
plt.loglog(xdummy,ydummy_lit,lw=2,color='b',label='Xue & Wu (2000)')
plt.loglog(xdummy,ydummy_fit,lw=2,color='magenta',ls='dotted',label='Linear Fit')
for i in np.arange(len(clusters)): 
    x,y,HA,VA=text_dict[clusters[i]][0]*offsetfracx,text_dict[clusters[i]][1]*offsetfracy,text_dict[clusters[i]][2],text_dict[clusters[i]][3]
    if clusters[i]=='Lynx_W':x,y,VA,HA=3.8,690,'top','right'
    if clusters[i]=='RCS0224B': y,VA=710,'top'
    if clusters[i]=='Cluster_A': x,HA=3.5,'right'
    if clusters[i]=='Cluster_B': x,HA=1.27,'right'
    if clusters[i]=='RXJ1821': x,HA=5.8,'right'
    if clusters[i]=='RXJ1757': x,HA=text_dict[clusters[i]][0],'center'
    if clusters[i]=='Cl1350C': x,HA=text_dict[clusters[i]][0],'center'
    if clusters[i]=='Cluster_I': x,HA=2.8,'right'
    if name_dict[clusters[i]]=='SC0910A': x,HA=2.8,'right'
    if name_dict[clusters[i]]=='SC0910B': HA='center'
    if name_dict[clusters[i]]=='Lynx E': y,VA=835,'top'

    plt.text(x,y,name_dict[clusters[i]],horizontalalignment=HA,verticalalignment=VA,color='k')
plt.xlim(0.48,xlim[1])
plt.ylim(ylim)
plt.xlabel('Temperature (keV)')
plt.ylabel('Velocity Dispersion (km/s)')
plt.legend(frameon=False,loc='upper left')
#plt.savefig('/home/rumbaugh/Chandra/plots/scaling_relations.sig-T.6.4.17.png')
print plt.xlim()
mindistlit,mindistfit=calc_SR_dists(xdummy,ydummy_lit,temps,sigs,terrhi,sigerrs,Xerrlo=terrlo),calc_SR_dists(xdummy,ydummy_fit,temps,sigs,terrhi,sigerrs,Xerrlo=terrlo)

outcr['mindistlit_sigT'],outcr['mindistfit_sigT']=mindistlit,mindistfit


lumXW=lums[gdo]/(1.-1./np.sqrt(1+(r500/r0)**2))
lumXWerr=lumerrs[gdo]/(1.-1./np.sqrt(1+(r500/r0)**2))

def f_sigLx(B,L):
    #Remember, this function is in log-log form, and Lx is divided by E(z)
    return B[0]*L+B[1]
linearsigLx=odr.Model(f_sigLx)
sigLxdata=odr.Data(np.log(sigs),np.log(lumXW/Ezs),wd=(sigerrs/sigs)**-2,we=(lumXWerr/lumXW)**-2)
odrsigLx=odr.ODR(sigLxdata,linearsigLx,beta0=[5.30,np.log(10**(42-12.9))])
sigLxout=odrsigLx.run()


offsetfracx,offsetfracy=1.01,1.02
text_dict={clusters[x]: [sigs[x],lumXW[x]/Ezs[x],'left','bottom'] for x in np.arange(len(clusters))}

plt.subplot(3,1,3)
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(sigs,lumXW/Ezs,xerr=sigerrs,yerr=lumXWerr/Ezs,color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(sigs,lumXW/Ezs,s=32,color='r')
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(np.max([xlim[0],.000001]),xlim[1],dummypoints)
ydummy_lit=10**-12.9*xdummy**5.30*10**42
ydummy_fit=np.e**sigLxout.beta[1]*xdummy**sigLxout.beta[0]
plt.loglog(xdummy,ydummy_lit,lw=2,color='b',label='Xue & Wu (2000)')
plt.loglog(xdummy,ydummy_fit,lw=2,color='magenta',ls='dotted',label='Linear Fit')
for i in np.arange(len(clusters)): 
    x,y,HA,VA=text_dict[clusters[i]][0]*offsetfracx,text_dict[clusters[i]][1]*offsetfracy,'left','bottom'
    print name_dict[clusters[i]],x,y
    if clusters[i]=='RXJ1221B': x,y,HA,VA=text_dict[clusters[i]][0],1.12*10**45,'center','top'
    if clusters[i]=='Cl1350C': x,HA=795,'right'
    if clusters[i]=='RCS0224B': x,HA=705,'right'
    if clusters[i]=='Cluster_I': y,VA=1.45*10**44,'top'
    if clusters[i]=='Cluster_B': x,y,VA,HA=810,1.14*10**44,'top','right'
    if clusters[i]=='Cluster_D': x,y,VA,HA=682,9.2*10.**43,'top','right'
    if clusters[i]=='RXJ1757': x,y,VA,HA=860,1.8*10**44,'top','right'
    if name_dict[clusters[i]]=='Lynx E': x,y,VA,HA=830,text_dict[clusters[i]][1],'center','right'
    if name_dict[clusters[i]]=='SC0910A': y,VA=1.2*10**44,'top'
    if name_dict[clusters[i]]=='SC0910B': x,y,VA,HA=719,1.55*10**44,'top','right'
    plt.text(x,y,name_dict[clusters[i]],horizontalalignment=HA,verticalalignment=VA,color='k')
plt.xlim(xlim[0],xlim[1])
plt.ylim(3E43,ylim[1])
plt.xlabel('Velocity Dispersion (km/s)')
plt.ylabel(r'$L_x\ E(z)^{-1}$ ergs s$^{-1}$')
plt.legend(frameon=False,loc='lower right')
fig.tight_layout()

fig.subplots_adjust(bottom=0.05)
plt.savefig('/home/rumbaugh/Chandra/plots/scaling_relations_for_paper.8.13.17.pdf')
