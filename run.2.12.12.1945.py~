import os
import sys
import numpy as np
import random as rand
import math as m
import time

cr = read_file("/local3/rumbaugh/ChandraData/4936/opt_match/opt_Xray_matched_catalog_3high.twk.dat")
cr2 = read_file("/local3/rumbaugh/ChandraData/4936/opt_match/opt_Xray_matched_catalog_3high.twk.dat.minsrch.dat")

FILE=open("/local3/rumbaugh/ChandraData/4936/opt_match/regions/discrepant_sources.reg","w")
for i in range(0,1):
    ID = copy_colvals(cr,'col1')
    raX = copy_colvals(cr,'col2')
    decX = copy_colvals(cr,'col3')
    errX = copy_colvals(cr,'col4')
    nm = copy_colvals(cr,'col5')
    raopt1 = copy_colvals(cr,'col6')
    decopt1 = copy_colvals(cr,'col7')
    idopt1 = copy_colvals(cr,'col8')
    raopt2 = copy_colvals(cr,'col11')
    decopt2 = copy_colvals(cr,'col12')
    idopt2 = copy_colvals(cr,'col13')
    raopt3 = copy_colvals(cr,'col16')
    decopt3 = copy_colvals(cr,'col17')
    idopt3 = copy_colvals(cr,'col18')
    sigmax = copy_colvals(cr,'col23')
    prob1 = copy_colvals(cr,'col9')
    prob2 = copy_colvals(cr,'col14')
    prob3 = copy_colvals(cr,'col19')
    raX2 = copy_colvals(cr2,'col2')
    decX2 = copy_colvals(cr2,'col3')
    nm2 = copy_colvals(cr2,'col5')
    raopt12 = copy_colvals(cr2,'col6')
    decopt12 = copy_colvals(cr2,'col7')
    idopt12 = copy_colvals(cr2,'col8')
    raopt22 = copy_colvals(cr2,'col11')
    decopt22 = copy_colvals(cr2,'col12')
    idopt22 = copy_colvals(cr2,'col13')
    raopt32 = copy_colvals(cr2,'col16')
    decopt32 = copy_colvals(cr2,'col17')
    idopt32 = copy_colvals(cr2,'col18')
    prob12 = copy_colvals(cr2,'col9')
    prob22 = copy_colvals(cr2,'col14')
    prob32 = copy_colvals(cr2,'col19')
g = np.where(nm-nm2 != 0)
g = g[0]
FILE.write('global color=green dashlist=8 3 width=1 font="helvetica 10 normal" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
for i in range(0,len(g)):
    FILE.write('circle(%f,%f,%f") # color=green\n# text(%f,%f) text={%i}\n'%(raX[g[i]],decX[g[i]],errX[g[i]],raX[g[i]],decX[g[i]],ID[g[i]]))
    if nm[g[i]] > 0.1: FILE.write('circle(%f,%f,3.0") # color=cyan\n# text(%f,%f) text={%i}\n'%(raopt1[g[i]],decopt1[g[i]],raopt1[g[i]],decopt1[g[i]],idopt1[g[i]]))
    if nm[g[i]] > 1.1: FILE.write('circle(%f,%f,3.0") # color=yellow\n# text(%f,%f) text={%i}\n'%(raopt2[g[i]],decopt2[g[i]],raopt2[g[i]],decopt2[g[i]],idopt2[g[i]]))
    if nm[g[i]] > 2.1: FILE.write('circle(%f,%f,3.0") # color=blue\n# text(%f,%f) text={%i}\n'%(raopt3[g[i]],decopt3[g[i]],raopt3[g[i]],decopt3[g[i]],idopt3[g[i]]))
    if nm2[g[i]] > 0.1: FILE.write('circle(%f,%f,3.3") # color=red\n# text(%f,%f) text={%i}\n'%(raopt12[g[i]],decopt12[g[i]],raopt12[g[i]],decopt12[g[i]],idopt12[g[i]]))
    if nm2[g[i]] > 1.1: FILE.write('circle(%f,%f,3.3") # color=orange\n# text(%f,%f) text={%i}\n'%(raopt22[g[i]],decopt22[g[i]],raopt22[g[i]],decopt22[g[i]],idopt22[g[i]]))
    if nm2[g[i]] > 2.1: FILE.write('circle(%f,%f,3.3") # color=purple\n# text(%f,%f) text={%i}\n'%(raopt32[g[i]],decopt32[g[i]],raopt32[g[i]],decopt32[g[i]],idopt32[g[i]]))
FILE.close()
