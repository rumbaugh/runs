import numpy as np
execfile('/mnt/data2/rumbaugh/EVLA/11A-138/scripts/utils_11A-138.py')

set_obs_arr()

for EorL in ['Late']:
    #for groupnum in np.sort(EVLA_obs_dict[EorL].keys()):
    for groupnum in [2,3]:
        for SBnum in np.sort(EVLA_obs_dict[EorL][groupnum].keys()):
            print '%5s %i %2s\n'%(EorL,groupnum,str(SBnum))
            if SBnum != '?': SBnum = int(SBnum)
            vis = EVLA_obs_dict[EorL][groupnum][SBnum]
            plotants(vis=vis)
            f = raw_input('\n\nNext?\n\n')
            while ((f != 'y') & (f != 'Y')):
                print 'Invalid input'
                f = raw_input('\n\nNext?\n\n')
FILE.close()
