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

plottype = np.array(['Amp vs. Time','Amp vs. UVDist','Amp vs. Frequency'])
xaxis_arr = np.array(['time','uvdist','frequency'])

obskey = np.loadtxt('/mnt/data3/rumbaugh/EVLA/data/11A-138/PartialObskey.8.7.12.dat',dtype='string')

EarlyorLate_arr = obskey[:,0].copy()
SBgrouparr = obskey[:,1].copy()
SBnumarr = obskey[:,2].copy()
montharr = obskey[:,3].copy()
datearr = obskey[:,4].copy()
SBlongnum_arr = obskey[:,6] .copy()
badants_arr = obskey[:,10].copy()
fieldskey = np.loadtxt('/mnt/data3/rumbaugh/EVLA/data/11A-138/Fieldskey.dat',dtype='string')
EorLcheck_arr = fieldskey[:,0]
SBcheck_arr = fieldskey[:,1]
numfield_arr = fieldskey[:,2]
fieldsdict = {'Early': {'1': int(numfield_arr[3]), '2': int(numfield_arr[4])}, 'Late': {'1': int(numfield_arr[0]), '2': int(numfield_arr[1]), '3': int(numfield_arr[2])}}

BPfielddict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': '9', '2': '3', '3': '3'}}

PFCdict = {'Early': {'1': '3C48', '2': '3C48'}, 'Late': {'1': '3C286', '2': '3C48', '3': '3C48'}}

avgchannelarr = np.array(['64','64',''])
avgtimearr = np.array(['','','30000'])
avgscanarr = np.array([False,False,True])

i,endloop = 0,0
if skipahead == 1:
    i = init
st = time.time()
prevtime = st
if appendflag == 0:
    wora = 'w'
else:
    wora = 'a'
#FILE = open('/mnt/data2/rumbaugh/EVLA/11A-138/data/timerecords.8.6.12.dat',wora)
#for i in range(0,len(datearr)):
cur_dir = '/mnt/data2/rumbaugh/EVLA/11A-138/data/'
vis = 'test.ms'
curvis = vis
os.chdir('%s'%cur_dir)
#listobs(vis=vis)
prevtime = time.time()
REFANT = 'ea28'
EarlyorLate = 'Late'
SBgroupnum = '2'
tflagdata(vis=curvis,mode='manual',antenna='ea10,ea15,ea18',spw='0')
tflagdata(vis=curvis,mode='manual',antenna='ea10,ea18',spw='1')
execfile("/mnt/data3/rumbaugh/EVLA/scripts/calib_general.py")
print '\n\nAll Done!\n'
    
