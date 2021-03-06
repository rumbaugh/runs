execfile("/home/rumbaugh/FindCloseSources.py")
from CalcVelDisp import *

zlb = [0.82,0.65,0.68,0.805,0.84,0.84,1.0]
zub = [0.87,0.79,0.71,0.83,0.96,0.96,1.2]

names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

files = ['FINAL.SG0023.deimos.lris.feb2012.nodups.cat','FINAL.cl1322.lrisplusdeimos.cat','newcats/FINAL.spectroscopic.autocompile.N200.blemaux.feb2012.nh.cat','newcats/FINAL.nep5281.deimos.gioia.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','newcats/FINAL.spectroscopic.autocompile.blemaux.sc0910.mar2012.plusT08.nodups.cat']

RGalPeakRA = np.array([201.20353640,201.09003360,201.20748930,(17+(57+18.769/60)/60)*360/24.0,275.38377060,241.089458,241.0988952,(360.0/24)*(9+(10+(4.168/60))/60.0),(360.0/24)*(9+(10+(47.686/60))/60.0)])
RGalPeakDec = np.array([30.19424680,30.21497820,30.97371310,66+(31+37.46/60)/60.0,68.47118870,43.076133,43.2355028,(54+(18+(54.21/60))/60.0),(54+(22+(13.82/60))/60.0)])

srchdist = np.array([3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92])*0.7
ccnt = 0

for i in range(0,len(names)):
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
    for j in range(0,len(g)): dists[j] = SphDist(sRA[g[j]],sDec[g[j]],RGalPeakRA[i],RGalPeakDec[i])
    gRGP = np.where(dists < srchdist[i])
    gRGP = gRGP[0]
    print '\n\n%s'%(names[i])
    DisplayVelDisp(sz[g[gRGP]])
