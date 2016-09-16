from LRIS.resample import resample
import pyfits,numpy
from LRIS.LRIStools import *
from LRIS.XSolve import *

try:
    date
except NameError:
    date = '3.7.13'

indir = '/local3/rumbaugh/LRISdata/2011oct25/'
bgroups,rgroups=2,2
obsdata = numpy.loadtxt('/local3/rumbaugh/LRISdata/2011oct25/obslog.dat',dtype='string')
obsshape = numpy.shape(obsdata)
obs_rows = obsshape[0]
obs_nums = numpy.zeros(obs_rows,dtype='int16')
for i in range(0,obs_rows): obs_nums[i] = int(obsdata[i,1])
for i in range(0,2):
    mslit = 0
    if i == 0:
        arc = 43
        flat = 42
        images = [40,41,44,45,46]
    if i == 1:
        arc = 52
        flat = 51
        images = [49,50,53,54,55]
    images_num = numpy.zeros(len(images),dtype='int16')
    for j in range(0,len(images)): images_num[j] = int(obsdata[images[j],1])
    flat_num = int(obsdata[flat,1])
    arc_num = int(obsdata[arc,1])
    pref = obsdata[images[0],0]
    outname = '%s_b.%s'%(obsdata[images[0],2],date)
    #slitID(indir,pref,[flat,arc,110],outname,side='top',slits=[[50,100]])
    #print flat_num,arc_num,images_num
    if mslit == 0:
        slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='top',slits=[[100,200]])
        #slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='bottom',slits=[[0,500]])
    else:
        slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='top')
    oldName = None
    sf = True
    for img in images_num:
        newName = '%s_%2d'%(outname,img)
        XSolve(outname,newName,indir,pref,[flat_num,arc_num,img])
        SlitCross(newName)
        WaveSolve(newName,oldName,showFit=sf)
        resample(newName,nobgsub=True,doCR=False,clobber=True)
        oldName = newName
for i in range(0,2):
    mslit = 0
    if i == 0:
        arc = 99
        flat = 98
        images = [97,96,100,101,102]
    if i == 1:
        arc = 106
        flat = 105
        images = [103,104,107,108,109]
    images_num = numpy.zeros(len(images),dtype='int16')
    for j in range(0,len(images)): images_num[j] = int(obsdata[images[j],1])
    flat_num = int(obsdata[flat,1])
    arc_num = int(obsdata[arc,1])
    print arc_num,flat_num,images_num
    pref = obsdata[images[0],0]
    outname = '%s_r.5.18.12_145-245.noCR'%(obsdata[images[0],2])
    #slitID(indir,pref,[flat,arc,110],outname,side='top',slits=[[50,100]])
    if mslit == 0:
        slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='top',slits=[[145,245]])
    else:
        slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='top')
    oldName = None
    sf = True
    for img in images_num:
        newName = '%s_%2d'%(outname,img)
        XSolve(outname,newName,indir,pref,[flat_num,arc_num,img])
        SlitCross(newName)
        WaveSolve(newName,oldName,showFit=sf)
        #resample(newName,nobgsub=True,doCR=False,clobber=True)
        resample(newName,nobgsub=True,clobber=True)
        oldName = newName

