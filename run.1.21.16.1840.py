import numpy as np
import os
from pyds9 import *
execfile("/home/rumbaugh/check_opt_match.py")

dum=os.system('ds9 &')

field='cl0023'

basedir='/home/rumbaugh//Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)

fitsfile='%s/%s_full.img'%(basedir,field)
srcfile='%s/%s_optmatch.1.19.16.dat'%(basedir,field)
srcfile2='%s/%s_optmatch.1.19.16_min5.dat'%(basedir,field)
regfile='%s/%s_optmatch.1.19.16.reg'%(basedir,field)
regfile2='%s/%s_optmatch.1.19.16_min5.reg'%(basedir,field)
outfile='%s/testout.dat'%basedir
outregfile='%s/testout.reg'%basedir
optfile='/home/rumbaugh/Chandra/optimages/%s_i_shift_norm.fits'%field

sourcefiles=np.array([srcfile,srcfile2])
regfiles=np.array([regfile,regfile2])

check_opt_match(fitsfile,sourcefiles,regfiles,optfile,outfile,outregfile,srcfilenames=['Default','min5'],startds9=False)
