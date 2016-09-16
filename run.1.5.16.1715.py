execfile('/home/rumbaugh/git/ORELSE/Catalog Matching/optical_matching.py')
refcat='/home/rumbaugh/Chandra/photcats/cl0023_rizdata.corr.gz'
catin='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/cl0023/proc/cl0023/cl0023_xray_phot.dat'

outcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/cl0023/proc/cl0023/testmatch.1.5.16.dat'
outreg='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/cl0023/proc/cl0023/testmatch.1.5.16.reg'
raaim,decaim=5.9623443990511,4.3820249628906
#refdict={'names':('ID','ra','dec','magR','magI','magZ'),'formats':('|S64','f8','f8','f8','f8','f8')}
refdict={'names':('ID','d1','d2','ra','dec','magR','dmagR','magI'),'formats':('|S64','|S64','|S64','f8','f8','f8','f8','f8')}
load_dict={'names':('raX','decX','netcnts_corrX_soft','netcnts_corrX_hard','netcnts_corrX_full'),'formats':('f8','f8','f8','f8','f8')}

MatchCat(catin,refcat,outcat,outreg,raaim,decaim,setup='xray',load_dict=load_dict,ref_load_dict=refdict,minsrch=1.5,useConcaveHull=True,reps=1000,usesig=False)
