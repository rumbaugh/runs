import numpy as np
import pyfits as py
execfile('/home/rumbaugh/git/data_redux_code/spec_simple.py')

b0813_list = np.array([193,194,370,371,373,374],dtype='S99')
r0813_list = np.array([142,149,352,353,361,362],dtype='S99')
for i in np.arange(len(b0813_list)): b0813_list[i] = '/home/rumbaugh/KAST/Science/spec_skysub_noCR.b%s.dat'%b0813_list[i]
for i in np.arange(len(r0813_list)): r0813_list[i] = '/home/rumbaugh/KAST/Science/spec_skysub_noCR.r%s.dat'%r0813_list[i]

combine_spectra(b0813_list,'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0813_blue.dat')
combine_spectra(r0813_list,'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0813_red.dat')
