from numpy import *
from scipy import *
from pylab import *
import scipy.optimize
import leastsq
import fitmodel

#this shows two methods to use python to fit models to the surface brightness data for RXJ1821

cr = np.loadtxt('DE_counts_profile.RXJ1821.10.16.12.dat')
ann = cr[:,1]
SB = cr[:,4]
SBerr = cr[:,6]

#background fixed from last two data points
bkginit = average(SB[len(SB)-2:len(SB)])

#fit with fixed core radius
fitfunc = lambda p, x: p[0]*(1+x**2/(23.814**2))**(-1.5)+bkginit
errfunc = lambda p, x, y:(fitfunc(p,x)-y)/SBerr
p0 = [0.3]
# subtracted 5 from annulus measurements because ann is the outer radius of the annulus
p1, success = scipy.optimize.leastsq(errfunc, p0[:], args=(ann-5.0, SB))
time = linspace(0, ann.max()+50, 100)
plot(ann-5, SB, "ro", time, fitfunc([p1], time), "g-")

#fit with floating core radius
fitfunc = lambda p, x: p[0]*(1+x**2/(p[1]**2))**(-1.5)+bkginit
errfunc = lambda p, x, y:(fitfunc(p,x)-y)/SBerr
p0 = [0.3,23.814]
# subtracted 5 from annulus measurements because ann is the outer radius of the annulus
p1, success = scipy.optimize.leastsq(errfunc, p0[:], args=(ann-5.0, SB))
plot(ann-5, SB, "ro", time, fitfunc(p1, time), "r-")

#last two fits don't calculate errors on fitted parameters, nor does it calculate goodness of fit. I found a script online that does calculate these, which is called leastsqs.py

def model(x,p):
    a0 = p[0]
    a1 = p[1]
    return a0*(1+x**2/(a1**2))**(-1.5)+bkginit
p1, chisq, covar, success = leastsq.leastsq(model,p0,ann-5.0,SB,SBerr,fullOutput=True)

def model2(x,a0):
    return a0*(1+x**2/(23.814**2))**(-1.5)+bkginit
fitfunc = lambda p, x: p[0]*(1+x**2/(23.814**2))**(-1.5)+bkginit
p0 = [0.01]
p2, chisq2, covar2, success2 = leastsq.leastsq(model2,0.3,ann-5.0,SB,SBerr,fullOutput=True)

p0 = [0.3,23.814]
fit = fitmodel.FitModel(ann-5,SB,SBerr,model,fitmodel.ChiSqStat,p0)
