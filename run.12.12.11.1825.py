import numpy as np
import matplotlib
import matplotlib.pylab as pylab
import math as m
execfile("/home/rumbaugh/LinReg.py")
try:
    t3013
except NameError:
    t3013 = 300
try:
    Bvar
except NameError:
    Bvar = 0

html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FFCC00'

#5281,1757,1324+3059,1324+3011,1604A,1604B

pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)

names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','RXJ0910+5422','RXJ0910+5419'])
names2 = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])
#ncnts = np.array([670,298,96,212,108,219,69])

crc = read_file("/home/rumbaugh/cosmocalc_out.9.7.11.nh.dat")
Hz = get_colvals(crc,'col5')*0.7
Hz = np.append(Hz,Hz[len(Hz)-1])
Ez = Hz/70.0
mpc = get_colvals(crc,'col12')*0.7
mpc = np.append(mpc,mpc[len(mpc)-1])
mpccm = get_colvals(crc,'col13')*0.7
mpccm = np.append(mpccm,mpccm[len(mpccm)-1])
lumdists = get_colvals(crc,'col9')/0.7
lumdists = np.append(lumdists,lumdists[len(lumdists)-1])
lumdistcm = lumdists*3.09e24
lumdistmod = lumdists*3.09
fourpiDL2 = 1e-57*get_colvals(crc,'col10')/(0.7*0.7)
fourpiDL2 = np.append(fourpiDL2,fourpiDL2[len(fourpiDL2)-1])

crl = read_file('/home/rumbaugh/paperstuff/clus.lums.soft.9.22.11.dat')
lums = get_colvals(crl,'col2')/10.0
lumes = get_colvals(crl,'col3')/10.0

crl = read_file('/home/rumbaugh/paperstuff/clus.lums.bol.9.22.11.dat')
lumbol = get_colvals(crl,'col1')
lumbolnoE = lumbol*Ez
lumboles = np.zeros(len(lumbol))
for i in range(0,len(lumbol)): lumboles[i] = lumes[i]*lumbol[i]/lums[i]
lumbolenoE = lumboles*Ez


Temps = np.array([4.95,3.75,3.6,3.71,t3013,3.50,1.64,4.50,2.52])
TerrU = np.array([0.99,1.00,3.5,1.44,100,1.82,0.65,1.07,0.59])
TerrD = np.array([0.74,0.68,1.56,0.94,2.99,1.08,0.45,0.78,0.48])
sigma = np.array([921,652,880,914,819,619,811,675,1028])
sigerr = np.array([76,123,124,137,242,96,76,190,140])
sigma2 = np.array([921,652,880,914,819,619,811,1028,675])
sigerr2 = np.array([76,123,124,137,242,96,76,140,190])
Temps2 = np.array([4.95,3.75,3.6,3.71,t3013,3.50,1.64,2.52,4.50])
TerrU2 = np.array([0.99,1.00,3.5,1.44,10,1.82,0.65,0.59,1.07])
TerrD2 = np.array([0.74,0.68,1.56,0.94,2.99,1.08,0.45,0.48,0.78])

lineslope = (m.log(1125)-m.log(0.1))/(m.log(20)-m.log(1.333333))
lineb = m.log(1125)-lineslope*m.log(20)
expb = m.exp(lineb)
expb = 3.11/(0.7*0.7)
lineslope = 2.64
lineX = (np.arange(10000)+1)*(10.0/10000)
lineY = expb*(lineX/6.0)**lineslope
predL = Ez*expb*(Temps/6.0)**lineslope
predT = 6*(lumbol/expb)**(1.0/lineslope)


logEz = np.zeros(len(Ez))
loglumbolnoE = np.zeros(len(lumbol))
logTemps = np.zeros(len(Temps))
for ii in range(0,len(Temps)):
    logEz[ii] = m.log(Ez[ii])
    loglumbolnoE[ii] = m.log(lumbolnoE[ii])
    logTemps[ii] = m.log(Temps[ii])

