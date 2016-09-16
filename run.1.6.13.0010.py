import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab

execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/smoothing_1d.py")
execfile("/home/rumbaugh/chi_squared_min.py")

try:
    justone
except NameError:
    justone = False
try:
    skipahead
except NameError:
    skipahead = 0
try:
    init
except NameError:
    init = 0
try:
    fluxratio_err
except NameError:
    fluxratio_err = 0.0095

try:
    timestep
except NameError:
    timestep = 1.0
try:
    mustep
except NameError:
    mustep = 0.001
try:
    maxtimestep
except NameError:
    maxtimestep = 117*timestep
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

load1608 = np.loadtxt('/home/rumbaugh/B1938+666_files/1608_g.ab922_nh')
ltime = load1608[:,0].copy()
Aflux,Bflux,Cflux,Dflux,Aerr,Berr,Cerr,Derr = load1608[:,1].copy(),load1608[:,2].copy(),load1608[:,3].copy(),load1608[:,4].copy(),load1608[:,5].copy(),load1608[:,6].copy(),load1608[:,7].copy(),load1608[:,8].copy()

Anflux,Bnflux,Cnflux,Dnflux = Aflux/np.average(Aflux),Bflux/np.average(Bflux),Cflux/np.average(Cflux),Dflux/np.average(Dflux)
Aavgerr,Bavgerr,Cavgerr,Davgerr = m.sqrt(np.sum(Aerr*Aerr))/len(Aerr),m.sqrt(np.sum(Berr*Berr))/len(Berr),m.sqrt(np.sum(Cerr*Cerr))/len(Cerr),m.sqrt(np.sum(Derr*Derr))/len(Derr)
Anerr,Bnerr,Cnerr,Dnerr = np.zeros(len(Aflux)),np.zeros(len(Aflux)),np.zeros(len(Aflux)),np.zeros(len(Aflux))
for i in range(0,len(Aerr)):
    Anerr[i],Bnerr[i],Cnerr[i],Dnerr[i] = Anflux[i]*m.sqrt((Aerr[i]/Aflux[i])**2+(Aavgerr/np.average(Aflux))**2),Bnflux[i]*m.sqrt((Berr[i]/Bflux[i])**2+(Bavgerr/np.average(Bflux))**2),Cnflux[i]*m.sqrt((Cerr[i]/Cflux[i])**2+(Cavgerr/np.average(Cflux))**2),Dnflux[i]*m.sqrt((Derr[i]/Dflux[i])**2+(Davgerr/np.average(Dflux))**2)

ltime = (ltime-ltime[0])

#find time delays
bcar_widths = np.array([5.,10.,15.])
t_grid = np.arange(int(max(ltime))+3)-1
for i in range(0,len(bcar_widths)):
    BA_delay,BAmu,BAchisq,BAneff = chi_squared_min_delays(Aflux,Bflux,ltime,ltime,Aerr,Berr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([bcar_widths[i]]))
    BC_delay,BCmu,BCchisq,BCneff = chi_squared_min_delays(Cflux,Bflux,ltime,ltime,Cerr,Berr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([bcar_widths[i]]))
    BD_delay,BDmu,BDchisq,BDneff = chi_squared_min_delays(Dflux,Bflux,ltime,ltime,Derr,Berr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_param=np.array([bcar_widths[i]]))
    print "\nBoxcar Width: %i days\n B-A - Delay: %3i days  Mu: %6.4f\nChi^2: %f  Reduced: %f  Neff:%i\n B-C - Delay: %3i days  Mu: %6.4f\nChi^2: %f  Reduced: %f  Neff:%i\n B-D - Delay: %3i days  Mu: %6.4f\nChi^2: %f  Reduced: %f  Neff:%i\n"%(bcar_widths[i],BA_delay,BAmu,BAchisq,BAchisq/BAneff,BAneff,BC_delay,BCmu,BCchisq,BCchisq/BCneff,BCneff,BD_delay,BDmu,BDchisq,BDchisq/BDneff,BDneff)
