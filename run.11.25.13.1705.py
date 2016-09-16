import numpy as np
import os
execfile('/home/rumbaugh/Dispersion.py')
delta = 17.5
maxmu = 1.25
minmu = 0.75
timestep = 0.5
mustep = 0.0025

suffix = 'BA_extended.dat'
tau_extension = 30

ref_dict = {#'tdc1_rung0_double_pair6':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung0_double_pair201':  {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung0_double_pair301':  {'infile':  '', 'range': np.array([30,60])},
#'tdc1_rung0_double_pair321':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung0_double_pair341':  {'infile':  '', 'range': np.array([30,60])}#,
#'tdc1_rung0_double_pair381':  {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung0_double_pair401':  {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung0_double_pair501':  {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung0_quad_pair6A': {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung0_quad_pair6B': {'infile':  '', 'range': np.array([0,30])}
}
os.system('mkdir -p /mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/output/')
for tdcfile in ref_dict:
    infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/%s.txt'%tdcfile
    outfile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung0/output/%s.%s'%(tdcfile,suffix)
    mintime = ref_dict[tdcfile]['range'][0] - tau_extension
    maxtime = ref_dict[tdcfile]['range'][1] + tau_extension
    cr = np.loadtxt(infile)
    ltime,A,Aerr,B,Berr = cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]
    ttmp,mtmp,BA_disp_mat = calc_disp_delay(B,A,ltime,ltime,Berr,Aerr,maxtime,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,mintime=mintime,outfile=outfile)

ref_dict = {'tdc1_rung2_double_pair8':  {'infile':  '', 'range': np.array([90,120])},
'tdc1_rung2_double_pair203':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung2_double_pair303':  {'infile':  '', 'range': np.array([60,90])},
#'tdc1_rung2_double_pair323':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung2_double_pair343':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung2_double_pair383':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung2_double_pair403':  {'infile':  '', 'range': np.array([60,90])},
'tdc1_rung2_double_pair503':  {'infile':  '', 'range': np.array([30,60])}#,
#'tdc1_rung2_quad_pair8A': {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung2_quad_pair8B': {'infile':  '', 'range': np.array([0,30])}
}
os.system('mkdir -p /mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung2/output/')
for tdcfile in ref_dict:
    infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung2/%s.txt'%tdcfile
    outfile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung2/output/%s.%s'%(tdcfile,suffix)
    mintime = ref_dict[tdcfile]['range'][0] - tau_extension
    maxtime = ref_dict[tdcfile]['range'][1] + tau_extension
    cr = np.loadtxt(infile)
    ltime,A,Aerr,B,Berr = cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]
    ttmp,mtmp,BA_disp_mat = calc_disp_delay(B,A,ltime,ltime,Berr,Aerr,maxtime,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,mintime=mintime,outfile=outfile)

ref_dict = {'tdc1_rung3_double_pair9':  {'infile':  '', 'range': np.array([90,120])},
#'tdc1_rung3_double_pair204':  {'infile':  '', 'range': np.array([0,30])},
'tdc1_rung3_double_pair304':  {'infile':  '', 'range': np.array([90,120])},
'tdc1_rung3_double_pair324':  {'infile':  '', 'range': np.array([90,120])}#,
#'tdc1_rung3_double_pair344':  {'infile':  '', 'range': np.array([60,90])},
#'tdc1_rung3_double_pair384':  {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung3_double_pair404':  {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung3_double_pair504':  {'infile':  '', 'range': np.array([60,90])},
#'tdc1_rung3_quad_pair9A': {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung3_quad_pair9B': {'infile':  '', 'range': np.array([0,30])}
}
os.system('mkdir -p /mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung3/output/')
for tdcfile in ref_dict:
    infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung3/%s.txt'%tdcfile
    outfile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung3/output/%s.%s'%(tdcfile,suffix)
    mintime = ref_dict[tdcfile]['range'][0] - tau_extension
    maxtime = ref_dict[tdcfile]['range'][1] + tau_extension
    cr = np.loadtxt(infile)
    ltime,A,Aerr,B,Berr = cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]
    ttmp,mtmp,BA_disp_mat = calc_disp_delay(B,A,ltime,ltime,Berr,Aerr,maxtime,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,mintime=mintime,outfile=outfile)


ref_dict = {#'tdc1_rung4_double_pair10':  {'infile':  '', 'range': np.array([30,60])},
'tdc1_rung4_double_pair205':  {'infile':  '', 'range': np.array([0,30])}#,
#'tdc1_rung4_double_pair305':  {'infile':  '', 'range': np.array([30,60])},
#'tdc1_rung4_double_pair325':  {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung4_double_pair345':  {'infile':  '', 'range': np.array([60,90])},
#'tdc1_rung4_double_pair385':  {'infile':  '', 'range': np.array([30,60])},
#'tdc1_rung4_double_pair405':  {'infile':  '', 'range': np.array([0,30])},
#'tdc1_rung4_double_pair505':  {'infile':  '', 'range': np.array([30,60])},
#'tdc1_rung4_quad_pair10A': {'infile':  '', 'range': np.array([30,60])},
#'tdc1_rung4_quad_pair10B': {'infile':  '', 'range': np.array([0,30])}
}
os.system('mkdir -p /mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung4/output/')
for tdcfile in ref_dict:
    infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung4/%s.txt'%tdcfile
    outfile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung4/output/%s.%s'%(tdcfile,suffix)
    mintime = ref_dict[tdcfile]['range'][0] - tau_extension
    maxtime = ref_dict[tdcfile]['range'][1] + tau_extension
    cr = np.loadtxt(infile)
    ltime,A,Aerr,B,Berr = cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]
    ttmp,mtmp,BA_disp_mat = calc_disp_delay(B,A,ltime,ltime,Berr,Aerr,maxtime,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,mintime=mintime,outfile=outfile)
