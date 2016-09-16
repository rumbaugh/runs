import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/chi_squared_min.py")

try:
    ALAG
except NameError:
    ALAG = 31.5
try:
    CLAG
except NameError:
    CLAG = 36.5
try:
    DLAG
except NameError:
    DLAG = 80.5
try:
    justone
except NameError:
    justone = True
try:
    timestep
except NameError:
    timestep = 0.5
try:
    mustep
except NameError:
    mustep = 0.001
try:
    maxtimestep
except NameError:
    maxtimestep = 119
try:
    maxmu
except NameError:
    maxmu = 1.05
try:
    minmu
except NameError:
    minmu = 0.95
load1608 = np.loadtxt('/home/rumbaugh/B1938+666_files/1608_g.ab922_nh')
ltime = load1608[:,0].copy()
Aflux,Bflux,Cflux,Dflux,Aerr,Berr,Cerr,Derr = load1608[:,1].copy(),load1608[:,2].copy(),load1608[:,3].copy(),load1608[:,4].copy(),load1608[:,5].copy(),load1608[:,6].copy(),load1608[:,7].copy(),load1608[:,8].copy()
#Aerr,Berr,Cerr,Derr = Aerr**0.5,Berr**0.5,Cerr**0.5,Derr**0.5

Anflux,Bnflux,Cnflux,Dnflux = Aflux/np.average(Aflux),Bflux/np.average(Bflux),Cflux/np.average(Cflux),Dflux/np.average(Dflux)
Aavgerr,Bavgerr,Cavgerr,Davgerr = m.sqrt(np.sum(Aerr*Aerr))/len(Aerr),m.sqrt(np.sum(Berr*Berr))/len(Berr),m.sqrt(np.sum(Cerr*Cerr))/len(Cerr),m.sqrt(np.sum(Derr*Derr))/len(Derr)
Anerr,Bnerr,Cnerr,Dnerr = np.zeros(len(Aflux)),np.zeros(len(Aflux)),np.zeros(len(Aflux)),np.zeros(len(Aflux))
for i in range(0,len(Aerr)):
    Anerr[i],Bnerr[i],Cnerr[i],Dnerr[i] = Anflux[i]*m.sqrt((Aerr[i]/Aflux[i])**2+(Aavgerr/np.average(Aflux))**2),Bnflux[i]*m.sqrt((Berr[i]/Bflux[i])**2+(Bavgerr/np.average(Bflux))**2),Cnflux[i]*m.sqrt((Cerr[i]/Cflux[i])**2+(Cavgerr/np.average(Cflux))**2),Dnflux[i]*m.sqrt((Derr[i]/Dflux[i])**2+(Davgerr/np.average(Dflux))**2)

st1 = time.time()

ltime = (ltime-ltime[0])
t_grid = np.arange(int(max(ltime))+3)-1
#find time delays
chisqmatAB,tau_out,mu_out,min_chisq,Neff,mu0 = chi_squared_min_delays(Aflux,Bflux,ltime,ltime,Aerr,Berr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([10.]),output=5,use_overlap_mean=True,ALAG=ALAG,chisqmatrix=True)
pylab.imshow(chisqmatAB,extent=[minmu,maxmu,-1*maxtimestep,maxtimestep],aspect='auto',origin='lower')
pylab.savefig('/home/rumbaugh/chisq_plot.1608_delay_AB.2.7.13.png')
pylab.close()
t1 = time.time()
print 'AB delay: %4.1f days   mu = %f\n'%(tau_out,mu_out)
print "33%% Done. Elapsed Time: %f seconds"%(t1-st1)
if not justone:
    chisqmatBC,tau_out,mu_out,min_chisq,Neff,mu0 = chi_squared_min_delays(Cflux,Bflux,ltime,ltime,Cerr,Berr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([10.]),output=5,use_overlap_mean=True,ALAG=CLAG,chisqmatrix=True)
    pylab.imshow(chisqmatBC,extent=[minmu,maxmu,-1*maxtimestep,maxtimestep],aspect='auto',origin='lower')
    pylab.savefig('/home/rumbaugh/chisq_plot.1608_delay_BC.2.7.13.png')
    pylab.close()
    t2 = time.time()
    print 'BC delay: %4.1f days   mu = %f\n'%(tau_out,mu_out)
    print "66%% Done. Elapsed Time: %f seconds"%(t2-st1)
    chisqmatBD,tau_out,mu_out,min_chisq,Neff,mu0 = chi_squared_min_delays(Dflux,Bflux,ltime,ltime,Derr,Berr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([10.]),output=5,use_overlap_mean=True,ALAG=DLAG,chisqmatrix=True)
    pylab.imshow(chisqmatBD,extent=[minmu,maxmu,-1*maxtimestep,maxtimestep],aspect='auto',origin='lower')
    pylab.savefig('/home/rumbaugh/chisq_plot.1608_delay_BD.2.7.13.png')
    pylab.close()
    print 'BD delay: %4.1f days   mu = %f\n'%(tau_out,mu_out)
t3 = time.time()
print "All Done. Elapsed Time: %f seconds"%(t3-st1)
