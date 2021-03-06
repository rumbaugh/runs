import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/KStest.py')
execfile('/home/rumbaugh/RandFromHist.py')


targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])#,"cl1324_north","cl1324_south"])


indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

crn=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.3.4.16.dat',dtype=indict)
g1324=np.where((crn['field']=='cl1324_north')|(crn['field']=='cl1324_south'))[0]
crn['field'][g1324]='cl1324'

crxall=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.3.15.16.dat',dtype=indict)

allz4hist=crxall['redshift'][((crxall['lum_full']>0)&(crxall['redshift']>=0.65))]
lums4hist=np.log10(crxall['lum_full'][((crxall['lum_full']>0)&(crxall['redshift']>=0.65))])
