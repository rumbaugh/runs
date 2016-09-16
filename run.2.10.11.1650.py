import numpy as np
import math as m
import matplotlib
import matplotlib.pylab as pylab
import matplotlib.colors

execfile("/home/rumbaugh/FindCloseSources.py")

RAc = 201.08962000
Decc = 30.21934290

cr = read_file("/home/rumbaugh/LFC/FINAL.cl1322.lrisplusdeimos.cat")
zt = get_colvals(cr,'col9')
Q = get_colvals(cr,'col11')
g = np.where(Q > 2.9)
RAt = get_colvals(cr,'col4')
Dect = get_colvals(cr,'col5')
z,RA,Dec = zt[g],RAt[g],Dect[g]
RAs = np.zeros(0)
Decs = np.zeros(0)
colors = np.zeros(0)
for i in range(0,len(z)):
    dist = SphDist(RA[i],Dec[i],RAc,Decc)
    if ((dist < 3) & (z[i] < 1) & (z[i] > 0.5)):
        RAs = np.append(RAs,RA[i])
        Decs = np.append(Decs,Dec[i])
        colors = np.append(colors,(z[i]-0.5)*512)
#RAs = np.append(RAs,201.14)
#Decs = np.append(Decs,30.205)
#colors = np.append(colors,0.76*127)
pylab.scatter(RAc,Decc,marker='x')
pylab.scatter(RAs,Decs,marker='o',c=colors)
pylab.scatter(RAc,Decc,marker='x')
RAc = 201.09805
Decc = 30.183444

pylab.scatter(RAc,Decc,marker='x')
pylab.savefig('/home/rumbaugh/ChandraData/Cl1324/colormap.2.10.11.png')
pylab.close('all')
