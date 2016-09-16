import numpy as np
import os
os.chdir('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa')
from LRIS.resample import resample
import pyfits,numpy
from LRIS.LRIStools import *
from LRIS.XSolve import *
execfile('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa/lris_reduce_multislit.py')

indir = "/local/rumbaugh/LRIS/2011_01/Raw/"
outdir = "/local/rumbaugh/LRIS/2011_01/reduced/"
files_dict = {'1131m3': {'prefix': '110106_', \
'blue': {'arc': 264, 'flat': 263, 'images': np.array([267])}, \
'red': {'arc': 257, 'flat': 256, 'images': np.array([254,255,258,259,260])}}, \
'1131m4': {'prefix': '110106_', \
'blue': {'arc': 273, 'flat': 272, 'images': np.array([270,271,274,275,276])}, \
'red': {'arc': 264, 'flat': 263, 'images': np.array([261,262,265,266,267])}}}

for mask in ['1131m3']:
        #lris_reduce_multislit(indir,outdir,files_dict[mask]['prefix'],files_dict[mask],colors='blue',sides=['bottom'])
        #lris_reduce_multislit(indir,outdir,files_dict[mask]['prefix'],files_dict[mask],colors='red',sides=['bottom'])
    #else:
        lris_reduce_multislit(indir,outdir,files_dict[mask]['prefix'],files_dict[mask],mask,colors='blue',sides=['bottom'])