logEzfit,loglumbolnoEfit,lumbolenoEfit,logTempsfit,TerrDfit,TerrUfit,Tempsfit,Ezfit,lumbolfit,lumbolnoEfit = np.zeros(len(Ez)-3),np.zeros(len(Ez)-3),np.zeros(len(Ez)-3),np.zeros(len(Ez)-3),np.zeros(len(Ez)-3),np.zeros(len(Ez)-3),np.zeros(len(Ez)-3),np.zeros(len(Ez)-3),np.zeros(len(Ez)-3),np.zeros(len(Ez)-3)
jjcnt = 0
for jj in range(0,len(logEz)):
    if ((jj != 4) & (jj != 6) & (jj != 7)): 
        logEzfit[jjcnt] = logEz[jj]
        lumbolenoEfit[jjcnt] = lumbolenoE[jj]
        loglumbolnoEfit[jjcnt] = loglumbolnoE[jj]
        logTempsfit[jjcnt] = logTemps[jj]
        Tempsfit[jjcnt],TerrUfit[jjcnt],TerrDfit[jjcnt] = Temps[jj],TerrU[jj],TerrD[jj]
        Ezfit[jjcnt],lumbolnoEfit[jjcnt],lumbolfit[jjcnt] = Ez[jj],lumbolnoE[jj],lumbol[jj]
        jjcnt += 1

A,B,errA,errB = LinReg(logEzfit,loglumbolnoEfit,logTempsfit,wz=Tempsfit*Tempsfit*(0.5*(TerrDfit+TerrUfit))**-2,numvar=3,C=1.0/2.64,err=1)
#A,B,errA,errB = LinReg(logEz,loglumbolnoE,logTemps,wy=lumbolnoE*lumbolnoE/lumbolenoE/lumbolenoE,wz=Temps*Temps*(0.5*(TerrD+TerrU))**-2,numvar=3,C=1.0/2.64,err=1)
print A,B,errA,errB
predLfit = (Temps*m.exp(-A)*Ez**B)**2.64
predTfit = m.exp(A)*Ez**B*lumbolnoE**(1.0/2.64)

lineY3 = m.exp(-2.64*A)*(lineX)**2.64
pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.xlim(1,8)
pylab.ylim(0.05,15)
pylab.loglog(lineX,lineY3)
dummyX = [100000,100000]
dummyY = [100000,100000]
pylab.scatter(dummyX,dummyY,color='red')
pylab.scatter(dummyX,dummyY,color='blue')
pylab.scatter(dummyX,dummyY,color=html_brwn)
pylab.scatter(dummyX,dummyY,color=html_teal)
pylab.legend(('fit','-5.4','+0','-0.23','-1'),loc=3,markerscale=0.8,labelspacing=0.3)
pylab.errorbar(Tempsfit, lumbolnoEfit*Ezfit**(2.64*(B)), xerr=[TerrDfit,TerrUfit],yerr=[lumbolenoEfit*Ezfit**(2.64*(B)),lumbolenoEfit*Ezfit**(2.64*(B))],fmt='ro',lw=1,capsize=3,mew=1,label='_nolegend_')
pylab.errorbar(Tempsfit, lumbolnoEfit*Ezfit**(0), xerr=[TerrDfit,TerrUfit],yerr=[lumbolenoEfit*Ezfit**(-0),lumbolenoEfit*Ezfit**(-0)],color='blue',fmt='ro',lw=1,capsize=3,mew=1,label='_nolegend_')
pylab.errorbar(Tempsfit, lumbolnoEfit*Ezfit**(-0.23), xerr=[TerrDfit,TerrUfit],yerr=[lumbolenoEfit*Ezfit**(-0.23),lumbolenoEfit*Ezfit**(-0.23)],color=html_brwn,fmt='ro',lw=1,capsize=3,mew=1,label='_nolegend_')
pylab.errorbar(Tempsfit, lumbolnoEfit*Ezfit**(-1), xerr=[TerrDfit,TerrUfit],yerr=[lumbolenoEfit*Ezfit**(-1),lumbolenoEfit*Ezfit**(-1)],color=html_teal,fmt='ro',lw=1,capsize=3,mew=1,label='_nolegend_')
pylab.xlabel('T')
pylab.ylabel('Lx E(z)^gamma')
pylab.savefig('/home/rumbaugh/LxTtest.12.15.11.png')
pylab.close('all')


pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.xlim(1.4,2)
pylab.ylim(1.1,10.0)
pylab.loglog(lineX,lineY,lw=2)
pylab.scatter(Ezfit,lumbolnoEfit,c='red')
pylab.xlabel('E(z)')
pylab.ylabel('Lx')
pylab.savefig('/home/rumbaugh/LvsEz.12.15.11.png')
pylab.close('all')
pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.xlim(1,8)
pylab.ylim(1.4,2.0)
pylab.loglog(lineX,lineY,lw=2)
pylab.scatter(Tempsfit,Ezfit,c='red')
pylab.xlabel('T')
pylab.ylabel('E(z)')
pylab.savefig('/home/rumbaugh/TvsEz.12.15.11.png')
pylab.close('all')
pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.xlim(1,8)
pylab.ylim(1.1,10.0)
pylab.loglog(lineX,lineY,lw=2)
pylab.scatter(Tempsfit,lumbolnoEfit,c='red')
pylab.xlabel('T')
pylab.ylabel('Lx')
pylab.savefig('/home/rumbaugh/LvsTnoE.12.15.11.png')
pylab.close('all')
pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.ylim(-0.2,0.2)
pylab.xlim(1.4,1.9)
pylab.scatter(Ez,(lumbolnoE-predL)/predL,c='red')
print lumbolnoE-predL
pylab.scatter(Ez,(lumbolnoE-predLfit)/predLfit,c='blue')
print lumbolnoE-predLfit
pylab.xlabel('E(z)')
pylab.ylabel('Offset from expected Lx')
pylab.savefig('/home/rumbaugh/L_offset_12.14.11.png')
pylab.close('all')
pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.ylim(-0.2,0.2)
pylab.xlim(1.4,1.9)
pylab.scatter(Ez,(Temps-predT)/predT,c='red')
print Temps-predT
pylab.scatter(Ez,(Temps-predTfit)/predTfit,c='blue')
print Temps-predTfit
pylab.xlabel('E(z)')
pylab.ylabel('Offset from expected T')
pylab.savefig('/home/rumbaugh/T_offset_12.14.11.png')
pylab.close('all')

lineY2 = m.exp(-A*2.64)*Ez**(-B*2.64)*Temps**2.64

pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.xlim(1,8)
pylab.ylim(0.5,7.5)
pylab.loglog(lineX,lineY,lw=2)
pylab.scatter(Temps,lineY2)
pylab.errorbar(Temps, lumbol, xerr=[TerrD,TerrU],yerr=[lumboles,lumboles],fmt='ro',lw=2,capsize=5,mew=2)
pylab.xlabel('T (keV)',fontsize='16')
pylab.ylabel('Bolometric X-ray Luminosity (10$^{44}$ erg s$^{-1}$)',fontsize='16')
for i in range(0,len(Temps)): 
    if i == 0: 
        pylab.text(Temps[i]-1.2,lumbol[i]+0.12,names[i],color='black',weight='extra bold')
    elif i == 1: 
        pylab.text(Temps[i]-0.9,lumbol[i]+0.10,names[i],color='black',weight='extra bold')
    elif i == 2:
        pylab.text(Temps[i]+0.1,lumbol[i]+0.005,names[i],color='black',weight='extra bold')
    elif i == 3:
        pylab.text(Temps[i]+0.18,lumbol[i]-0.17,names[i],color='black',weight='extra bold')
    elif i == 5:
        pylab.text(Temps[i]-0.85,lumbol[i]-0.2,names[i],color='black',weight='extra bold')
    elif i == 6:
        pylab.text(Temps[i]+0.05,lumbol[i]+0.022,names[i],color='black',weight='extra bold')
    elif i == 8:
        pylab.text(Temps[i]-0.95,lumbol[i]+0.022,names[i],color='black',weight='extra bold')
    else:
        pylab.text(Temps[i]+0.15,lumbol[i]+0.1,names[i],color='black',weight='extra bold')
pylab.savefig('/home/rumbaugh/LxT.plot.bol.12.12.11.png')
pylab.close('all')

