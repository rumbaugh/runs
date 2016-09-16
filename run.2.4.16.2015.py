import numpy as np
import os
from pyds9 import *

targets=np.array(['rcs0224','cl0849','rxj0910','rxj1221','cl1350','rxj1716','cl1324_north','cl1324_south','rxj1757','rxj1821','rxj1053','cl1604'])
obsids=np.array([[3181,4987],[927,1708],[2227,2452],[1662],[2229],[548],[9403,9840],[9404,9836],[10443,11999],[10444,10924],[4936],[6932,6933,7343]])
obsdict=dict(zip(targets,obsids))

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clus_rad.dat',dtype={'names':('field','cluster','rad','RA','Dec','imgX','imgY'),'formats':('|S24','|S24','f8','f8','f8','f8','f8')})

cr0=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.XYzeropoints.dat',dtype={'names':('field','X','Y'),'formats':('|S24','i8','i8')})

dtgts=ds9_targets()
ds9targ=dtgts[-1][8:]
d=DS9(ds9targ)

for i in range(-4,0):
    field,cluster=cr['field'][i],cr['cluster'][i]
                
    g0=np.where(cr0['field']==field)[0][0]
    x0,y0=cr0['X'][g0],cr0['Y'][g0]
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    fitsfile='%s/%s_full.img'%(curdir,field)
    bkgreg='%s/%s_bkg_spec.reg'%(curdir,cluster)
    d.set('file %s'%fitsfile)
    d.set('regions delete all')
    d.set('regions load %s'%(bkgreg))
    d.set('regions format ds9');d.set('regions system wcs');d.set('regions sky fk5')
    d.set('regions save ds9tmp.reg')
    for obs in obsdict[field]:
        try:
            d.set('file %s/../../raw/%i/primary/acisf%05iN002_evt2.fits.gz'%(curdir,obs,obs))
        except:
            try:
                d.set('file %s/../../raw/%i/primary/acisf%05iN003_evt2.fits.gz'%(curdir,obs,obs))
            except:
                d.set('file %s/../../raw/%i/primary/acisf%05iN004_evt2.fits.gz'%(curdir,obs,obs))
        d.set('regions delete all')
        d.set('regions format ds9');d.set('regions system wcs');d.set('regions sky fk5')
        d.set('regions load ds9tmp.reg')
        d.set('regions format ciao');d.set('regions system physical')
        d.set('regions save %s/%s_%i_bkg_spec.reg'%(curdir,cluster,obs))
    d.set('file %s'%fitsfile)
    for band in ['soft','hard','full']:
        outreg='%s/%s_%s_spec.reg'%(curdir,cluster,band)
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
        physX,physY=x0+cr['imgX'][i],y0+cr['imgY'][i]
        disttmp=np.sqrt((xs-cr['imgX'][i])**2+(ys-cr['imgY'][i])**2)
        g=np.where(disttmp<cr['rad'][i]+radtmp)[0]
        FILE=open(outreg,'w')
        FILE.write('circle(%f,%f,%f)'%(physX,physY,cr['rad'][i]))
        for j in range(0,len(g)):
            strtmp=crt[g[j]].split(',')
            begstr=strtmp[0].split('(')
            FILE.write('-%s(%f,%f'%(begstr[0],float(begstr[1])+x0,float(strtmp[1])+y0))
            for k in range(2,len(strtmp)): FILE.write(',%s'%strtmp[k])
            #FILE.write('-%s'%(crt[g[j]]))
        FILE.close()
        outregtmp='%s/tmp_%s_%s_spec.reg'%(curdir,cluster,band)
        FILE=open(outregtmp,'w')
        FILE.write('circle(%f,%f,%f)'%(physX,physY,cr['rad'][i]))
        for j in range(0,len(g)):
            strtmp=crt[g[j]].split(',')
            begstr=strtmp[0].split('(')
            FILE.write('\n%s(%f,%f'%(begstr[0],float(begstr[1])+x0,float(strtmp[1])+y0))
            for k in range(2,len(strtmp)): FILE.write(',%s'%strtmp[k])
            #FILE.write('-%s'%(crt[g[j]]))
        FILE.close()
        d.set('regions delete all')
        d.set('regions load %s'%(outregtmp))
        d.set('regions format ds9');d.set('regions system wcs');d.set('regions sky fk5')
        d.set('regions save ds9tmp.reg')
        for obs in obsdict[field]:
            try:
                d.set('file %s/../../raw/%i/primary/acisf%05iN002_evt2.fits.gz'%(curdir,obs,obs))
            except:
                try:
                    d.set('file %s/../../raw/%i/primary/acisf%05iN003_evt2.fits.gz'%(curdir,obs,obs))
                except:
                    d.set('file %s/../../raw/%i/primary/acisf%05iN004_evt2.fits.gz'%(curdir,obs,obs))
            d.set('regions delete all')
            d.set('regions format ds9');d.set('regions system wcs');d.set('regions sky fk5')
            d.set('regions load ds9tmp.reg')
            d.set('regions format ciao');d.set('regions system physical')
            d.set('regions save %s/tmp_%s_%i_%s_spec.reg'%(curdir,cluster,obs,band))
            print '%s/tmp_%s_%i_%s_spec.reg'%(curdir,cluster,obs,band)
            crtro=np.loadtxt('%s/tmp_%s_%i_%s_spec.reg'%(curdir,cluster,obs,band),dtype='|S128')
            if np.shape(crtro)==():crtro=np.array([crtro])
            FILE=open('%s/%s_%i_%s_spec.reg'%(curdir,cluster,obs,band),'w')
            FILE.write('%s'%crtro[0])
            if len(crtro)>0:
                for k in range(1,len(crtro)):FILE.write('-%s'%crtro[k])
            FILE.close()
        d.set('file %s'%fitsfile)
            
        
