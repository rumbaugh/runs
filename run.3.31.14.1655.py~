import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

execfile("/home/rumbaugh/radmon_var_chisq_test.py")

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

date = '3.15.14'

execfile("/home/rumbaugh/LoadVLA_2001.py")
ltime,flux_arr,flux_err_arr = LoadVLA_2001('0414')

A1flux,A2flux,Bflux,Cflux = flux_arr[0],flux_arr[1],flux_arr[2],flux_arr[3]
A1err,A2err,Berr,Cerr = flux_err_arr[0],flux_err_arr[1],flux_err_arr[2],flux_err_arr[3]

st = time.time()
ltime = (ltime-ltime[0])#/86400
#find time delays
BA_disp_mat = np.zeros(1000)
delta = 10.5
BC_disp_mat = np.zeros(1000)

color_arr = ['blue','red','green','purple']

plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

fluxdict = {0: A1flux, 1: A2flux, 2: Cflux}
errdict = {0: A1err, 1: A2err, 2: Cerr}
imgname = {0: 'A1', 1: 'A2', 2: 'C'}

gAonly = np.where(ltime < 1946-1839)[0]

for imgnum in [0,1,2]:
    FILE = open('/home/rumbaugh/EVLA/light_curves/Dispersions/delta_var.0414_B%s.%s.dat'%(imgname[imgnum],date),'w')
    FILE2 = '/home/rumbaugh/EVLA/light_curves/Dispersions/dispmat.delta_var.0414_B%s.D_2.%s.dat'%(imgname[imgnum],date)
    dispmat,ttmp,mtmp,BA_disp = calc_disp_delay(fluxdict[imgnum],Bflux,ltime,ltime,errdict[imgnum],Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=3,simplemuerr=True,dispmatrix=True,outfile=FILE2)
    FILE.write('%4.1f %4.1f %f %E\n'%(0.0,ttmp,mtmp,BA_disp))
    for delta in np.arange(18)+2.5:
        FILE2 = '/home/rumbaugh/EVLA/light_curves/Dispersions/dispmat.delta_var.0414_B%s.D_4_2.delta_%.1f.%s.dat'%(imgname[imgnum],delta,date)
        dispmat,ttmp,mtmp,BA_disp = calc_disp_delay(fluxdict[imgnum],Bflux,ltime,ltime,errdict[imgnum],Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta,dispmatrix=True,output=3,simplemuerr=True,outfile=FILE2)
        FILE.write('%4.1f %4.1f %f %E\n'%(delta,ttmp,mtmp,BA_disp))
    FILE.close()

    #Now only using A configuration data

    FILE = open('/home/rumbaugh/EVLA/light_curves/Dispersions/delta_var.0414_B%s.VLA_A_only.%s.dat'%(imgname[imgnum],date),'w')
    FILE2 = '/home/rumbaugh/EVLA/light_curves/Dispersions/dispmat.delta_var.0414_B%s.VLA_A_only.D_2.%s.dat'%(imgname[imgnum],date)
    dispmat,ttmp,mtmp,BA_disp = calc_disp_delay(fluxdict[imgnum][gAonly],Bflux[gAonly],ltime[gAonly],ltime[gAonly],errdict[imgnum][gAonly],Berr[gAonly],maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=3,simplemuerr=True,dispmatrix=True,outfile=FILE2)
    FILE.write('%4.1f %4.1f %f %E\n'%(0.0,ttmp,mtmp,BA_disp))
    for delta in np.arange(18)+2.5:
        FILE2 = '/home/rumbaugh/EVLA/light_curves/Dispersions/dispmat.delta_var.0414_B%s.VLA_A_only.D_4_2.delta_%.1f.%s.dat'%(imgname[imgnum],delta,date)
        dispmat,ttmp,mtmp,BA_disp = calc_disp_delay(fluxdict[imgnum][gAonly],Bflux[gAonly],ltime[gAonly],ltime[gAonly],errdict[imgnum][gAonly],Berr[gAonly],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta,dispmatrix=True,output=3,simplemuerr=True,outfile=FILE2)
        FILE.write('%4.1f %4.1f %f %E\n'%(delta,ttmp,mtmp,BA_disp))
    FILE.close()
