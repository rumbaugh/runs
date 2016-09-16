import numpy as np
import math as m
import sys
import os
import time

try:
    xaxis
except NameError:
    xaxis = 'time'

try:
    caxisvar
except NameError:
    caxisvar = 'antenna2'

if xaxis == 'frequency':
    avgchannel = ''
    avgtime = '30000'
else:
    avgchannel = '64'
    avgtime = ''

print curvis
print antenna

vis = curvis
listobs(vis=vis)
i,endloop = 0,0
while ((i < 10) & (endloop < 0.5)):
    plotms(vis=curvis,xaxis=xaxis,yaxis='amp',field='%i'%i,spw='',antenna=antenna,correlation='LL,RR',avgchannel=avgchannel,avgtime=avgtime,avgscan=F,avgspw=True,iteraxis='field',coloraxis=caxisvar,ydatacolumn='corrected')
    gotcon = 0
    con = raw_input("Continue? \n(y/n)")
    while gotcon < 0.5:
        if ((con == 'y') | (con == 'yes') | (con == 'Y') | (con == 'Yes')): 
            gotcon = 1
        elif ((con == 'n') | (con == 'no') | (con == 'N') | (con == 'No')):
            print '\nEnding script...'
            endloop = 1
            gotcon = 1
        else:
            con =  raw_input("'%s' is invalid. Enter 'y' or 'n':"%con)
    if endloop != 1: i += 1
if endloop != 1: print 'Done'

        

