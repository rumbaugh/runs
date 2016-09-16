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

execfile("/home/rumbaugh/Load1938.py")
ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()


st = time.time()
FILEt = open('/home/rumbaugh/tracking.run.1.23.13.2215.txt','w')
FILEt.write('Starting run.1.23.13.2215.py...')
FILEt.close()

ltime = (ltime-ltime[0])
#find time delays
C1A_delay_d2,C1Amud2,C1Adispd2 = calc_disp_delay(Aflux,C1flux,ltime,ltime,Aerr,C1err,maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=2,simplemuerr=True)
t1 = time.time()
print "33%% Done. Elapsed Time: %f seconds"%(t1-st)
BC1_delay_d2,BC1mud2,BC1dispd2 = calc_disp_delay(Bflux,C1flux,ltime,ltime,Berr,C1err,maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=2,simplemuerr=True)
t2 = time.time()
print "66%% Done. Elapsed Time: %f seconds"%(t2-st)
C1C2_delay_d2,C1C2mud2,C1C2dispd2 = calc_disp_delay(C2flux,C1flux,ltime,ltime,C2err,C1err,maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=2,simplemuerr=True)
t3 = time.time()
if not justone:
#now use D_4_2 with range of deltas
    delta_arr = np.arange(19)+3.5
    C1A_delay_d42,C1Amud42,C1Adispd42,BC1_delay_d42,BC1mud42,BC1dispd42,C1C2_delay_d42,C1C2mud42,C1C2dispd42 = np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr))
    for i in range(0,len(delta_arr)):
        C1A_delay_d42[i],C1Amud42[i],C1Adispd42[i] = calc_disp_delay(Aflux,C1flux,ltime,ltime,Aerr,C1err,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta_arr[i],output=2,simplemuerr=True)     
        tA = time.time()
        FILEt = open('/home/rumbaugh/tracking.run.1.23.13.2215.txt','a')
        FILEt.write('Finished call to D_4_2b for C1A with delta = %4.1f\nOutput: tau = %5.1f  mu = %6.4f disp = %8.6f\nElapsed time - %f seconds. ETA: %f seconds\n'%(delta_arr[i],C1A_delay_d42[i],C1Amud42[i],C1Adispd42[i],tA-st,(tA-t3)/(3*i+1)*(3*(len(delta_arr)-i-1))+2))
        FILEt.close()
        BC1_delay_d42[i],BC1mud42[i],BC1dispd42[i] = calc_disp_delay(Bflux,C1flux,ltime,ltime,Berr,C1err,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta_arr[i],output=2,simplemuerr=True)    
        tC = time.time()
        FILEt = open('/home/rumbaugh/tracking.run.1.23.13.2215.txt','a')
        FILEt.write('Finished call to D_4_2b for BC1 with delta = %4.1f\nOutput: tau = %5.1f  mu = %6.4f disp = %8.6f\nElapsed time - %f seconds. ETA: %f seconds\n'%(delta_arr[i],BC1_delay_d42[i],BC1mud42[i],BC1dispd42[i],tC-st,(tC-t3)/(3*i+2)*(3*(len(delta_arr)-i-1))+1))
        FILEt.close()
        C1C2_delay_d42[i],C1C2mud42[i],C1C2dispd42[i] = calc_disp_delay(C2flux,C1flux,ltime,ltime,C2err,C1err,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta_arr[i],output=2,simplemuerr=True)    
        tD = time.time()
        FILEt = open('/home/rumbaugh/tracking.run.1.23.13.2215.txt','a')
        FILEt.write('Finished call to D_4_2b for C1C2 with delta = %4.1f\nOutput: tau = %5.1f  mu = %6.4f disp = %8.6f\nElapsed time - %f seconds. ETA: %f seconds\n'%(delta_arr[i],C1C2_delay_d42[i],C1C2mud42[i],C1C2dispd42[i],tD-st,(tD-t3)/(3*i+3)*(3*(len(delta_arr)-i-1))+0))
        FILEt.close()
print "\n\nC1-A:\nD_2 delay: %4.1f days  mu: %6.4f   disp: %f:"%(C1A_delay_d2,C1Amud2,C1Adispd2)
if not justone:
    for i in range(0,len(delta_arr)): 
        print "_4_2:\ndelta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],C1A_delay_d42[i],C1Amud42[i],C1Adispd42[i])
print "\n\nC1-B:\nD_2 delay: %4.1f days  mu: %6.4f   disp: %f\n"%(BC1_delay_d2,BC1mud2,BC1dispd2)
if not justone:
    for i in range(0,len(delta_arr)): 
        print "D_4_2:\ndelta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BC1_delay_d42[i],BC1mud42[i],BC1dispd42[i])
print "\n\nC1-C2:\nD_2 delay: %4.1f days  mu: %6.4f   disp: %f:"%(C1C2_delay_d2,C1C2mud2,C1C2dispd2)
if not justone:
    for i in range(0,len(delta_arr)): 
        print "_4_2:\ndelta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],C1C2_delay_d42[i],C1C2mud42[i],C1C2dispd42[i])
t3 = time.time()
print "All Done. Elapsed Time: %f seconds"%(t3-st)
FILEt = open('/home/rumbaugh/tracking.run.1.23.13.2215.txt','a')
FILEt.write("All Done. Elapsed Time: %f seconds"%(t3-st))
FILEt.close()
