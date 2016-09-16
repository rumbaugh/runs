import math as m
import numpy as np

for i in range(1,99):
    cr = read_file("/home/rumbaugh/COSMOS/analysis/test.spat.error.1.16.11.2100_" + str(i) + ".dat")
    ra = get_colvals(cr,'col1')
    dec = get_colvals(cr,'col2')
    FILE = open("/home/rumbaugh/COSMOS/analysis/test.spat.error.1.17.11.1400_" + str(i) + ".dat","w")
    for j in range(0,len(ra)): 
        dist = m.sqrt((ra[j]-512)**2 + (dec[j]-512)**2)
        FILE.write('%4i %4i %10.6f\n'%(ra[j],dec[j],dist))
    FILE.close()
