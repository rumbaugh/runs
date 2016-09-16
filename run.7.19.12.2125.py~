execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/scale_estimators.py")
execfile("/home/rumbaugh/DStest.py")
execfile('/home/rumbaugh/angconvert.py')
execfile('/home/rumbaugh/CalcVelDisp.py')
import matplotlib
import matplotlib.pylab as pylab
import random as rand
c = 3.0*10**5

def sigclip(data,mean,sig,sigthresh=3.0):
    gsc = np.where((data < mean + sigthresh*sig) & (data > mean - sigthresh*sig))
    gsc = gsc[0]
    #if ccnt == 6:
    #    print mean,sig,data[gsc]
    return gsc

def CalcInitVelDisp(z,g,gcen,method,cenRA,cenDec):
    vels = (z[g[gcen]]-biweight_loc(z[g[gcen]]))*c/(1+z[g[gcen]])
    sig = CalcVelDisp(vels,method=method,ConfInvMethod='none')
    prevcen = 9999
    gcentemp = np.arange(len(gcen))
    meancen = biweight_loc(vels)
    velstemp = np.copy(vels)
    while len(gcentemp) < prevcen:
        prevcen = len(gcentemp)
        gcentemp = sigclip(velstemp,meancen,sig)
        velstemp = (z[g[gcen]]-biweight_loc(sz[g[gcen[gcentemp]]]))*(3.0*10**5)/(1+sz[g[gcen]])
        meancen = biweight_loc(velstemp[gcentemp])
        sig = CalcVelDisp(velstemp[gcentemp],method=method,ConfInvMethod='none')
        if names[i] == "RXJ1821": sig,sige = CalcVelDisp(z[g[gcen]],method=method,ConfInvMethod='jackknife')
        if names[i] == "RXJ1821": sig,sigeBSL,sigeBSH = CalcVelDisp(z[g[gcen]],method=method,ConfInvMethod='bootstrap')
    znew = sz[g[gcen[gcentemp]]]
    RAnew = RA[g[gcen[gcentemp]]]
    Decnew = Dec[g[gcen[gcentemp]]]
    srBnew = srB[g[gcen[gcentemp]]]
    siBnew = siB[g[gcen[gcentemp]]]
    szBnew = szB[g[gcen[gcentemp]]]
    for isid in range(0,len(gcentemp)):
        gsid = np.where(sID[g[gcen[gcentemp]]] == sID[g[gcen[gcentemp[isid]]]])
        gsid = gsid[0]
    vels = np.copy(velstemp)
    avg_z = biweight_loc(z[g[gcen[gcentemp]]])
    zsig = sig*(1+avg_z)/c
    gq = np.where(sq > 2.2)
    if names[i] == "RXJ1757": gq = np.where((sq > 2.2) & ((smask != 'N200M1') | (sslit != 64)) & ((smask != 'N200M1') | (sslit != 67)) & ((smask != 'N200M1') | (sslit != 80)) & ((smask != 'N200M1') | (sslit != 83)))
    if names[i] == "RXJ1821": gq = np.where((sq > 2.2) & ((z < 0.80721891) | (z > 0.80721901)))
    if names[i] == "Cl1604A": gq = np.where((sq > 2.2) & ((sID != "LFC_SC2_06516") | (z > 0.9)))
    if names[i] == "Cl1604B": gq = np.where((sq > 2.2) & ((sID != "LFC_SC1_01472") | (z < 0.87)))
    gq = gq[0]
    dists2 = np.zeros(len(gq))
    for j in range(0,len(gq)): dists2[j] = SphDist(sRA[gq[j]],sDec[gq[j]],cenRA[i],cenDec[i])
    gd2 = np.where(dists2 < srchdist[i])
    velstemp2 =  (z[gq]-biweight_loc(sz[g[gcen[gcentemp]]]))*(3.0*10**5)/(1+sz[gq])
    if names[i] != "RXJ1821": 
        gcen2 = np.where((velstemp2 < 3000) & (velstemp2 > -3000) & (dists2 < srchdist[i]))
        gcen2 = gcen2[0]
        gcentemp = np.arange(len(gcen2))
        meancen = biweight_loc(velstemp2[gcen2])
        velstemp2 = velstemp2[gcen2]
        sig = CalcVelDisp(velstemp2,method=method,ConfInvMethod='none',CalcVels=0)
        prevcen=9999
        while len(gcentemp) < prevcen:
            prevcen = len(gcentemp)
            gcentemp = sigclip(velstemp2,meancen,sig)
            velstemp2 = (z[gq[gcen2]]-biweight_loc(sz[gq[gcen2[gcentemp]]]))*(3.0*10**5)/(1+sz[gq[gcen2]])
            meancen = biweight_loc(velstemp2[gcentemp])
            sig = CalcVelDisp(velstemp2[gcentemp],method=method,ConfInvMethod='none',CalcVels=0)
            sig2,sige = CalcVelDisp(velstemp2[gcentemp],method=method,ConfInvMethod='jackknife',CalcVels=0)
            sig2,sigeBSL,sigeBSH = CalcVelDisp(velstemp2[gcentemp],method=method,ConfInvMethod='bootstrap',CalcVels=0)
    return sig,sige,sigeBSL,sigeBSH,vels,velstemp,gcentemp

