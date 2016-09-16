import numpy as np

FILE = open('/home/rumbaugh/KAST/Science/offsets.0956.dat','w')

cr = np.loadtxt('/home/rumbaugh/KAST/Science/mupoly.0956.dat',dtype={'names': ('obs','mp3','mp2','mp1','mp0','LB','UB'),'formats':('|S8','float64','float64','float64','float64','float','float')})

x = np.arange(2048)


bbase = cr[0]
y0 = bbase[5]+bbase[4]+x*bbase[3]+x**2*bbase[2]+x**3*bbase[1]
FILE.write('%s %f\n'%(bbase[0],0.))
for i in range(1,6):
    temp = cr[i]
    y = temp[5]+temp[4]+x*temp[3]+x**2*temp[2]+x**3*temp[1]
    diff = y0-y
    FILE.write('%s %f\n'%(temp[0],np.average(diff)))

bbase = cr[6]
y0 = bbase[5]+bbase[4]+x*bbase[3]+x**2*bbase[2]+x**3*bbase[1]
FILE.write('%s %f\n'%(bbase[0],0.))
for i in range(7,12):
    temp = cr[i]
    y = temp[5]+temp[4]+x*temp[3]+x**2*temp[2]+x**3*temp[1]
    diff = y0-y
    FILE.write('%s %f\n'%(temp[0],np.average(diff)))

FILE.close()
