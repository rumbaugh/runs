import numpy as np
import matplotlib.pyplot as plt

crxl=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.4.17.16.dat',dtype={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','sig_soft','sig_hard','sig_full'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S64','|S24','f8','f8','f8')})

lS,lH,lF=crxl['lum_soft'],crxl['lum_hard'],crxl['lum_full']

hardness=(lS-lH)/(lS+lH)
hardness[lS+lH==0]=0
hardnessF=(lS-lF)/(lS+lF)
hardnessF[lS+lF==0]=0

FILE=open('/home/rumbaugh/Chandra/X-ray_lum_hardness.6.3.16.dat','w')
FILE.write('# field RA Dec hardness{(lS-lH)/(lS+lH)} hardness{(lS-lF)/(lS+lF)} lum_soft lum_hard lum_full flux_soft flux_hard flux_full ncnts_soft ncnts_hard ncnts_full redshift mask slit sig_soft sig_hard sig_full\n')

for i in range(0,len(lS)):
    FILE.write('%s %i %f %f %f %f %E %E %E %E %E %E %f %f %f %f %s %s %f %f %f\n'%(crxl['field'][i],crxl['number'][i],crxl['RA'][i],crxl['Dec'][i],hardness[i],hardnessF[i],crxl['lum_soft'][i],crxl['lum_hard'][i],crxl['lum_full'][i],crxl['flux_soft'][i],crxl['flux_hard'][i],crxl['flux_full'][i],crxl['ncnts_soft'][i],crxl['ncnts_hard'][i],crxl['ncnts_full'][i],crxl['redshift'][i],crxl['mask'][i],crxl['slit'][i],crxl['sig_soft'][i],crxl['sig_hard'][i],crxl['sig_full'][i]))
FILE.close()

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=plt.hist(hardness)
plt.xlabel('Hardness Ratio (lS-lH)/(lS+lH)')
plt.savefig('/home/rumbaugh/Chandra/plots/hardness_ratio_dist.6.3.16.png')
plt.figure(1)

plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(hardnessF)
plt.xlabel('Hardness Ratio (lS-lF)/(lS+lF)')
plt.savefig('/home/rumbaugh/Chandra/plots/hardness_ratioF_dist.6.3.16.png')
