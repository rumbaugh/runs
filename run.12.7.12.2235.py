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
    fluxratio_err
except NameError:
    fluxratio_err = 0.0095

try:
    timestep
except NameError:
    timestep = 86400
try:
    mustep
except NameError:
    mustep = 0.001
try:
    maxtimestep
except NameError:
    maxtimestep = 60*timestep
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

CSO_arr = np.array(['J0003+4807','J1400+6210','J1414+4554','J1545+4751','J1734+0926','J1816+3457','J1823+7938','J1826+1831','J1927+7358','J1945+7055'])
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

i,endloop = 0,0
if skipahead == 1:
    i = init
for i in range(0,len(CSO_arr)):
    CSOload = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/%s.fluxes.8.17.12.dat'%CSO_arr[i],dtype='string')
    CSOload2 = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/%s.fluxes.11.5.12.dat'%CSO_arr[i],dtype='string')
    timest,fluxest = arrconv.str2float(CSOload[:,5].copy()),arrconv.str2float(CSOload[:,6].copy())
    SBgrouparrt = CSOload[:,1].copy()
    SBnumarrt = CSOload[:,2].copy()
    if len(CSOload2.shape) > 1:
        timest2,fluxest2 = arrconv.str2float(CSOload2[:,5].copy()),arrconv.str2float(CSOload2[:,6].copy())
        times,fluxes = np.append(timest,timest2),np.append(fluxest,fluxest2)
        SBgrouparrt2 = CSOload2[:,1].copy()
        SBnumarrt2 = CSOload2[:,2].copy()
        SBgrouparr,SBnumarr = np.append(SBgrouparrt,SBgrouparrt2),np.append(SBnumarrt,SBnumarrt2)
    else:
        timest2,fluxest2 = CSOload2[5],CSOload2[6]
        SBgrouparrt2 = CSOload2[1]
        SBnumarrt2 = CSOload2[2]
        SBgrouparr,SBnumarr = np.append(SBgrouparrt,SBgrouparrt2),np.append(SBnumarrt,SBnumarrt2)
        times,fluxes = np.append(timest,float(timest2)),np.append(fluxest,float(fluxest2))
rmsload = np.loadtxt('/home/rumbaugh/rms_errors.B1938+666.12.7.12.dat',dtype='string')

rmsgrouparr,rmsnumarr,rms_arr = rmsload[:,1].copy(),rmsload[:,2].copy(),str2float(rmsload[:,3].copy())


min_disp_D_2 = -99
min_disp_D_4_2 = -99
mu = minmu
while mu le maxmu:
    delay = -1.0*maxtimestep
    while delay le maxtimestep:
        D_2_tmp = D_2(
