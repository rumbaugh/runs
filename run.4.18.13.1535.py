import os
os.chdir('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa/')

from LRIS.resample import resample
import pyfits,numpy
from LRIS.LRIStools import *
from LRIS.XSolve import *

indir = "/local/rumbaugh/LRIS/Marusa/raw/" 
pref = 'b101102_'
flat=81
arc=76
outname = 'miki03A_blue_t'
print 'Slit ID'
slitID(indir,pref,[flat,arc,46],outname,side='top')
oldName = None
sf = True
for img in [44,45,46]:
    print 'Working on image', img
    newName = '%s_%2d'%(outname,img)
    XSolve(outname,newName,indir,pref,[flat,arc,img])
    SlitCross(newName)
    WaveSolve(newName,oldName,showFit=sf)
    resample(newName,nobgsub=True,clobber=True)
    oldName = newName
pref = 'b101103_'
flat=127
arc=122
for img in [163,164,165]:
    newName = '%s_%2d'%(outname,img)
    XSolve(outname,newName,indir,pref,[flat,arc,img])
    SlitCross(newName)
    WaveSolve(newName,oldName,showFit=sf)
    resample(newName,nobgsub=True,clobber=True)
    oldName = newName
