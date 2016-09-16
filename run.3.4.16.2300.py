import numpy as np
import matplotlib.pyplot as plt

crRS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets.AGN.3.4.16.dat',dtype={'names':('field','number','RA','Dec','RSoffset','magR','magI','magZ','SCmagRed','SCmagBlue'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8')})



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
plt.scatter(-crRS['RSoffset'],np.log10(crn['lum_full'][gAGN]))
plt.xlabel('RS Offset')
plt.ylabel('X-ray Luminosity')
plt.axhline(43.3,lw=2,ls='--',color='k')
plt.axvline(-1,lw=2,ls='--',color='k')
plt.axvline(-3,lw=2,ls='--',color='k')
plt.savefig('/home/rumbaugh/Chandra/plots/RSoffset_vs_Lum.3.4.16.png')
