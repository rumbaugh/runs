date = '9.21.15'
import numpy as np
import pyfits as py
hdu = py.open('/home/rumbaugh/Fermi/data/0218/S30218+35_86400.lc')
d = hdu[1].data
ltime = (d['START']-d['START'][0])/86400
g = np.where((ltime > 350) & (ltime < 525))[0]
Sfull = d['FLUX_100_300000']
Sfullerr = d['ERROR_100_300000']

Shard = d['FLUX_1000_300000']
Sharderr = d['ERROR_1000_300000']
Ssoft = d['FLUX_300_1000']
Ssofterr = d['ERROR_300_1000']

FILEs = open('/home/rumbaugh/Fermi/data/0218/0218_TimeBombsInput_soft.dat','w')
FILEh = open('/home/rumbaugh/Fermi/data/0218/0218_TimeBombsInput_hard.dat','w')
#for i in range(0,len(Sfull)):
for i in g:
    FILEs.write('%E %E %E\n'%(ltime[i],Ssoft[i]*100000000,Ssofterr[i]*100000000))
    FILEh.write('%E %E %E\n'%(ltime[i],Shard[i]*100000000,Sharderr[i]*100000000))
FILEs.close()
FILEh.close()
