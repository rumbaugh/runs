import numpy as np
import matplotlib
import matplotlib.pylab as pylab
import math as m
try:
    t3013
except NameError:
    t3013 = 300

#5281,1757,1324+3059,1324+3011,1604A,1604B

names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B'])
ncnts = np.array([670,298,96,212,108,219,69])

crl = read_file('/home/rumbaugh/paperstuff/clus.lums.soft.6.22.11.dat')
lums = get_colvals(crl,'col2')/10.0
lumes = get_colvals(crl,'col3')/10.0

crl = read_file('/home/rumbaugh/paperstuff/clus.lums.bol.6.22.11.dat')
lumbol = get_colvals(crl,'col1')

lumboles = np.zeros(len(lums))
for i in range(0,len(lumbol)): lumboles[i] = lumes[i]*lumbol[i]/lums[i]

Temps = np.array([4.95,3.75,3.6,3.71,t3013,3.50,1.64])
TerrU = np.array([0.99,1.00,3.5,1.44,10,1.82,0.65])
TerrD = np.array([0.74,0.68,1.56,0.94,2.99,1.08,0.45])
sigma = np.array([921,652,880,914,819,619,811])
sigerr = np.array([76,123,124,137,242,96,76])

lineslope = (m.log(200)-m.log(0.1))/(m.log(1800)-m.log(429))
lineb = m.log(200)-lineslope*m.log(1800)
expb = m.exp(lineb)
lineX = (np.arange(10000)+1)/3.0
lineY = expb*lineX**lineslope


pylab.ylim(0.0999,105)
pylab.xlim(300,1500)
pylab.loglog(lineX,lineY)
pylab.errorbar(sigma, lumbol, xerr=[sigerr,sigerr],yerr=[lumboles,lumboles],fmt='ro')
pylab.xlabel('Velocity Dispersion (km/s)')
pylab.ylabel('Bolometric X-ray Luminosity (1e44 erg/s)')
for i in range(0,len(Temps)): 
    if i == 0: 
        pylab.text(sigma[i]+0.2,lumbol[i]+0.0040,names[i],color='black',weight='extra bold')
    elif i == 2:
        pylab.text(sigma[i]+0.1,lumbol[i]-0.005,names[i],color='black',weight='extra bold')
    elif i == 4:
        pylab.text(sigma[i]+20,lumbol[i]+0.02,names[i],color='black',weight='extra bold')
    elif i == 6:
        pylab.text(sigma[i]-150,lumbol[i]+0.022,names[i],color='black',weight='extra bold')
    else:
        pylab.text(sigma[i],lumbol[i],names[i],color='black',weight='extra bold')
pylab.savefig('/home/rumbaugh/paperstuff/sigLx.plot.6.22.11.png')
pylab.close('all')

