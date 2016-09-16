import drizzlepac
from drizzlepac import astrodrizzle
import os
import sys
import numpy as np

execfile('/mnt/data2/rumbaugh/HST/scripts/matt_astrodrizzle_script.py')
indir = '/mnt/data2/rumbaugh/HST/10886/raw'
outdir = '/mnt/data2/rumbaugh/HST/10886/drizzled'
os.chdir('/mnt/data2/rumbaugh/HST/10886/raw')

os.system('rm -f temp.dat')
os.system('ls HST*flc.fits > temp.dat')
fcr = np.loadtxt('temp.dat',dtype='str')
targets = np.array([])
file_dict = {}
prevtarg = None
date = '10.16.13'
for infile in fcr:
    ttarg = infile[4:18]
    if ttarg not in targets: 
        if prevtarg != None:
            file_dict[prevtarg] = t_file_arr
        targets = np.append(targets,ttarg)
        t_file_arr = np.array([])
    t_file_arr = np.append(t_file_arr,infile)
    prevtarg = ttarg


try:
    pf
except NameError:
    pf = 1.0
try:
    fs
except NameError:
    fs = 0.03
try:
    fk
except NameError:
    fk = 'lanczos3'

for target in targets:
    band = 'CLEAR1L_F814W'
    insearch = 'HST.%s.*flc.fits'%target
    outroot = 'ADrizOut.HST.%s_%s.pf_%4.2f.fs_%5.3f.%s'%(target,band,pf,fs,date)
    #astrodrizzle.AstroDrizzle('%s'%(insearch),output='%s'%(outroot),final_scale=fs,final_pixfrac=pf)
    #os.system('mv test.ADriz* %s/.'%outdir)
    matt_astrodrizzle(indir,outdir,outroot,insearch=insearch,doCTE=False,fscale=fs,pixfrac=pf,finalkernel=fk)
