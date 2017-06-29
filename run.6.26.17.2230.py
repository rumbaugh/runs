import numpy as np
execfile('/home/rumbaugh/angconvert.py')

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clus_rad.dat',dtype={'names':('field','cluster','rad','RA','Dec'),'formats':('|S24','|S24','f8','f8','f8')},usecols=(0,1,2,3,4))

FILE=open('/home/rumbaugh/Chandra/ORELSE.X-ray_centers_for_paper.dat','w')

FILE.write('# field cluster RA(deg) Dec(deg) RA(sex) Dec(sex)\n')
for i in range(0,len(cr['RA'])):
    rah,ram,ras=deg2hms(cr['RA'][i])
    decd,decm,decs=deg2dms(cr['Dec'][i])
    FILE.write('%12s %12s %9.5f %9.5f %02i %02i %04.1f %02i %02i %04.1f \n'%(cr['field'][i],cr['cluster'][i],cr['RA'][i],cr['Dec'][i],rah,ram,ras,decd,decm,decs))
FILE.close()
