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
    lens
except NameError:
    lens = '1030'

execfile("/home/rumbaugh/LoadVLA_2001.py")
ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)

Aflux,Bflux = flux_arr[0],flux_arr[1]
Aerr,Berr = flux_err_arr[0],flux_err_arr[1]

if lens == '0712': 
    Aflux += Bflux
    Aerr = np.sqrt(Aerr**2+Berr**2)
    Bflux,Berr = flux_arr[2],flux_err_arr[2]

st = time.time()
ltime = (ltime-ltime[0])#/86400
#find time delays
BA_disp_mat = np.zeros(1000)
delta = 17.5
g = np.arange(len(ltime))[:len(ltime)-10]
if lens == '1938':
    maxtimestep = 60.
else:
    maxtimestep = 105.

t_grid = np.arange(int(max(ltime[g])-min(ltime[g]))+3)-1

ttmp,mtmp,BA_disp,nefft = chi_squared_min_delays(Aflux[g],Bflux[g],ltime[g],ltime[g],Aerr[g],Berr[g],t_grid,maxtimestep,timestep,minmu,maxmu,mustep,smooth_function='gauss',smooth_param=np.array([10.]),use_overlap_mean=True,outfile='/home/rumbaugh/EVLA/light_curves/Dispersions/test.Chisq_grid_out.%s.11.14.13.dat'%lens,dotime=True)
