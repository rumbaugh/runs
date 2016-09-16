import numpy as np
import pyfits as py
execfile('/home/rumbaugh/git/data_redux_code/spec_simple.py')
#execfile('/home/rumbaugh/git/imcombine/imcombine.py')

b0956_list = np.array([195,196,197,198,199,200,201,375,376,377,378],dtype='S99')
r0956_list = np.array([151,158,159,174,175,182,369,370,377,378],dtype='S99')
b0737_list = np.array([366,367,368,369],dtype='S99')
r0737_list = np.array([342,343,350,351],dtype='S99')

FILEr = open('/home/rumbaugh/KAST/Science/r0813_files.list','w')
FILEb = open('/home/rumbaugh/KAST/Science/b0813_files.list','w')


r0813_list = np.array([142,149,352,353,361,362],dtype='S99')
b0813_list = np.array([193,194,370,371,373,374],dtype='S99')

for i in np.arange(len(b0813_list)): 
    print '/home/rumbaugh/KAST/Science/sci-b%s.fits[0]\n'%b0813_list[i]
    FILEb.write('/home/rumbaugh/KAST/Science/sci-b%s.fits[0]\n'%b0813_list[i])
    b0956_list[i] = '/home/rumbaugh/KAST/Science/sci-b%s.fits\n'%b0813_list[i]
for i in np.arange(len(r0813_list)): 
    FILEr.write('/home/rumbaugh/KAST/Science/sci-r%s.fits[0]\n'%r0813_list[i])
    r0956_list[i] = '/home/rumbaugh/KAST/Science/sci-r%s.fits\n'%r0813_list[i]

FILEb.close()
FILEr.close()

#imcombine(r0956_list,'/home/rumbaugh/KAST/Science/coadd_0813_red.7.30.15.fits')
#imcombine(b0956_list,'/home/rumbaugh/KAST/Science/coadd_0813_blue.7.30.15.fits')

#imcombine @/home/rumbaugh/KAST/Science/r0813_files.list coadd_0813_red.7.30.15.fits
#imcombine @/home/rumbaugh/KAST/Science/b0813_files.list coadd_0813_blue.7.30.15.fits


#for i in np.arange(len(b0956_list)): b0956_list[i] = '/home/rumbaugh/KAST/Science/spec.b%s.dat'%b0956_list[i]
#for i in np.arange(len(r0956_list)): r0956_list[i] = '/home/rumbaugh/KAST/Science/spec.r%s.dat'%r0956_list[i]
#for i in np.arange(len(b0813_list)): b0813_list[i] = '/home/rumbaugh/KAST/Science/spec.b%s.dat'%b0813_list[i]
#for i in np.arange(len(r0813_list)): r0813_list[i] = '/home/rumbaugh/KAST/Science/spec.r%s.dat'%r0813_list[i]


#combine_spectra(b0956_list,'/home/rumbaugh/KAST/Science/comb_spec.0956_blue.dat')
#combine_spectra(r0956_list,'/home/rumbaugh/KAST/Science/comb_spec.0956_red.dat')
#combine_spectra(b0813_list,'/home/rumbaugh/KAST/Science/comb_spec.0813_blue_2.19.dat')
#combine_spectra(r0813_list,'/home/rumbaugh/KAST/Science/comb_spec.0813_red_2.19.dat')
