import pyfits as pf
import numpy as np
import os
import sys

os.chdir('/mnt/data2/rumbaugh/HST/10494/raw')
os.system('rm -f temp.dat')
os.system('ls j*flc.fits > temp.dat')
fcr = np.loadtxt('temp.dat',dtype='str')
for infile in fcr:
    print infile
    targ,time,date = pf.getval(infile,'TARGNAME'),pf.getval(infile,'TIME-OBS'),pf.getval(infile,'DATE-OBS')
    filt1,filt2 = pf.getval(infile,'FILTER1'),pf.getval(infile,'FILTER2')
    outfile = '/mnt/data2/rumbaugh/HST/10494/raw/HST.%s.%s.%s_%s_%s_flc.fits'%(targ,date,time.replace(':','')[:4],filt1,filt2)
    os.system('ln -s %s %s'%(infile,outfile))
