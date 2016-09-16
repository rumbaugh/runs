import numpy as np
import os
import sys

import drizzlepac
from drizzlepac import astrodrizzle

date = '10.9.13'
try:
    fs
except NameError:
    fs = 0.03

try:
    pf
except NameError:
    pf = 0.6

os.chdir('/mnt/data2/rumbaugh/HST/12898/raw')
os.system('rm -f temp.dat')
os.system('ls HST*_flt.fits > temp.dat')
fcr = np.loadtxt('temp.dat',dtype='str')
targets = np.array([])
file_dict = {}
prevtarg = None
for infile in fcr:
    ttarg = infile[4:28]
    if ttarg not in targets: 
        if prevtarg != None:
            file_dict[prevtarg] = t_file_arr
        targets = np.append(targets,ttarg)
        t_file_arr = np.array([])
    t_file_arr = np.append(t_file_arr,infile)
    prevtarg = ttarg
for target,i in zip(targets,np.arange(len(targets))):
    if i > len(targets)-5:
        iraf.unlearn('astrodrizzle')
        astrodrizzle.AstroDrizzle('HST.%s.*_flt.fits'%target,output='../drizzled/ADrizOut.HST.%s.pf_%4.2f.fs_%5.3f.%s'%(target,pf,fs,date),final_scale=fs,final_pixfrac=pf)
