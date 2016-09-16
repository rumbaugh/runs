import numpy as np
import math as m
import time
import sys
import matplotlib
import matplotlib.pylab as pylab
execfile("FindCloseSources.py")

try:
    aperture
except NameError:
    aperture = 1.0

rsb = np.array([1.777,1.325,1.84,1.203,1.305,3.182,1.7563])
rsm = np.array([0.0229,0.0084,0.0319,0.0012,0.00485,0.063,0.02392])
rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0813,0.0907,0.0455])
rsNSTD = np.array([3.0,2.0,3.0,3.0,2.0,2.0,3.0])
#files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])
pfiles=np.array(['cl0023_radecIDmags.cat','sc1322.lfc.newIDsandoldIds.radecmag.cat','nep200.idradecmag.lfc.uhcorr.neat','nep5281.lfc.newIDradecmag.cat','final.idradecmag.lfcpluscosmic.withsdss.cat','ACS_merged.F606W+F814W_deep.all.coll.nh.dat','../cl0910.LFC.IDradecnmags.cat'])
imcensY = np.array([768.422,720.375,2236.0,1380.492,815.5,798.656,1986.469,1117.562,1501.609])
imcensX = np.array([1349.594,2021.5,1525.25,774.523,873.5,1283.375,1219.219,1523.375,871.5])

cRAh = np.array([13,13,13,17,18,16,16,9,9])
cRAm = np.array([24,24,24,57,21,4,4,10,10])
cRAs = np.array([48.9,20.3,49.2,19.3,32.3,23.5,26.5,8.5,45.0])
cDd = np.array([30,30,30,66,68,43,43,54,54])
cDm = np.array([11,12,58,31,27,4,14,18,22])
cDs = np.array([26,52,35,29,57,39,22,56,7])
#centerRAs = np.array([((16+(4.0+23.5/60)/60)*360.0/24,(16+(4.0+26.5/60)/60)*360.0/24])
#centerDecs = np.array([43+(4.0+39.0/60)/60,43+(14.0+22.0/60)/60])
centerRAs = (cRAh + (cRAm + (cRAs/60.0))/60.0)*360.0/24
centerDecs = cDd + (cDm + (cDs/60.0))/60.0
centerzs = np.array([0.76,0.76,0.69,0.69,0.82,0.89861,0.86531,1.1,1.1])
#1 Mpc = 3.06*0.7 Arcmin
srchdist = np.array([3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92])*0.7*aperture*60

