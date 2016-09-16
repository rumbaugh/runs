import numpy as np
names = np.array(['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757'])
sroot = np.array(['7914','6933+7343','9403+9840','10444+10924','RXJ1757'])
nha = np.array([2.79,1.23,1.16,5.66,4.07])/100
times = np.array([49383.247922195,46103.507982594,48391.890220549,49548.501183658,46451.792387024])
zs = np.array([0.82,0.9,0.76,0.84,0.69])
for i in range(0,5):
    if i < 2:
        path = '/scratch/rumbaugh/ciaotesting/%s/master'%(names[i])
    else:
        path = '/home/rumbaugh/ChandraData/%s/master/spec'%names[i])
    
    load_pha("%s/spec_%s_soft_grp.pi"%(path,names[i]))
    rmf1 = unpack_rmf("%s/spec_%s_soft.wrmf"%(path,names[i]))
    set_rmf(rmf1)
    arf1 = unpack_arf("%s/spec_%s_soft.warf"%(path,names[i]))
    set_arf(arf1)
    ignore()
    notice(0.5,2)
    paramprompt()
    set_model(powlaw1d.pl*xswabs.abs1)
    pl.gamma = 1.4
    abs1.nh = nha[i]
    freeze(abs1.nh)
    time = times[i]
    fake_pha(1,arf1,rmf1,time)
    mcnt = calc_model_sum(0.5,2.0)
    pl.ampl = 1.0/mcnt
    freeze(pl.ampl)
    fake_pha(1,arf1,rmf1,time)
    eflx = calc_energy_flux(0.5,2.0)
    mcnt2 = calc_model_sum(0.5,2.0)
    abs1.nh = 0.0
    fake_pha(1,arf1,rmf1,time)
    eflx2 = calc_energy_flux(0.5/(1+zs[i]),8.0/(1+zs[i]))) 
    cnt2flux = time*eflx2
    print "\nField: %s"%(names[i])
    print "Count rate to unabsorbed flux conversion: " + str(cnt2flux)

