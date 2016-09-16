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

FILE = open('/mnt/data2/rumbaugh/VLA/AF377/difmap_results/chisq_results_1938.12.9.13.dat','w')
FILE.write("# lens img1 chisq1 P1 img2 chisq2 P2 img3 chisq3 P3 img4 chisq4 P4")

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

FILE.write("\n1938 ")
chisq_arr,prob_arr = np.zeros(4),np.zeros(4)
for img in range(0,3):
    S,Serr = fluxdict[img].copy(),errdict[img].copy()
    S,Serr = S/np.mean(S),Serr/np.mean(S)
    plt.plot(ltime+(img-1)*0.5,S,color=color_arr[img],lw=1.5,label=imgname[img])
    plt.errorbar(ltime+(img-1)*0.5,S,yerr=Serr,color=color_arr[img],fmt='ro',lw=1,capsize=3,mew=1,label='_nolegend_')
    plt.scatter(ltime+(img-1)*0.5,S,color=color_arr[img],label='_nolegend_')
    chisq_arr[img],prob_arr[img] = calc_chi_sqrd(S,Serr,calcprob=True,trials=trials)
#plt.legend(('C','B','A'),loc=2)
plt.legend(loc=2)
plt.title('Normalized Lightcurve for B1938')
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
#plt.ylim(0.7,1.3)
#plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/B1938.lc_norm_plot.8.31.13.png')
plt.close('all')

for img in range(0,3):
    FILE.write("%2s %6.2f %6.4f "%(imgname[img],chisq_arr[img],prob_arr[img]))
FILE.write("NA      0     0")
FILE.close()

mu = 5.138

for img in range(0,2):
    S,Serr = fluxdict[img].copy(),errdict[img].copy()
    if img == 1: 
        ltime += 45.5
        S,Serr = S/np.mean(fluxdict[0]),Serr/np.mean(fluxdict[0])
    else:
        S,Serr = S*mu/np.mean(fluxdict[0]),Serr*mu/np.mean(fluxdict[0])
    plt.plot(ltime+(img-1),S,color=color_arr[img],lw=1.5,label=imgname[img])
    plt.errorbar(ltime+(img-1),S,yerr=Serr,color=color_arr[img],fmt='ro',lw=1,capsize=3,mew=1,label='_nolegend_')
    plt.scatter(ltime+(img-1),S,color=color_arr[img],label='_nolegend_')
#plt.legend(('C','B','A'),loc=2)
plt.legend(loc=2)
plt.title('Offset Lightcurves for B1938')
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
#plt.ylim(0.7,1.3)
#plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/B1938.lc_delay_plot.8.31.13.png')
plt.close('all')
