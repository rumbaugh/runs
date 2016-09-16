import numpy as np

bolfact=1.0246397298007854

crf=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_fits.dat',dtype={'names':('cluster','r0','r0-','r0+','bkg','bkg-','bkg+','r500','r500C','NC'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

crl=np.loadtxt('/home/rumbaugh/Chandra/test.ORELSE.clusters_lums.dat',dtype={'names':('field','cluster','ls','lh','lf','lserr','lherr','lferr'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8')})

ls500,lh500,lf500=crl['ls']*crf['r500C']/crf['NC'],crl['lh']*crf['r500C']/crf['NC'],crl['lf']*crf['r500C']/crf['NC']
ls500err,lh500err,lf500err=crl['lserr']*crf['r500C']/crf['NC'],crl['lherr']*crf['r500C']/crf['NC'],crl['lferr']*crf['r500C']/crf['NC']

for i in range(0,len(ls500)):
    print '%12s %16s - %.1f %.1f'%(crl['field'][i],crf['cluster'][i],crf['NC'][i],crf['r500C'][i])
