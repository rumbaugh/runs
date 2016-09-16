import numpy as np
import os
import sys

import drizzlepac
from drizzlepac import astrodrizzle

date = '7.16.14'
try:
    fs
except NameError:
    fs = 0.03

try:
    pf
except NameError:
    pf = 0.6

os.chdir('/mnt/data2/rumbaugh/HST/HS0810/data')
os.system('rm -f temp.dat')
os.system('ls *_flt.fits > temp.dat')
fcr = np.loadtxt('temp.dat',dtype='str')
targets = np.array([])
file_dict = {}
prevtarg = None
#for infile in fcr:
#    ttarg = infile[:9]
#    if ttarg not in targets: 
#        if prevtarg != None:
#            file_dict[prevtarg] = t_file_arr
#        targets = np.append(targets,ttarg)
#        t_file_arr = np.array([])
#    t_file_arr = np.append(t_file_arr,infile)
#    prevtarg = ttarg
#for target in targets:
iraf.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle('j8oi24p[l-z]q_flt.fits',output='ADrizOut.HS0218_F814W.pf_%4.2f.fs_%5.3f.%s'%(pf,fs,date),final_scale=fs,final_pixfrac=pf)

iraf.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle('j8oi24p[6-e]q_flt.fits',output='ADrizOut.HS0218_F555W.pf_%4.2f.fs_%5.3f.%s'%(pf,fs,date),final_scale=fs,final_pixfrac=pf)
