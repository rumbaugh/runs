import numpy as np
import matplotlib as py

cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/TimeBombs/output/test.sample.testlightcurve_3.tau_7.22.mu_0.841.7.31.14.dat')

slen = 110

lc1 = cr[0][-slen:]
lct = cr[0][-2*slen:-slen]
lc2 = lct-lc1
mu = cr[0][2]


plot(lc1,color='red',lw=1)
plot(lc2,color='blue',lw=1)
