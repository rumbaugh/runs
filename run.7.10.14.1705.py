import numpy as np
import matplotlib.pylab as plt

ldate = '7.10.14'

cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/TimeBombs/output/results.testlightcurves.%s.dat'%ldate)
for i in range(0,np.shape(cr)[0]):
    pair,tau,mu = cr[:,0][i],cr[:,1][i],cr[:,2][i]

