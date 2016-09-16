import numpy as np
import sys
import os
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
while ((i < len(datearr)) & (endloop < 0.5)):
    cur_dir = '/local3/rumbaugh/EVLA/data/11A-138/%sSB%s/data/'%(EarlyorLate_arr[i],SBgrouparr[i])
    vis = '%sSB%s_%s.%s.%s.11.11A-138.%s.ms'%(EarlyorLate_arr[i],SBgrouparr[i],SBnumarr[i],montharr[i],datearr[i],SBlongnum_arr[i])
    os.chdir('%s'%cur_dir)
    numfields = fieldsdict[EarlyorLate_arr[i]][SBgrouparr[i]]
    ifield = 0
    print '\n%s'%vis
    while ((ifield < numfields+1) & (endloop < 0.5)):
        ispw = 0
        print 'field = %i'%ifield
        while ((ispw < 2) & (endloop < 0.5)):
            print 'spw = %i'%ispw
            plotms(vis=vis,field='%i'%ifield,spw='%i'%ispw)
            con =  raw_input("Continue? \n(y/n)")
            if ((con != 'y') & (con != 'yes') & (con != 'Y') & (con != 'Yes')): 
                print '\nEnding script...'
                endloop = 1
            ispw += 1
        ifield += 1
    i += 1
if endloop < 0.4: print '\n\nAll Done!\n'
            
