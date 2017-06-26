import numpy as np

crl=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_lums.dat',dtype={'names':('field','cluster','ls','lh','lf'),'formats':('|S24','|S24','f8','f8','f8')})
crn=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.cluster_netcounts.dat',dtype={'names':('field','cluster','ncntsS','cntsS','bkgcntsS','ncnts_noVCS','cnts_noVCS','bkgcnts_noVCS','speccenXS','speccenYS','specradS','ncntsH','cntsH','bkgcntsH','ncnts_noVCH','cnts_noVCH','bkgcnts_noVCH','speccenXH','speccenYH','specradH','ncntsF','cntsF','bkgcntsF','ncnts_noVCF','cnts_noVCF','bkgcnts_noVCF','speccenXF','speccenYF','specradF','bkgcenXF','bkgcenYF','bkgradF'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','i8','i8','i8','i8','i8','i8')})

gl,gn=np.where(crl['cluster']=='0848+4451')[0][0],np.where(crn['cluster']=='0848+4451')[0][0]

convS,convH,convF=crl['ls'][gl]/crn['ncntsS'][gn],crl['lh'][gl]/crn['ncntsH'][gn],crl['lf'][gl]/crn['ncntsF'][gn]

gw=np.where(crn['cluster']=='Lynx_W')[0][0]

print 'Lynx_W:',crn['ncntsS'][gw]*convS,crn['ncntsH'][gw]*convH,crn['ncntsF'][gw]*convF
