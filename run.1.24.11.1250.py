import numpy as np
import math as m
import sys
import os

path = '/scratch/rumbaugh/ciaotesting'

cr = read_file("/home/rumbaugh/COSMOS/lens_sample_id_z_exp_rc.dat")
ID = get_colvals(cr,'col1')
z = get_colvals(cr,'col2')
exp = get_colvals(cr,'col3')
rc = get_colvals(cr,'col4')
FILE=open('/home/rumbaugh/COSMOS/lens.analysis.1.24.11.dat','w')
for i in range(0,len(z)):
    ost = os.system('dmstat %s/%i/conv.beta.12.4.10.fits verbose=0'%(path,ID[i]))
    ost = os.system("pget dmstat out_max_loc | sed 's/,/ /g' | tee centemp.txt")
    crt = read_file("centemp.txt")
    t1 = get_colvals(crt,'col1')
    t1 = t1[0]
    t2 = get_colvals(crt,'col2')
    t2 = t2[0]
    FILE.write('%5i %4.2f %5.2f %5.2f %7.2f %7.2f'%(ID[i],z[i],exp[i],rc[i],t1,t2))
FILE.close()
