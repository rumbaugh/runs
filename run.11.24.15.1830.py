execfile('/home/rumbaugh/git/ORELSE/Catalog Matching/optical_matching.py')
#refcat='/home/rumbaugh/git/Chandra/Catalogs/Photometric/rxj1716.radecIDnmags.cat'
refcat='/home/rumbaugh/Chandra/photcats/cl1604_rizdata.corr.gz'
catin='/home/rumbaugh/git/ORELSE/Work_Lu/Cl1604_vla_bob_degs.cat'

outcat='/home/rumbaugh/testLu_minsrch_0.1.dat'
outreg='/home/rumbaugh/testLu.reg'
raaim,decaim=241.08917,43.309936
#refdict={'names':('ID','ra','dec','magR','magI','magZ'),'formats':('|S8','f8','f8','f8','f8','f8')}
refdict={'names':('ID','d1','d2','ra','dec','magR','dR','magI','dI''magZ'),'formats':('|S8','|S8','|S8','f8','f8','f8','f8','f8','f8','f8')}

MatchCat(catin,refcat,outcat,outreg,raaim,decaim,ref_load_dict=refdict,minsrch=0.1,radius_opt_cen=3600*5,useConcaveHull=True,reps=10000)
