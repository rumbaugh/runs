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

crc=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat',dtype={'names':('field','cluster','ra','dec'),'formats':('|S24','|S24','f8','f8')},usecols=(0,1,2,3))

testclus=np.zeros(np.shape(crx)[0],dtype='|S128')
for i in range(0,len(testclus)): testclus[i]=crx['cluster'][i].lower()

lums=crl['lbol']
lumerrs=crl['lbolerr']

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
LSS,cluss,ras,decs,temps,tubs,tlbs,Ezs,sigs,sigerrs,r0,r500=np.zeros(len(gdo),dtype='|S20'),np.zeros(len(gdo),dtype='|S20'),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo)),np.zeros(len(gdo))
for i,i0 in zip(gdo,np.arange(len(gdo))):
    print crl['cluster'][i]
    g=np.where(crx['cluster']==crl['cluster'][i])[0][0]
    gf=np.where(crf['cluster']==crl['cluster'][i])[0][0]
    gc=np.where(cr['cluster']==crl['cluster'][i])[0][0]
    gcen=np.where(crc['cluster']==crl['cluster'][i])[0][0]
    gcc=np.argsort(np.abs(cr['z'][gc]-cc_z))[0]
    Ezs[i0]=Ez[gcc]
    LSS[i0],cluss[i0],ras[i0],decs[i0]=crl['field'][i],crl['cluster'][i],crc['ra'][gcen],crc['dec'][gcen]
    temps[i0],tubs[i0],tlbs[i0]=crx['kt'][g],crx['ub'][g],crx['lb'][g]
    sigs[i0],sigerrs[i0]=cr['sig'][gc],cr['sigerr'][gc]
    r0[i0],r500[i0]=np.abs(crf['r0'][gf]),crf['r500'][gf]
    
#plt.errorbar(temps,lums[gdo]/Ezs,xerr=[tlbs,tubs],yerr=lumerrs[gdo]/Ezs,color='r',fmt='ro',lw=2,capsize=3,mew=1)
#plt.scatter(temps,lums[gdo]/Ezs,s=32,color='r')

#plt.errorbar(temps,sigs,xerr=[tlbs,tubs],yerr=sigerrs,color='r',fmt='ro',lw=2,capsize=3,mew=1)
#plt.scatter(temps,sigs,s=32,color='r')
lumXW=lums[gdo]/(1.-1./np.sqrt(1+(r500/r0)**2))
lumXWerr=lumerrs[gdo]/(1.-1./np.sqrt(1+(r500/r0)**2))

#plt.errorbar(sigs,lumXW/Ezs,xerr=sigerrs,yerr=lumXWerr/Ezs,color='r',fmt='ro',lw=2,capsize=3,mew=1)
#plt.scatter(sigs,lumXW/Ezs,s=32,color='r')

outcr=np.zeros((len(Ezs),),dtype={'names':('LSS','Cluster','RA','Dec','Vel_disp','Vel_disp_err','T_X','T_X_err_hi','T_X_err_lo','L_X','L_X_err','E(z)'),'formats':('|S15','|S15','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
outcr['LSS'],outcr['Cluster'],outcr['RA'],outcr['Dec'],outcr['Vel_disp'],outcr['Vel_disp_err'],outcr['T_X'],outcr['T_X_err_hi'],outcr['T_X_err_lo'],outcr['L_X'],outcr['L_X_err'],outcr['E(z)']=LSS,cluss,ras,decs,sigs,sigerrs,temps,tubs,tlbs,lumXW,lumXWerr,Ezs

np.savetxt('/home/rumbaugh/Chandra/ORELSE.DE_summary.dat',outcr,fmt='%13s %12s %10.6f %10.6f %4.0f %4.0f %5.2f %5.2f %5.2f %E %E %f',header=('LSS Cluster RA Dec Vel_disp Vel_disp_err T_X T_X_err_hi T_X_err_lo L_X L_X_err E(z)'))

