import drizzlepac
from drizzlepac import astrodrizzle
import os
import sys
import numpy as np

execfile('/mnt/data2/rumbaugh/HST/scripts/matt_astrodrizzle_script.py')
indir = '/mnt/data2/rumbaugh/HST/10494/raw'
outdir = '/mnt/data2/rumbaugh/HST/10494/drizzled'

targets = ['SDSS-J095944.07+041017.0']
#targets = ['SDSS-J091205.31+002901.1']
#targets = ['SDSS-J073728.44+321618.6']
targets = ['GAL-0572-52289-495']
date = '10.15.13'

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
    raw = 'HST.%s.*raw.fits'%target
    insearch = 'HST.%s.*flc.fits'%target
    outroot = 'ADrizOut.HST.%s.pf_%4.2f.fs_%5.3f.%s'%(target,pf,fs,date)
    #astrodrizzle.AstroDrizzle('%s'%(insearch),output='%s'%(outroot),final_scale=fs,final_pixfrac=pf)
    #os.system('mv test.ADriz* %s/.'%outdir)
    matt_astrodrizzle(indir,outdir,outroot,insearch=insearch,doCTE=True,fscale=fs,pixfrac=pf,finalkernel=fk,raw=raw)
