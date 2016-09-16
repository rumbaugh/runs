import numpy as np
import time
import math as m
execfile('/home/rumbaugh/get_cols_batch.py')
horf = np.array(['soft','hard'])
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

mx = (43.2104078-43.348505)/(240.9472-241.28263)
cl1324rac = 0.5*(30.86373172217+30.279328719557)
icnt = -1
names = np.array(['Cl0023','Cl1604','Cl1604','Cl1324','Cl1324','NEP5281','RXJ1757'])
snames = np.array(['0023','1604','1604','1322','1322','N5281','N200'])
st = time.time()
tarr = np.zeros(8)
tarr[0] = st
zmf = [0.84,0.9,0.9,0.76,0.76,0.82,0.69]

#FILEs = open("/home/rumbaugh/LFC/testc2f.pointings.avgz.8.9.11.dat",'w')
c2ftemp = np.array([1e-10,1e-10])

zhb = [0.87,0.96,0.96,0.79,0.79,0.84,0.71]
zlb = [0.820,0.84,0.84,0.65,0.65,0.80,0.68]
#ids = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']

cr4piDl2 = read_file('/home/rumbaugh/input.4piDl2.8.9.11.dat')
fourPiDL2 = get_colvals(cr4piDl2,'col10')*1e-57/(0.7*0.7)
ztest = get_colvals(cr4piDl2,'col1')

m1604 = (43.35861-43.28914)/(240.9075-241.19939)
y01604 = 43.28914
x01604 = 241.19939

cnt4pd = -1

