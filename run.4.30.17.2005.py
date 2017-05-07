import numpy as np
import matplotlib
import matplotlib.pyplot as plt


crd=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_full_magdiffs_wDBID.4.30.17.tab',dtype={'names':('RA','DEC','z','mjdlo','glo','siglo','flaglo','mjdhi','ghi','sighi','flaghi','RA_DES','DEC_DES','DBID','y3a1_mag_auto_g','ilo','ihi','rlo','rhi'),'formats':('f8','f8','f8','f8','f8','f8','i8','f8','f8','f8','i8','f8','f8','|S24','f8','f8','f8','f8','f8')})

gswap=np.where(crd['mjdlo']>crd['mjdhi'])[0]
if len(gswap)>0:
    crd['glo'][gswap],crd['ghi'][gswap],crd['ilo'][gswap],crd['ihi'][gswap],crd['mjdlo'][gswap],crd['mjdhi'][gswap],crd['rlo'][gswap],crd['rhi'][gswap]=crd['ghi'][gswap],crd['glo'][gswap],crd['ihi'][gswap],crd['ilo'][gswap],crd['mjdhi'][gswap],crd['mjdlo'][gswap],crd['rhi'][gswap],crd['rlo'][gswap]

crd=crd[(crd['ilo']>0)&(crd['ihi']>0)&(crd['rlo']>0)&(crd['rhi']>0)]

gdrop=crd['ghi']-crd['glo']
gihi,gilo,grhi,grlo=crd['ghi']-crd['ihi'],crd['glo']-crd['ilo'],crd['ghi']-crd['rhi'],crd['glo']-crd['rlo']
gidrop,grdrop=gihi-gilo,grhi-grlo

matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=14

yticks_minor=np.arange(-1.25,1.75,0.5)
xticks_minor=np.arange(-2.25,2.75,0.5)

fig=plt.figure(1)
fig.clf()
plt.clf()
ax1=fig.add_subplot(1,1,1)
pos1 = ax1.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0 + 0.03,  pos1.width, pos1.height] 
ax1.set_position(pos2)
ax1.tick_params(which='major',length=8,width=3,labelsize=17)
ax1.tick_params(which='minor',length=5,width=2,labelsize=17)
ax1.scatter(gdrop,gidrop,color='k',edgecolor='None',s=6)
ax1.scatter(gdrop[np.abs(gdrop)>1],gidrop[np.abs(gdrop)>1],color='r',edgecolor='None',s=6)
ax1.set_xlim(-2.4,2.4)
ax1.set_ylim(-1.4,1.4)
ax1.set_xlabel(r'$\Delta g$',fontsize=20)
ax1.set_ylabel(r'$\Delta g-i$',fontsize=20)
ax1.set_xticks(xticks_minor,minor=True)
ax1.set_yticks(yticks_minor,minor=True)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/g_vs_g-i.EVQs.png')

fig=plt.figure(1)
fig.clf()
plt.clf()
ax1=fig.add_subplot(1,1,1)
pos1 = ax1.get_position() # get the original position 
pos2 = [pos1.x0, pos1.y0 + 0.03,  pos1.width, pos1.height] 
ax1.set_position(pos2)
ax1.tick_params(which='major',length=8,width=3,labelsize=17)
ax1.tick_params(which='minor',length=5,width=2,labelsize=17)
ax1.scatter(gdrop,grdrop,color='k',edgecolor='None',s=6)
ax1.scatter(gdrop[np.abs(gdrop)>1],grdrop[np.abs(gdrop)>1],color='r',edgecolor='None',s=6)
ax1.set_xlim(-2.4,2.4)
ax1.set_ylim(-1.4,1.4)
ax1.set_xlabel(r'$\Delta g$',fontsize=20)
ax1.set_ylabel(r'$\Delta g-r$',fontsize=20)
ax1.set_xticks(xticks_minor,minor=True)
ax1.set_yticks(yticks_minor,minor=True)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/g_vs_g-r.EVQs.png')
