import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab

try:
    skipahead
except NameError:
    skipahead = 0
try:
    init
except NameError:
    init = 0

try:
    appendflag
except NameError:
    appendflag = 0

try:
    caxisvar
except NameError:
    caxisvar = 'antenna2'

CSO_arr = np.array(['J0003+4807','J1400+6210','J1414+4554','J1545+4751','J1734+0926','J1816+3457','J1823+7938','J1826+1831','J1927+7358','J1945+7055'])

plottype = np.array(['Amp vs. Time','Amp vs. UVDist','Amp vs. Frequency'])
xaxis_arr = np.array(['time','uvdist','frequency'])

obskey = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/PartialObskey_Late.8.30.12.dat',dtype='string')

EarlyorLate_arr = obskey[:,0].copy()
SBgrouparr = obskey[:,1].copy()
SBnumarr = obskey[:,2].copy()
montharr = obskey[:,3].copy()
datearr = obskey[:,4].copy()
SBlongnum_arr = obskey[:,6] .copy()
badants_arr = obskey[:,10].copy()
fieldskey = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/Fieldskey.dat',dtype='string')
EorLcheck_arr = fieldskey[:,0]
SBcheck_arr = fieldskey[:,1]
numfield_arr = fieldskey[:,2]
fieldsdict = {'Early': {'1': int(numfield_arr[3]), '2': int(numfield_arr[4])}, 'Late': {'1': int(numfield_arr[0]), '2': int(numfield_arr[1]), '3': int(numfield_arr[2])}}

BPfielddict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': '9', '2': '3', '3': '3'}}

PFCdict = {'Early': {'1': '3C48', '2': '3C48'}, 'Late': {'1': '3C286', '2': '3C48', '3': '3C48'}}

CSO_fieldnums_dict = {'Early': {'1': np.array(['4','7']), '2': np.array(['1','7'])}, 'Late': {'1': np.array(['1','2','3','4','8','10']), '2': np.array(['1','2','3','4','7','8']), '3': np.array(['1','2','4','8','9','10'])}}

CSO_fieldnames_dict = {'Early': {'1': np.array(['J0427+4133','J0754+5324']), '2': np.array(['J0204+0903','J0754+5324'])}, 'Late': {'1': np.array(['J1414+4554','J1400+6210','J1545+4751','J1816+3457','J1945+7055','J1823+7938']), '2': np.array(['J0003+4807','J1823+7938','J1927+7358','J1945+7055','J1816+3457','J1826+1831']), '3': np.array(['J0003+4807','J1823+7938','J1945+7055','J1816+3457','J1826+1831','J1734+0926'])}}

PCfieldnumdict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': np.array(['5','7']), '2': np.array(['5']), '3': np.array(['5','7'])}}

PCfieldnamedict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': np.array(['J2006+6424']), '2': np.array(['J2006+6424']), '3': np.array(['J2006+6424'])}}

avgchannelarr = np.array(['64','64',''])
avgtimearr = np.array(['','','30000'])
avgscanarr = np.array([False,False,True])

june10th_time = 4814380883
timeticks = june10th_time+86400+86400*10*(np.arange(11)-1)
timelabels = np.array(['6-01','6-11','6-21','7-1','7-11','7-21','7-31','8-10','8-20','8-30','9-9'])
pylab.xticks(timeticks,timelabels)
pylab.xlabel('Time')
pylab.ylabel('Normalized Flux')
i,endloop = 0,0
if skipahead == 1:
    i = init
st = time.time()
prevtime = st
for i in range(0,len(CSO_arr)):
    CSOload = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/%s.fluxes.8.17.12.dat'%CSO_arr[i],dtype='string')
    CSOload2 = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/%s.fluxes.11.5.12.dat'%CSO_arr[i],dtype='string')
    timest,fluxest = CSOload[:,5],CSOload[:,6]
    times,fluxes = np.zeros(len(timest)),np.zeros(len(timest))
    for j in range(len(timest)):
        times[j],fluxes[j] = float(timest[j]),float(fluxest[j])
    if len(CSOload2.shape) > 1:
        timest2,fluxest2 = CSOload2[:,5],CSOload2[:,6]
        times2,fluxes2 = np.zeros(len(timest2)),np.zeros(len(timest2))
        for j in range(len(timest2)):
            times2[j],fluxes2[j] = float(timest2[j]),float(fluxest2[j])
        times,fluxes = np.append(times,times2),np.append(fluxes,fluxes2)
    else:
        timest2,fluxest2 = CSOload2[5],CSOload2[6]
        times,fluxes = np.append(times,float(timest2)),np.append(fluxes,float(fluxest2))
    pylab.plot(times,fluxes/np.average(fluxes))
    pylab.scatter(times,fluxes/np.average(fluxes))
june10th_time = 4814380883.0
#pylab.xlim(4814250883,4819371930)
pylab.xlim(timeticks[0]-20000,timeticks[len(timeticks)-1]+20000)
pylab.savefig('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/CSO_fluxplot.8.17.12.png')
#pylab.close('all')
    

