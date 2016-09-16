execfile("/home/rumbaugh/FindCloseSources.py")
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
f2l = np.array([1.676,1.987,1.987,1.310,1.310,1.580,1.034])/(0.7*0.7)
matchfiles = np.array(['FINAL.matched.0023.specnXray.nov2010.rumbaugh.cat','FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat[opt colnames=none]','FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat[opt colnames=none]','FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat[opt colnames=none]','FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat[opt colnames=none]','FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat[opt colnames=none]','FINAL.matched.N200.specnXray.nov2010.rumbaugh.cat[opt colnames=none]'])
mx = (43.2104078-43.348505)/(240.9472-241.28263)
cl1324rac = 0.5*(30.86373172217+30.279328719557)
icnt = -1
names = np.array(['Cl0023','Cl1604','Cl1604','Cl1324','Cl1324','NEP5281','RXJ1757'])
st = time.time()
tarr = np.zeros(8)
tarr[0] = st
for i in names:
    icnt += 1
    crmf = read_file("/home/rumbaugh/LFC/" + matchfiles[icnt])
    crX = read_file("/scratch/rumbaugh/ciaotesting/" + i + "/" + mas0[icnt] + "/photometry/" + i + ".xray_phot.soft_hard_full.dat")
    ramf,decmf = get_colvals(crmf,'col14'),get_colvals(crmf,'col15')
    zmf = get_colvals(crmf,'col9')
    q = get_colvals(crmf,'col11')
    raX,decX = get_colvals(crX,'col1'),get_colvals(crX,'col2')
    if ((icnt == 2) or (icnt == 1)): ramf,decmf = get_colvals(crmf,'col20'),get_colvals(crmf,'col21')
    ncntsS,ncntsH,ncntsF = get_colvals(crX,'col6'),get_colvals(crX,'col7'),get_colvals(crX,'col8')
    ncnts = np.zeros((2,len(ncntsS)))
    ncnts[0,:] = ncntsS
    ncnts[1,:] = ncntsH
    gq = np.where(q > 2.5)
    gq = gq[0]
    closeinds = np.zeros(len(gq))
    if ((icnt != 2) and (icnt != 4)): FILEs = open("/home/rumbaugh/LFC/XrayLums." + i + ".soft.8.10.11.dat","w")
    if ((icnt != 2) and (icnt != 4)): FILEh = open("/home/rumbaugh/LFC/XrayLums." + i + ".hard.8.10.11.dat","w")
    xraylums = np.zeros((2,len(gq)))
    flux = np.zeros((2,len(gq)))
    for j in range(0,2):
        load_pha('spec/spec_' + str(inum[icnt]) + '_' + str(z[j]) + '_grp.pi')
        rmf1 = unpack_rmf('spec/spec_' + str(inum[icnt]) + '_' + str(z[j]) + '.wrmf')
        set_rmf(rmf1)
        arf1 = unpack_arf('spec/spec_' + str(inum[icnt]) + '_' + str(z[j]) + '.warf')
        set_arf(arf1)
        for iq in range(0,len(gq)):
            ci = FindCloseSources(ramf[gq[iq]],decmf[gq[iq]],1,raX,decX,0)
            closeinds[iq] = ci[0]
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
            eflx2 = calc_energy_flux(ndL[j]/(1+zmf[gq[iq]]),ndH[j]/(1+zmf[gq[iq]]))
            cnt2flux = times*eflx2
            #print 'Count rate to unabsorbed flux conversion: ' + str(cnt2flux)
            #FILE = open('c2f/c2f.' + str(inum[icnt]) + '.' + str(z) + '.txt','w')
            #FILE.write(str(cnt2flux))
            #FILE.close()
            flux[j,iq] = ncnts[j,closeinds[iq]]*cnt2flux/exps[icnt]
            if ((icnt == 0) or (icnt > 4)):
                if j == 0: FILEs.write('%E %E %f %f %f %f\n'%(10.0**15.0*flux[j,iq]*f2l[icnt],flux[j,iq],ncnts[j,closeinds[iq]],zmf[gq[iq]],ramf[gq[iq]],decmf[gq[iq]]))
                if j == 1: FILEh.write('%E %E %f %f %f %f\n'%(10.0**15.0*flux[j,iq]*f2l[icnt],flux[j,iq],ncnts[j,closeinds[iq]],zmf[gq[iq]],ramf[gq[iq]],decmf[gq[iq]]))
            if icnt == 1:
                dectemp = mx*(ramf[gq[iq]]-241.28263)+43.348505
                if decmf[gq[iq]] < dectemp:
                    if j == 0: FILEs.write('%E %E %f %f %f %f\n'%(10.0**15.0*flux[j,iq]*f2l[icnt],flux[j,iq],ncnts[j,closeinds[iq]],zmf[gq[iq]],ramf[gq[iq]],decmf[gq[iq]]))
                    if j == 1: FILEh.write('%E %E %f %f %f %f\n'%(10.0**15.0*flux[j,iq]*f2l[icnt],flux[j,iq],ncnts[j,closeinds[iq]],zmf[gq[iq]],ramf[gq[iq]],decmf[gq[iq]]))
            if icnt == 2:
                dectemp = mx*(ramf[gq[iq]]-241.28263)+43.348505
                if decmf[gq[iq]] > dectemp:
                    if j == 0: FILEs.write('%E %E %f %f %f %f\n'%(10.0**15.0*flux[j,iq]*f2l[icnt],flux[j,iq],ncnts[j,closeinds[iq]],zmf[gq[iq]],ramf[gq[iq]],decmf[gq[iq]]))
                    if j == 1: FILEh.write('%E %E %f %f %f %f\n'%(10.0**15.0*flux[j,iq]*f2l[icnt],flux[j,iq],ncnts[j,closeinds[iq]],zmf[gq[iq]],ramf[gq[iq]],decmf[gq[iq]]))
            if icnt == 3:
                if decmf[gq[iq]] > cl1324rac:
                    if j == 0: FILEs.write('%E %E %f %f %f %f\n'%(10.0**15.0*flux[j,iq]*f2l[icnt],flux[j,iq],ncnts[j,closeinds[iq]],zmf[gq[iq]],ramf[gq[iq]],decmf[gq[iq]]))
                    if j == 1: FILEh.write('%E %E %f %f %f %f\n'%(10.0**15.0*flux[j,iq]*f2l[icnt],flux[j,iq],ncnts[j,closeinds[iq]],zmf[gq[iq]],ramf[gq[iq]],decmf[gq[iq]]))
            if icnt == 4:
                if decmf[gq[iq]] < cl1324rac:
                    if j == 0: FILEs.write('%E %E %f %f %f %f\n'%(10.0**15.0*flux[j,iq]*f2l[icnt],flux[j,iq],ncnts[j,closeinds[iq]],zmf[gq[iq]],ramf[gq[iq]],decmf[gq[iq]]))
                    if j == 1: FILEh.write('%E %E %f %f %f %f\n'%(10.0**15.0*flux[j,iq]*f2l[icnt],flux[j,iq],ncnts[j,closeinds[iq]],zmf[gq[iq]],ramf[gq[iq]],decmf[gq[iq]]))
    if ((icnt != 1) and (icnt != 3)): FILEs.close()
    if ((icnt != 1) and (icnt != 3)): FILEh.close()
    tarr[icnt+1] = time.time()
    print '%i/7 done. Elapsed: %10.4f seconds. ETA: %10.4f seconds'%(icnt+1,tarr[icnt+1]-st,(tarr[icnt+1]-st)*((7-icnt-1)/(1.0*icnt+1.0)))
