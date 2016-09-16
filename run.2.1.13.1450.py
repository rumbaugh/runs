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

Cflux = C1flux+C2flux
Cerr = np.zeros(len(Cflux))
for i in range(0,len(Cerr)): Cerr[i] = m.sqrt((C1err[i])**2+(C2err[i])**2)

st = time.time()
FILEt = open('/home/rumbaugh/tracking.run.2.1.13.1450.txt','w')
FILEt.write('Starting run.2.1.13.1450.py...')
FILEt.close()

ltime = (ltime-ltime[0])/86400
#find time delays
CAdispmat,CA_delay_d2,CAmud2,CAdispd2,CAmu02 = calc_disp_delay(Aflux,Cflux,ltime,ltime,Aerr,Cerr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=4,simplemuerr=True,dispmatrix=True)
pylab.imshow(CAdispmat,extent=[minmu,maxmu,-1*maxtimestep,maxtimestep],aspect='auto',origin='lower')
pylab.savefig('/home/rumbaugh/B1938+666_files/dispmat_plot.B1938_CA_delay.D_2.2.1.13.png')
pylab.close('all')
t1 = time.time()
FILEt = open('/home/rumbaugh/tracking.run.2.1.13.1450.txt','a')
FILEt.write('Finished call to D_2b for CA\nOutput: tau = %5.1f  mu = %6.4f mu0 = %7.4f disp = %8.6f\nElapsed time - %f seconds.\n'%(CA_delay_d2,CAmud2,CAmu02,CAdispd2,t1-st))
FILEt.close()
print "33%% Done. Elapsed Time: %f seconds"%(t1-st)
BCdispmat,BC_delay_d2,BCmud2,BCdispd2,BCmu02 = calc_disp_delay(Bflux,Cflux,ltime,ltime,Berr,Cerr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=4,simplemuerr=True,dispmatrix=True)
pylab.imshow(BCdispmat,extent=[minmu,maxmu,-1*maxtimestep,maxtimestep],aspect='auto',origin='lower')
pylab.savefig('/home/rumbaugh/B1938+666_files/dispmat_plot.B1938_BC_delay.D_2.2.1.13.png')
pylab.close('all')
t2 = time.time()
FILEt = open('/home/rumbaugh/tracking.run.2.1.13.1450.txt','a')
FILEt.write('Finished call to D_2b for CA\nOutput: tau = %5.1f  mu = %6.4f mu0 = %7.4f disp = %8.6f\nElapsed time - %f seconds.\n'%(BC_delay_d2,BCmud2,BCmu02,BCdispd2,t2-st))
FILEt.close()
print "66%% Done. Elapsed Time: %f seconds"%(t2-st)
BAdispmat,BA_delay_d2,BAmud2,BAdispd2,BAmu02 = calc_disp_delay(Aflux,Bflux,ltime,ltime,Aerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=4,simplemuerr=True,dispmatrix=True)
pylab.imshow(BAdispmat,extent=[minmu,maxmu,-1*maxtimestep,maxtimestep],aspect='auto',origin='lower')
pylab.savefig('/home/rumbaugh/B1938+666_files/dispmat_plot.B1938_BA_delay.D_2.2.1.13.png')
pylab.close('all')
t3 = time.time()
FILEt = open('/home/rumbaugh/tracking.run.2.1.13.1450.txt','a')
FILEt.write('Finished call to D_2b for BA\nOutput: tau = %5.1f  mu = %6.4f mu0 = %7.4f disp = %8.6f\nElapsed time - %f seconds.\n'%(BA_delay_d2,BAmud2,BAmu02,BAdispd2,t3-st))
FILEt.close()
if not justone:
#now use D_4_2 with range of deltas
    delta_arr = np.arange(19)+3.5
    CA_delay_d42,CAmud42,CAdispd42,BA_delay_d42,BAmud42,BAdispd42,BC_delay_d42,BCmud42,BCdispd42,CC2_delay_d42,CC2mud42,CC2dispd42 = np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr))
    for i in range(0,len(delta_arr)):
        CAdispmat, CA_delay_d42[i],CAmud42[i],CAdispd42[i],CAmu042 = calc_disp_delay(Aflux,Cflux,ltime,ltime,Aerr,Cerr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta_arr[i],output=4,simplemuerr=True,dispmatrix=True)  
        tA = time.time()
        FILEt = open('/home/rumbaugh/tracking.run.2.1.13.1450.txt','a')
        FILEt.write('Finished call to D_4_2b for CA with delta = %4.1f\nOutput: tau = %5.1f  mu = %6.4f mu0 = %7.4f disp = %8.6f\nElapsed time - %f seconds. ETA: %f seconds\n'%(delta_arr[i],CA_delay_d42[i],CAmud42[i],CAmu042,CAdispd42[i],tA-st,(tA-t3)/(3*i+1)*(3*(len(delta_arr)-i-1))+2))
        FILEt.close()
        pylab.imshow(CAdispmat,extent=[minmu,maxmu,-1*maxtimestep,maxtimestep],aspect='auto',origin='lower')
        pylab.savefig('/home/rumbaugh/B1938+666_files/dispmat_plot.B1938_CA_delay.D_4_2.delta_%.1f.2.1.13.png'%(delta_arr[i]))
        pylab.close('all')
        BCdispmat,BC_delay_d42[i],BCmud42[i],BCdispd42[i],BCmu042 = calc_disp_delay(Bflux,Cflux,ltime,ltime,Berr,Cerr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta_arr[i],output=4,simplemuerr=True,dispmatrix=True)  
        tC = time.time()
        FILEt = open('/home/rumbaugh/tracking.run.2.1.13.1450.txt','a')
        FILEt.write('Finished call to D_4_2b for BC with delta = %4.1f\nOutput: tau = %5.1f  mu = %6.4f mu0 = %7.4f disp = %8.6f\nElapsed time - %f seconds. ETA: %f seconds\n'%(delta_arr[i],BC_delay_d42[i],BCmud42[i],BCmu042,BCdispd42[i],tC-st,(tC-t3)/(3*i+2)*(3*(len(delta_arr)-i-1))+1))
        FILEt.close()
        pylab.imshow(BCdispmat,extent=[minmu,maxmu,-1*maxtimestep,maxtimestep],aspect='auto',origin='lower')
        pylab.savefig('/home/rumbaugh/B1938+666_files/dispmat_plot.B1938_BC_delay.D_4_2.delta_%.1f.2.1.13.png'%(delta_arr[i]))
        pylab.close('all')
        BAdispmat,BA_delay_d42[i],BAmud42[i],BAdispd42[i],BAmu042 = calc_disp_delay(Aflux,Bflux,ltime,ltime,Aerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta_arr[i],output=4,simplemuerr=True,dispmatrix=True)     
        tB = time.time()
        FILEt = open('/home/rumbaugh/tracking.run.2.1.13.1450.txt','a')
        FILEt.write('Finished call to D_4_2b for BA with delta = %4.1f\nOutput: tau = %5.1f  mu = %6.4f mu0 = %7.4f disp = %8.6f\nElapsed time - %f seconds. ETA: %f seconds\n'%(delta_arr[i],BA_delay_d42[i],BAmud42[i],BAmu042,BAdispd42[i],tB-st,(tB-t3)/(3*i+1)*(3*(len(delta_arr)-i-1))+2))
        FILEt.close()
        pylab.imshow(BAdispmat,extent=[minmu,maxmu,-1*maxtimestep,maxtimestep],aspect='auto',origin='lower')
        pylab.savefig('/home/rumbaugh/B1938+666_files/dispmat_plot.B1938_BA_delay.D_4_2.delta_%.1f.2.1.13.png'%(delta_arr[i]))
        pylab.close('all')
print "\n\nC-A:\nD_2 delay: %4.1f days  mu: %6.4f   disp: %f:"%(CA_delay_d2,CAmud2,CAdispd2)
if not justone:
    for i in range(0,len(delta_arr)): 
        print "_4_2:\ndelta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],CA_delay_d42[i],CAmud42[i],CAdispd42[i])
print "\n\nC-B:\nD_2 delay: %4.1f days  mu: %6.4f   disp: %f\n"%(BC_delay_d2,BCmud2,BCdispd2)
if not justone:
    for i in range(0,len(delta_arr)): 
        print "D_4_2:\ndelta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BC_delay_d42[i],BCmud42[i],BCdispd42[i])
t3 = time.time()
print "All Done. Elapsed Time: %f seconds"%(t3-st)
FILEt = open('/home/rumbaugh/tracking.run.2.1.13.1450.txt','a')
FILEt.write("All Done. Elapsed Time: %f seconds"%(t3-st))
FILEt.close()
