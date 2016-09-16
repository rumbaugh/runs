import numpy as np

cr = read_file("/scratch/rumbaugh/ciaotesting/analysis/lens.analysis.Amp.1.17.11.dat")
names = get_colvals(cr,'col1')
rcore = get_colvals(cr,'col2')
bg = get_colvals(cr,'col3')
amp = get_colvals(cr,'col4')
cr2 = read_file("/home/rumbaugh/COSMOS/lens_sample_id_z_exp_rc.dat")

cc = amp/bg
FILE = open("/home/rumbaugh/temp.1.17.11.dat","w")
for i in range(0,len(names)): FILE.write('%i '%(names[i]))
FILE.write('\n')
for i in range(0,len(names)): FILE.write('%6.2f '%(rcore[i]))
FILE.write('\n')
for i in range(0,len(names)): FILE.write('%6.2f '%(cc[i]))
FILE.write('\n')
for i in range(0,len(names)): FILE.write('%9.7f '%(bg[i]))
FILE.write('\n')
FILE.close()

