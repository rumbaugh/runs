import numpy as np
import pyfits as py
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])
zlist=np.array([0.77,1.26,1.11,0.70,0.80,0.69,0.90,0.84,0.76,0.82,0.96,0.81,1.14,0.76,0.76])

for field,z in zip(targets,zlist):
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    for band in ['soft','hard','full']:
        smthfile='%s/%s_%s_nops.smoothed.z_%.2f.beta_0.67.rc_180kpc.img'%(curdir,field,band,z)
        smtherrfile='%s/%s_%s_nops.smoothed_sqrd.z_%.2f.beta_0.67.rc_180kpc.img'%(curdir,field,band,z)
        hdu=py.open(smtherrfile)
        hdu[0].data=np.sqrt(hdu[0].data)
        hdu.writeto('%s/%s_%s_nops.smoothed_err.z_%.2f.beta_0.67.rc_180kpc.img'%(curdir,field,band,z))
