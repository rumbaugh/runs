import numpy as np
execfile('/mnt/data2/rumbaugh/EVLA/11A-138/scripts/utils_11A-138.py')

set_obs_arr()
for EorL in ['Late']:
    for groupnum in [1,2,3]:
        for SBnum in EVLA_obs_dict[EorL][groupnum]:
            #unflagEVLA(EorL,groupnum,SBnum)
            quackEVLA(EorL,groupnum,SBnum)
