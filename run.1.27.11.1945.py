import numpy as np
import math as m

names = np.array(['5603'])

try:
    conflvl
except NameError:
    conflvl = 0.95

FILE=open('/home/rumbaugh/COSMOS/analysis/FPerroranal/conf.lims.%4.2f.dat'%(conflvl),'a')
for i in range(0,len(names)):
    dists = []
    for j in range(1,11):
        cr = read_file('/home/rumbaugh/COSMOS/analysis/FPerroranal/%s/test.spat.error.1.25.11_%i.dat'%(names[i],j))
        xposT = get_colvals(cr,'col1')
        yposT = get_colvals(cr,'col2')
        distT = ((xposT-512)**2+(yposT-512)**2)**0.5
        dists = np.append(dists,distT)
    distSort = np.sort(dists)
    lim = distSort[int(conflvl*len(dists))]
    FILE.write('%5s %5.3f %f\n'%(names[i],conflvl,lim))
    print '%5s - %2i percent confidence limit - %6.2f'%(names[i],int(conflvl*100),lim)
FILE.close()
