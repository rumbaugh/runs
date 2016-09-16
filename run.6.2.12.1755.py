import numpy as np
import math as m
import time
import sys
import matplotlib
import matplotlib.pylab as pylab

pfile = '/home/rumbaugh/LFC/sc1322.lfc.newIDsandoldIds.radecmag.cat'
sfile= '/home/rumbaugh/FINAL.cl1322.lrisplusdeimos.cat'

cr = read_file(pfile)
crs = read_file(sfile)

RA = copy_colvals(cr,'col3')
Dec = copy_colvals(cr,'col4')
sRA = copy_colvals(crs,'col4')
sDec = copy_colvals(crs,'col5')
sz = copy_colvals(crs,'col9')
sq = copy_colvals(crs,'col11')

FILE = open('/home/rumbaugh/Cl1324+3013.companion.anal.reg','w')

FILE.write('global color=green font="helvetica 10 normal" select=1 highlite=1 edit=1 move=1 delete=1 include=1 fixed=0 width=2 source\nfk5\n')
for i in range(0,len(RA)):
    FILE.write('circle(%f,%f,0.8") # color=cyan\n'%(RA[i],Dec[i]))
g = np.where((sq < 0.2) | (sq > 1.2))
g = g[0]
for i in range(0,len(g)):
    FILE.write('circle(%f,%f,3") # color=magenta\n'%(sRA[g[i]],sDec[g[i]]))
FILE.close()