lineslope = (m.log(200)-m.log(0.1))/(m.log(1800)-m.log(429))
lineb = m.log(200)-lineslope*m.log(1800)
expb = m.exp(lineb)
expb = 0.01*10**(-13.68)*(7/5.0)**(5.3)
lineslope = 5.30
lineX = (np.arange(10000)+1)/3.0
lineY = expb*lineX**lineslope



pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.ylim(0.5,7.5)
pylab.xlim(450,1200)
pylab.loglog(lineX,lineY,lw=2)
pylab.errorbar(sigma, lumbol, xerr=[sigerr,sigerr],yerr=[lumboles,lumboles],fmt='ro',lw=2,capsize=5,mew=2)
pylab.xlabel('Velocity Dispersion (km s$^{-1}$)',fontsize=16)
pylab.ylabel('Bolometric X-ray Luminosity (10$^{44}$ erg s$^{-1}$)',fontsize=16)
for i in range(0,len(Temps)): 
    if i == 0: 
        pylab.text(sigma[i]+20,lumbol[i]+0.1,names[i],color='black',weight='extra bold')
    elif i == 5: 
        pylab.text(sigma[i]-80,lumbol[i]-0.17,names[i],color='black',weight='extra bold')
    elif i == 3:
        pylab.text(sigma[i]-170,lumbol[i]-0.14,names[i],color='black',weight='extra bold')
    elif i == 4:
        pylab.text(sigma[i]+20,lumbol[i]+0.02,names[i],color='black',weight='extra bold')
    elif i == 6:
        pylab.text(sigma[i]-95,lumbol[i]+0.022,names[i],color='black',weight='extra bold')
    elif i == 7:
        pylab.text(sigma[i]+10,lumbol[i]+0.05,names[i],color='black',weight='extra bold')
    elif i == 8:
        pylab.text(sigma[i]-59,lumbol[i]-0.25,names[i],color='black',weight='extra bold')
    else:
        pylab.text(sigma[i]+10,lumbol[i]+0.05,names[i],color='black',weight='extra bold')
#pylab.savefig('/home/rumbaugh/sigLx.plot.11.2.11.png')
pylab.close('all')

lineslope = (m.log(2146)-m.log(308))/(m.log(20))
lineb = m.log(308)
expb = 308.0
expb = 10**2.49
lineslope=0.65
lineX = (np.arange(10000)+5)*(10.0/10000)
lineY = expb*lineX**lineslope

pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.xlim(1,8)
pylab.ylim(450,1200)
pylab.loglog(lineX,lineY,lw=2)
pylab.errorbar(Temps, sigma, xerr=[TerrD,TerrU], yerr=[sigerr,sigerr], fmt='ro',lw=2,capsize=5,mew=2)
pylab.xlabel('T (keV)',fontsize='16')
pylab.ylabel('Vel. Dispersion (km s$^{-1}$)',fontsize='16')
for i in range(0,len(Temps)): 
    if i == 0: 
        pylab.text(Temps[i]-0.6,sigma[i]+10,names[i],color='black',weight='extra bold')
    elif i == 2:
        pylab.text(Temps[i]-1.23,sigma[i]-30,names[i],color='black',weight='extra bold')
    elif i == 3:
        pylab.text(Temps[i]-1.3,sigma[i]+10,names[i],color='black',weight='extra bold')
    elif i == 7:
        pylab.text(Temps[i]+0.05,sigma[i]+10,names[i],color='black',weight='extra bold')
    elif i == 8:
        pylab.text(Temps[i]+0.08,sigma[i]+13,names[i],color='black',weight='extra bold')
    elif i == 5:
        pylab.text(Temps[i]-0.82,sigma[i]-20,names[i],color='black',weight='extra bold')
    elif i == 1:
        pylab.text(Temps[i]+0.07,sigma[i]-25,names[i],color='black',weight='extra bold')
    else:
        pylab.text(Temps[i]+0.05,sigma[i]+10,names[i],color='black',weight='extra bold')
#pylab.savefig('/home/rumbaugh/sigT.plot.11.2.11.png')
pylab.close('all')
