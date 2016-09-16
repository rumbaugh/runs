import numpy as np
import pyfits as py
import os

for pid in [10494,10886,12898]:
    os.chdir('/home/rumbaugh/HST/%i/drizzled'%pid)
    print pid
    scifiles=np.loadtxt('scifiles.lst',dtype='string')
    for curfile in scifiles:
        print curfile
        hdr=py.getheader(curfile)
        print hdr['EXPTIME']
        print '\n'
