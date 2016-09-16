import numpy as np
import math as m

names = np.array(['8177','363','7757','367','5602','5604','3571','3460','4199','9515','10576','6249','7759','7761','5192','1644','1642','427','3461','5194','5794','4763','4807','1629','419','5193','8176','423','424','3572','3419'])

try:
    conflvl
except NameError:
    conflvl = 0.95

FILE=open('/home/rumbaugh/COSMOS/analysis/FPerroranal/conf.lims.%4.2f.dat'%(conflvl),'w')
for i in range(0,len(names)):
    dists = []
    for j in range(1,11):
        cr = read_file('/home/rumbaugh/COSMOS/analysis/FPerroranal/%s/test.spat.error.1.17.11.2315_%i.dat'%(names[i],j))
        xposT = get_colvals(cr,'col1')
        yposT = get_colvals(cr,'col2')
        distT = ((xposT-512)**2+(yposT-512)**2)**0.5
        dists = np.append(dists,distT)
    distSort = np.sort(dists)
    lim = distSort[int(conflvl*len(dists))]
    FILE.write('%5s %5.3f %f\n'%(names[i],conflvl,lim))
    print '%5s - %2i percent confidence limit - %6.2f'%(names[i],int(conflvl*100),lim)
FILE.close()
