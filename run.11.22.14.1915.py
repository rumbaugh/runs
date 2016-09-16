import numpy as np

execfile('/home/rumbaugh/B1938+666_files/scripts/utils_11A-138.py')
set_obs_arr()
concat_vises = []

for EorL in ['Late']:
    for groupnum in np.sort(EVLA_obs_dict[EorL].keys()):
        set_fields(EorL,groupnum)
        for SBnum in np.sort(EVLA_obs_dict[EorL][groupnum].keys()):
            if SBnum != 'X': SBnum = int(SBnum)
            date = EVLA_date_dict[EorL][groupnum][SBnum]
            vistmp = '/home/rumbaugh/B1938+666_files/%sSB%i_%s.%s.11A-138.B1938+666.ms'%(EorL,groupnum,str(SBnum),EVLA_date_dict[EorL][groupnum][SBnum])
            concat_vises.append(vistmp)
concat(vis=concat_vises,concatvis='/home/rumbaugh/B1938+666_files/concatvis.B1938+666.ms')

exportuvfits(vis="/home/rumbaugh/B1938+666_files/concatvis.B1938+666.ms",fitsfile="/home/rumbaugh/B1938+666_files/concatvis.B1938+666.uvfits",datacolumn="corrected",field="0",spw="",antenna="",timerange="",nchan=-1,start=0,width=1,writesyscal=False,multisource=True,combinespw=True,writestation=True,padwithflags=True)
