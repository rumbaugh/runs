import numpy as np
execfile('/home/rumbaugh/obs_lens.radio_monitoring.py')
for lens in ['MG0414','B0712','B1938']:
    times = np.zeros(0)
    for gnum in obs_len_dict[lens]:
        for SBnum in obs_len_dict[lens][gnum]:
            h1,m1,s1 = obs_len_dict[lens][gnum][SBnum][0].split(':')
            h2,m2,s2 = obs_len_dict[lens][gnum][SBnum][1].split(':')
            diff = 3600*(int(h2)-int(h1))+60*(int(m2)-int(m1))+float(s2)-float(s1)
            times = np.append(times,diff)
    print '%s - %f'%(lens,np.median(times))
