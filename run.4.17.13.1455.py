import numpy as np
import os
os.chdir('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa')
from LRIS.resample import resample
import pyfits,numpy
from LRIS.LRIStools import *
from LRIS.XSolve import *

indir = "/local/rumbaugh/LRIS/2011_01/Raw/"
outdir = "/local/rumbaugh/LRIS/2011_01/reduced/"
files_dict = {'1131m3': {'prefix': '110106_', \
'blue': {'arc': 264, 'flat': 263, 'images': np.array([261,262,265,266,267])}, \
'red': {'arc': 257, 'flat': 256, 'images': np.array([254,255,258,259,260])}}, \
'1131m4': {'prefix': '110106_', \
'blue': {'arc': 273, 'flat': 272, 'images': np.array([270,271,274,275,276])}, \
'red': {'arc': 264, 'flat': 263, 'images': np.array([261,262,265,266,267])}}}

files_dict['1131m3']['blue']['refimage'] = 266

isblue = False
for mask in ['1131m3','1131m4']:
    if isblue: 
        prefpref = 'b'
        bluorred = 'blue'
    else:
        prefpref = 'r'
        bluorred = 'red'
    pref = prefpref + '110106_'
    flat,arc = files_dict[mask][bluorred]['flat'],files_dict[mask][bluorred]['arc']
    for side in ['top','bottom']:
        outname = '%s%s_%s_%s'%(outdir,mask,bluorred,side)
        try:
            files_dict[mask][bluorred]['refimage']
        except KeyError:
            files_dict[mask][bluorred]['refimage'] = files_dict[mask][bluorred]['images'][0]
        slitID(indir,pref,[flat,arc,files_dict[mask][bluorred]['refimage']],outname,side=side)
        oldName = None
        sf = True
        for img in files_dict[mask][bluorred]['images']:
            newName = '%s_%2d'%(outname,img)
            XSolve(outname,newName,indir,pref,[flat,arc,img])
            SlitCross(newName)
            WaveSolve(newName,oldName,showFit=sf)
            resample(newName,nobgsub=True,clobber=True)
            oldName = newName
