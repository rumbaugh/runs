import numpy as np

indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

crn=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.1.13.16.dat',dtype=indict)

crn['flux_soft']*=1E-42
crn['flux_hard']*=1E-42
crn['flux_full']*=1E-42

np.savetxt('/home/rumbaugh/X-ray_cat.1.13.16.csv',crn,fmt='%s,%i,%f,%f,%f,%f,%f,%E,%E,%E,%f,%f,%f,%f,%s,%s',delimiter=',')