degree_symbol = unichr(176)
html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FFCC00'
html_pink = '#FF00FF'

zlb = [0.82,0.65,0.68,0.805,0.84,0.84,1.0]
zub = [0.87,0.79,0.71,0.83,0.96,0.96,1.2]

try:
    skipMC
except NameError:
    skipMC = 1
try:
    writeMC
except NameError:
    writeMC = 1

try:
    secsize
except NameError:
    secsize = 1.1

strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

crcc = read_file('/home/rumbaugh/cc_out.6.1.12.nh.dat')
amin1mpc = copy_colvals(crcc,'col12')*0.7

#files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
#files = ['FINAL.SG0023.deimos.lris.feb2012.nodups.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.feb2012.nh.cat','FINAL.nep5281.deimos.gioia.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectroscopic.autocompile.blemaux.sc0910.mar2012.T08needstoberedone.nodups.cat']
files = ['FINAL.SG0023.deimos.lris.feb2012.nodups.cat','FINAL.cl1322.lrisplusdeimos.cat','newcats/FINAL.spectroscopic.autocompile.N200.blemaux.feb2012.nh.cat','newcats/FINAL.nep5281.deimos.gioia.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','newcats/FINAL.spectroscopic.autocompile.blemaux.sc0910.mar2012.plusT08.nodups.cat']
RGalPeakRA = np.array([201.20353640,201.09003360,201.20748930,(17+(57+18.769/60)/60)*360/24.0,275.383771,241.08946,241.09890,(360.0/24)*(9+(10+(4.168/60))/60.0),(360.0/24)*(9+(10+(47.686/60))/60.0)])
RGalPeakDec = np.array([30.19424680,30.21497820,30.97371310,66+(31+37.46/60)/60.0,68.471189,43.07613,43.23550,(54+(18+(54.21/60))/60.0),(54+(22+(13.82/60))/60.0)])

boundsDecHi = RGalPeakDec+1.1*amin1mpc/60
boundsDecLo = RGalPeakDec-1.1*amin1mpc/60
boundsRALo,boundsRAHi = np.zeros(len(RGalPeakRA)),np.zeros(len(RGalPeakRA)) 
for i in range(0,len(RGalPeakRA)):
    boundsRAHi[i] = RGalPeakRA[i]+1.1*amin1mpc[i]/60/m.cos(m.pi*RGalPeakDec[i]/180)
    boundsRALo[i] = RGalPeakRA[i]-1.1*amin1mpc[i]/60/m.cos(m.pi*RGalPeakDec[i]/180)

names2 = np.array(['RXJ1757','RXJ1821','Cl0910+5422'])
#names = np.array(['nep200','nep5281','cl0910'])

cRAh = np.array([13,13,13,17,18,16,16,9,9])
cRAm = np.array([24,24,24,57,21,4,4,10,10])
cRAs = np.array([48.9,20.3,49.2,19.3,32.3,23.5,26.5,8.5,45.0])
cDd = np.array([30,30,30,66,68,43,43,54,54])
cDm = np.array([11,12,58,31,27,4,14,18,22])
cDs = np.array([26,52,35,29,57,39,22,56,7])
centerRAs = (cRAh + (cRAm + (cRAs/60.0))/60.0)*360.0/24
centerDecs = cDd + (cDm + (cDs/60.0))/60.0
centerzs = np.array([0.76,0.76,0.69,0.69,0.82,0.89861,0.86531,1.1,1.1])

BCGfile = '/home/rumbaugh/BCGpositions.2.15.12.dat'
crBCG = read_file(BCGfile)
BCGRA = copy_colvals(crBCG,'col2')
BCGDec = copy_colvals(crBCG,'col3')
BCGzs = copy_colvals(crBCG,'col7')
srchdist = np.array([3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92])*0.7
ccnt = 0

