import numpy as np
import os

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1053","rxj1716"])

cr_aim=np.loadtxt('/home/rumbaugh/Chandra/aimpnts.dat',dtype={'names':('ID','RA','DEC','TIME'),'formats':('|S16','f8','f8','f8')})

gc=15

band_dict={'soft': {'erange': '0.5-2.0','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','LB':0.5,'UB':8.0}}

times=np.array([51730.160737324,125146.86866667,79084.755891771,61469.789688443,105735.52582365,58307.676632384,65311.025181476,14370.453707409,92237.849235535,88973.209339125])
nh = np.array([3.71,2.73,1.44,2.73,1.98,1.76,1.98,2.86,0.58,2.86])
obs = np.array(['548','927','1662','1708','2227','2229','2452','3181','4936','4987'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,10)}

cr_nh=np.loadtxt('/home/rumbaugh/Chandra/NH_table.dat',dtype={'names':('ID','nh'),'formats':('|S16','f8')})


obj_dict=dict(zip(np.array(["548","1662","2229","4936","927+1708","2227+2452","3181+4987"]),np.zeros(7)))
names=obj_dict.keys()
for field in targets: 
    g=np.where(cr_aim['ID']==field)[0][0]
    g2=np.where(cr_nh['ID']==field)[0][0]
    time=cr_aim['TIME'][g]
    nh=cr_nh['nh'][g2]
    #tmp_obs=names[i].split('+')
    #if len(tmp_obs)==1:
    #    obj_dict[names[i]]={'exp':obs_dict[names[i]]['exp'],'nh':obs_dict[names[i]]['nh']}
    #else:
    #    obj_dict[names[i]]={'exp':obs_dict[tmp_obs[0]]['exp']+obs_dict[tmp_obs[1]]['exp'],'nh':obs_dict[tmp_obs[0]]['nh']}
    os.chdir('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%field)
    FILE = open('cnt2flux.conv.dat','w')
    for band in ['soft','hard']:
        specbase="spec_%s_%s"%(field,band_dict[band]['erange'])
        if len(tmp_obs)>1:specbase="spec_%s_%s_combined_src"%(field,band)
        load_pha("%s.pi"%(specbase))
        rmf1 = unpack_rmf("%s.rmf"%(specbase))
        set_rmf(rmf1)
        arf1 = unpack_arf("%s.arf"%(specbase))
        set_arf(arf1)
        ignore()
        notice(band_dict[band]['LB'],band_dict[band]['UB'])
        group_counts(gc)
        paramprompt()
        set_model(powlaw1d.pl*xswabs.abs1)
        pl.gamma = 1.4
        pl.ampl = 1.0
        abs1.nh = nh/100.0
        freeze(abs1.nh)
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
