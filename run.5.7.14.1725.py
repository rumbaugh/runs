import numpy as np
import math as m
import sys
import os
import time

execfile('/mnt/data2/rumbaugh/EVLA/11A-138/scripts/utils_11A-138.py')

set_obs_arr()

for EorL in ['Early']:
    for groupnum in [2]:
        for SBnum in [9,10]:
            quackEVLA(EorL,groupnum,SBnum)
            run_calib(EorL,groupnum,SBnum)
