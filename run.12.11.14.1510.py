import numpy as np

execfile('/home/rumbaugh/B1938+666_files/scripts/utils_11A-138.py')
set_obs_arr()

rms_tot = 0.

for EorL in ['Late']:
    for groupnum in np.sort(EVLA_obs_dict[EorL].keys()):
        set_fields(EorL,groupnum)
        for SBnum in np.sort(EVLA_obs_dict[EorL][groupnum].keys()):
            if SBnum != 'X': SBnum = int(SBnum)
            date = EVLA_date_dict[EorL][groupnum][SBnum]
            #for field,fieldname in zip(CSOfields_arr,CSOnames):
            #    source = fieldname
            #    FILE.write(opening_string)
            #    uvfile = '/mnt/data2/rumbaugh/EVLA/11A-138/data/%sSB%i/data/%sSB%i_%s.%s.11A-138.%s.uvfits'%(EorL,groupnum,EorL,groupnum,str(SBnum),EVLA_date_dict[EorL][groupnum][SBnum],fieldname)
            #    FILE.write('obs %s\n'%uvfile)
            #    FILE.write(setup_string)
            #    FILE.write('addcmp 0.1,true,0,0,varpos\n')
            #    FILE.write(fit_string)
            #    outfile = '/mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit_wrms.%s.%sSB%i_%s.fixpos.%s.mod'%(source,EorL,groupnum,str(SBnum),date)
            #    FILE.write('wmod %s\n'%outfile)
            #    FILE.write(end_string)
            for field,fieldname in zip(lensfields_arr,lensnames):
                source = fieldname
                if SBnum != 'X':
                    infile = '/home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.%s.%sSB%i_%s.fixpos.%s.mod'%(source,EorL,groupnum,str(SBnum),date)
                    cr = np.loadtxt(infile,comments='!',dtype='string')
                    rms = float(cr[-1][0])
                    rms_tot = np.sqrt(rms_tot**2+rms**2)
print rms_tot
