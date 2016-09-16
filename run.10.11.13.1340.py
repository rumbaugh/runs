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

os.chdir('/mnt/data2/rumbaugh/HST/10494/raw')
os.system('rm -f temp.dat')
os.system('ls HST*_flc.fits > temp.dat')
fcr = np.loadtxt('temp.dat',dtype='str')
targets = np.array([])
bands = np.array([])
file_dict = {}
prevtarg = None
prevband = None
for infile in fcr:
    ttarg = infile[4:22]
    band = infile[39:52]
    if ttarg not in targets: 
        if prevtarg != None:
            file_dict[prevtarg] = t_file_arr
        targets = np.append(targets,ttarg)
        t_file_arr = np.array([])
    if band not in bands: 
        if prevband != None:
            file_dict[band] = t_file_arr
        bands = np.append(bands,band)
        t_file_arr = np.array([])
    t_file_arr = np.append(t_file_arr,infile)
    prevtarg = ttarg
    prevband = band
for band,i in zip(bands,np.arange(len(bands))):
    target = targets[0]
    #if i > len(bands)-5:
    iraf.unlearn('astrodrizzle')
    astrodrizzle.AstroDrizzle('HST.%s.*%s*_flc.fits'%(target,band),output='../drizzled/ADrizOut.HST.%s_%s.pf_%4.2f.fs_%5.3f.%s'%(target,band,pf,fs,date),final_scale=fs,final_pixfrac=pf)
