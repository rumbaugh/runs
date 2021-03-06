import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

date = '12.5.13'
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
ls_arr = ['solid','dashed','dotted','-.']

plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

fluxdict = {0: Cflux, 1: Bflux, 2: Aflux}
errdict = {0: Cerr, 1: Berr, 2: Aerr}
imgname = {0: 'C', 1: 'B', 2: 'A'}

space_inbetween = 0.15
yticklocs,yticklabs = np.array([0.925,0.95,0.975,1.,1.025,1.05,1.075,1.1,1.125,1.15,1.175])+space_inbetween*(-1),np.array(['','0.95','','1.00','','1.05','','','','',''])
yticklocso,yticklabso = np.copy(yticklocs)-space_inbetween*(-1),np.copy(yticklabs)
yticklocs,yticklabs = np.append(yticklocs,yticklocso+space_inbetween*(1-1)),np.append(yticklabs,yticklabso)
yticklocs,yticklabs = np.append(yticklocs,yticklocso+space_inbetween*(2-1)),np.append(yticklabs,np.array(['','0.95','','1.00','','1.05','','1.1','','1.2','']))
testlegs = []
for img in range(0,3):
    arb_offset = space_inbetween*(img-1)
    S,Serr = fluxdict[img].copy(),errdict[img].copy()
    S,Serr = S/np.mean(S),Serr/np.mean(S)
    S += arb_offset
    #plt.plot(ltime+(img-1)*0.5,S,color=color_arr[img],lw=1.5,label=imgname[img])
    plt.errorbar(ltime+(img-1)*0.5,S,yerr=Serr,color=color_arr[img],fmt='ro',lw=1,capsize=3,mew=1,label='_nolegend_')
    plt.scatter(ltime+(img-1)*0.5,S,color=color_arr[img],label='_nolegend_')
    testlegs = np.append(testlegs,plt.plot(ltime+(img-1)*0.5,S,color=color_arr[img],lw=2,ls=ls_arr[img]))
plt.legend(testlegs,('C','B','A'),loc=2)
#plt.legend(loc=2)
plt.title('Normalized Lightcurve for B1938')
plt.xlabel('Days',fontsize=14)
plt.ylabel('Normalized Flux',fontsize=14)
plt.yticks(yticklocs,yticklabs)
plt.ylim(0.8,1.35)
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/B1938.lc_norm_plot_offset.%s.png'%date)
plt.close('all')
