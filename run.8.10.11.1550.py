import numpy as np
import time
z = np.array(['soft','hard'])
nd = np.array(['0.5,2.0','2.0,8.0'])
ndL = np.array([0.5,2.0])
ndH = np.array([2.0,8.0])
nh = np.array([2.79,1.22,1.22,1.155,1.155,5.66,4.07])
mas0 = np.array(['7914','master','master','master','master','master','master'])
mas = np.array(['7914','6932','master','master','master','master','master'])
inum = np.array(['7914','6932','6933+7343','9403+9840','9404+9836','10444+10924','10443+11999'])
singnum = np.array([7914,6932,6933,9403,9404,10444,11999])
mas2 = np.array(['7914','6932','master','9403','9404','master','master'])
icnt = 0
zs = np.array([0.84,0.9,0.9,0.76,0.76,0.82,0.69])
exps = np.array([49383.247922195,49478.092354796,46103.507982594,48391.890220549,50399.00069391,49548.501183658,46451.792387024])
f2l = np.array([1.676,1.987,1.987,1.310,1.310,1.580,1.034])

mx = (43.2104078-43.348505)/(240.9472-241.28263)
cl1324rac = 0.5*(30.86373172217+30.279328719557)
icnt = -1
names = np.array(['Cl0023','Cl1604','Cl1604','Cl1324','Cl1324','NEP5281','RXJ1757'])
st = time.time()
tarr = np.zeros(8)
tarr[0] = st
zmf = [0.82,0.86,0.86,0.66,0.66,0.8,0.69]

FILEs = open("/home/rumbaugh/LFC/c2f.pointings.avgz.8.10.11.dat",'w')
c2ftemp = np.array([1e-10,1e-10])

for i in names:
    icnt += 1
    for j in range(0,2):
        load_pha('/home/rumbaugh/CDF/spec/spec_' + str(inum[icnt]) + '_' + str(z[j]) + '_grp.pi')
        rmf1 = unpack_rmf('/home/rumbaugh/CDF/spec/spec_' + str(inum[icnt]) + '_' + str(z[j]) + '.wrmf')
        set_rmf(rmf1)
        arf1 = unpack_arf('/home/rumbaugh/CDF/spec/spec_' + str(inum[icnt]) + '_' + str(z[j]) + '.warf')
        set_arf(arf1)
        ignore()
        notice(ndL[j],ndH[j])
        paramprompt()
        set_model(powlaw1d.pl*xswabs.abs1)
        thaw(pl.ampl)
        pl.ampl = 1.0
        pl.gamma = 1.4
        abs1.nh = nh[icnt]/100.0
        freeze(abs1.nh)
        times = exps[icnt]
        fake_pha(1,arf1,rmf1,times)
        mcnt = calc_model_sum(ndL[j],ndH[j])
        pl.ampl = 1.0/mcnt
        freeze(pl.ampl)
        fake_pha(1,arf1,rmf1,times)
        eflx = calc_energy_flux(ndL[j],ndH[j])
        mcnt2 = calc_model_sum(ndL[j],ndH[j])
        abs1.nh = 0.0
        fake_pha(1,arf1,rmf1,times)
        eflx2 = calc_energy_flux(ndL[j]/(1+zmf[icnt]),ndH[j]/(1+zmf[icnt]))
        cnt2flux = times*eflx2
        c2ftemp[j] = cnt2flux
    FILEs.write('%E  %E\n'%(c2ftemp[0],c2ftemp[1]))
FILEs.close()
