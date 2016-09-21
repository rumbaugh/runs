import numpy as np
import matplotlib.pyplot as plt
execfile("/home/rumbaugh/makeCMD.py")
execfile("/home/rumbaugh/set_spec_dict.py")
execfile("/home/rumbaugh/KStest.py")


cmloaddict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigs','sigh','sigf'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')}

refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
date='3.6.16'

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]

crRS=np.loadtxt('/home/rumbaugh/Chandra/RS_offsets_wACS.6.13.16.dat',dtype={'names':('field','AGNnumber','specID','RA','Dec','RSoffset','magR','magI','magZ','SCmagRed','SCmagBlue'),'formats':('|S24','i8','|S48','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

crl=np.loadtxt('/home/rumbaugh/Chandra/lums_newphotoz_adam.1sig.5.5.16.dat',dtype={'names':('field','ID','RA','Dec','z_peak','nh','lum_soft','lum_hard','lum_full','P_inclus'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8')})

gm=np.zeros(len(crRS['RA']),dtype='i8')
for i in range(0,len(gm)): 
    tmpdist=np.sqrt((crRS['RA'][i]-crl['RA'])**2+(crRS['Dec'][i]-crl['Dec'])**2)
    gm[i]=np.argsort(tmpdist)[0]

#crRS=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.composite_colors.nofit.%s.dat'%date,dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})
#crRS_ACS=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.cl1604_ACS.nofit.%s.dat'%date,dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})
fig=figure(1)
zarr=np.linspace(0.1,2,191)

lums=crl['lum_full'][gm]

rso,rso_all=-crRS['RSoffset'][((crRS['AGNnumber']>=0)&(lums>10**42.5))],-crRS['RSoffset'][crRS['AGNnumber']==-1]
rso1604,rso_all1604=-crRS['RSoffset'][((crRS['AGNnumber']>=0)&(crRS['field']=='cl1604')&(lums>10**42.5))],-crRS['RSoffset'][((crRS['AGNnumber']==-1)&(crRS['field']=='cl1604'))]

rsonot1604,rso_allnot1604=-crRS['RSoffset'][((crRS['AGNnumber']>=0)&(crRS['field']!='cl1604')&(lums>10**42.5))],-crRS['RSoffset'][((crRS['AGNnumber']==-1)&(crRS['field']!='cl1604'))]


rsonot0023no1604,rso_allnot0023no1604=-crRS['RSoffset'][((crRS['AGNnumber']>=0)&(crRS['field']!='cl1604')&(crRS['field']!='cl0023')&(lums>10**42.5))],-crRS['RSoffset'][((crRS['AGNnumber']==-1)&(crRS['field']!='cl0023')&(crRS['field']!='cl1604'))]

rsolowlum=-crRS['RSoffset'][((crRS['AGNnumber']>=0)&(lums<10**43.4)&(lums>10**42.5))]

fig.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax2.tick_params(which='major',length=8,width=2,labelsize=14)
ax2.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=ax.hist(rso,range=(-7,2),bins=9,color='r')
#ax.hist(rso_all,range=(-7,2),bins=9,color='b',alpha=0.3,weights=20*np.ones(len(rso_all))*1./len(rso_all))
b=ax2.hist(rso_all,range=(-7,2),bins=9,color='b',alpha=0.3,weights=100*np.ones(len(rso_all))*1./len(rso_all))
ax.set_xlabel("Red Sequence Offset")
ax.set_ylabel("Number of AGN Hosts")
ax.set_xlim(-7,2)
ax.set_ylim(0,20)
ax2.set_ylim(0,20./len(rso)*100)
ax2.set_ylabel("Percentage of All Sources")
print 'All'
for i in range(0,len(a[0])):
    print '%i-%i (AGN): %.2f'%(a[1][i],a[1][1+i],a[0][i]*1./np.sum(a[0]))
for i in range(0,len(a[0])):
    print '%i-%i (all): %.2f'%(b[1][i],b[1][1+i],b[0][i]*1./np.sum(b[0]))
fig.savefig('/home/rumbaugh/Chandra/plots/RS_offset.hist.7.4.16.png')

fig.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax2.tick_params(which='major',length=8,width=2,labelsize=14)
ax2.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=ax.hist(rso1604,range=(-7,2),bins=9,color='r')
b=ax2.hist(rso_all1604,range=(-7,2),bins=9,color='b',alpha=0.3,weights=100*np.ones(len(rso_all1604))*1./len(rso_all1604))
ax.set_xlabel("Red Sequence Offset")
ax.set_ylabel("Number of Sources")
ax.set_xlim(-7,2)
ax.set_ylim(0,3.1)
ax2.set_ylim(0,3.1/len(rso1604)*100)
ax2.set_ylabel("Percentage of All Sources")
fig.savefig('/home/rumbaugh/Chandra/plots/RS_offset_cl1604.hist.7.4.16.png')
print 'Cl1604'
for i in range(0,len(a[0])):
    print '%i-%i (AGN): %.2f'%(a[1][i],a[1][1+i],a[0][i]*1./np.sum(a[0]))
for i in range(0,len(a[0])):
    print '%i-%i (all): %.2f'%(b[1][i],b[1][1+i],b[0][i]*1./np.sum(b[0]))
#psfpdf.close()    
#FILERS.close()

fig.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax2.tick_params(which='major',length=8,width=2,labelsize=14)
ax2.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=ax.hist(rsonot1604,range=(-7,2),bins=9,color='r')
b=ax2.hist(rso_allnot1604,range=(-7,2),bins=9,color='b',alpha=0.3,weights=100*np.ones(len(rso_allnot1604))*1./len(rso_allnot1604))
ax.set_xlabel("Red Sequence Offset")
ax.set_ylabel("Number of Sources")
ax.set_xlim(-7,2)
ax.set_ylim(0,20)
ax2.set_ylim(0,20./len(rsonot1604)*100)
ax2.set_ylabel("Percentage of All Sources")
fig.savefig('/home/rumbaugh/Chandra/plots/RS_offset_not1604.hist.7.4.16.png')
print 'not 1604'
for i in range(0,len(a[0])):
    print '%i-%i (AGN): %.2f'%(a[1][i],a[1][1+i],a[0][i]*1./np.sum(a[0]))
for i in range(0,len(a[0])):
    print '%i-%i (all): %.2f'%(b[1][i],b[1][1+i],b[0][i]*1./np.sum(b[0]))

fig.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax2.tick_params(which='major',length=8,width=2,labelsize=14)
ax2.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=ax.hist(rsonot0023no1604,range=(-7,2),bins=9,color='r')
b=ax2.hist(rso_allnot0023no1604,range=(-7,2),bins=9,color='b',alpha=0.3,weights=100*np.ones(len(rso_allnot0023no1604))*1./len(rso_allnot0023no1604))
ax.set_xlabel("Red Sequence Offset")
ax.set_ylabel("Number of Sources")
ax.set_xlim(-7,2)
ax.set_ylim(0,20)
ax2.set_ylim(0,20./len(rsonot0023no1604)*100)
#ax2.set_ylim(0,40)
ax2.set_ylabel("Percentage of All Sources")
fig.savefig('/home/rumbaugh/Chandra/plots/RS_offset_not0023no1604.hist.7.4.16.png')
print 'not 1604'
for i in range(0,len(a[0])):
    print '%i-%i (AGN): %.2f'%(a[1][i],a[1][1+i],a[0][i]*1./np.sum(a[0]))
for i in range(0,len(a[0])):
    print '%i-%i (all): %.2f'%(b[1][i],b[1][1+i],b[0][i]*1./np.sum(b[0]))

fig.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax2.tick_params(which='major',length=8,width=2,labelsize=14)
ax2.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=ax.hist(rsolowlum,range=(-7,2),bins=9,color='r')
b=ax2.hist(rso_all,range=(-7,2),bins=9,color='b',alpha=0.3,weights=100*np.ones(len(rso_all))*1./len(rso_all))
ax.set_xlabel("Red Sequence Offset")
ax.set_ylabel("Number of Sources")
ax.set_xlim(-7,2)
ax.set_ylim(0,20)
ax2.set_ylim(0,20./len(rsolowlum)*100)
#ax2.set_ylim(0,40)
ax2.set_ylabel("Percentage of All Sources")
fig.savefig('/home/rumbaugh/Chandra/plots/RS_offset_lowlum.hist.7.4.16.png')
print 'Low lum'
for i in range(0,len(a[0])):
    print '%i-%i (AGN): %.2f'%(a[1][i],a[1][1+i],a[0][i]*1./np.sum(a[0]))
for i in range(0,len(a[0])):
    print '%i-%i (all): %.2f'%(b[1][i],b[1][1+i],b[0][i]*1./np.sum(b[0]))
#psfpdf.close()    
#FILERS.close()

print KStest(rso[((rso>-7)&(rso<2))],rso_all[((rso_all>-7)&(rso_all<2))])
print KStest(rso1604[((rso1604>-7)&(rso1604<2))],rso_all1604[((rso_all1604>-7)&(rso_all1604<2))])
print KStest(rsonot1604[((rsonot1604>-7)&(rsonot1604<2))],rso_allnot1604[((rso_allnot1604>-7)&(rso_allnot1604<2))])
print KStest(rsonot0023no1604[((rsonot0023no1604>-7)&(rsonot0023no1604<2))],rso_allnot0023no1604[((rso_allnot0023no1604>-7)&(rso_allnot0023no1604<2))])
print KStest(rsolowlum[((rsolowlum>-7)&(rsolowlum<2))],rso_allnot1604[((rso_allnot1604>-7)&(rso_allnot1604<2))])
print KStest(rsolowlum[((rsolowlum>-7)&(rsolowlum<2))],rso_all[((rso_all>-7)&(rso_all<2))])
