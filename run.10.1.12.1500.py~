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

crc = read_file("/home/rumbaugh/cc_out.6.29.12.nh.dat")
rs = get_colvals(crc,'col1')
#rs = np.append(rs,rs[len(rs)-1])

rs = np.array([0.818,0.692,0.696,0.755,0.697,0.898,0.865,1.101,1.103])

Hz = get_colvals(crc,'col5')*0.7
#Hz = np.append(Hz,Hz[len(Hz)-1])
Ez = Hz/70.0
mpc = get_colvals(crc,'col12')*0.7
#mpc = np.append(mpc,mpc[len(mpc)-1])
mpccm = get_colvals(crc,'col13')*0.7
#mpccm = np.append(mpccm,mpccm[len(mpccm)-1])
lumdists = get_colvals(crc,'col9')/0.7
#lumdists = np.append(lumdists,lumdists[len(lumdists)-1])
lumdistcm = lumdists*3.09e24
lumdistmod = lumdists*3.09
fourpiDL2 = 1e-57*get_colvals(crc,'col10')/(0.7*0.7)
#fourpiDL2 = np.append(fourpiDL2,fourpiDL2[len(fourpiDL2)-1])

crl = read_file('/home/rumbaugh/paperstuff/clus.lums.soft.6.29.12.dat')
lums = get_colvals(crl,'col2')/10.0
lumes = get_colvals(crl,'col3')/10.0

crl = read_file('/home/rumbaugh/paperstuff/clus.lums.bol.6.29.12.dat')
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
Ezfit,lumbolfit,Tempsfit = np.zeros(len(Ez)-1),np.zeros(len(Ez)-1),np.zeros(len(Ez)-1)
jjcnt = 0
for jj in range(0,len(Temps)):
    if ((jj != 4)): 
        Ezfit[jjcnt],lumbolfit[jjcnt],Tempsfit[jjcnt] = Ez[jj],lumbol[jj],Temps[jj]
        jjcnt += 1
lineslope = (m.log(1125)-m.log(0.1))/(m.log(20)-m.log(1.333333))
lineb = m.log(1125)-lineslope*m.log(20)
expb = m.exp(lineb)
expb = 3.11/(0.7*0.7)
lineslope = 2.64
lineX = (np.arange(10000)+1)*(10.0/10000)
lineY = expb*(lineX/6.0)**lineslope
#predL = Ezfit*expb*(Tempsfit/6.0)**lineslope
predL = Ezfit*0.112*(Tempsfit/1.0)**2.53
predT = 6*(lumbolfit/expb)**(1.0/lineslope)

crrei = read_file("/home/rumbaugh/reichert_cluster_data.dat")
rei_z = copy_colvals(crrei,'col1')
rei_T = copy_colvals(crrei,'col2')
rei_L = copy_colvals(crrei,'col3')
crreicc = read_file("/home/rumbaugh/reichert_cc_out.nh.dat")
rei_Hz = copy_colvals(crreicc,'col5')*0.7
rei_Ez = rei_Hz/70.0
rei_PL = rei_Ez*0.112*(rei_T)**2.53

logEz = np.zeros(len(Ez))
loglumbolnoE = np.zeros(len(lumbol))
logTemps = np.zeros(len(Temps))
for ii in range(0,len(Temps)):
    logEz[ii] = m.log(Ez[ii])
    loglumbolnoE[ii] = m.log(lumbolnoE[ii])
    logTemps[ii] = m.log(Temps[ii])

rsfit,logEzfit,loglumbolnoEfit,lumbolenoEfit,logTempsfit,TerrDfit,TerrUfit,Tempsfit,Ezfit,lumbolfit,lumbolnoEfit = np.zeros(len(Ez)-1),np.zeros(len(Ez)-1),np.zeros(len(Ez)-1),np.zeros(len(Ez)-1),np.zeros(len(Ez)-1),np.zeros(len(Ez)-1),np.zeros(len(Ez)-1),np.zeros(len(Ez)-1),np.zeros(len(Ez)-1),np.zeros(len(Ez)-1),np.zeros(len(Ez)-1)

jjcnt = 0
for jj in range(0,len(logEz)):
    if ((jj != 4)): 
        logEzfit[jjcnt] = logEz[jj]
        lumbolenoEfit[jjcnt] = lumbolenoE[jj]
        loglumbolnoEfit[jjcnt] = loglumbolnoE[jj]
        logTempsfit[jjcnt] = logTemps[jj]
        Tempsfit[jjcnt],TerrUfit[jjcnt],TerrDfit[jjcnt] = Temps[jj],TerrU[jj],TerrD[jj]
        Ezfit[jjcnt],lumbolnoEfit[jjcnt],lumbolfit[jjcnt] = Ez[jj],lumbolnoE[jj],lumbol[jj]
        rsfit[jjcnt] = rs[jj]
        jjcnt += 1

