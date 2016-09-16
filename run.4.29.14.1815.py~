import numpy as np
execfile('/mnt/data2/rumbaugh/EVLA/11A-138/scripts/utils_11A-138.py')

set_obs_arr()
for EorL in ['Early','Late']:
    for groupnum in [1,2,3]:
        if ((EorL == 'Late') | (groupnum < 3)):
            for SBnum in EVLA_obs_dict[EorL][groupnum]:
                vis = EVLA_obs_dict[EarlyorLate][groupnum][SBnum]
                tflagdata(vis=vis,scan='1')
