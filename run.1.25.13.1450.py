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

t_grid = np.arange(int(max(ltime))+3)-1

st1 = time.time()

ltime = (ltime-ltime[0])
#find time delays
BA_delay_d2,BAmud2,BAdispd2,BANeff = chi_squared_min_delays(Aflux,Bflux,ltime,ltime,Aerr,Berr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([5]),output=3,use_overlap_mean=True,ALAG=ALAG)
t1 = time.time()
print "33%% Done. Elapsed Time: %f seconds"%(t1-st1)
if not justone:
    BC_delay_d2,BCmud2,BCdispd2,BANeff = chi_squared_min_delays(Cflux,Bflux,ltime,ltime,Cerr,Berr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([5]),output=3,use_overlap_mean=True,ALAG=CLAG)
    t2 = time.time()
    print "66%% Done. Elapsed Time: %f seconds"%(t2-st1)
    BD_delay_d2,BDmud2,BDdispd2,BANeff = chi_squared_min_delays(Dflux,Bflux,ltime,ltime,Derr,Berr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([5]),output=3,use_overlap_mean=True,ALAG=DLAG)
print "\n\nB-A:\nD_2 delay: %4.1f days  mu: %6.4f   chi^2: %f\nD_4_2:"%(BA_delay_d2,BAmud2,BAdispd2)
if not justone: print "\n\nB-C:\nD_2 delay: %4.1f days  mu: %6.4f   chi^2: %f\nD_4_2:"%(BC_delay_d2,BCmud2,BCdispd2)
if not justone: print "\n\nB-D:\nD_2 delay: %4.1f days  mu: %6.4f   chi^2: %f\nD_4_2:"%(BD_delay_d2,BDmud2,BDdispd2)
t3 = time.time()
print "All Done. Elapsed Time: %f seconds"%(t3-st1)
FILE = open("output.chi_squared_delays.1.25.13.dat",'w')
FILE.write("\n\nB-A:\nD_2 delay: %4.1f days  mu: %6.4f   chi^2: %f\nD_4_2:"%(BA_delay_d2,BAmud2,BAdispd2))
if not justone: FILE.write("\n\nB-C:\nD_2 delay: %4.1f days  mu: %6.4f   chi^2: %f\nD_4_2:"%(BC_delay_d2,BCmud2,BCdispd2))
if not justone: FILE.write("\n\nB-D:\nD_2 delay: %4.1f days  mu: %6.4f   chi^2: %f\nD_4_2:"%(BD_delay_d2,BDmud2,BDdispd2))
FILE.write('Total Elapse Time: %f seconds'%(t3-st1))
FILE.close()