#A,B,errA,errB = LinReg(logEzfit,loglumbolnoEfit,logTempsfit,wz=Tempsfit*Tempsfit*(0.5*(TerrDfit+TerrUfit))**-2,numvar=3,C=1.0/2.64,err=1)
#A,B,errA,errB = LinReg(logEz,loglumbolnoE,logTemps,wy=lumbolnoE*lumbolnoE/lumbolenoE/lumbolenoE,wz=Temps*Temps*(0.5*(TerrD+TerrU))**-2,numvar=3,C=1.0/2.64,err=1)
#print A,B,errA,errB
#predLfit = (Tempsfit*m.exp(-A)*Ezfit**B)**2.64
#predTfit = m.exp(A)*Ezfit**B*lumbolnoEfit**(1.0/2.64)

#l#ineY3 = m.exp(-2.64*A)*(lineX)**2.64
grel = [5,7]

yerrL = np.zeros(len(Ezfit))
yerrU = np.zeros(len(Ezfit))
for i in range(0,len(yerrU)):
    yerrU[i] = (Ezfit[i]*lumbolnoEfit[i]*0.5*(TerrUfit[i]+TerrDfit[i])*(lineslope*predL[i]/Tempsfit[i])/(predL[i]*predL[i]))
    yerrL[i] = yerrU[i]
    if Ezfit[i]*lumbolnoEfit[i]/predL[i]-yerrU[i] <= 0: yerrL[i] = Ezfit[i]*lumbolnoEfit[i]/predL[i]-0.001

rsplot = np.append(np.zeros(1),rsfit)
Ezplot = np.append(np.ones(1),Ezfit)
rsplot = np.append(rsplot,rei_z[0])
Ezplot = np.append(Ezplot,rei_Ez[0])

dummyX = [100000,100000]
dummyY = [100000,100000]
pylab.rc('axes',linewidth=2)
pylab.rc('font',size=16)
#matplotlib.use('PDF')
#pylab.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
#pylab.rcParams['ps.useafm'] = True
#pylab.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
#pylab.rcParams['pdf.fonttype'] = 42

pylab.fontsize = 18
pylab.tick_params(which='major',length=8,width=2,labelsize=16)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=16)
#pylab.xlim(0.67,1.15)
pylab.xlim(0.35,1.2)
pylab.ylim(0.1,18)
#pylab.semilogy(rsfit,Ezfit**(-B*2.64)*(6**lineslope)/expb/m.exp(2.64*A),color='red')
ga = np.argsort(rsplot)
pylab.semilogy(rsplot[ga],Ezplot[ga]**(-0.23),color='red',ls='--',lw=2)
pylab.semilogy(rsplot[ga],Ezplot[ga],color=html_purp,lw=2)
#pylab.semilogy(rsfit,Ezfit**(B*2.64)*m.exp(2.64*A),color='red')
#pylab.semilogy(rsfit,Ezfit**(-1)*(6**lineslope)/expb,color='blue')
pylab.legend(('Reichert et al. (2011) (E(z)$^{-0.23}$)','self-similar (E(z)$^{+1}$)'),loc=2,frameon=False)
pylab.scatter(rei_z,rei_Ez*rei_L/rei_PL,color='black',s=5)
pylab.errorbar(rsfit,Ezfit*lumbolnoEfit/predL,yerr=[yerrL,yerrU],color='blue',fmt='ro',lw=2,capsize=3,mew=1,ms=12,label='_nolegend_')
print (Ezfit*lumbolnoEfit/predL-Ezfit**(-0.23))/yerrL
print -(Ezfit*lumbolnoEfit/predL-Ezfit)/yerrU
pylab.errorbar(rsfit[grel],Ezfit[grel]*lumbolnoEfit[grel]/predL[grel],yerr=[yerrU[grel],yerrL[grel]],marker='d',fmt='ro',color=html_brwn,lw=3,capsize=3,mew=1,ms=16)
pylab.xlabel('Redshift',fontsize=18)
pylab.ylabel('L/L$_{z=0}$',fontsize=22)
pylab.yticks([0.1,1,10],['0.1','1','10'])
pylab.savefig('/home/rumbaugh/Lx_evol.6.29.12.png')
pylab.close('all')
