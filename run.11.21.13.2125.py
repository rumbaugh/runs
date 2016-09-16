import numpy as np
import matplotlib.pylab as py
execfile('/home/rumbaugh/Dispersion.py')

ref_dict = {#'tdc1_rung1_double_pair7':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung1_double_pair202':  {'infile':  '', 'range': np.array([30,120])},
#'tdc1_rung1_double_pair302':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung1_double_pair322':  {'infile':  '', 'range': np.array([-30,60])},
#'tdc1_rung1_double_pair342':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung1_double_pair382':  {'infile':  '', 'range': np.array([-30,60])}#,
#'tdc1_rung1_double_pair403':  {'infile':  '', 'range': np.array([30,60])},
#'tdc1_rung1_double_pair502':  {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung1_quad_pair7A': {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung1_quad_pair7B': {'infile':  '', 'range': np.array([60,90])}
}


infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung1/tdc1_rung1_double_pair502'
for tdcfile in ref_dict:
    infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung1/%s.txt'%tdcfile
    outfile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung1/output/%s.BA_extended_mu+tau.dat'%tdcfile

    timestep = 1.
#mustep = 0.001
    mustep = 0.01
    mintime = ref_dict[tdcfile]['range'][0]
    maxtime = ref_dict[tdcfile]['range'][1]
    maxmu = 1.3
    minmu = 0.7
    delta = 17.5

    cr = np.loadtxt(infile)
    ltime,A,Aerr,B,Berr = cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]

    ttmp,mtmp,BA_disp_mat = calc_disp_delay(B,A,ltime,ltime,Berr,Aerr,maxtime,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,mintime=mintime,outfile=outfile)

