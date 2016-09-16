import numpy as np
import pyfits as py
execfile('/home/rumbaugh/git/data_redux_code/spec_simple.py')

b0956_list = np.array([195,196,197,198,199,200,201,375,376,377,378],dtype='S99')
r0956_list = np.array([151,158,159,174,175,369,370,377,378],dtype='S99')
b0737_list = np.array([366,367,368,369],dtype='S99')
r0737_list = np.array([342,343,350,351],dtype='S99')
for i in np.arange(len(b0956_list)): b0956_list[i] = '/home/rumbaugh/KAST/Science/spec_skysub_noCR.b%s.dat'%b0956_list[i]
for i in np.arange(len(r0956_list)): r0956_list[i] = '/home/rumbaugh/KAST/Science/spec_skysub_noCR.r%s.dat'%r0956_list[i]
for i in np.arange(len(b0737_list)): b0737_list[i] = '/home/rumbaugh/KAST/Science/spec_skysub_noCR.b%s.dat'%b0737_list[i]
for i in np.arange(len(r0737_list)): r0737_list[i] = '/home/rumbaugh/KAST/Science/spec_skysub_noCR.r%s.dat'%r0737_list[i]

combine_spectra(b0956_list,'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0956_blue.dat')
combine_spectra(r0956_list,'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0956_red.dat')
combine_spectra(b0737_list,'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0737_blue_2.19.dat')
combine_spectra(r0737_list,'/home/rumbaugh/KAST/Science/comb_spec_skysub_noCR.0737_red_2.19.dat')
