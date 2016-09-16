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

names = np.array(['NEP5281','RXJ1757','Cl1324','Cl1324'])
bounds = np.array([100,100,83,67])

cnt = -1

annuli = np.arange(bins)
annuli = 5 + annuli*6
counts = np.zeros((4,bins))

bgmaxR = annuli[bins-1]
bgminR = annuli[bins-7]

if FC != 0: FILE = open("/home/rumbaugh/LFC/DEcenters.dat","w")
if FC == 0:
    crFC = read_file("/home/rumbaugh/LFC/DEcenters.dat")
    cens = get_colvals(crFC,'col1')

for i in names:
    cnt += 1
    convfile = "conv.beta.12.15.10.fits"
    if cnt == 3: convfile = "conv.beta.12.15.10_2.fits"
    if FC != 0:
        ostemp = os.system("dmstat /scratch/rumbaugh/ciaotesting/" + i + "/master/" + convfile + " verbose=0")
        ostemp = os.system("pget dmstat out_max_loc > temptemp.txt")
        crcen = read_file("temptemp.txt")
        coltemp = get_colvals(crcen,'col1')
        cen = coltemp[0]
        FILE.write(cen)
    if FC == 0: cen = cens[cnt]
    load_data("/scratch/rumbaugh/ciaotesting/" + i + "/master/" + convfile)
    set_coord("physical")
    for r in range(0,bins):
        counts[cnt,r] = calc_data_sum2d('circle(%s,%f)'%(str(cen),annuli[r]))
        #print counts[cnt,r]
if FC != 0: FILE.close()
ncnts = np.zeros((4,bins))
for i in range(0,4):
    bg = (counts[i,len(annuli)-1]-counts[i,len(annuli)-7])/(m.pi*(annuli[len(annuli)-1]*annuli[len(annuli)-1]-annuli[len(annuli)-7]*annuli[len(annuli)-7]))
    for r in range(0,bins):
        ncnts[i,r] = counts[i,r] - bg*m.pi*annuli[r]*annuli[r]
        #print ncnts[i,r]
    print counts[i,bounds[i]] - bg*m.pi*annuli[bounds[i]]*annuli[bounds[i]]
FILE = open("/home/rumbaugh/LFC/diffuseemission.4.5.11.dat","w")
for r in range(0,bins):
    FILE.write('%4.1f %4.1f %4.1f %4.1f %4.1f %4.1f %4.1f %4.1f\n'%(ncnts[0,r],counts[0,r],ncnts[1,r],counts[1,r],ncnts[2,r],counts[2,r],ncnts[3,r],counts[3,r]))

FILE.close()
