import os
import numpy as np
import math as m
import matplotlib
import matplotlib.pylab as pylab

names = np.array(['RXJ1757','acis10444+10924','acis9403+9840','acis9404+9836'])
paths = np.array(['/scratch/rumbaugh/ciaotesting/RXJ1757/master','/scratch/rumbaugh/ciaotesting/NEP5281/master','/scratch/rumbaugh/ciaotesting/Cl1324/master','/scratch/rumbaugh/ciaotesting/Cl1324/master'])
zz = np.array(['RXJ1757','10444+10924','9403+9840','9404+9836'])
pbk = np.array(['acis11999','acis10444','acis9840','../9836/acis9836'])
full = np.array(['full','full','full','full_2'])
bnds = np.array([300,300,250,200])
temps = np.array([1,1,1.8,0.9])

path = '/home/rumbaugh/ChandraData/'
pathspec = np.array(['NEP5281/10444+10924/spec','RXJ1757/master/spec','Cl1324/master/spec','Cl1324/master/spec'])
fields = np.array(['NEP5281','RXJ1757','Cl1324','Cl1324'])
namespec = np.array(['10444+10924','RXJ1757','9403+9840','9404+9836'])
nharr = np.array([0.0566,0.0407,0.0115,0.0115])
z = np.array([0.82,0.69,0.76,0.76])
times = np.array([50000,50000,48391.890220549,50399.00069391])


nh = 0.0115
temp2 = ''
cen2 = '4584.3139,3388.91'
cen1 = '4631.314,3641'
bgcen = '4346.314,3644.9'
for i in range(3,4):
    load_data('%s/%s.img.500-2000.nops.fits'%(paths[i],names[i]))
    set_coord("physical")
    ann = np.arange(51)*8+5
    cnts = np.zeros(51)
    cnts[0] = calc_data_sum2d('circle(%s,%i)'%(cen1,ann[0]))/(m.pi*(ann[0]**2))
    for r in range(0,51):
        cnts[r] = calc_data_sum2d('circle(%s,%i)-circle(%s,%i)'%(cen1,ann[r],cen1,ann[r-1]))/(m.pi*(ann[r]**2-ann[r-1]**2))
    pylab.scatter(ann,cnts)
    pylab.savefig("test.png")
    pylab.close('all')
