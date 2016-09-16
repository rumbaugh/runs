import numpy as np
import os
from pyds9 import *

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clus_rad.dat',dtype={'names':('field','cluster','rad','RA','Dec','imgX','imgY'),'formats':('|S24','|S24','f8','f8','f8','f8','f8')})

dtgts=ds9_targets()
ds9targ=dtgts[-1][8:]
d=DS9(ds9targ)

for i in range(-4,0):
    field,cluster=cr['field'][i],cr['cluster'][i]
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    fitsfile='%s/%s_full.img'%(curdir,field)
    d.set('file %s'%fitsfile)
    for band in ['soft','hard','full']:
        outreg='%s/%s_%s_spec.reg'%(curdir,cluster,band)
        bkgreg='%s/%s_%s_spec_bkg.reg'%(curdir,band,cluster)
        PSreg='%s/%s_PS_masks_%s.reg'%(curdir,field,band)
        d.set('regions delete all')
        d.set('regions load %s'%(PSreg))
        d.set('regions system image')
        d.set('regions save ds9tmp.reg')
        crt=np.loadtxt('ds9tmp.reg',dtype='|S128',skiprows=3)
        xs,ys,rads=np.zeros(len(crt)),np.zeros(len(crt)),np.zeros(len(crt))
        for j in range(0,len(crt)):
            strtmp=crt[j].split(',')
            xtmp,ytmp,radtmp=strtmp[0].split('('),float(strtmp[1]),strtmp[2].split(')')
            xtmp,radtmp=float(xtmp[1]),float(radtmp[0])
            if crt[j][0]=='e': 
                radtmp=np.max([radtmp,float(strtmp[3])])
            xs[j],ys[j],rads[j]=xtmp,ytmp,radtmp
        disttmp=np.sqrt((xs-cr['imgX'][i])**2+(ys-cr['imgY'][i])**2)
        g=np.where(disttmp<cr['rad'][i]+radtmp)[0]
        FILE=open(outreg,'w')
        FILE.write('circle(%f,%f,%f)'%(cr['imgX'][i],cr['imgY'][i],cr['rad'][i]))
        for j in range(0,len(g)):
            FILE.write('-%s'%(crt[g[j]]))
        FILE.write('\n')
        FILE.close()
        
