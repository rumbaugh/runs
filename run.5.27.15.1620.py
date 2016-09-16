date = '5.27.15'
import numpy as np
import pyfits as py
hdu = py.open('/home/rumbaugh/Fermi/data/0218/S30218+35_86400.lc')
d = hdu[1].data
ltime = (d['START']-d['START'][0])/86400
g = np.where((ltime > 350) & (ltime < 525))[0]
Sfull = d['FLUX_100_300000']
Sfullerr = d['ERROR_100_300000']

FILE = open('/home/rumbaugh/Fermi/data/0218/0218_TimeBombsInput_werr.dat','w')
#for i in range(0,len(Sfull)):
for i in g:
    FILE.write('%E %E %E\n'%(ltime[i],Sfull[i]*100000000,Sfullerr[i]*100000000))
FILE.close()
