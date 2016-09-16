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

obskey = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/PartialObskey.8.28.12.dat',dtype='string')

EarlyorLate_arr = obskey[:,0].copy()
SBgrouparr = obskey[:,1].copy()
SBnumarr = obskey[:,2].copy()
montharr = obskey[:,3].copy()
datearr = obskey[:,4].copy()
SBlongnum_arr = obskey[:,6] .copy()
badants_arr = obskey[:,7].copy()
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

i,endloop = 0,0
if skipahead == 1:
    i = init[0]
st = time.time()
prevtime = st
if appendflag == 0:
    wora = 'w'
else:
    wora = 'a'
#FILE = open('/local3/rumbaugh/EVLA/data/11A-138/timerecords.8.6.12.dat',wora)
while ((i < len(datearr)) & (endloop < 0.5)):
#for i in range(0,len(datearr)):
    cur_dir = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/'%(EarlyorLate_arr[i],SBgrouparr[i])
    vis = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/%sSB%s_%s.%s.%s.11.11A-138.%s.ms'%(EarlyorLate_arr[i],SBgrouparr[i],EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i],SBlongnum_arr[i])
    curvis = vis
    os.chdir('%s'%cur_dir)
    listobs(vis=vis)
    prevtime = time.time()
    print '\n%sSB%s_%s.%s.%s.11.11A-138.%s.ms'%(EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i],SBlongnum_arr[i])
    print 'Bad ants: %s'%badants_arr[i]
    BPfield = BPfielddict[EarlyorLate_arr[i]][SBgrouparr[i]]
    PFCname = PFCdict[EarlyorLate_arr[i]][SBgrouparr[i]]
    REFANT = 'ea28'
    EarlyorLate = EarlyorLate_arr[i]
    SBgroupnum = SBgrouparr[i]
    if badants_arr[i] != 'none':
        plotms(vis=curvis,selectdata=T,iteraxis='antenna',coloraxis='antenna2',avgchannel='64',avgtime='30',avgspw=T,averagedata=T)    
        gotcon = 0
        con =  raw_input("Continue? \n(y/n)")
        while gotcon == 0:
            if ((con == 'y') | (con == 'yes') | (con == 'Y') | (con == 'Yes')): 
                gotcon = 1
            elif ((con == 'n') | (con == 'no') | (con == 'N') | (con == 'No')):
                print '\nEnding script...'
                endloop = 1
                gotcon = 1
            else:
                con =  raw_input("'%s' is invalid. Enter 'y' or 'n':"%con)
    #conflagarr = np.loadtxt('/home/rumbaugh/Continue.txt',dtype='string')  
    #if conflagarr[0] == 'False': endloop = 1
    if endloop != 1: i += 1
if endloop < 0.4: print '\n\nAll Done!\n'
    
