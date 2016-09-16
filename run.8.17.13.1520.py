import numpy as np
import os
os.chdir("/mnt/data2/rumbaugh/dump/ChandraData/0910/master")
FILE = open('other1.reg','w')
FILE.write("# Region file format: CIAO version 1.0\n")
cr = np.loadtxt("/mnt/data2/rumbaugh/dump/ChandraData/photometry_files/Cl0910.radec_sig_xerr.mod.dat")
for i in range(0,len(cr[:,0])):
    FILE.write('circle(%f,%f,20") # color = red\n'%(cr[i][0],cr[i][1]))
FILE.close()
