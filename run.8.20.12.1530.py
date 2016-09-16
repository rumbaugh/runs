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

obskey = np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/PartialObskey.8.20.12.dat',dtype='string')

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

avgchannelarr = np.array(['64','64',''])
avgtimearr = np.array(['','','30000'])
avgscanarr = np.array([False,False,True])

EarlyorLate = vis[0:5]
if EarlyorLate == 'LateS': 
    EarlyorLate = 'Late'
    SBgroupnum = vis[6]
else:
    SBgroupnum = vis[7]

curvis = vis
BPfield = BPfielddict[EarlyorLate][SBgroupnum]
iplot = 0
prevtime = time.time()
endloop,iplot = 0,0
while ((iplot < 3) & (endloop < 0.5)):
    print plottype[iplot]
    plotms(vis=curvis,xaxis=xaxis_arr[iplot],yaxis='amp',field=BPfield,spw='',correlation='LL,RR',avgchannel=avgchannelarr[iplot],avgtime=avgtimearr[iplot],avgscan=avgscanarr[iplot],avgspw=True,coloraxis=caxisvar,ydatacolumn='corrected')
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
    prevtime = curtime
    if endloop != 1: iplot += 1
if endloop < 0.4: print '\n\nAll Done!\n'
            
