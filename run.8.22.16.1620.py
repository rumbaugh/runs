import numpy as np

bolfact=1.0246397298007854

crf=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.soft_cluster_fits.dat',dtype={'names':('cluster','r0','r0-','r0+','bkg','bkg-','bkg+','r500','r500C','NC'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

crl=np.loadtxt('/home/rumbaugh/Chandra/test.ORELSE.clusters_lums.dat',dtype={'names':('field','cluster','ls','lh','lf','lserr','lherr','lferr','bfs','bfh','bff'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})

bfs,bfh,bff=crl['bfs'],crl['bfh'],crl['bff']
ls500,lh500,lf500=crl['ls']*crf['r500C']/crf['NC'],crl['lh']*crf['r500C']/crf['NC'],crl['lf']*crf['r500C']/crf['NC']
ls500err,lh500err,lf500err=crl['lserr']*crf['r500C']/crf['NC'],crl['lherr']*crf['r500C']/crf['NC'],crl['lferr']*crf['r500C']/crf['NC']

FILE=open('/home/rumbaugh/Chandra/test.ORELSE.clusters_lums.dat','w')
FILE.write('# field cluster LumSoft LumHard LumFull LumSoft_r500 LumHard_r500 LumFull_r500 LumBol LumSofterr LumHarderr LumFullerr LumSoft_r500err LumHard_r500err LumFull_r500err LumBolerr\n')
for i in range(0,len(ls500)):
    FILE.write('%12s %12s %E %E %E %E %E %E %E %E %E %E %E %E %E %E\n'%(crl['field'][i],crl['cluster'][i],crl['ls'][i],crl['lh'][i],crl['lf'][i],ls500[i],lh500[i],lf500[i],bfs[i]*ls500[i],crl['lserr'][i],crl['lherr'][i],crl['lferr'][i],ls500err[i],lh500err[i],lf500err[i],bfs[i]*ls500err[i]))
FILE.close()
