import numpy as np
import os
from pyds9 import *
execfile("/home/rumbaugh/check_opt_match.py")

dum=os.system('ds9 &')

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])

for field in targets:

    basedir='/home/rumbaugh//Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)

    fitsfile='%s/%s_full.img'%(basedir,field)
    srcfile='%s/%s_optmatch.1.19.16.dat'%(basedir,field)
    srcfile2='%s/%s_optmatch.1.19.16_min5.dat'%(basedir,field)
    regfile='%s/%s_optmatch.1.19.16.reg'%(basedir,field)
    regfile2='%s/%s_optmatch.1.19.16_min5.reg'%(basedir,field)
    outfile='%s/%s_optmatch_comb.1.19.16.dat'%(basedir,field)
    outregfile='%s/%s_optmatch_comb.1.19.16.reg'%(basedir,field)
    optfile='/home/rumbaugh/Chandra/optimages/%s_I.fits'%field
    if field=='cl1604': optfile=np.array(['/home/rumbaugh/Chandra/optimages/%s_1_I.fits'%field,'/home/rumbaugh/Chandra/optimages/%s_2_I.fits'%field])

    sourcefiles=np.array([srcfile,srcfile2])
    regfiles=np.array([regfile,regfile2])

    check_opt_match(fitsfile,sourcefiles,regfiles,optfile,outfile,outregfile,srcfilenames=['Default','min5'],startds9=False)
