import numpy as np
execfile('/home/rumbaugh/Dispersion.py')

infile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung1/tdc1_rung1_double_pair502.txt'
outfile = '/mnt/data2/rumbaugh/TDC/tdc1sample_for_test/rung1/output/tdc1_rung1_double_pair502.dat'

timestep = 0.5
mustep = 0.001
mintime = 0
maxtime = 30
maxmu = 1.1
minmu = 0.9
delta = 17.5

cr = np.loadtxt(infile)
ltime,A,Aerr,B,Berr = cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]

ttmp,mtmp,BA_disp_mat = calc_disp_delay(A,B,ltime,ltime,Aerr,Berr,maxtime,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,mintime=mintime,outfile=outfile)
