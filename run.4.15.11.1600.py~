import numpy as np
import math as m
import time
import sys
import os

try:
    FC
except NameError:
    FC = 0
try:
    bins
except NameError:
    bins = 60 

names = np.array(['NEP5281','RXJ1757','Cl1324','Cl1324','Cl1324'])
names2 = np.array(['acis10444+10924','RXJ1757','acis9403+9840','acis9404+9836'])
bounds = np.array([100,100,83,67,100])
annmult = np.array([1.0,1.0,2.0,1.5,1.5])

cnt = -1

annulitemp = np.arange(bins)
annulitemp = 10 + annulitemp*10
counts = np.zeros((5,bins))

bgmaxR = annulitemp[bins-1]
bgminR = annulitemp[bins-7]

if FC != 0: FILE = open("/home/rumbaugh/LFC/DEcenters.dat","w")
if FC == 0:
    crFC = read_file("/home/rumbaugh/LFC/DEcenters.dat")
    cens = get_colvals(crFC,'col1')

for i in names:
    cnt += 1
    cntfile = "/home/rumbaugh/ChandraData/" + i + "/master/" + names2[cnt] + ".img.500-2000.nops.fits"
    convfile = "conv.beta.12.15.10.fits"
    if cnt == 3: convfile = "conv.beta.12.15.10_2.fits"
    if FC != 0:
        print 'FC != 0'
        ostemp = os.system("dmstat /scratch/rumbaugh/ciaotesting/" + i + "/master/" + convfile + " verbose=0")
        ostemp = os.system("pget dmstat out_max_loc > temptemp.txt")
        crcen = read_file("temptemp.txt")
        coltemp = get_colvals(crcen,'col1')
        cen = coltemp[0]
        FILE.write(cen)
    if FC == 0: cen = cens[cnt]
    annuli = annmult[cnt]*annulitemp
    #load_data("/scratch/rumbaugh/ciaotesting/" + i + "/master/" + !!convfile)
    load_data(cntfile)
    set_coord("physical")
    for r in range(0,bins):
        counts[cnt,r] = calc_data_sum2d('circle(%s,%f)'%(str(cen),annuli[r]))
        #print counts[cnt,r]
xcen,ycen = 2071.7567,978.87219
for r in range(0,bins):
    counts[4,r] = calc_data_sum2d('circle(%f,%f,%f)'%(xcen,ycen,annuli[r]))

if FC != 0: FILE.close()
ncnts = np.zeros((5,bins))
for i in range(0,5):
    bg = (counts[i,len(annuli)-1]-counts[i,len(annuli)-7])/(m.pi*(annuli[len(annuli)-1]*annuli[len(annuli)-1]-annuli[len(annuli)-7]*annuli[len(annuli)-7]))
    for r in range(0,bins):
        ncnts[i,r] = counts[i,r] - bg*m.pi*annuli[r]*annuli[r]
        #print ncnts[i,r]
    #print counts[i,bounds[i]] - bg*m.pi*annuli[bounds[i]]*annuli[bounds[i]]
FILE = open("/home/rumbaugh/LFC/diffuseemission.4.19.11.dat","w")
for r in range(0,bins):
    FILE.write('%4.1f %4.1f %4.1f %4.1f %4.1f %4.1f %4.1f %4.1f %4.1f %4.1f\n'%(ncnts[0,r],counts[0,r],ncnts[1,r],counts[1,r],ncnts[2,r],counts[2,r],ncnts[3,r],counts[3,r],ncnts[4,r],counts[4,r]))

FILE.close()
