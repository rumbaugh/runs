import numpy as np
execfile('/mnt/data2/rumbaugh/EVLA/11A-138/scripts/utils_11A-138.py')

set_obs_arr()

FILE = open('/mnt/data2/rumbaugh/EVLA/11A-138/scripts/obsreflist.txt','w')

for EorL in ['Early','Late']:
    for groupnum in np.sort(EVLA_obs_dict[EorL].keys()):
        for SBnum in np.sort(EVLA_obs_dict[EorL][groupnum].keys()):
            FILE.write('%5s %i %2s\n'%(EorL,groupnum,str(SBnum)))
FILE.close()
