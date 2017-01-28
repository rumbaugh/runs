import numpy as np
import matplotlib.pyplot as plt

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
for i,i0 in zip(gdo,np.arange(len(gdo))):
    print crl['cluster'][i]
    g=np.where(crx['cluster']==crl['cluster'][i])[0][0]
    gf=np.where(crf['cluster']==crl['cluster'][i])[0][0]
    gc=np.where(cr['cluster']==crl['cluster'][i])[0][0]
    gcc=np.argsort(np.abs(cr['z'][gc]-cc_z))[0]
    Ezs[i0]=Ez[gcc]
    temps[i0],tubs[i0],tlbs[i0]=crx['kt'][g],crx['ub'][g],crx['lb'][g]
    sigs[i0],sigerrs[i0]=cr['sig'][gc],cr['sigerr'][gc]
    r0[i0],r500[i0]=np.abs(crf['r0'][gf]),crf['r500'][gf]

def f_LxT(B,T):
    #Remember, this function is in log-log form, and Lx is divided by E(z)
    return B[0]*T+B[1]
linearLxT=odr.Model(f_LxT)
LxTdata=odr.Data(np.log(temps),np.log(lums[gdo]/Ezs),wd=(0.5*(tubs-tlbs)/temps)**-2,we=(lumerrs[gdo]/lums[gdo])**-2)
odrLxT=odr.ODR(LxTdata,linearLxT,beta0=[2.6,np.log(0.1)])
LxTout=odrLxT.run()

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(temps,lums[gdo]/Ezs,xerr=[tlbs,tubs],yerr=lumerrs[gdo]/Ezs,color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(temps,lums[gdo]/Ezs,s=32,color='r')
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(np.max([xlim[0],0.7]),xlim[1],1000)
plt.loglog(xdummy,0.112*xdummy**2.53*10**44,lw=2,color='b')
plt.loglog(xdummy,0.079*xdummy**2.7*10**44,lw=2,color='cyan',ls='dashed')
plt.loglog(xdummy,10**44.05*(xdummy/5.)**2.9,lw=2,color='purple')#,ls='-.')
plt.loglog(xdummy,np.e**LxTout.beta[1]*xdummy**LxTout.beta[0],lw=2,color='magenta',ls='dotted')
plt.xlim(xlim)
plt.ylim(3E43,ylim[1])
plt.xlabel('Temperature (keV)')
plt.ylabel(r'$L_x\ E(z)^{-1}$ ergs s$^{-1}$')
plt.savefig('/home/rumbaugh/Chandra/plots/scaling_relations.Lx-T.1.25.17.png')

def f_sigT(B,sig):
    #Remember, this function is in log-log form, and Lx is divided by E(z)
    return B[0]*sig+B[1]
linearsigT=odr.Model(f_sigT)
sigTdata=odr.Data(np.log(sigs),np.log(temps),wd=(sigerrs/sigs)**-2,we=(0.5*(tubs-tlbs)/temps)**-2)
odrsigT=odr.ODR(sigTdata,linearsigT,beta0=[0.65,np.log(10**2.49)])
sigTout=odrsigT.run()

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(temps,sigs,xerr=[tlbs,tubs],yerr=sigerrs,color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(temps,sigs,s=32,color='r')
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(np.max([xlim[0],0.7]),xlim[1],1000)
plt.loglog(xdummy,10**2.49*xdummy**0.65,lw=2,color='b')
plt.loglog(xdummy,np.e**sigTout.beta[1]*xdummy**sigTout.beta[0],lw=2,color='magenta',ls='dotted')
plt.xlim(xlim)
plt.ylim(ylim)
plt.xlabel('Temperature (keV)')
plt.ylabel('Velocity Dispersion (km/s)')
plt.savefig('/home/rumbaugh/Chandra/plots/scaling_relations.sig-T.1.25.17.png')

lumXW=lums[gdo]/(1.-1./np.sqrt(1+(r500/r0)**2))
lumXWerr=lumerrs[gdo]/(1.-1./np.sqrt(1+(r500/r0)**2))

def f_sigLx(B,L):
    #Remember, this function is in log-log form, and Lx is divided by E(z)
    return B[0]*L+B[1]
linearsigLx=odr.Model(f_sigLx)
sigLxdata=odr.Data(np.log(sigs),np.log(lumXW/Ezs),wd=(sigerrs/sigs)**-2,we=(lumXWerr/lumXW)**-2)
odrsigLx=odr.ODR(sigLxdata,linearsigLx,beta0=[5.30,np.log(10**(42-12.9))])
sigLxout=odrsigLx.run()

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.errorbar(sigs,lumXW/Ezs,xerr=sigerrs,yerr=lumXWerr/Ezs,color='r',fmt='ro',lw=2,capsize=3,mew=1)
plt.scatter(sigs,lumXW/Ezs,s=32,color='r')
xlim=plt.xlim()
ylim=plt.ylim()
xdummy=np.linspace(np.max([xlim[0],100]),xlim[1],1000)
ydummy=10**-12.9*xdummy**5.30*10**42
plt.loglog(xdummy,ydummy,lw=2,color='b')
plt.loglog(xdummy,np.e**sigLxout.beta[1]*xdummy**sigLxout.beta[0],lw=2,color='magenta',ls='dotted')
plt.xlim(xlim)
plt.ylim(7E43,ylim[1])
plt.xlabel('Velocity Dispersion (km/s)')
plt.ylabel(r'$L_x\ E(z)^{-1}$ ergs s$^{-1}$')
plt.savefig('/home/rumbaugh/Chandra/plots/scaling_relations.sig-Lx.1.25.17.png')

