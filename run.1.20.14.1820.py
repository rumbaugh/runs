import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

execfile("/home/rumbaugh/chi_squared_min.py")

try:
    trials
except NameError:
    trials = 1000000

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
    justone = False
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
    maxtimestep = 60
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

try:
    bwidth
except NameError:
    bwidth = 10.

execfile("/home/rumbaugh/Load1938.py")
ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()

Cflux = C1flux+C2flux
Cerr = np.zeros(len(Cflux))
for i in range(0,len(Cerr)): Cerr[i] = m.sqrt((C1err[i])**2+(C2err[i])**2)

st = time.time()
ltime = (ltime-ltime[0])/86400
#find time delays
BA_disp_mat = np.zeros(1000)
delta = 17.5
BC_disp_mat = np.zeros(1000)

color_arr = ['blue','red','green','purple']

plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

fluxdict = {0: Cflux, 1: Bflux, 2: Aflux}
errdict = {0: Cerr, 1: Berr, 2: Aerr}
imgname = {0: 'C', 1: 'B', 2: 'A'}

#t_grid = np.arange(int(max(ltime))+3)-1
t_grid = None

ttmp,mtmp,BA_disp,neff = chi_squared_min_delays(Cflux,Bflux,ltime,ltime,Cerr,Berr,t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_function='gauss',smooth_param=np.array([bwidth.]),use_overlap_mean=True,outfile='/home/rumbaugh/EVLA/light_curves/Dispersions/Chisq_grid_out.1938.1.20.14.dat',dotime=True,use_cov_matrix=True,write_cov_matrix=True)
