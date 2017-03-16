import numpy as np
execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')

cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/CLQ_candidates_DR7.3.8.17.dat',dtype={'names':('DBID','drop','S1','S2','S82','flag'),'formats':('|S24','f8','|S4','|S4','i8','i8')},skiprows=1)

cr=cr[cr['flag']==0]

plt.figure(1)
plt.clf()
plt.hist(np.abs(cr['drop']),range=(1,3.125),bins=17)
plt.xlabel('Magnitude Change')
plt.ylabel('Number of objects')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/MagDropPlot.CLQ_candidates.DR7.3.16.17.png')
