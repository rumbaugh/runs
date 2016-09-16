import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

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
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9
try:
    FILE_BA
except NameError:
    FILE_BA = '/home/rumbaugh/dispersion_output.BA_delay.1608.mu_%4.2f_%4.2f.tau_%i.1.15.13.dat'%(minmu,maxmu,maxtimestep)
try:
    FILE_BC
except NameError:
    FILE_BC = '/home/rumbaugh/dispersion_output.BC_delay.1608.mu_%4.2f_%4.2f.tau_%i.1.15.13.dat'%(minmu,maxmu,maxtimestep)
try:
    FILE_BD
except NameError:
    FILE_BD = '/home/rumbaugh/dispersion_output.BD_delay.1608.mu_%4.2f_%4.2f.tau_%i.1.15.13.dat'%(minmu,maxmu,maxtimestep)
try:
    dispfromfile
except NameError:
    dispfromfile = True

load1608 = np.loadtxt('/home/rumbaugh/B1938+666_files/1608_g.ab922_nh')
ltime = load1608[:,0].copy()
Aflux,Bflux,Cflux,Dflux,Aerr,Berr,Cerr,Derr = load1608[:,1].copy(),load1608[:,2].copy(),load1608[:,3].copy(),load1608[:,4].copy(),load1608[:,5].copy(),load1608[:,6].copy(),load1608[:,7].copy(),load1608[:,8].copy()

Anflux,Bnflux,Cnflux,Dnflux = Aflux/np.average(Aflux),Bflux/np.average(Bflux),Cflux/np.average(Cflux),Dflux/np.average(Dflux)
Aavgerr,Bavgerr,Cavgerr,Davgerr = m.sqrt(np.sum(Aerr*Aerr))/len(Aerr),m.sqrt(np.sum(Berr*Berr))/len(Berr),m.sqrt(np.sum(Cerr*Cerr))/len(Cerr),m.sqrt(np.sum(Derr*Derr))/len(Derr)
Anerr,Bnerr,Cnerr,Dnerr = np.zeros(len(Aflux)),np.zeros(len(Aflux)),np.zeros(len(Aflux)),np.zeros(len(Aflux))
for i in range(0,len(Aerr)):
    Anerr[i],Bnerr[i],Cnerr[i],Dnerr[i] = Anflux[i]*m.sqrt((Aerr[i]/Aflux[i])**2+(Aavgerr/np.average(Aflux))**2),Bnflux[i]*m.sqrt((Berr[i]/Bflux[i])**2+(Bavgerr/np.average(Bflux))**2),Cnflux[i]*m.sqrt((Cerr[i]/Cflux[i])**2+(Cavgerr/np.average(Cflux))**2),Dnflux[i]*m.sqrt((Derr[i]/Dflux[i])**2+(Davgerr/np.average(Dflux))**2)

st1 = time.time()

ltime = (ltime-ltime[0])
#find time delays
if dispfromfile:
    dispmatrixAB = np.loadtxt(FILE_BA)
    dispmatrixBC = np.loadtxt(FILE_BC)
    dispmatrixBD = np.loadtxt(FILE_BD)
else:
    dispmatrixAB = calc_disp_delay(Aflux,Bflux,ltime,ltime,Aerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2,dispmatrix=True)
    np.savetxt(FILE_BA,dispmatrixAB,delimiter=' ')
    t1 = time.time()
    print "33%% Done. Elapsed Time: %f seconds"%(t1-st1)
    dispmatrixBC = calc_disp_delay(Cflux,Bflux,ltime,ltime,Cerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2,dispmatrix=True)
    np.savetxt(FILE_BC,dispmatrixBC,delimiter=' ')
    t2 = time.time()
    print "66%% Done. Elapsed Time: %f seconds"%(t2-st1)
    dispmatrixBD = calc_disp_delay(Dflux,Bflux,ltime,ltime,Derr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2,dispmatrix=True)
    np.savetxt(FILE_BD,dispmatrixBD,delimiter=' ')
    if not justone:
#now use D_4_2 with range of deltas
        delta_arr = np.arange(19)+3.5
        BA_delay_d42,BAmud42,BAdispd42,BC_delay_d42,BCmud42,BCdispd42,BD_delay_d42,BDmud42,BDdispd42 = np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr))
        for i in range(0,len(delta_arr)):
            BA_delay_d42[i],BAmud42[i],BAdispd42[i] = calc_disp_delay(Aflux,Bflux,ltime,ltime,Aerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta=delta_arr[i],output=2)
            BC_delay_d42[i],BCmud42[i],BCdispd42[i] = calc_disp_delay(Cflux,Bflux,ltime,ltime,Cerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta=delta_arr[i],output=2)
            BD_delay_d42[i],BDmud42[i],BDdispd42[i] = calc_disp_delay(Dflux,Bflux,ltime,ltime,Derr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta=delta_arr[i],output=2)

pylab.imshow(dispmatrixAB,extent=[-1*maxtimestep,maxtimestep,minmu,maxmu],origin='lower',aspect='auto')
pylab.savefig('dispplot2D.1608_AB.mu_%4.2f_%4.2f.tau_%i.1.15.13.png'%(minmu,maxmu,maxtimestep))
pylab.close('all')
pylab.imshow(dispmatrixBC,extent=[-1*maxtimestep,maxtimestep,minmu,maxmu],origin='lower',aspect='auto')
pylab.savefig('dispplot2D.1608_BC.mu_%4.2f_%4.2f.tau_%i.1.15.13.png'%(minmu,maxmu,maxtimestep))
pylab.close('all')
pylab.imshow(dispmatrixBD,extent=[-1*maxtimestep,maxtimestep,minmu,maxmu],origin='lower',aspect='auto')
pylab.savefig('dispplot2D.1608_BD.mu_%4.2f_%4.2f.tau_%i.1.15.13.png'%(minmu,maxmu,maxtimestep))
pylab.close('all')
 
t3 = time.time()
print "All Done. Elapsed Time: %f seconds"%(t3-st1)
