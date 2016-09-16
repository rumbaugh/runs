import numpy as np
import os

gc=15

band_dict={'soft': {'erange': '0.5-2.0','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','LB':0.5,'UB':8.0}}

times=np.array([49383.247922195])
nh = np.array([2.79])
obs = np.array(['7914'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,1)}

obj_dict=dict(zip(np.array(["7914"]),np.zeros(1)))
names=obj_dict.keys()
for i in range(0,1): 
    tmp_obs=names[i].split('+')
    if len(tmp_obs)==1:
        obj_dict[names[i]]={'exp':obs_dict[names[i]]['exp'],'nh':obs_dict[names[i]]['nh']}
    else:
        obj_dict[names[i]]={'exp':obs_dict[tmp_obs[0]]['exp']+obs_dict[tmp_obs[1]]['exp'],'nh':obs_dict[tmp_obs[0]]['nh']}
    os.chdir('/home/rumbaugh/Chandra/%s'%names[i])
    FILE = open('7914.cnt2flux.conv.dat','w')
    for band in ['soft','hard']:
        specbase="spec_%s_%s"%(names[i],band)
        if len(tmp_obs)>1:specbase="spec_%s_%s_combined_src"%(names[i],band)
        load_pha("%s.pi"%(specbase))
        rmf1 = unpack_rmf("%s.rmf"%(specbase))
        set_rmf(rmf1)
        arf1 = unpack_arf("%s.arf"%(specbase))
        set_arf(arf1)
        print calc_data_sum(lo=band_dict[band]['LB'],hi=band_dict[band]['UB'])
        ignore()
        notice(band_dict[band]['LB'],band_dict[band]['UB'])
        group_counts(gc)
        paramprompt()
        set_model(powlaw1d.pl*xswabs.abs1)
        pl.gamma = 1.4
        pl.ampl = 1.0
        abs1.nh = nh[i]/100.0
        freeze(abs1.nh)
        time = obj_dict[names[i]]['exp']
        fake_pha(1,arf1,rmf1,time)
        mcnt = calc_model_sum(band_dict[band]['LB'],band_dict[band]['UB'])
        pl.ampl = 1.0/mcnt
        freeze(pl.ampl)
        fake_pha(1,arf1,rmf1,time)
        eflx = calc_energy_flux(band_dict[band]['LB'],band_dict[band]['UB'])
        mcnt2 = calc_model_sum(band_dict[band]['LB'],band_dict[band]['UB'])
        abs1.nh = 0.0
        fake_pha(1,arf1,rmf1,time)
        eflx2 = calc_energy_flux(band_dict[band]['LB'],band_dict[band]['UB'])
        cnt2flux = time*eflx2
        print "Count rate to unabsorbed flux conversion: " + str(cnt2flux)
        FILE.write('%E %s\n'%(cnt2flux,band))
    FILE.close()