ccnt = 0
for i in range(0,len(names)):
    if ((i != 1) & (i != 2) & (i != 6) & (i != 8)): ccnt += 1
    if i == 5: ccnt += 1
    sfile = '/home/rumbaugh/%s'%(files[ccnt])
    pfile = '/home/rumbaugh/LFC/%s'%(pfiles[ccnt])
    cr = read_file(pfile)
    crs = read_file(sfile)
    
    sRA = copy_colvals(crs,'col4')
    sDec = copy_colvals(crs,'col5')
    if ((i == 5) | (i == 6)):
        ACSRA = copy_colvals(crs,'col14')
        ACSDec = copy_colvals(crs,'col15')
        sf606 = copy_colvals(crs,'col17')
        sf814 = copy_colvals(crs,'col18')
    sLFCrB = copy_colvals(crs,'col6')
    sLFCiB = copy_colvals(crs,'col7')
    szB = copy_colvals(crs,'col8')
    sz = copy_colvals(crs,'col9')
    sq = copy_colvals(crs,'col11')

    siB = sLFCiB
    srB = sLFCrB
    if ((i == 5) | (i == 6)):
        siB = sf814
        srB = sf606
        sRA = sACSRA
        sDec = sACSDec
    if i < 6.7:
        gs = np.where((sq > 2.2) & (siB > 0.1) & (srB > 0.1) & (siB < 90) & (srB < 90))
    else:
        gs = np.where((sq > 2.2) & (siB > 0.1) & (szB > 0.1) & (siB < 90) & (szB < 90))
    gs = gs[0]
    galls = FindCloseSources(centerRAs[i],centerDecs[i],srchdist[i],sRA[gs],sDec[gs],0)
    gzs = np.where((sz[gs[galls]] > centerzs[i]-0.01) & (sz[gs[galls]] < centerzs[i]+0.01))
    if i == 1: gzs = np.where((sz[gs[galls]] > 0.65) & (sz[gs[galls]] < 0.76))
    gzs = gzs[0]
    if i < 6.7:
        grss = np.where((srB[gs[galls[gzs]]]-siB[gs[galls[gzs]]] > rsb[ccnt]-rsm[ccnt]*siB[gs[galls[gzs]]]-rsNSTD[ccnt]*rsSTD[ccnt]) & (srB[gs[galls[gzs]]]-siB[gs[galls[gzs]]] < rsb[ccnt]-rsm[ccnt]*siB[gs[galls[gzs]]]+rsNSTD[ccnt]*rsSTD[ccnt]))
    else:
        grss = np.where((siB[gs[galls[gzs]]]-szB[gs[galls[gzs]]] > rsb[ccnt]-rsm[ccnt]*szB[gs[galls[gzs]]]-rsNSTD[ccnt]*rsSTD[ccnt]) & (siB[gs[galls[gzs]]]-szB[gs[galls[gzs]]] < rsb[ccnt]-rsm[ccnt]*szB[gs[galls[gzs]]]+rsNSTD[ccnt]*rsSTD[ccnt]))
    grss = grss[0]

    if ((i < 2.3)):
        RA = copy_colvals(cr,'col3')
        Dec = copy_colvals(cr,'col4')
        LFCrB = copy_colvals(cr,'col5')
        LFCiB = copy_colvals(cr,'col6')
        zB = copy_colvals(cr,'col7')
    elif ((i == 5) | (i == 6)):
        ACSRA = copy_colvals(cr,'col1')
        ACSDec = copy_colvals(cr,'col2')
        f814 = copy_colvals(cr,'col4')
        f606 = copy_colvals(cr,'col3')
    else:
        RA = copy_colvals(cr,'col2')
        Dec = copy_colvals(cr,'col3')
        LFCrB = copy_colvals(cr,'col4')
        LFCiB = copy_colvals(cr,'col5')
        zB = copy_colvals(cr,'col6')

    iB = LFCiB
    rB = LFCrB
    if ((i == 5) | (i == 6)):
        iB = f814
        rB = f606
        RA = ACSRA
        Dec = ACSDec
    if i < 6.7:
        g = np.where((iB > 0.1) & (rB > 0.1) & (iB < 90) & (rB < 90))
    else:
        g = np.where((iB > 0.1) & (zB > 0.1) & (iB < 90) & (zB < 90))
    g = g[0]
    gall = FindCloseSources(centerRAs[i],centerDecs[i],srchdist[i],RA[g],Dec[g],0)
    if i < 6.7:
        grs = np.where((rB[g[gall]]-iB[g[gall]] > rsb[ccnt]-rsm[ccnt]*iB[g[gall]]-rsNSTD[ccnt]*rsSTD[ccnt]) & (rB[g[gall]]-iB[g[gall]] < rsb[ccnt]-rsm[ccnt]*iB[g[gall]]+rsNSTD[ccnt]*rsSTD[ccnt]))
    else:
        grs = np.where((iB[g[gall]]-zB[g[gall]] > rsb[ccnt]-rsm[ccnt]*zB[g[gall]]-rsNSTD[ccnt]*rsSTD[ccnt]) & (iB[g[gall]]-zB[g[gall]] < rsb[ccnt]-rsm[ccnt]*zB[g[gall]]+rsNSTD[ccnt]*rsSTD[ccnt]))
    grs = grs[0]
    garg = np.argsort(iB[g[gall[grs]]])
    validBCGIDs = np.zeros(4)
    validBCGs = 0
    si = -1
    while validBCGs < 3.4:
        si += 1
        gsi = FindCloseSources(RA[g[gall[grs[garg[si]]]]],Dec[g[gall[grs[garg[si]]]]],0.1,sRA[gs[galls[gzs[grss]]]],sDec[gs[galls[gzs[grss]]]],0)
        if len(grss) > 0:
            validBCGIDs[validBCGs] = si
            validBCGs += 1
    print "%s - BCG Position\n(RA,Dec) = (%f,%f)\ni'/f814 magnitude: %f\n"%(names[i],RA[g[gall[grs[garg[validBCGIDs[0]]]]]],Dec[g[gall[grs[garg[validBCGIDs[0]]]]]],iB[g[gall[grs[garg[0]]]]])
    print "%s - 2nd Position\n(RA,Dec) = (%f,%f)\ni'/f814 magnitude: %f\n"%(names[i],RA[g[gall[grs[garg[validBCGIDs[1]]]]]],Dec[g[gall[grs[garg[validBCGIDs[1]]]]]],iB[g[gall[grs[garg[1]]]]])
    print "%s - 3rd Position\n(RA,Dec) = (%f,%f)\ni'/f814 magnitude: %f\n"%(names[i],RA[g[gall[grs[garg[validBCGIDs[2]]]]]],Dec[g[gall[grs[garg[validBCGIDs[2]]]]]],iB[g[gall[grs[garg[2]]]]])
    print "%s - 4th Position\n(RA,Dec) = (%f,%f)\ni'/f814 magnitude: %f\n"%(names[i],RA[g[gall[grs[garg[validBCGIDs[3]]]]]],Dec[g[gall[grs[garg[validBCGIDs[3]]]]]],iB[g[gall[grs[garg[3]]]]])
    
    
