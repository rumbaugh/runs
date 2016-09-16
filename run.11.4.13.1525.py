import pyfits as pf
import numpy as np
import os
import sys

os.chdir('/mnt/data2/rumbaugh/HST/10494/raw')
os.system('rm -f temp.dat')
os.system('ls j*flt.fits > temp.dat')
fcr = np.loadtxt('temp.dat',dtype='str')
for infile in fcr:
    print infile
    targ,time,date = pf.getval(infile,'TARGNAME'),pf.getval(infile,'TIME-OBS'),pf.getval(infile,'DATE-OBS')
    filt1,filt2 = pf.getval(infile,'FILTER1'),pf.getval(infile,'FILTER2')
    band = '%s_%s'%(filt1,filt2)
    outfile = '/mnt/data2/rumbaugh/HST/10494/raw/HST.%s_%s.%s.%s_flt.fits'%(targ,band,date,time.replace(':','')[:4])
    if targ == 'GAL-0472-51955-429': os.system('ln -s %s %s'%(infile,outfile))

