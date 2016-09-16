import numpy as np

try:
    reps
except NameError:
    reps = 10

execfile('/home/rumbaugh/optical_matching.py')

date = '1.25.15'

cat_in = '/home/rumbaugh/Cl0023.xray_phot.soft_hard_full.dat'
opt_in = '/home/rumbaugh/Downloads/FINAL.onlykindafinal.cl0023.deimos.lris.feb2010.cat'
outcat = '/home/rumbaugh/Chandra/opt_match/test/Cl0023.opt_match.test.%s.dat'%date
outreg = '/home/rumbaugh/Chandra/opt_match/test/Cl0023.opt_match.test.%s.reg'%date

opt_load = {'names': ('ID','mask','num','ra','dec','magR','magI','magZ'),'formats': ('|S8','|S8','|S8','f8','f8','f8','f8','f8')}

ra_aim,dec_aim = 5.9623443182206,4.3820249449499

MatchCat(cat_in,opt_in,outcat,outreg,ra_aim,dec_aim,reps=reps,ref_load_dict=opt_load)
