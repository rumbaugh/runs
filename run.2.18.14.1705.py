import numpy as np


date = '2.18.14'

FILE = open('LRIS_redshift_summary.%s.dat'%date,'w')

for lens in ['1131','0435']:
    cr = np.loadtxt('/home/rumbaugh/%s_master.tab'%lens,dtype='string')
    for row in range(0,np.shape(cr)[0]):
        if float(cr[row][3]) < 90:
            FILE.write('%4s %s %5.3f\n'%(lens,cr[row][np.shape(cr)[1]-1],float(cr[row][3])))
FILE.close()
