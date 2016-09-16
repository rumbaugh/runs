import numpy as np
import os
os.chdir('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa')
from LRIS.resample import resample
import pyfits,numpy
from LRIS.LRIStools import *
from LRIS.XSolve import *
execfile('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa/lris_reduce_multislit.py')
execfile('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa/lris_reduce_longslit.py')

indir = "/local/rumbaugh/LRIS/2011_01/Raw/"
outdir = "/local/rumbaugh/LRIS/2011_01/reduced/"
files_dict = {'1131m3': {'prefix': '110106_', \
'blue': {'arc': 264, 'flat': 263, 'images': np.array([261,262,265,266,267])}, \
'red': {'arc': 257, 'flat': 256, 'images': np.array([254,255,258,259,260])}}, \
'1131m4': {'prefix': '110106_', \
'blue': {'arc': 273, 'flat': 272, 'images': np.array([270,271,274,275,276])}, \
'red': {'arc': 264, 'flat': 263, 'images': np.array([261,262,265,266,267])}}, \
'Feige110': {'prefix': '110106_', \
'blue': {'arc': 229, 'arcarray': np.array([228,229]), 'flat': 230, 'flatarray': np.array([227,230]), 'images': np.array([226,231])}, 'slit': [125,225], \
'red': {'arc': 225, 'arcarray': np.array([224,225]), 'flat': 226, 'flatarray': np.array([223,226]), 'images': np.array([222,227])}}, \
'Feige110_1': {'prefix': '110106_', \
'blue': {'arc': 228, 'flat': 227, 'images': np.array([226]), 'slit': [125,225,'top']}, \
'red': {'arc': 224, 'flat': 223, 'images': np.array([222]), 'slit': [100,150,'top']}}, \
'Feige110_2': {'prefix': '110106_', \
'blue': {'arc': 229, 'flat': 230, 'images': np.array([231]), 'slit': [75,275,'top']}, \
'red': {'arc': 225, 'flat': 226, 'images': np.array([227]), 'slit': [125,205,'top']}},\
'AGY_GRB_SN': {'prefix': '110106_', \
'blue': {'arc': 234, 'flat': 233, 'images': np.array([232])}, 'slit': [220,250,'top']}, \
'red': {'arc': 230, 'flat': 229, 'images': np.array([228])}}, 'slit': [175,205,'top']}, \
'HE0435-1223_1': {'prefix': '110106_', \
'blue': {'arc': 239, 'arcarray': np.array([238,239]), 'flat': 237, 'images': np.array([235,236,240,241])}, 'slit': [155,215,'top']},\
'red': {'arc': 234, 'flat': 233, 'images': np.array([231,232,235,236])}}, 'slit': [125,285,'top']},\
'HE0435-1223_2': {'prefix': '110106_', \
'blue': {'arc': 245, 'flat': 244, 'images': np.array([242,243,246,247,248])}, 'slit': [155,215,'top']},\
'red': {'arc': 240, 'flat': 239, 'images': np.array([237,238,241,242,243])}},  'slit': [125,285,'top']},\
'0435_slit1': {'prefix': '110106_', \
'blue': {'arc': 253, 'flat': 252, 'images': np.array([249,250,251])}, \
'red': {'arc': 248, 'flat': 247, 'images': np.array([244,245,246])}}, \
'0435_slit2': {'prefix': '110106_', \
'blue': {'arc': 254, 'flat': 255, 'images': np.array([256,257,258])}, \
'red': {'arc': 249, 'flat': 250, 'images': np.array([251,252,253])}}, \
}

for mask in ['Feige110_2']:
    lris_reduce_longslit(indir,outdir,files_dict[mask]['prefix'],files_dict[mask],colors='both')
