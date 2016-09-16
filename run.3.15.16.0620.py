import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/KStest.py')


targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])#,"cl1324_north","cl1324_south"])


indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

crn=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.3.4.16.dat',dtype=indict)
g1324=np.where((crn['field']=='cl1324_north')|(crn['field']=='cl1324_south'))[0]
crn['field'][g1324]='cl1324'

crxall=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.3.15.16.dat',dtype=indict)


plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=plt.hist(np.log10(crn['lum_full'][crn['lum_full']>0]),color='r',range=(42,45),bins=8)
b=plt.hist(np.log10(crxall['lum_full'][crxall['lum_full']>0]),color='b',alpha=0.3,range=(42,45),bins=8)
plt.xlabel('X-ray Luminosity')
plt.ylabel('Number of Sources')
plt.savefig('/home/rumbaugh/Chandra/plots/lumhist_all.3.15.16.png')

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
AGNzdf=plt.hist(crn['redshift'][crn['lum_full']>0],color='r',range=(0.6,1.3),bins=7)
allzdf=plt.hist(crxall['redshift'][((crxall['lum_full']>0)&(crxall['redshift']>=0.65))],color='b',alpha=0.3,range=(0.6,1.3),bins=7)
plt.xlabel('Redshift')
plt.ylabel('Number of Sources')

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=plt.hist(crn['redshift'][crn['lum_full']>0],color='r',range=(0.65,1.3),bins=13)
b=plt.hist(crxall['redshift'][crxall['lum_full']>0],color='b',alpha=0.3,range=(0.65,1.3),bins=13)
plt.xlabel('Redshift')
plt.ylabel('Number of Sources')
plt.savefig('/home/rumbaugh/Chandra/plots/zhist_all.3.15.16.png')

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(crxall['redshift'][crxall['lum_full']>0],np.log10(crxall['lum_full'][crxall['lum_full']>0],color='b')
plt.xlabel('Redshift')
plt.ylabel('Luminosity')
plt.savefig('/home/rumbaugh/Chandra/plots/lum_vs_z.3.15.16.png')

k1,k2=KStest(np.log10(crn['lum_full'][crn['lum_full']>0]),np.log10(crxall['lum_full'][crxall['lum_full']>0]))
print k1,k2