for i in names:
    xpfile = '/scratch/rumbaugh/ciaotesting/' + i + '/master/photometry/' + i + '.xray_phot.soft_hard_full.dat'
    if ((icnt != 1) & (icnt != 3)): crxp = read_file(xpfile)
    if ((icnt != 1) & (icnt != 3)): xpRA,xpDec,sflux,hflux,fflux,sncnts,hncnts,fncnts,ssig,hsig,fsig,wssig,whsig,wfsig,wmask,wflag = get_cols_batch(crxp,16)
    sfile = '/home/rumbaugh/LFC/FINAL.matched.' + snames[icnt+1]  + '.specnXray.nov2010.rumbaugh.noheader.cat'
    if ((icnt != 1) & (icnt != 3)): crs = read_file(sfile)
    if ((icnt != 1) & (icnt != 3) & (icnt != 0)): LFC_ID,mask,slit,RA_opt,dec_opt,rband, iband, zband, z,z_err,q,old_ID, Xray_ID, RA_Xray,dec_Xray,poserr, Num_opt, Rel,Sig = get_cols_batch(crs,19)
    if icnt == 0: 
        LFC_ID,mask,slit,RA_opt,dec_opt,rband, iband, zband, z,z_err,q,old_ID, maskACS, RA_ACS, dec_ACS,ACS_ID, F606W, F814W, Xray_ID, RA_Xray,dec_Xray,poserr, Num_opt, Rel,Sig = get_cols_batch(crs,25)
        crxm = read_file("/home/rumbaugh/Cl1604.opt_Xray_matched_catalog_3high.corrected.twk.8.4.11.dat")
        xpID = get_colvals(crxm,'col25')
    icnt += 1
    g = np.where((z > zlb[icnt]) & (z < zhb[icnt]) & (q > 2.3))
    g = g[0]
    if ((icnt != 2) and (icnt != 4)):
        temp4piDl2 = np.zeros(len(g))
        for i4 in range(0,len(g)):
            cnt4pd += 1
            if ((ztest[cnt4pd]+ 0.001 < z[g[i4]]) | (ztest[cnt4pd]- 0.001 > z[g[i4]])): sys.exit("%f != %f"%(ztest[cnt4pd],z[g[i4]]))
            temp4piDl2[i4] = fourPiDL2[cnt4pd]
    for j in range(0,2):
        load_pha('/home/rumbaugh/CDF/spec/spec_' + str(inum[icnt]) + '_' + str(horf[j]) + '_grp.pi')
        rmf1 = unpack_rmf('/home/rumbaugh/CDF/spec/spec_' + str(inum[icnt]) + '_' + str(horf[j]) + '.wrmf')
        set_rmf(rmf1)
        arf1 = unpack_arf('/home/rumbaugh/CDF/spec/spec_' + str(inum[icnt]) + '_' + str(horf[j]) + '.warf')
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
    if ((icnt != 2) and (icnt != 4)): FILES = open("/home/rumbaugh/LFC/XrayLums." + i + ".soft.8.10.11.dat","w")
    if ((icnt != 2) and (icnt != 4)): FILEH = open("/home/rumbaugh/LFC/XrayLums." + i + ".hard.8.10.11.dat","w")
    for i4 in range(0,len(g)):
        tflux = 0.0
        tflux2 = 0.0
        flag = 0
        for j in range(0,2):
            flag2 = 0
            load_pha('/home/rumbaugh/CDF/spec/spec_' + str(inum[icnt]) + '_' + str(horf[j]) + '_grp.pi')
            rmf1 = unpack_rmf('/home/rumbaugh/CDF/spec/spec_' + str(inum[icnt]) + '_' + str(horf[j]) + '.wrmf')
            set_rmf(rmf1)
            arf1 = unpack_arf('/home/rumbaugh/CDF/spec/spec_' + str(inum[icnt]) + '_' + str(horf[j]) + '.warf')
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
            eflx2 = calc_energy_flux(ndL[j]/(1+z[g[i4]]),ndH[j]/(1+z[g[i4]]))
            print mcnt2,calc_energy_flux(ndL[j],ndH[j]),eflx2,z[g[i4]]
            cnt2flux = times*eflx2
            c2ftemp[j] = cnt2flux
            if ((j == 0) & (icnt != 1) & (icnt != 2)): cntstemp = sncnts[int(Xray_ID[g[i4]])]
            if ((j == 0) & ((icnt == 1) | (icnt == 2))): cntstemp = sncnts[int(xpID[int(Xray_ID[g[i4]])])]
            if ((j == 1) & (icnt != 1) & (icnt != 2)): cntstemp = hncnts[int(Xray_ID[g[i4]])]
            if ((j == 1) & ((icnt == 1) | (icnt == 2))): cntstemp = hncnts[int(xpID[int(Xray_ID[g[i4]])])]
            if ((icnt == 1 ) & (m1604*(RA_Xray[g[i4]]-x01604)+y01604 > dec_Xray[g[i4]])):  
                tflux += cnt2flux*cntstemp/exps[icnt]
                tflux2 += c2ftemp[j]*cntstemp/exps[icnt]
                flag,flag2 = 1,1
            if ((icnt == 2 ) & (m1604*(RA_Xray[g[i4]]-x01604)+y01604 < dec_Xray[g[i4]])):  
                tflux += cnt2flux*cntstemp/exps[icnt]
                tflux2 += c2ftemp[j]*cntstemp/exps[icnt]
                flag,flag2 = 1,1
            if ((icnt == 3 ) & (dec_Xray[g[i4]] > 30.6)):  
                tflux += cnt2flux*cntstemp/exps[icnt]
                tflux2 += c2ftemp[j]*cntstemp/exps[icnt]
                flag,flag2 = 1,1
            if ((icnt == 4 ) & (dec_Xray[g[i4]] < 30.6)):  
                tflux += cnt2flux*cntstemp/exps[icnt]
                tflux2 += c2ftemp[j]*cntstemp/exps[icnt]
                flag,flag2 = 1,1
            if ((icnt == 0) | (icnt > 4.5)): 
                tflux += cnt2flux*cntstemp/exps[icnt]
                tflux2 += c2ftemp[j]*cntstemp/exps[icnt]
                flag,flag2 = 1,1
            if flag2 == 1:
                if j == 0: FILES.write('%E  %E %f %f %f %f %i\n'%(cnt2flux*cntstemp/exps[icnt]*temp4piDl2[i4]*10**15,cnt2flux*cntstemp/exps[icnt],cntstemp,z[g[i4]],RA_Xray[g[i4]],dec_Xray[g[i4]],q[g[i4]]))
                if j == 1: FILEH.write('%E  %E %f %f %f %f %i\n'%(cnt2flux*cntstemp/exps[icnt]*temp4piDl2[i4]*10**15,cnt2flux*cntstemp/exps[icnt],cntstemp,z[g[i4]],RA_Xray[g[i4]],dec_Xray[g[i4]],q[g[i4]]))
        if flag == 1:
            print 'z = %6.4f  %6.4f  %8.5f  %8.5f\n'%(z[g[i4]],10**(m.log10(tflux*temp4piDl2[i4])+15),m.log10(tflux*temp4piDl2[i4])+57,m.log10(tflux2*f2l[icnt])+57)
    #FILEs.write('%E  %E\n'%(c2ftemp[0],c2ftemp[1]))
    if ((icnt != 1) and (icnt != 3)):
        FILES.close()
        FILEH.close()
