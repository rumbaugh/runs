import numpy as np
import os
os.chdir('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa')
execfile("/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa/lris_reduce_multislit.py")
execfile("/home/rumbaugh/LRIS_files_dict_master.py")
indir = '/local/rumbaugh/LRIS/Marusa/LRIS5_062011/data'
outdir = '/local/rumbaugh/LRIS/Marusa/test/'
if files_dict[mask][color]['arc'] != None:
    lris_reduce_multislit(indir,outdir,files_dict[mask]['prefix'],files_dict[mask],mask,colors=color,sides=[side])
else:
    lris_reduce_multislit(indir,outdir,files_dict[mask]['prefix'],files_dict[mask],mask,colors=color,sides=[side],fakearc=998)
