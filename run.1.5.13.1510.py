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
    justone = False
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
BA_delay_d2,BAmud2,BAdispd2 = calc_disp_delay(Aflux,Bflux,ltime,ltime,Aerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2)
BC_delay_d2,BCmud2,BCdispd2 = calc_disp_delay(Cflux,Bflux,ltime,ltime,Cerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2)
BD_delay_d2,BDmud2,BDdispd2 = calc_disp_delay(Dflux,Bflux,ltime,ltime,Derr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2)
if not justone:
#now use D_4_2 with range of deltas
    delta_arr = np.arange(19)+3.5
    BA_delay_d42,BAmud42,BAdispd42,BC_delay_d42,BCmud42,BCdispd42,BD_delay_d42,BDmud42,BDdispd42 = np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr))
    for i in range(0,len(delta_arr)):
        BA_delay_d42[i],BAmud42[i],BAdispd42[i] = calc_disp_delay(Aflux,Bflux,ltime,ltime,Aerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta=delta_arr[i],output=2)
        BC_delay_d42[i],BCmud42[i],BCdispd42[i] = calc_disp_delay(Cflux,Bflux,ltime,ltime,Cerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta=delta_arr[i],output=2)
        BD_delay_d42[i],BDmud42[i],BDdispd42[i] = calc_disp_delay(Dflux,Bflux,ltime,ltime,Derr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta=delta_arr[i],output=2)
FILE = open('/home/rumbaugh/output.1.5.13.dat','w')
print "\n\nB-A:\nD_2 delay: %3.0f days  mu: %6.4f   disp: %f\nD_4_2:"%(BA_delay_d2,BAmud2,BAdispd2)
FILE.write("\n\nB-A:\nD_2 delay: %3.0f days  mu: %6.4f   disp: %f\nD_4_2:"%(BA_delay_d2,BAmud2,BAdispd2))
if not justone:
    for i in range(0,len(delta_arr)): 
        print "delta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BA_delay_d42[i],BAmud42[i],BAdispd42[i])
        FILE.write("delta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BA_delay_d42[i],BAmud42[i],BAdispd42[i]))
print "\n\nB-C:\nD_2 delay: %3.0f days  mu: %6.4f   disp: %f\nD_4_2:"%(BC_delay_d2,BCmud2,BCdispd2)
FILE.write("\n\nB-C:\nD_2 delay: %3.0f days  mu: %6.4f   disp: %f\nD_4_2:"%(BC_delay_d2,BCmud2,BCdispd2))
if not justone:
    for i in range(0,len(delta_arr)): 
        print "delta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BC_delay_d42[i],BCmud42[i],BCdispd42[i])
        FILE.write("delta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BC_delay_d42[i],BCmud42[i],BCdispd42[i]))
print "\n\nB-D:\nD_2 delay: %3.0f days  mu: %6.4f   disp: %f\nD_4_2:"%(BD_delay_d2,BDmud2,BDdispd2)
FILE.write("\n\nB-D:\nD_2 delay: %3.0f days  mu: %6.4f   disp: %f\nD_4_2:"%(BD_delay_d2,BDmud2,BDdispd2))
if not justone:
    for i in range(0,len(delta_arr)): 
        print "delta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BD_delay_d42[i],BDmud42[i],BDdispd42[i])
        FILE.write("delta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BD_delay_d42[i],BDmud42[i],BDdispd42[i]))
FILE.close()
