import numpy
import matplotlib.pyplot as plt

DBID='MQ200905'

DBdir='/home/rumbaugh/var_database/Y3A1'

cr=np.loadtxt('%s/%s/SF.tab'%(DBdir,DBID),dtype={'names':('tau','SF1','SF2','SF3','SF4','SF5'),'formats':('f8','f8','f8','f8','f8','f8')})

plt.figure(1)
plt.clf()
color_arr=['magenta','red','blue','green','cyan']
for i in np.arange(1,6):plt.plot(cr['tau'],cr['SF%i'%i],lw=2,c=color_arr[i],label='SF%i'%i)
plt.legend()
plt.xlabel(r'$\Delta t$')
plt.ylabel('Structure Function')
plt.savefig('/home/rumbaugh/testplot_SF.png'
