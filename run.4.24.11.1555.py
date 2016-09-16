import numpy as np
import matplotlib
import matplotlib.pylab as pylab
import math as m

#5281,1757,1324+3059,1324+3011,1604A,1604B

siglet = u'\u03c3'
names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1604A','Cl1604B'])

Temps = np.array([4.95,3.75,3.6,3.71,3.50,1.64])
TerrU = np.array([0.99,1.00,3.5,1.44,1.82,0.65])
TerrD = np.array([0.74,0.68,1.56,0.94,1.08,0.45])
sigma = np.array([921,652,880,914,619,811])
sigerr = np.array([76,123,124,137,96,76])

lineslope = (m.log(2146)-m.log(308))/(m.log(20))
lineb = m.log(308)
expb = 308.0
lineX = (np.arange(10000)+5)*(10.0/10000)
lineY = expb*lineX**lineslope


pylab.xlim(1,8)
pylab.ylim(300,1500)
pylab.loglog(lineX,lineY)
pylab.errorbar(Temps, sigma, xerr=[TerrD,TerrU], yerr=[sigerr,sigerr], fmt='ro')
pylab.xlabel('T (keV)')
pylab.ylabel('Vel. Dispersion (km/s)')
for i in range(0,len(Temps)): 
    if i == 0: 
        pylab.text(Temps[i]+0.2,sigma[i]+40,names[i],color='black',weight='extra bold')
    elif i == 2:
        pylab.text(Temps[i]+0.1,sigma[i]-50,names[i],color='black',weight='extra bold')
    elif i == 3:
        pylab.text(Temps[i]-1,sigma[i]+10,names[i],color='black',weight='extra bold')
    else:
        pylab.text(Temps[i],sigma[i],names[i],color='black',weight='extra bold')
pylab.savefig('/home/rumbaugh/paperstuff/sigT.plot.4.24.11.png')
pylab.close('all')

