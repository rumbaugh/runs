import numpy as np
import pyfits as py
import os

os.chdir('/mnt/data2/rumbaugh/Fermi/data/MSL_LC')
cr = py.open('3C66A_604800.lc')
d = cr[1]
d1 = d.data['FLUX_300_1000']
plt.clf()
plt.scatter(np.arange(len(d1[d1>0])),d1[d1>0])
plt.ylim(0,1.5E-7)

