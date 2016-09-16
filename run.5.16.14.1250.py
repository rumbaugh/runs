import numpy as np
import os

execfile('/mnt/data2/rumbaugh/EVLA/11A-138/scripts/utils_11A-138.py')
set_obs_arr()

date = '5.16.14'

days4months_dict  = {1: 0, 2: 31, 3: 31+28, 4: 31+28+31, 5: 31+28+31+30, 6: 31+28+31+30+31, 7: 31+28+31+30+31+30, 8: 31+28+31+30+31+30+31, 9: 31+28+31+30+31+30+31+31, 10: 31+28+31+30+31+30+31+31+30, 11: 31+28+31+30+31+30+31+31+30+31, 12: 31+28+31+30+31+30+31+31+30+31+30}

sources_dict = {'Late': ['B1938+666'], 'Early': ['MG0414+0534','B0712+472']}
CSOs_dict = {'Late': ['J1414+4554','J1400+6210','J1545+4751','J0003+4807','J1823+7938','J1945+7055','J1816+3457','J1826+1831','J1734+0926'], 'Early': ['J0427+4133','J0204+0903','J0754+5324']}

for EorL in ['Late','Early']:
    for source in sources_dict[EorL]:
        FILE = open('/mnt/data2/rumbaugh/EVLA/11A-138/light_curves/lc_out.%s.%s.dat'%(source,date),'w')
        for groupnum in EVLA_obs_dict[EorL]:
            for SBnum in EVLA_obs_dict[EorL][groupnum]:
                if SBnum != 'X': SBnum = int(SBnum)
                day = days4months_dict[EVLA_time_dict[EorL][groupnum][SBnum]['month']] + EVLA_time_dict[EorL][groupnum][SBnum]['day'] + EVLA_time_dict[EorL][groupnum][SBnum]['hour']/24.
                FILE.write('%5s %i %2s %6.2f'%(EorL,groupnum,str(SBnum),day))
                try:
                    cr = np.loadtxt('/mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit_wrms.%s.%sSB%i_%s.fixpos.%s.mod'%(source,EorL,groupnum,str(SBnum),EVLA_date_dict[EorL][groupnum][SBnum]),dtype='string',comments='!')
                    num_img = np.shape(cr)[0]-1
                    for img in range(0,num_img):
                        fluxstr = cr[img][0]
                        FILE.write(' ' + fluxstr[:len(fluxstr)-1])
                    FILE.write(' %s\n'%(cr[num_img][0]))
                except IOError:
                    if source != 'B1938+666':
                        FILE.write(' 0 0 0 0 0\n')
                    else:
                        FILE.write(' 0 0 0 0 0 0 0\n')
        FILE.close()
    for source in CSOs_dict[EorL]:
        FILE = open('/mnt/data2/rumbaugh/EVLA/11A-138/light_curves/lc_out.%s.%s.dat'%(source,date),'w')
        for groupnum in EVLA_obs_dict[EorL]:
            for SBnum in EVLA_obs_dict[EorL][groupnum]:
                if SBnum != 'X': SBnum = int(SBnum)
                day = days4months_dict[EVLA_time_dict[EorL][groupnum][SBnum]['month']] + EVLA_time_dict[EorL][groupnum][SBnum]['day'] + EVLA_time_dict[EorL][groupnum][SBnum]['hour']/24.
                FILE.write('%5s %i %2s %6.2f'%(EorL,groupnum,str(SBnum),day))
                try:
                    cr = np.loadtxt('/mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit_wrms.%s.%sSB%i_%s.fixpos.%s.mod'%(source,EorL,groupnum,str(SBnum),EVLA_date_dict[EorL][groupnum][SBnum]),dtype='string',comments='!')
                    fluxstr = cr[0][0]
                    FILE.write(' ' + fluxstr[:len(fluxstr)-1])
                    FILE.write(' %s\n'%(cr[1][0]))
                except IOError:
                    FILE.write(' 0 0\n')
        FILE.close()
