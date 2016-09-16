import numpy as np

try:
    lens
except NameError:
    lens = '1131'

try:
    circrad
except NameError:
    circrad = 2.

try:
    xoff
except NameError:
    xoff = 0.

try:
    yoff
except NameError:
    yoff = 0.

date = '2.18.14'

cr = np.loadtxt('/home/rumbaugh/%s_master.tab'%lens,dtype='string')

FILE = open('/home/rumbaugh/LRIS_redshift_results.%s.%s.reg'%(lens,date),'w')
FILE.write('# Region file format: DS9 version 4.0\nglobal color=green font="helvetica 10 normal" select=1 highlite=1 edit=1 move=1 delete=1 include=1 fixed=0 source\nfk5\n')
if lens == '0435':
    yoff=0
    xoff=-4./60./60.
for row in range(0,np.shape(cr)[0]):
    if ((float(cr[row][3]) < 90) & (float(cr[row][3]) >= 0)):
        FILE.write('circle(%f,%f,%f") #color=red\n'%(float(cr[row][1]),float(cr[row][2]),circrad))
        #FILE.write('text(%f,%f) color=red font="helvetica 10 bold" text={%s - z = %5.3f}\n'%(float(cr[row][1]),float(cr[row][2]),cr[row][0],float(cr[row][3])))
        #FILE.write('# text(%f,%f) color=red text={%s - z = %5.3f}\n'%(float(cr[row][1])+xoff,float(cr[row][2])+yoff,cr[row][0],float(cr[row][3])))
        FILE.write('# text(%f,%f) color=red text={z = %5.3f}\n'%(float(cr[row][1])+xoff,float(cr[row][2])+yoff,float(cr[row][3])))
FILE.close()
