import numpy as np
import math as m
import sys
import os
import time

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

iarr = np.array([0,6,7,8,14,16,17])

plottype = np.array(['Amp vs. Time','Amp vs. UVDist','Amp vs. Frequency'])
xaxis_arr = np.array(['time','uvdist','frequency'])

obskey = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/PartialObskey.8.7.12.dat',dtype='string')

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

avgchannelarr = np.array(['64','64',''])
avgtimearr = np.array(['','','30000'])
avgscanarr = np.array([False,False,True])

for j in range(0,len(iarr)):
    i = iarr[j]
    cur_dir = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/'%(EarlyorLate_arr[i],SBgrouparr[i])
    vis = '%sSB%s_%s.%s.%s.11.11A-138.%s.ms'%(EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i],SBlongnum_arr[i])
    print vis
    
