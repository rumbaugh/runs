import numpy as np
import math as m
import sys

execfile("/home/rumbaugh/gaussint.py")
execfile("/home/rumbaugh/KStest.py")
path = '/home/rumbaugh/paperstuff'

zlb = np.array([0.65,0.80,0.82,0.84,0.68])
zub = np.array([0.79,0.84,0.87,0.96,0.71])
names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
i = 4
rfile = path + '/input.fullRShist.' + names[i] + '.dat'
cr = read_file(rfile)

z = get_colvals(cr,'col3')

g = np.where((z > zlb[i]) & (zub[i] > z))
g = g[0]
ztemp = z[g]
mu,std,var = ztemp.mean(),ztemp.std(),(ztemp.std())**2
cdf1 = np.zeros(len(g))
cdf2 = np.zeros(1000)
FILE=open('/home/rumbaugh/1757.cdf.plot.dat','w')
for i in range(0,len(g)):
    cdf1[i] = gausspdfbin(loB=-99,upB=z[g[i]],step=0.0001,center=mu,var=var,loBeqNI=True)
sort1 = np.argsort(z[g])
for i in range(0,len(g)):
    FILE.write("%f %f\n"%(z[g[sort1[i]]],cdf1[sort1[i]]))
gaussx = (np.arange(1000)-500)*5.5*std/500.0 + mu
gaussy = np.zeros(1000)
for j in range(0,1000): gaussy[j] = 10*m.exp(-0.5*(mu-gaussx[j])**2/var)
FILE2 = open('/home/rumbaugh/1757.cdf2.plot.dat','w')
for i in range(0,1000):
    cdf2[i] = gausspdfbin(loB=-99,upB=(-5.5+5.5*i/500.0)*std+mu,step=std/5000.0,center=mu,var=var,loBeqNI=True)
    FILE2.write("%f %f\n"%((-5.5+5.5*i/500.0)*std+mu,cdf2[i]))
dif,prob = KStest1var(z[g],cdf1)
FILE.close()
FILE2.close()
print dif,prob
