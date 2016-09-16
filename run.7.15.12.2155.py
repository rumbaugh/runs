import numpy as np
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
    init = np.zeros(2)

try:
    appendflag
except NameError:
    appendflag = 0

obskey = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/Obskey.dat',dtype='string')
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
i,endloop = 0,0
if skipahead == 1:
    i = init[0]
st = time.time()
prevtime = st
if appendflag == 0:
    wora = 'w'
else:
    wora = 'a'
FILE = open('/local3/rumbaugh/EVLA/data/11A-138/timerecords.7.15.12.dat',wora)
while ((i < len(datearr)) & (endloop < 0.5)):
#while ((i < 1) & (endloop < 0.5)):
    cur_dir = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/'%(EarlyorLate_arr[i],SBgrouparr[i])
    vis = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/%sSB%s_%s.%s.%s.11.11A-138.%s.ms'%(EarlyorLate_arr[i],SBgrouparr[i],EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i],SBlongnum_arr[i])
    os.chdir('%s'%cur_dir)
    listobs(vis=vis)
    prevtime = time.time()
    numfields = fieldsdict[EarlyorLate_arr[i]][SBgrouparr[i]]
    ifield = 0
    iant = 0
    if ((skipahead == 1) & (i == init[0])): iant = init[1]
    print '\n%s'%vis
    while ((iant < 29) & (endloop < 0.5)):
        ispw = 0
        curant = 'ea%02i'%(iant+1)
        print 'antenna = %s (badants: %s)'%(curant,badants_arr[i])
        while ((ispw < 2) & (endloop < 0.5)):
            print 'spw = %i'%ispw
            plotms(vis=vis,xaxis='time',yaxis='amp',antenna=curant,field='',spw='%i'%ispw)
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
            curtime = time.time()
            print 'Time taken for this plot: %f'%(curtime-prevtime)
            FILE.write('%2i %1i %.1f %sSB%s_%s.%s.%s.11\n'%(ifield,ispw,curtime-prevtime,EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i]))
            prevtime = curtime
            if endloop != 1: ispw += 1
        if endloop != 1: iant += 1
    if endloop != 1: i += 1
FILE.close()
if endloop < 0.4: print '\n\nAll Done!\n'
            
