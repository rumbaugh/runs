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

CSO_fieldnums_dict = {'Early': {'1': np.array(['4','7']), '2': np.array(['1','7'])}, 'Late': {'1': np.array(['1','2','3','4','8','10']), '2': np.array(['1','2','3','4','7','8']), '3': np.array(['1','2','4','8','9','10'])}}

CSO_fieldnames_dict = {'Early': {'1': np.array(['J0427+4133','J0754+5324']), '2': np.array(['J0204+0903','J0754+5324'])}, 'Late': {'1': np.array(['J1414+4554','J1400+6210','J1545+4751','J1816+3457','J1945+7055','J1823+7938']), '2': np.array(['J0003+4807','J1823+7938','J1927+7358','J1945+7055','J1816+3457','J1826+1831']), '3': np.array(['J0003+4807','J1823+7938','J1945+7055','J1816+3457','J1826+1831','J1734+0926'])}}

PCfieldnumdict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': np.array(['5','7']), '2': np.array(['5']), '3': np.array(['5','7'])}}

PCfieldnamedict = {'Early': {'1': '3', '2': '4'}, 'Late': {'1': np.array(['J2006+6424']), '2': np.array(['J2006+6424']), '3': np.array(['J2006+6424'])}}

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
FILE = open('/home/rumbaugh/runs/run.8.26.12.2310.sh','w')
while ((i < 13) & (endloop < 0.5)):
#for i in range(0,len(datearr)):
    cur_dir = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/'%(EarlyorLate_arr[i],SBgrouparr[i])
    vis = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/%sSB%s_%s.%s.%s.11.11A-138.%s.ms'%(EarlyorLate_arr[i],SBgrouparr[i],EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i],SBlongnum_arr[i])
    curvis = vis
    prevtime = time.time()
    print '\n%sSB%s_%s.%s.%s.11.11A-138.%s.ms'%(EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i],SBlongnum_arr[i])
    outbase = '%sSB%s_%s.%s.%s.11.11A-138'%(EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i])
    EarlyorLate = EarlyorLate_arr[i]
    SBgroupnum = SBgrouparr[i]
    CSO_fieldnames = CSO_fieldnames_dict[EarlyorLate][SBgroupnum]
    CSO_fieldnums = CSO_fieldnums_dict[EarlyorLate][SBgroupnum]
    if ((i != 13) & (i != 6) & (i != 14) & (i != 16)): 
        FILE.write('difmap << EOF\nobs %s%sSB%s_%s.%s.%s.11.11A-138.B1938+666.uvfits\nselect I\nmapunits arcsec\nmapsize 256,0.05\naddcmp peak(flux,max),true,peak(x,max),peak(y,max),true\nmodelfit 5\naddcmp peak(flux,max),true,peak(x,max),peak(y,max),true\nmodelfit 5\nselfcal false,false,60\naddcmp peak(flux,max),true,peak(x,max),peak(y,max),true\nmodelfit 5\naddcmp peak(flux,max),true,peak(x,max),peak(y,max),true\nmodelfit 5\nselfcal false,false,60\naddcmp peak(flux,max),true,peak(x,max),peak(y,max),true\nmodelfit 5\naddcmp peak(flux,max),true,peak(x,max),peak(y,max),true\nmodelfit 5\naddcmp peak(flux,max),true,peak(x,max),peak(y,max),true\nmodelfit 30\nwmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.%sSB%s_%s.8.25.12.mod\nquit\nEOF\n'%(cur_dir,EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i],EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i]))
    conflagarr = np.loadtxt('/home/rumbaugh/Continue.txt',dtype='string')  
    if conflagarr == 'False': endloop = 1
    if endloop != 1: i += 1
if endloop < 0.4: print '\n\nAll Done!\n'
FILE.close()
    
