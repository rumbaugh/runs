import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm
import time
import os

date = '12.10.13'

ref_dict = {'rung': {}}
ref_dict['rung'][0] = {'tdc1_rung0_double_pair6':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung0_double_pair201':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung0_double_pair301':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung0_double_pair321':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung0_double_pair341':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung0_double_pair381':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung0_double_pair401':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung0_double_pair501':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung0_quad_pair6A': {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung0_quad_pair6B': {'infile':  '', 'range': np.array([0,30])}}

ref_dict['rung'][1] = {'tdc1_rung1_double_pair7':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung1_double_pair202':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung1_double_pair302':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung1_double_pair322':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_double_pair342':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_double_pair382':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_double_pair402':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung1_double_pair502':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_quad_pair7A': {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_quad_pair7B': {'infile':  '', 'range': np.array([60,90])}}

ref_dict['rung'][2] = {'tdc1_rung2_double_pair8':  {'infile':  '', 'range': np.array([90,120])},
'tdc1_rung2_double_pair203':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung2_double_pair303':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung2_double_pair323':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung2_double_pair343':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung2_double_pair383':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung2_double_pair403':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung2_double_pair503':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung2_quad_pair8A': {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung2_quad_pair8B': {'infile':  '', 'range': np.array([0,30])}}
ref_dict['rung'][3] = {'tdc1_rung3_double_pair9':  {'infile':  '', 'range': np.array([90,120])},
'tdc1_rung3_double_pair204':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung3_double_pair304':  {'infile':  '', 'range': np.array([90,120])},
'tdc1_rung3_double_pair324':  {'infile':  '', 'range': np.array([90,120])},
'tdc1_rung3_double_pair344':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung3_double_pair384':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung3_double_pair404':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung3_double_pair504':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung3_quad_pair9A': {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung3_quad_pair9B': {'infile':  '', 'range': np.array([0,30])}}
ref_dict['rung'][4] = {'tdc1_rung4_double_pair10':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung4_double_pair205':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung4_double_pair305':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung4_double_pair325':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung4_double_pair345':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung4_double_pair385':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung4_double_pair405':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung4_double_pair505':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung4_quad_pair10A': {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung4_quad_pair10B': {'infile':  '', 'range': np.array([0,30])}}

commonbase = 'tdc1_rung'
basenames = np.array(['double_pair20','double_pair30','double_pair32','double_pair34','double_pair38','double_pair40','double_pair50','quad_pairA','quad_pairB'])
basenums = np.array([1,1,1,1,1,1,1,6,6])

FILE = open('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/emcee_anal.tau.defrange.%s.dat'%date,'w')
FILE.write('# pair       medtau   LB  UB\n')

for rung in range(0,5):
    for i in range(0,9):
        pair = '%s%i_%s%i'%(commonbase,rung,basenames[i],basenums[i]+rung)
        if basenums[i] == 6: pair = '%s%i_%s%i%s'%(commonbase,rung,basenames[i][:len(basenames[i])-1],basenums[i]+rung,basenames[i][len(basenames[i])-1])
        cr = np.loadtxt('/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung%i/emcee/%s.emcee_output_hist_tau.%s.dat'%(rung,pair,date))
        tau_sort = np.sort(cr)
        FILE.write('%25s %5.1f %5.1f %5.1f %3i %3i\n'%(pair,np.median(tau_sort),tau_sort[int(0.16*len(tau_sort))],tau_sort[int(0.84*len(tau_sort))],ref_dict['rung'][rung][pair]['range'][0],ref_dict['rung'][rung][pair]['range'][1]))
FILE.close()
