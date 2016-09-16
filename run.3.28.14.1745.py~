import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")
execfile("/home/rumbaugh/LinReg.py")
try:
    ntrials
except NameError:
    ntrials = 10


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
    maxtimestep = 105
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

try:
    delta
except NameError:
    delta = 17.5

date = '3.19.14'

lens = '0414'

execfile("/home/rumbaugh/LoadVLA_2001.py")
ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)
g = np.arange(len(ltime))[:len(ltime)-10]
ltime=ltime[g]
A1flux,A2flux,Bflux,Cflux = flux_arr[0][g],flux_arr[1][g],flux_arr[2][g],flux_arr[3][g]
A1err,A2err,Berr,Cerr = flux_err_arr[0][g],flux_err_arr[1][g],flux_err_arr[2][g],flux_err_arr[3][g]

st = time.time()
ltime = (ltime-ltime[0])#/86400
#find time delays


fluxdict = {'A1': A1flux, 'A2': A2flux, 'C': Cflux}
errdict = {'A1': A1err, 'A2': A2err, 'C': Cerr}
imgnames = ['A1','A2','C']

gAonly = np.where(ltime < 1946-1839)[0]

for imgname in imgnames:
    BA_disp_mat = np.zeros(ntrials)
    FILE = open('/home/rumbaugh/output.disp_sim.%s_B%s.%s.dat'%(lens,imgname,date),'w')
    st = time.time()
    for i in range(0,ntrials):
        g = np.arange(len(fluxdict[imgname]))
        rC = np.random.normal(0,1.,len(g))*errdict[imgname]
        np.random.shuffle(g)
        g2 = np.arange(len(Bflux))
        rB = np.random.normal(0,1.,len(g2))*Berr
        np.random.shuffle(g2)
        ttmp,mtmp,BA_disp_mat[i] = calc_disp_delay(fluxdict[imgname][g]+rC[g],Bflux[g2]+rB[g2],ltime,ltime,errdict[imgname][g],Berr[g2],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,verbose=True)
        FILE.write('%E\n'%(BA_disp_mat[i]))
        if i == 0: 
            t0 = time.time()
            print 'Initial ETA: %i seconds'%((t0-st)*(ntrials-1))
        for ichk in range(1,10):
            if ((i >= ntrials*ichk/10.) & (i < ntrials*ichk/10.+1)):
                tchk = time.time()
                print '%i%% done. ETA: %i second'%(ichk*10,(tchk-st)*1./ichk*(10.-ichk))
    tend = time.time()
    print '\n\nTotal Time Elapsed: %.0f seconds\n\n'%(tend-st)
    FILE.close()

for imgname in imgnames:
    BA_disp_mat = np.zeros(ntrials)
    FILE = open('/home/rumbaugh/output.disp_sim.%s_VLA_A_only_B%s.%s.dat'%(lens,imgname,date),'w')
    st = time.time()
    for i in range(0,ntrials):
        g = np.arange(len(fluxdict[imgname][gAonly]))
        rC = np.random.normal(0,1.,len(g))*errdict[imgname][gAonly]
        np.random.shuffle(g)
        g2 = np.arange(len(Bflux[gAonly]))
        rB = np.random.normal(0,1.,len(g2))*Berr[gAonly]
        np.random.shuffle(g2)
        ttmp,mtmp,BA_disp_mat[i] = calc_disp_delay(fluxdict[imgname][gAonly[g]]+rC[g],Bflux[gAonly[g2]]+rB[g2],ltime,ltime,errdict[imgname][gAonly[g]],Berr[gAonly[g2]],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,verbose=False)
        FILE.write('%E\n'%(BA_disp_mat[i]))
        if i == 0: 
            t0 = time.time()
            print 'Initial ETA: %i seconds'%((t0-st)*(ntrials-1))
        for ichk in range(1,10):
            if ((i >= ntrials*ichk/10.) & (i < ntrials*ichk/10.+1)):
                tchk = time.time()
                print '%i%% done. ETA: %i second'%(ichk*10,(tchk-st)*1./ichk*(10.-ichk))
    tend = time.time()
    print '\n\nTotal Time Elapsed: %.0f seconds\n\n'%(tend-st)
    FILE.close()
