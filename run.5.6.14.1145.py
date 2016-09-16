import numpy as np
import math as m
import sys
import os
import time

execfile('/mnt/data2/rumbaugh/EVLA/11A-138/scripts/utils_11A-138.py')

set_obs_arr()

for EorL in ['Late']:
    for groupnum in np.sort(EVLA_obs_dict[EorL].keys()):
        for SBnum in np.sort(EVLA_obs_dict[EorL][groupnum].keys()):
            if SBnum == 'X': run_calib(EorL,groupnum,SBnum)
