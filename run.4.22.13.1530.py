import numpy as np
import os
os.chdir('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa')
from LRIS.resample import resample
import pyfits,numpy
from LRIS.LRIStools import *
from LRIS.XSolve import *

indir = "/local/rumbaugh/LRIS/Marusa/LRIS19_022010/"
outdir = "/local/rumbaugh/LRIS/Marusa/reduced/"
files_dict = {'M0417_B': {'blue': {'arc': 56, 'flat': 42, 'images': np.array([49,50,51,53,54,55])}, 'red': {'arc': None, 'flat': 45, 'images': np.array([48,49,50,51,52,53])}}}

isblue = True
for mask in ['M0417_B']:
    if isblue: 
        prefpref = 'b'
        bluorred = 'blue'
    else:
        prefpref = 'r'
        bluorred = 'red'
    pref = prefpref + '100214_'
    flat,arc = files_dict[mask][bluorred]['flat'],files_dict[mask][bluorred]['arc']
    for side in ['top']:
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
            SlitCross(newName,showFit=sf)
            WaveSolve(newName,oldName,showFit=sf)
            resample(newName,nobgsub=True,clobber=True)
            oldName = newName
            sf = False
