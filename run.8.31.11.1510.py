cenx = [4656.28,4009.28]
ceny = [3974.77,4359.77]
import numpy as np
import matplotlib.pylab as pylab
radii = np.arange(20)*15.0+10

load_data("/home/rumbaugh/ChandraData/0910/master/acis2227+2452.img.500-2000.nops.fits")
set_coord("physical")
for i in range(0,2):
    cnts = np.zeros(20)
    SB = np.zeros(20)
    for j in range(0,len(radii)):
        if j == 0: 
            cnts[0] = calc_data_sum2d("circle(%f,%f,%f)"%(cenx[i],ceny[i],radii[j]))
            SB[0] = cnts[0]/(radii[0]*radii[0])
        if j != 0: 
            cnts[j] = calc_data_sum2d("circle(%f,%f,%f)"%(cenx[i],ceny[i],radii[j])) - calc_data_sum2d("circle(%f,%f,%f)"%(cenx[i],ceny[i],radii[j-1]))
            SB[j] = cnts[j]/(radii[j]*radii[j]-radii[j-1]*radii[j-1])
    pylab.scatter(radii,SB)
    pylab.savefig("/home/rumbaugh/ChandraData/0910/master/SBplot.%f_%f.png"%(cenx[i],ceny[i]))
    pylab.close('all')
