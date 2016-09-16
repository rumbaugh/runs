import numpy as np
from pyds9 import *
import os
import time

#dum=os.system('ds9 &')
time.sleep(1.5)

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

crc=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','ra','dec'),'formats':('|S24','|S24','f8','f8')})

zlist=np.array([0.77,1.26,1.11,0.70,0.80,0.69,0.90,0.84,0.82,0.96,0.81,1.14,0.76,0.76])

testfield=np.copy(crc['field'])
for j in range(0,len(testfield)): 
    ftmp=testfield[j].split('_')
    testfield[j]=ftmp[0].lower()

dtgts=ds9_targets()
ds9targ=dtgts[-1][8:]
d=DS9(ds9targ)

for field,z in zip(targets,zlist):
    for band in ['full']:
        curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
        fitsfile='%s/%s_%s_nops.smoothed.z_%.2f.beta_0.67.rc_180kpc.img'%(curdir,field,band,z)
        clusregs='%s/%s_clusters.reg'%(curdir,field)
        d.set('file %s'%fitsfile)
        d.set('cmap sls')
        d.set('zoom to fit')
        d.set('regions delete all')
        ftmp=field.split('_')
        if ftmp[0] in testfield: d.set('regions load %s'%clusregs)
        inp=raw_input('\nNow showing %s (%s band).\n\nContinue?\n'%(field,band))
