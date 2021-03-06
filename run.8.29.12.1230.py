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

avgposmod =  np.loadtxt('/local3/rumbaugh/EVLA/data/11A-138/difmap_results/B1938+666.A1_pos_compiled.8.25.12.dat',dtype='string')
A1xstr = avgposmod[:,7].copy()
A1ystr = avgposmod[:,8].copy()
A1x,A1y = np.zeros(len(A1xstr)),np.zeros(len(A1xstr))
for j in range(0,len(A1x)):
    A1x[j],A1y[j] = float(A1xstr[j]),float(A1ystr[j])
A1x_mean,A1y_mean = np.average(A1x),np.average(A1y)
ltime = np.zeros(12)
june10th_time = 4814380883.0

visarr = np.empty(12,dtype='string')
visarr2 = np.array(['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'])

i,endloop,i2 = 0,0,0
counter = 0
counter2 = 0
counter3 = 0
counter4 = 0
while ((i < 13) & (endloop < 0.5)):
    cur_dir = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/'%(EarlyorLate_arr[i],SBgrouparr[i])
    vis = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/%sSB%s_%s.%s.%s.11.11A-138.%s.ms'%(EarlyorLate_arr[i],SBgrouparr[i],EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i],SBlongnum_arr[i])
    curvis = vis
    EarlyorLate = EarlyorLate_arr[i]
    SBgroupnum = SBgrouparr[i]
    if ((i != 13) & (i != 6) & (i != 14) & (i != 16)): 
        visarr2[counter] = '%s%sSB%s_%s.%s.%s.11.11A-138.B1938+666.ms'%(cur_dir,EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i])
        if ((i == 1) | (i == 7)): savevis = visarr2[counter]
        i2 += 1
        counter += 1
        print counter,counter2,counter3,i,i2,visarr2
        if counter > 1:
            counter = 0
            counter4 += 1
            concat(vis=visarr2,concatvis='/local3/rumbaugh/EVLA/data/11A-138/temp.concat%i.ms'%(counter4))
            visarr2 = np.array(['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'])
            counter2 += 1
            if counter2 > 1:
                counter3 += 1
                if counter3 == 1:
                    concat(vis=[savevis,'/local3/rumbaugh/EVLA/data/11A-138/temp.concat2.ms'],concatvis = '/local3/rumbaugh/EVLA/data/11A-138/temp.concat_concat%i.ms'%counter3)
                    #exportuvfits(vis='/local3/rumbaugh/EVLA/data/11A-138/temp.concat2.ms',fitsfile='/local3/rumbaugh/EVLA/data/11A-138/temp.concat2.uvfits',field='0')
                elif counter3 == 2:
                    concat(vis=[savevis,'/local3/rumbaugh/EVLA/data/11A-138/temp.concat1.ms'],concatvis = '/local3/rumbaugh/EVLA/data/11A-138/temp.concat_concat%i.ms'%counter3)
                    #exportuvfits(vis='/local3/rumbaugh/EVLA/data/11A-138/temp.concat2.ms',fitsfile='/local3/rumbaugh/EVLA/data/11A-138/temp.concat2.uvfits',field='0')
                else:
                    concat(vis=['/local3/rumbaugh/EVLA/data/11A-138/temp.concat%i.ms'%(counter4-1),'/local3/rumbaugh/EVLA/data/11A-138/temp.concat%i.ms'%counter4],concatvis = '/local3/rumbaugh/EVLA/data/11A-138/temp.concat_concat%i.ms'%counter3)
                    #exportuvfits(vis='/local3/rumbaugh/EVLA/data/11A-138/temp.concat%i.ms'%(counter4-1),fitsfile='/local3/rumbaugh/EVLA/data/11A-138/temp.concat%i.uvfits'%(counter4-1),field='0')
                    #exportuvfits(vis='/local3/rumbaugh/EVLA/data/11A-138/temp.concat%i.ms'%(counter4),fitsfile='/local3/rumbaugh/EVLA/data/11A-138/temp.concat%i.uvfits'%(counter4),field='0')
                #exportuvfits(vis='/local3/rumbaugh/EVLA/data/11A-138/temp.concat_concat%i.ms'%(counter3),fitsfile='/local3/rumbaugh/EVLA/data/11A-138/temp.concat_concat%i.uvfits'%(counter3),field='0')
                counter2 = 0
                #os.system('rm -rf /local3/rumbaugh/EVLA/data/11A-138/temp.concat1.ms/')
                #os.system('rm -rf /local3/rumbaugh/EVLA/data/11A-138/temp.concat2.ms/')
                if counter3 != 1:
                    vis = '/local3/rumbaugh/EVLA/data/11A-138/temp.concat_concat%i.ms'%counter3
                    #tflagdata(vis=vis,mode='manual',antenna='ea21')
    conflagarr = np.loadtxt('/home/rumbaugh/Continue.txt',dtype='string')  
    if conflagarr == 'False': endloop = 1
    if endloop != 1: i += 1
concat(vis=['/local3/rumbaugh/EVLA/data/11A-138/temp.concat_concat1.ms','/local3/rumbaugh/EVLA/data/11A-138/temp.concat_concat2.ms'],concatvis='/local3/rumbaugh/EVLA/data/11A-138/temp.ccc_temp.ms')
concat(vis=['/local3/rumbaugh/EVLA/data/11A-138/temp.ccc_temp.ms','/local3/rumbaugh/EVLA/data/11A-138/temp.concat_concat3.ms'],concatvis='/local3/rumbaugh/EVLA/data/11A-138/B1938+666.Late_concat.8.27.12.ms')
if endloop < 0.4: print '\n\nAll Done!\n'
    
