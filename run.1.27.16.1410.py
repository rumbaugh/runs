import numpy as np
import pyfits as py

color='red'

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

crc=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','ra','dec'),'formats':('|S24','|S24','f8','f8')})

testfield=np.copy(crc['field'])
for j in range(0,len(testfield)): 
    ftmp=testfield[j].split('_')
    testfield[j]=ftmp[0].lower()

for field in targets:
    ftmp=field.split('_')
    if ftmp[0] in testfield:
        FILE=open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_clusters.reg'%(field,field,field),'w')
        FILE.write('# Region file format: DS9 version 4.1\nglobal color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
        inds=np.arange(len(crc['field']))[testfield==ftmp[0]]
        for i in inds:
            FILE.write('point(%f,%f) # point=x color=%s width=4 text={%s}\n'%(crc['ra'][i],crc['dec'][i],color,crc['cluster'][i]))
        FILE.close()
