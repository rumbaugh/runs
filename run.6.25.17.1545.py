import numpy as np

bolfact=1.0246397298007854

crf=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_fits.dat',dtype={'names':('cluster','r0','r0-','r0+','bkg','bkg-','bkg+','r500','r500C','NC'),'formats':('|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')})
crf=crf[crf['cluster']!='1324+3013']
crl=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_lums.dat',dtype={'names':('field','cluster','ls','lh','lf'),'formats':('|S24','|S24','f8','f8','f8')},usecols=(0,1,2,3,4))

ls500,lh500,lf500=crl['ls']*crf['r500C']/crf['NC'],crl['lh']*crf['r500C']/crf['NC'],crl['lf']*crf['r500C']/crf['NC']

crn=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_netcounts.dat',dtype={'names':('field','cluster','ncntsS','cntsS','bkgcntsS','ncnts_noVCS','cnts_noVCS','bkgcnts_noVCS','speccenXS','speccenYS','specradS','ncntsH','cntsH','bkgcntsH','ncnts_noVCH','cnts_noVCH','bkgcnts_noVCH','speccenXH','speccenYH','specradH','ncntsF','cntsF','bkgcntsF','ncnts_noVCF','cnts_noVCF','bkgcnts_noVCF','speccenXF','speccenYF','specradF','bkgcenXF','bkgcenYF','bkgradF'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','i8','i8','i8','i8','i8','i8')})


FILE=open('/home/rumbaugh/Chandra/ORELSE.clusters_lums.6.25.17.dat','w')
FILE.write('# field cluster LumSoft LumHard LumFull LumSoft_r500 LumHard_r500 LumFull_r500 LumBol LumSofterr LumHarderr LumFullerr LumSoft_r500err LumHard_r500err LumFull_r500err LumBolerr\n')
for i in range(0,len(ls500)):
    gn=np.where(crn['cluster']==crl['cluster'][i])[0][0]
    Xs,Xh,Xf=(crn['cntsS'][gn]-crn['ncntsS'][gn])/crn['bkgcntsS'][gn],(crn['cntsH'][gn]-crn['ncntsH'][gn])/crn['bkgcntsH'][gn],(crn['cntsF'][gn]-crn['ncntsF'][gn])/crn['bkgcntsF'][gn]
    lserr,lherr,lferr=crl['ls'][i]/crn['ncntsS'][gn]*np.sqrt(crn['cntsS'][gn]+Xs**2*crn['bkgcntsS'][gn]),crl['lh'][i]/crn['ncntsH'][gn]*np.sqrt(crn['cntsH'][gn]+Xh**2*crn['bkgcntsH'][gn]),crl['lf'][i]/crn['ncntsF'][gn]*np.sqrt(crn['cntsF'][gn]+Xf**2*crn['bkgcntsF'][gn])
    FILE.write('%12s %12s %E %E %E %E %E %E %E %E %E %E %E %E %E %E\n'%(crl['field'][i],crl['cluster'][i],crl['ls'][i],crl['lh'][i],crl['lf'][i],ls500[i],lh500[i],lf500[i],bolfact*lf500[i],lserr,lherr,lferr,lserr*ls500[i]/crl['ls'][i],lherr*ls500[i]/crl['ls'][i],lferr*ls500[i]/crl['ls'][i],bolfact*lferr*ls500[i]/crl['ls'][i]))
FILE.close()
