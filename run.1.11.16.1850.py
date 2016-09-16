import numpy as np
import os

nd = np.array(['0.5,2.0','2.0,8.0'])
ndL = np.array([0.5,2.0])
ndH = np.array([2.0,8.0])
bands=np.array(['soft','hard','full'])
#nh=np.array([2.73,2.73,3.71])
nh=np.array([2.73,2.73,2.73])
exp1708,exp927=61469.789688443,125146.86866667
exps=np.array([exp927,exp1708,51730.160737324])
os.chdir('/home/rumbaugh/Chandra/7914')

obsid=np.array(['7914'])

for i in range(0,1):
    for j in range(0,2):
        load_pha('spec_%s_%s_grp.pi'%(obsid[i],bands[j]))
        rmf1=unpack_rmf('spec_%s_%s.rmf'%(obsid[i],bands[j]))
        arf1=unpack_arf('spec_%s_%s.arf'%(obsid[i],bands[j]))
        set_rmf(rmf1)
        set_arf(arf1)
        ignore()
        notice(ndL[j],ndH[j])
        paramprompt()
        set_model(powlaw1d.pl*xswabs.abs1)
        thaw(pl.ampl)
        pl.ampl = 1.0
        pl.gamma = 1.4
        abs1.nh = nh[i]/100.0
        freeze(abs1.nh)
        #times = exps[i]
        #fake_pha(1,arf1,rmf1,times)
        mcnt = calc_model_sum(ndL[j],ndH[j])
        pl.ampl = 1.0/mcnt
        freeze(pl.ampl)
        #fake_pha(1,arf1,rmf1,times)
        eflx = calc_energy_flux(ndL[j],ndH[j])
        mcnt2 = calc_model_sum(ndL[j],ndH[j])
        abs1.nh = 0.0
        #fake_pha(1,arf1,rmf1,times)
        eflx2 = calc_energy_flux(ndL[j]/(1+0.75),ndH[j]/(1+0.75))
        #print mcnt2,calc_energy_flux(ndL[j],ndH[j]),eflx2,0.75
        #print mcnt2,calc_energy_flux(ndL[j],ndH[j])/exps[i-1],eflx2/exps[i-1],0.75
        print eflx2
        print eflx2/eflx
