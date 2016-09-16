import numpy as np
import matplotlib.pyplot as plt


old_dict={'RXJ1821': {'lum': 8.8,'sig': 1070},'RXJ1757': {'lum': 2.8,'sig': 890}, 'Cluster_I': {'lum': 1.7,'sig': 890}, '1324+3011': {'lum': 2.6,'sig': 920},'0910+5419': {'lum': 2.3,'sig': 950},'0910+5422': {'lum': 3.6,'sig': 780},'Cluster_A': {'lum': 1.9,'sig': 720},'Cluster_B': {'lum': 1.1,'sig': 810}}

crl=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_lums.dat',dtype={'names':('field','cluster','ls','lh','lf','ls500','lh500','lf500','lbol','lserr','lherr','lferr','ls500err','lh500err','lf500err','lbolerr'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

cr2=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','ra','dec','z','sig0.5mpc','sig0.5mpcerr','n0.5mpc','sig1mpc','sig1mpcerr','n1mpc','logMvir','LMVerr','nh'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','i8','f8','f8','i8','f8','f8','f8')})
clusters=np.array(old_dict.keys())

oldlums,oldsigs=np.zeros(len(clusters)),np.zeros(len(clusters))

gs=np.zeros(len(clusters),dtype='i8')
gs2=np.zeros(len(clusters),dtype='i8')
for i in range(0,len(gs)):
    gs[i]=np.where(crl['cluster']==clusters[i])[0]
    gs2[i]=np.where(cr2['cluster']==clusters[i])[0]
    oldlums[i],oldsigs[i]=old_dict[clusters[i]]['lum'],old_dict[clusters[i]]['sig']
newlums,newsigs=crl['lbol'][gs]*1E-44,cr2['sig1mpc'][gs2]




plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(oldsigs,oldlums,color='b',s=32)
plt.scatter(newsigs,newlums,color='r',s=32)
xlim=plt.xlim()
xrng=xlim[1]-xlim[0]
#plt.xlim(xlim[1],xlim[0])
for i in range(0,len(oldsigs)): 
    #plt.text(cr['Hd'][i]+xrng/50.,crbf['BF_cut'][gbf[i]],cr['field'][i],color='b')
    plt.arrow(oldsigs[i],oldlums[i],newsigs[i]-oldsigs[i],newlums[i]-oldlums[i],color='r',lw=2,width=0.005,head_length=0.01)
#plt.axvline(-4,lw=2,color='k',ls='dashed')
plt.ylabel(r'$\sigma_v$ (km/s)')
plt.xlabel(r'$L_X (10^{44}$ ergs/s)')
plt.savefig('/home/rumbaugh/Chandra/plots/lum+sig_comp.new_vs_new.png')
