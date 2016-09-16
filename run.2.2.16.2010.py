import numpy as np

bolfact=1.0246397298007854

crf=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_fits.dat',dtype={'names':('cluster','r0','r0-','r0+','bkg','bkg-','bkg+','r500','r500C','NC'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

crl=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_lums.dat',dtype={'names':('field','cluster','ls','lh','lf'),'formats':('|S24','|S24','f8','f8','f8')})

ls500,lh500,lf500=crl['ls']*crf['r500C']/crf['NC'],crl['lh']*crf['r500C']/crf['NC'],crl['lf']*crf['r500C']/crf['NC']

FILE=open('/home/rumbaugh/Chandra/ORELSE.clusters_lums.dat','w')
FILE.write('# field cluster LumSoft LumHard LumFull LumSoft_r500 LumHard_r500 LumFull_r500 LumBol\n')
for i in range(0,len(ls500)):
    FILE.write('%12s %12s %E %E %E %E %E %E %E\n'%(crl['field'][i],crl['cluster'][i],crl['ls'][i],crl['lh'][i],crl['lf'][i],ls500[i],lh500[i],lf500[i],bolfact*lf500[i]))
FILE.close()
