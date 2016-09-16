import numpy as np
import matplotlib.pyplot as plt

carr=np.array(['blue','green','orange','red','magenta','brown','pink','cyan'])
marr=np.array(['o','s','x','+','*'])

crRS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets.AGN.3.4.16.dat',dtype={'names':('field','number','RA','Dec','RSoffset','magR','magI','magZ','SCmagRed','SCmagBlue'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8')})


targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])#,"cl1324_north","cl1324_south"])

indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

crn=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.3.4.16.dat',dtype=indict)

gAGN=np.zeros(len(crRS['RA']),dtype='i8')
for i in range(0,len(crRS['RA'])):
    tmpdist=np.sqrt((crRS['RA'][i]-crn['RA'])**2+(crRS['Dec'][i]-crn['Dec'])**2)
    gAGN[i]=np.argsort(tmpdist)[0]
    if tmpdist[gAGN[i]]>1./3600: print 'Too big! %f'%(tmpdist[gAGN[i]]*3600)
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
for field,jf in zip(targets,np.arange(len(targets))):
    gf = np.where(crn['field'][gAGN]==field)[0]
    plt.scatter(-crRS['RSoffset'][gf],np.log10(crn['lum_full'][gAGN][gf]),color=carr[jf%len(carr)],marker=marr[jf%len(marr)],label=field)
plt.xlabel('RS Offset')
plt.ylabel('X-ray Luminosity')
plt.axhline(43.3,lw=2,ls='--',color='k')
plt.axvline(-1,lw=2,ls='--',color='k')
plt.axvline(-3,lw=2,ls='--',color='k')
plt.legend()
plt.savefig('/home/rumbaugh/Chandra/plots/RSoffset_vs_Lum.3.5.16.png')