rsb = np.array([1.777,1.325,1.84,1.203,1.305,3.182,1.7563])
rsm = np.array([0.0229,0.0084,0.0319,0.0012,0.00485,0.063,0.02392])
rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0813,0.0907,0.0455])
rsNSTD = np.array([3.0,2.0,3.0,3.0,2.0,2.0,3.0])
ymaxes = np.array([20,20,20,20,20,20,20,20,20]) 
#ccnt = np.array([2,3,6])
ccnt=0
#FILEo = open('/home/rumbaugh/DStest_output.4.10.12.dat','w')
#FILE3 = open('/home/rumbaugh/veldisp_output.4.10.12.dat','w')
FILE=open('/home/rumbaugh/veldisps.7.19.12.dat','w')
FILE.write("# Structure  Numgals_MAD_xray Numgals_MAD_BCG Numgals_MAD_RGP  Numgals_FP_xray Numgals_FP_BCG Numgals_FP_RGP  Numgals_BW_xray Numgals_BW_BCG Numgals_BW_RGP  Numgals_gap_xray Numgals_gap_BCG Numgals_gap_RGP MAD_xray MAD_BCG MAG_RGP FP_xray FP_BCG FP_RGP BW_xray BW_BCG BW_RGP gap_xray gap_BCG gap_RGP MAD_xray_errBSlo MAD_BCG_errBSlo MAG_RGP_errBSlo FP_xray_errBSlo FP_BCG_errBSlo FP_RGP_errBSlo BW_xray_errBSlo BW_BCG_errBSlo BW_RGP_errBSlo gap_xray_errBSlo gap_BCG_errBSlo gap_RGP_errBSlo MAD_xray_errBShi MAD_BCG_errBShi MAG_RGP_errBShi FP_xray_errBShi FP_BCG_errBShi FP_RGP_errBShi BW_xray_errBShi BW_BCG_errBShi BW_RGP_errBShi gap_xray_errBShi gap_BCG_errBShi gap_RGP_errBShi MAD_xray_errJK MAD_BCG_errJK MAG_RGP_errJK FP_xray_errJK FP_BCG_errJK FP_RGP_errJK BW_xray_errJK BW_BCG_errJK BW_RGP_errJK gap_xray_errJK gap_BCG_errJK gap_RGP_errJK \n")
for i in range(0,len(names)):
    #cr = read_file('/home/rumbaugh/%s.info.1Mpc.withvels'%(names[i]))
    #royID = copy_colvals(cr,'col1')
    #RA = copy_colvals(cr,'col2')
    #Dec = copy_colvals(cr,'col3')
    #z = copy_colvals(cr,'col4')
    #vels = copy_colvals(cr,'col5')
    if ((i != 1) & (i != 2) & (i != 6) & (i != 8)): ccnt += 1
    if i == 5: ccnt += 1
    sfile = '/home/rumbaugh/%s'%(files[ccnt])
    crs = read_file(sfile)
    sID = copy_colvals(crs,'col1')
    sslit = copy_colvals(crs,'col3')
    smask = copy_colvals(crs,'col2')
    sRA = copy_colvals(crs,'col4')
    sDec = copy_colvals(crs,'col5')
    sLFCrB = copy_colvals(crs,'col6')
    sLFCiB = copy_colvals(crs,'col7')
    RA,Dec = np.copy(sRA),np.copy(sDec)
    if ((i == 5) | (i == 6)):
        ACSRA = copy_colvals(crs,'col14')
        ACSDec = copy_colvals(crs,'col15')
        sf606 = copy_colvals(crs,'col17')
        sf814 = copy_colvals(crs,'col18')
        srB,siB = np.copy(sf606),np.copy(sf814)
    else:
        srB,siB = np.copy(sLFCrB),np.copy(sLFCiB)
    szB = copy_colvals(crs,'col8')
    z = copy_colvals(crs,'col9')
    sz = np.copy(z)
    #vels = sz*3*10**5
    sq = copy_colvals(crs,'col11')
    q = np.copy(sq)
    g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]))
    if names[i] == "RXJ1757": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((smask != 'N200M1') | (sslit != 64)) & ((smask != 'N200M1') | (sslit != 67)) & ((smask != 'N200M1') | (sslit != 80)) & ((smask != 'N200M1') | (sslit != 83)))
    if names[i] == "RXJ1821": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((z < 0.80721891) | (z > 0.80721901)))
    if names[i] == "Cl1604A": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((sID != "LFC_SC2_06516") | (z > 0.9)))
    if names[i] == "Cl1604B": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((sID != "LFC_SC1_01472") | (z < 0.87)))
    g = g[0]
    dists = np.zeros(len(g))
    for j in range(0,len(g)): dists[j] = SphDist(sRA[g[j]],sDec[g[j]],centerRAs[i],centerDecs[i])
    gx = np.where(dists < srchdist[i])
    gx = gx[0]
    dists = np.zeros(len(g))
    for j in range(0,len(g)): dists[j] = SphDist(sRA[g[j]],sDec[g[j]],BCGRA[i],BCGDec[i])
    gBCG = np.where(dists < srchdist[i])
    gBCG = gBCG[0]
    dists = np.zeros(len(g))
    for j in range(0,len(g)): dists[j] = SphDist(sRA[g[j]],sDec[g[j]],RGalPeakRA[i],RGalPeakDec[i])
    gRGP = np.where(dists < srchdist[i])
    gRGP = gRGP[0]
    sigRGPb,sigeRGPb,sigeBSL_RGPb,sigeBSH_RGPb,velsRGPb,velstempRGPb,gRGPtempb = CalcInitVelDisp(z,g,gRGP,'biweight_scale',RGalPeakRA,RGalPeakDec)
    sigRGPg,sigeRGPg,sigeBSL_RGPg,sigeBSH_RGPg,velsRGPg,velstempRGPg,gRGPtempg = CalcInitVelDisp(z,g,gRGP,'gapper',RGalPeakRA,RGalPeakDec)
    sigRGPm,sigeRGPm,sigeBSL_RGPm,sigeBSH_RGPm,velsRGPm,velstempRGPm,gRGPtempm = CalcInitVelDisp(z,g,gRGP,'MAD',RGalPeakRA,RGalPeakDec)
    sigRGPf,sigeRGPf,sigeBSL_RGPf,sigeBSH_RGPf,velsRGPf,velstempRGPf,gRGPtempf = CalcInitVelDisp(z,g,gRGP,'fpseudosigma',RGalPeakRA,RGalPeakDec)
    sigBCGb,sigeBCGb,sigeBSL_BCGb,sigeBSH_BCGb,velsBCGb,velstempBCGb,gBCGtempb = CalcInitVelDisp(z,g,gBCG,'biweight_scale',BCGRA,BCGDec)
    sigBCGg,sigeBCGg,sigeBSL_BCGg,sigeBSH_BCGg,velsBCGg,velstempBCGg,gBCGtempg = CalcInitVelDisp(z,g,gBCG,'gapper',BCGRA,BCGDec)
    sigBCGm,sigeBCGm,sigeBSL_BCGm,sigeBSH_BCGm,velsBCGm,velstempBCGm,gBCGtempm = CalcInitVelDisp(z,g,gBCG,'MAD',BCGRA,BCGDec)
    sigBCGf,sigeBCGf,sigeBSL_BCGf,sigeBSH_BCGf,velsBCGf,velstempBCGf,gBCGtempf = CalcInitVelDisp(z,g,gBCG,'fpseudosigma',BCGRA,BCGDec)
    sigxb,sigexb,sigeBSL_xb,sigeBSH_xb,velsxb,velstempxb,gxtempb = CalcInitVelDisp(z,g,gx,'biweight_scale',centerRAs,centerDecs)
    sigxg,sigexg,sigeBSL_xg,sigeBSH_xg,velsxg,velstempxg,gxtempg = CalcInitVelDisp(z,g,gx,'gapper',centerRAs,centerDecs)
    sigxm,sigexm,sigeBSL_xm,sigeBSH_xm,velsxm,velstempxm,gxtempm = CalcInitVelDisp(z,g,gx,'MAD',centerRAs,centerDecs)
    sigxf,sigexf,sigeBSL_xf,sigeBSH_xf,velsxf,velstempxf,gxtempf = CalcInitVelDisp(z,g,gx,'fpseudosigma',centerRAs,centerDecs)
    FILE.write('%13s %3i %3i %3i %3i %3i %3i %3i %3i %3i %3i %3i %3i %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f\n'%(names[i],len(gxtempm),len(gBCGtempm),len(gRGPtempm),len(gxtempf),len(gBCGtempf),len(gRGPtempf),len(gxtempb),len(gBCGtempb),len(gRGPtempb),len(gxtempg),len(gBCGtempg),len(gRGPtempg),sigxm,sigBCGm,sigRGPm,sigxf,sigBCGf,sigRGPf,sigxb,sigBCGb,sigRGPb,sigxg,sigBCGg,sigRGPg,sigexm,sigeBCGm,sigeRGPm,sigexf,sigeBCGf,sigeRGPf,sigexb,sigeBCGb,sigeRGPb,sigexg,sigeBCGg,sigeRGPg,sigeBSL_xm,sigeBSL_BCGm,sigeBSL_RGPm,sigeBSL_xf,sigeBSL_BCGf,sigeBSL_RGPf,sigeBSL_xb,sigeBSL_BCGb,sigeBSL_RGPb,sigeBSL_xg,sigeBSL_BCGg,sigeBSL_RGPg,sigeBSH_xm,sigeBSH_BCGm,sigeBSH_RGPm,sigeBSH_xf,sigeBSH_BCGf,sigeBSH_RGPf,sigeBSH_xb,sigeBSH_BCGb,sigeBSH_RGPb,sigeBSH_xg,sigeBSH_BCGg,sigeBSH_RGPg))
FILE.close()



    
