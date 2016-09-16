import numpy as np
cr = read_file('/local3/rumbaugh/ChandraData/nh.list.dat')
nh = copy_colvals(cr,'col1')
names = copy_colvals(cr,'col2')
crt = read_file('/local3/rumbaugh/ChandraData/times.list.temp.dat')
times = copy_colvals(crt,'col1')
i = np.size(times)-1
print names,nh,times,i
if i == 0:
    ttimes = times
    times = np.zeros(1)
    times[0] = ttimes
print names,nh,times,i
print names[i],nh[i],times[i]


load_pha("spec_%i_soft_grp.pi"%(names[i]))
rmf1 = unpack_rmf("spec_%i_soft.wrmf"%(names[i]))
set_rmf(rmf1)
arf1 = unpack_arf("spec_%i_soft.warf"%(names[i]))
set_arf(arf1)
ignore()
notice(0.5,2.0)
paramprompt()
set_model(powlaw1d.pl*xswabs.abs1)
pl.gamma = 1.4
pl.ampl = 1.0
abs1.nh = nh[i]/100.0
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
eflx2 = calc_energy_flux(0.5,2.0)
cnt2flux = time*eflx2
print "Count rate to unabsorbed flux conversion: " + str(cnt2flux)
FILE = open('/local3/rumbaugh/ChandraData/%i/cnt2flux.conv.dat'%(names[i]),'w')
FILE.write(str(cnt2flux) + ' soft\n')

load_pha("spec_%i_hard_grp.pi"%(names[i]))
rmf1 = unpack_rmf("spec_%i_hard.wrmf"%(names[i]))
set_rmf(rmf1)
arf1 = unpack_arf("spec_%i_hard.warf"%(names[i]))
set_arf(arf1)
ignore()
notice(2.0,10.0)
paramprompt()
set_model(powlaw1d.pl*xswabs.abs1)
pl.gamma = 1.4
pl.ampl = 1.0
abs1.nh = nh[i]
freeze(abs1.nh)
time = times[i]
fake_pha(1,arf1,rmf1,time)
mcnt = calc_model_sum(2.0,8.0)
pl.ampl = 1.0/mcnt
freeze(pl.ampl)
fake_pha(1,arf1,rmf1,time)
eflx = calc_energy_flux(2.0,8.0)
mcnt2 = calc_model_sum(2.0,8.0)
abs1.nh = 0.0
fake_pha(1,arf1,rmf1,time)
eflx2 = calc_energy_flux(2.0,8.0)
cnt2flux = time*eflx2
print "Count rate to unabsorbed flux conversion: " + str(cnt2flux)
FILE.write(str(cnt2flux) + ' hard\n')
FILE.close()
exit
