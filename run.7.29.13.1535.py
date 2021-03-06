import numpy as np
import os
os.chdir('/mnt/data2/rumbaugh/LRIS/Marusa/lrispipeline_marusa')
from LRIS.resample import resample
import pyfits,numpy
from LRIS.LRIStools import *
from LRIS.XSolve import *
execfile('/mnt/data2/rumbaugh/LRIS/Marusa/lrispipeline_marusa/lris_reduce_multislit.py')
execfile('/home/rumbaugh/LRIS_files_dict_master.py')
import copy

indir_dict = {'miki22.f': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night1", 'miki03_A': {'night': {'1': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night1", '2': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night2"}}, 'miki04.f': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night1", 'miki04_A': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night1", 'miki21.f': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night2", 'miki03_B': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night2", 'miki04_B': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night2", 'miki16B.': '/mnt/data2/rumbaugh/LRIS/Marusa/LRIS13_082011/data', 'miki21C.': '/mnt/data2/rumbaugh/LRIS/Marusa/LRIS13_082011/data', 'miki21D.': '/mnt/data2/rumbaugh/LRIS/Marusa/LRIS13_082011/data', 'bc3.file': '/mnt/data2/rumbaugh/LRIS/Marusa/LRIS13_082011/data', 'bc3B.fil': '/mnt/data2/rumbaugh/LRIS/Marusa/LRIS13_082011/data', '0414m3': '/mnt/data3/rumbaugh/LRISdata/2011oct25', '0414m3_1': '/mnt/data3/rumbaugh/LRISdata/2011oct25', '0414m3_2': '/mnt/data3/rumbaugh/LRISdata/2011oct25', '0435m2': "/mnt/data2/rumbaugh/LRIS/2011_01/Raw", '0435m3_v2': "/mnt/data2/rumbaugh/LRIS/2011_01/Raw", '1131m1_v2': "/mnt/data2/rumbaugh/LRIS/2011_01/Raw", '1131m2_v2': "/mnt/data2/rumbaugh/LRIS/2011_01/Raw"}
outdir_dict = {'miki22.f': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki03_A': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki04.f': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki04_A': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki21.f': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki03_B': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki04_B': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki16B.': '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/', 'miki21C.': '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/', 'miki21D.': '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/', 'bc3.file': '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/', 'bc3B.fil': '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/', '0414m3': '/mnt/data3/rumbaugh/LRISdata/reduced/', '0414m3_1': '/mnt/data3/rumbaugh/LRISdata/reduced/', '0414m3_2': '/mnt/data3/rumbaugh/LRISdata/reduced/', '0435m2': "/mnt/data2/rumbaugh/LRIS/2011_01/reduced/", '0435m3_v2': "/mnt/data2/rumbaugh/LRIS/2011_01/reduced/", '1131m1_v2': "/mnt/data2/rumbaugh/LRIS/2011_01/reduced/", '1131m2_v2': "/mnt/data2/rumbaugh/LRIS/2011_01/reduced/"}

for mask in ['1131m2_v2']:
#for mask in ['0435m2','1131m1_v2','1131m2_v2']:
	if mask == '1131m2_v2':
	#	lris_reduce_multislit(indir_dict[mask],outdir_dict[mask],files_dict[mask]['prefix'],files_dict[mask],mask,colors='blue',sides=['bottom'],doCR=False,subset=[2])
		#for slit,i in zip(['1','54','80','261','490','484','564','663','678','948'],np.arange(10)):
		#for slit,i in zip(['1','91','121','197','227','517','600','679','786'],np.arange(9)):
		#for slit,i in zip(['176','77'],[0,1]):
		for slit,i in zip(['98','426'],[0,1]):
			tdict = copy.deepcopy(files_dict[mask])
		#tdict['blue']['images_split'][1] = np.delete(tdict['blue']['images_split'][1],[1])
		#lris_reduce_multislit(indir_dict[mask],outdir_dict[mask],files_dict[mask]['prefix'],tdict,mask,colors='red',sides=['bottom'],doCR=False,subset=[1])
		#lris_reduce_multislit(indir_dict[mask],outdir_dict[mask],files_dict[mask]['prefix'],tdict,mask,colors='blue',sides=['bottom'],doCR=False)
			print 'Slit #%i'%(i+1)
			lris_reduce_multislit(indir_dict[mask],outdir_dict[mask],files_dict[mask]['prefix'],tdict,mask,colors='blue',sides=['bottom'],doCR=False,slitname=slit)
	else:
		lris_reduce_multislit(indir_dict[mask],outdir_dict[mask],files_dict[mask]['prefix'],files_dict[mask],mask,colors='both',sides=['top','bottom'],doCR=False)
