import numpy as np
execfile('/home/rumbaugh/convMpc2cm.py')

load_pha("/home/rumbaugh/diffuse/diffuse_stuff/cluster.6932a.3.28.pi")

try:
    lumLB
except NameError:
    lumLB = 1e42
try:
    lumUB
except NameError:
    lumUB = 1e44

lumLBa = lumLB/(1e40)
lumUBa = lumUB/(1e40)

FILE= open('/home/rumbaugh/paperstuff/xraybounds.5.3.11.dat','w')

names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
zlb = np.array([0.655,0.808,0.82,0.84,0.68])
zub = np.array([0.785,0.828,0.856,0.96,0.705])
nha = np.array([1.16,5.66,2.79,1.23,4.07])/100
crzlb = read_file('/home/rumbaugh/ccout.zlb.5.3.11.dat')
crzub = read_file('/home/rumbaugh/ccout.zub.5.3.11.dat')
DLzlb = get_colvals(crzlb,'col9')*0.7
DLzub = get_colvals(crzub,'col9')*0.7

for i in range(0,5):
    set_model(powlaw1d.pl*xswabs.abs1)
    pl.ampl = 1.0
    pl.gamma = 1.4
    thaw(pl.ampl)
    rs.abundanc = 0.3
    abs1.nh = nha[i]
    freeze(abs1.nh)
    mcnt = calc_model_sum(0.5,8.0)
    pl.ampl = 1.0/mcnt
    abs1.nh = 0.0
    eflxl = calc_energy_flux(0.5/zlb[i],8.0/zlb[i])
    eflxu = calc_energy_flux(0.5/zub[i],8.0/zub[i])
    DLzlba = convMpc2cm(d=DLzlb[i],abb=True)
    DLzuba = convMpc2cm(d=DLzub[i],abb=True)
    fluxhi = lumUBa*1e-8/(4*m.pi*DLzlba**2)
    fluxlo = lumLBa*1e-8/(4*m.pi*DLzuba**2)
    cntliml = fluxlo/eflxu
    cntlimu = fluxhi/eflxl
    FILE.write('%7s %9.3f %9.3f\n'%(names[i],cntliml,cntlimu))
FILE.close()
    
    
