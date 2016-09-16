import drizzlepac
from drizzlepac import astrodrizzle
import os
import sys
import numpy as np

execfile('/mnt/data2/rumbaugh/HST/scripts/matt_astrodrizzle_script.py')
indir = '/mnt/data2/rumbaugh/HST/12898/raw'
outdir = '/mnt/data2/rumbaugh/HST/12898/drizzled'

targets = ['SDSS-J095944.07+041017.0']
targets = ['SDSS-J091205.31+002901.1']
targets = ['SDSS-J073728.44+321618.6']
date = '10.14.13'

try:
    pf
except NameError:
    pf = 0.9
try:
    fs
except NameError:
    fs = 0.03
try:
    fk
except NameError:
    fk = 'lanczos3'

for target in targets:
    insearch = 'HST.%s.*flt.fits'%target
    outroot = 'test.ADrizOut.HST.%s.pf_%4.2f.fs_%5.3f.%s'%(target,pf,fs,date)
    os.chdir(outdir)
    iraf.unlearn('astrodrizzle')
    astrodrizzle.AstroDrizzle('%s/%s'%(indir,insearch),output='%s/%s'%(outdir,outroot),final_scale=fs,final_pixfrac=pf)
    #matt_astrodrizzle(indir,outdir,outroot,insearch=insearch,doCTE=False,fscale=fs,pixfrac=pf,finalkernel=fk,dotest=True)
