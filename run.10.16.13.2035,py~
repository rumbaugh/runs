import pyfits as pf
import numpy as np
import os
import sys

os.chdir('/mnt/data2/rumbaugh/HST/10886/raw')
os.system('rm -f temp.dat')
os.system('ls j*flc.fits > temp.dat')
fcr = np.loadtxt('temp.dat',dtype='str')
for infile in fcr:
    print infile
    targ,time,date = pf.getval(infile,'TARGNAME'),pf.getval(infile,'TIME-OBS'),pf.getval(infile,'DATE-OBS')
    outfile = '/mnt/data2/rumbaugh/HST/10886/raw/HST.%s.%s.%s_flc.fits'%(targ,date,time.replace(':','')[:4])
    os.system('ln -s %s %s'%(infile,outfile))
