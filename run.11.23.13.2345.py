import numpy as np
execfile('/home/rumbaugh/Dispersion.py')

ref_dict = {'tdc1_rung0_double_pair6':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung0_double_pair201':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung0_double_pair301':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung0_double_pair321':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung0_double_pair341':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung0_double_pair381':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung0_double_pair401':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung0_double_pair501':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung0_quad_pair6A': {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung0_quad_pair6B': {'infile':  '', 'range': np.array([0,30])}}


infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/tdc1_rung0_double_pair502'
for tdcfile in ref_dict:
    infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/%s.txt'%tdcfile
    outfile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/output/%s.BA.dat'%tdcfile

    timestep = 0.5
#mustep = 0.001
    mustep = 0.001
    mintime = ref_dict[tdcfile]['range'][0]
    maxtime = ref_dict[tdcfile]['range'][1]
    maxmu = 1.1
    minmu = 0.9
    delta = 17.5

    cr = np.loadtxt(infile)
    ltime,A,Aerr,B,Berr = cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]

    ttmp,mtmp,BA_disp_mat = calc_disp_delay(B,A,ltime,ltime,Berr,Aerr,maxtime,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,mintime=mintime,outfile=outfile)
