import pyfits as pf
import numpy as np
import os
import sys

os.chdir('/mnt/data2/rumbaugh/HST/12898/raw')
os.system('rm -f temp.dat')
os.system('ls i*flt.fits > temp.dat')
fcr = np.loadtxt('temp.dat',dtype='str')
for infile in fcr:
    print infile
    targ,time,date = pf.getval(infile,'TARGNAME'),pf.getval(infile,'TIME-OBS'),pf.getval(infile,'DATE-OBS')
    outfile = '/mnt/data2/rumbaugh/HST/12898/raw/HST.%s.%s.%s_flt.fits'%(targ,date,time.replace(':','')[:4])
    os.system('ln -s %s %s'%(infile,outfile))
