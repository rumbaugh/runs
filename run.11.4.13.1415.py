import drizzlepac
from drizzlepac import astrodrizzle
import os
import sys
import numpy as np

execfile('/mnt/data2/rumbaugh/HST/scripts/matt_astrodrizzle_script.py')
indir = '/mnt/data2/rumbaugh/HST/10494/raw'
outdir = '/mnt/data2/rumbaugh/HST/10494/drizzled'

targets = ['SDSS-J091205.31+002901.1']
targets = ['GAL-0472-51955-429']
date = '11.4.13'

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
    insearch = 'HST.%s*11-05*flc.fits'%target
    outroot = 'ADrizOut.HST.%s.pf_%4.2f.fs_%5.3f.%s'%(target,pf,fs,date)
    os.chdir(indir)
    iraf.unlearn('astrodrizzle')
    astrodrizzle.AstroDrizzle('%s'%(insearch),output='%s'%(outroot),final_scale=fs,final_pixfrac=pf)
    os.system('mv ADriz* %s/.'%outdir)
    #matt_astrodrizzle(indir,outdir,outroot,insearch=insearch,doCTE=False,fscale=fs,pixfrac=pf,finalkernel=fk,dotest=True)
