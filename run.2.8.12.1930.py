import numpy as np
import math as m
import time
import sys
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/angconvert.py")

html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FF9900'
html_pink = '#FF00FF'

try:
    aperture
except NameError:
    aperture = 0.5

rsb = np.array([1.777,1.325,1.84,1.203,1.305,3.182,1.7563])
rsm = np.array([0.0229,0.0084,0.0319,0.0012,0.00485,0.063,0.02392])
rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0813,0.0907,0.0455])
rsNSTD = np.array([3.0,2.0,3.0,3.0,2.0,2.0,3.0])
#files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

RGalPeakRA = np.array([201.20353640,201.09003360,201.20748930,0.0001,275.3801,241.08946,241.09890,(360.0/24)*(9+(10+(4.168/60))/60.0),(360.0/24)*(9+(10+(47.686/60))/60.0)])
RGalPeakDec = np.array([30.19424680,30.21497820,30.97371310,0.0001,68.4651,43.07613,43.23550,(54+(18+(54.21/60))/60.0),(54+(22+(13.82/60))/60.0)])

pfiles=np.array(['cl0023_radecIDmags.cat','sc1322.lfc.newIDsandoldIds.radecmag.cat','nep200.idradecmag.lfc.uhcorr.neat','nep5281.lfc.newIDradecmag.cat','final.idradecmag.lfcpluscosmic.withsdss.cat','ACS_merged.F606W+F814W_deep.all.coll.nh.dat','../cl0910.LFC.IDradecnmags.cat'])
imcensY = np.array([768.422,720.375,2236.0,1380.492,815.5,798.656,1986.469,1117.562,1501.609])
imcensX = np.array([1349.594,2021.5,1525.25,774.523,873.5,1283.375,1219.219,1523.375,871.5])
zlb = [0.82,0.65,0.68,0.80,0.84,0.84,1.0]
zub = [0.87,0.79,0.71,0.84,0.96,0.96,1.2]

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
        sRA = ACSRA
        sDec = ACSDec
    if i < 6.7:
        gs = np.where(((sq > 2.2) | (sq < -0.1)) & (siB > 0.1) & (srB > 0.1) & (siB < 90) & (srB < 90))
    else:
        gs = np.where(((sq > 2.2) | (sq < -0.1)) & (siB > 0.1) & (szB > 0.1) & (siB < 90) & (szB < 90))
    gs = gs[0]
    galls = FindCloseSources(centerRAs[i],centerDecs[i],srchdist[i],sRA[gs],sDec[gs],0)
    #gzs = np.where((sz[gs[galls]] > zlb[ccnt]) & (sz[gs[galls]] < zub[ccnt]))
    #gzs = gzs[0]
    if i < 6.7:
        grss = np.where((srB[gs[galls]]-siB[gs[galls]] > rsb[ccnt]-rsm[ccnt]*siB[gs[galls]]-rsNSTD[ccnt]*rsSTD[ccnt]) & (srB[gs[galls]]-siB[gs[galls]] < rsb[ccnt]-rsm[ccnt]*siB[gs[galls]]+rsNSTD[ccnt]*rsSTD[ccnt]))
        garss = np.where((srB[gs[galls]]-siB[gs[galls]] > rsb[ccnt]-rsm[ccnt]*siB[gs[galls]]+rsNSTD[ccnt]*rsSTD[ccnt]))
        gblus = np.where((srB[gs[galls]]-siB[gs[galls]] < rsb[ccnt]-rsm[ccnt]*siB[gs[galls]]-rsNSTD[ccnt]*rsSTD[ccnt]))
    else:
        grss = np.where((siB[gs[galls]]-szB[gs[galls]] > rsb[ccnt]-rsm[ccnt]*szB[gs[galls]]-rsNSTD[ccnt]*rsSTD[ccnt]) & (siB[gs[galls]]-szB[gs[galls]] < rsb[ccnt]-rsm[ccnt]*szB[gs[galls]]+rsNSTD[ccnt]*rsSTD[ccnt]))
        garss = np.where((siB[gs[galls]]-szB[gs[galls]] > rsb[ccnt]-rsm[ccnt]*szB[gs[galls]]+rsNSTD[ccnt]*rsSTD[ccnt]))
        gblus = np.where((siB[gs[galls]]-szB[gs[galls]] < rsb[ccnt]-rsm[ccnt]*szB[gs[galls]]-rsNSTD[ccnt]*rsSTD[ccnt]))
    garss = garss[0]
    gblus = gblus[0]
    grss = grss[0]
    print 'd'

    if ((i < 2.3)):
        RA = copy_colvals(cr,'col3')
        Dec = copy_colvals(cr,'col4')
        LFCrB = copy_colvals(cr,'col5')
        LFCiB = copy_colvals(cr,'col6')
        zB = copy_colvals(cr,'col7')
    elif ((i == 5) | (i == 6)):
        pfile2 = '/home/rumbaugh/LFC/%s'%(pfiles[ccnt-1])
        crl = read_file(pfile2)
        ACSRA = copy_colvals(cr,'col1')
        ACSDec = copy_colvals(cr,'col2')
        f814 = copy_colvals(cr,'col4')
        f606 = copy_colvals(cr,'col3')
        LFCRA = copy_colvals(crl,'col2')
        LFCDec = copy_colvals(crl,'col3')
        LFCrB = copy_colvals(crl,'col4')
        LFCiB = copy_colvals(crl,'col5')
        zB = copy_colvals(crl,'col6')
    else:
        RA = copy_colvals(cr,'col2')
        Dec = copy_colvals(cr,'col3')
        LFCrB = copy_colvals(cr,'col4')
        LFCiB = copy_colvals(cr,'col5')
        zB = copy_colvals(cr,'col6')

    print 'e'
    iB = LFCiB
    rB = LFCrB
    if ((i == 5) | (i == 6)):
        iB = f814
        rB = f606
        RA = ACSRA
        Dec = ACSDec
    CMDx = iB
    CMDx2 = zB
    CMDy = rB-iB
    if ((i != 5) & (i != 6)): 
        CMDy2 = iB-zB
    else: 
        CMDy2 = LFCiB-zB
    if ((i == 5) | (i == 6)):
        CMDi = LFCiB
        CMDr = LFCrB
    if i < 6.7:
        g = np.where((iB > 0.1) & (rB > 0.1) & (iB < 90) & (rB < 90))
        gbad = np.where((iB < 0.1) | (rB < 0.1) | (iB > 90) | (rB > 90))
    else:
        g = np.where((iB > 0.1) & (zB > 0.1) & (iB < 90) & (zB < 90))
        gbad = np.where((iB < 0.1) | (zB < 0.1) | (iB > 90) | (zB > 90))
    g = g[0]
    gbad = gbad[0]
    print 'f'
    gall = FindCloseSources(centerRAs[i],centerDecs[i],srchdist[i],RA[g],Dec[g],0)
    if i < 6.7:
        grs = np.where((rB[g[gall]]-iB[g[gall]] > rsb[ccnt]-rsm[ccnt]*iB[g[gall]]-rsNSTD[ccnt]*rsSTD[ccnt]) & (rB[g[gall]]-iB[g[gall]] < rsb[ccnt]-rsm[ccnt]*iB[g[gall]]+rsNSTD[ccnt]*rsSTD[ccnt]))
        gars = np.where((rB[g[gall]]-iB[g[gall]] > rsb[ccnt]-rsm[ccnt]*iB[g[gall]]+rsNSTD[ccnt]*rsSTD[ccnt]))
        gblu = np.where((rB[g[gall]]-iB[g[gall]] < rsb[ccnt]-rsm[ccnt]*iB[g[gall]]-rsNSTD[ccnt]*rsSTD[ccnt]))
    else:
        grs = np.where((iB[g[gall]]-zB[g[gall]] > rsb[ccnt]-rsm[ccnt]*zB[g[gall]]-rsNSTD[ccnt]*rsSTD[ccnt]) & (iB[g[gall]]-zB[g[gall]] < rsb[ccnt]-rsm[ccnt]*zB[g[gall]]+rsNSTD[ccnt]*rsSTD[ccnt]))
        gars = np.where((iB[g[gall]]-zB[g[gall]] > rsb[ccnt]-rsm[ccnt]*zB[g[gall]]+rsNSTD[ccnt]*rsSTD[ccnt]))
        gblu = np.where((iB[g[gall]]-zB[g[gall]] < rsb[ccnt]-rsm[ccnt]*zB[g[gall]]-rsNSTD[ccnt]*rsSTD[ccnt]))
    print 'g'
    grs = grs[0]
    gars = gars[0]
    gblu = gblu[0]
    garg = np.argsort(iB[g[gall[grs]]])
    validBCGIDs = np.zeros(4)
    validBCGs = 0
    si = -1
    while validBCGs < 3.4:
        isgood = 0
        si += 1
        gsi = FindCloseSources(RA[g[gall[grs[garg[si]]]]],Dec[g[gall[grs[garg[si]]]]],0.01,sRA[gs[galls[grss]]],sDec[gs[galls[grss]]],0)
        if len(gsi) > 0: 
            if ((sz[gs[galls[grss[gsi[0]]]]] > centerzs[i]-0.01) & (sz[gs[galls[grss[gsi[0]]]]] < centerzs[i]+0.01)): isgood = 1
        if ((len(gsi) == 0) | (isgood == 1)):
            validBCGIDs[validBCGs] = si
            validBCGs += 1
            #if isgood == 1: 
            #    print sq[gs[galls[gzs[grss[gsi[0]]]]]],sz[gs[galls[gzs[grss[gsi[0]]]]]]
        #else: 
            #    print 'None'
    print 'h'
    print validBCGIDs
    rastrs = np.array(['12345678901234567890',' ',' ',' '])
    decstrs = np.array(['12345678901234567890',' ',' ',' '])
    for ir in range(0,4):
        rah,ram,ras = dec2hms(RA[g[gall[grs[garg[validBCGIDs[ir]]]]]])
        decd,decm,decs = dec2dms(Dec[g[gall[grs[garg[validBCGIDs[ir]]]]]])
        ramextra0,rasextra0,decmextra0,decsextra0 = '','','',''
        if ram < 10: ramextra0 = '0'
        if ras < 10: rasextra0 = '0'
        if decm < 10: decmextra0 = '0'
        if decs < 10: decsextra0 = '0'
        rastrs[ir] = '%3i:%s%i:%s%f'%(rah,ramextra0,ram,rasextra0,ras)
        decstrs[ir] = '%2i:%s%i:%s%f'%(decd,decmextra0,decm,decsextra0,decs)
            
    print 'i'

    pylab.xlim(18,23)
    pylab.ylim(0,2)
    pylab.xlabel("i'")
    pylab.ylabel("r'-i'")
    if ((i == 5) | (i == 6)): 
        pylab.ylim(0,3)
        pylab.xlabel("F814W")
        pylab.ylabel("F606W-F814W")
    if i > 6.6:
        pylab.xlabel("z'")
        pylab.ylabel("i'-z'")
    pylab.plot(np.arange(50),rsb[ccnt]-np.arange(50)*rsm[ccnt]-rsNSTD[ccnt]*rsSTD[ccnt],color='red')
    pylab.plot(np.arange(50),rsb[ccnt]-np.arange(50)*rsm[ccnt]+rsNSTD[ccnt]*rsSTD[ccnt],color='red')
    pylab.scatter(CMDx[g[gall]],CMDy[g[gall]],s=8,color='black')
    print 'j'

#    print "%s - BCG Position\n(RA,Dec) = (%s,%s)\ni'/f814 magnitude: %f\n"%(names[i],rastrs[0],decstrs[0],iB[g[gall[grs[garg[validBCGIDs[0]]]]]])
#    print "%s - 2nd Position\n(RA,Dec) = (%s,%s)\ni'/f814 magnitude: %f\n"%(names[i],rastrs[1],decstrs[1],iB[g[gall[grs[garg[validBCGIDs[1]]]]]])
#    print "%s - 3rd Position\n(RA,Dec) = (%s,%s)\ni'/f814 magnitude: %f\n"%(names[i],rastrs[2],decstrs[2],iB[g[gall[grs[garg[validBCGIDs[2]]]]]])
#    print "%s - 4th Position\n(RA,Dec) = (%s,%s)\ni'/f814 magnitude: %f\n"%(names[i],rastrs[3],decstrs[3],iB[g[gall[grs[garg[validBCGIDs[3]]]]]])
    FILE = open('/home/rumbaugh/BCG.anal.%s.gal_list_%4.2fMpc.2.8.12.dat'%(names[i],aperture),'w')
    FILE2 = open('/home/rumbaugh/BCG.anal.%s.gals_%4.2fMpc.2.8.12.reg'%(names[i],aperture),'w')
    FILE2.write('global color=green font="helvetica 10 normal" select=1 highlite=1 edit=1 move=1 delete=1 include=1 fixed=0 width=2 source\nfk5\n')
    FILE2.write('point(%f,%f) # point=diamond color=orange\n'%(RGalPeakRA[i],RGalPeakDec[i]))
    print 'k'
    for iw in range(0,len(gbad)):
        FILE2.write('point(%f,%f) # point=x color=%s\n'%(RA[gbad[iw]],Dec[gbad[iw]],'black'))
    print 'a'
    for iw in range(0,len(gblu)):
        qtemp = 0
        isgood = 0
        regcol = 'blue'
        giw = FindCloseSources(RA[g[gall[gblu[iw]]]],Dec[g[gall[gblu[iw]]]],0.01,sRA[gs[galls[gblus]]],sDec[gs[galls[gblus]]],0)
        if len(giw) > 0: 
            if ((sz[gs[galls[gblus[giw[0]]]]] > centerzs[i]-0.01) & (sz[gs[galls[gblus[giw[0]]]]] < centerzs[i]+0.01)):
                isgood = 1
                regcol = 'blue'
                pylab.scatter(CMDx[g[gall[gblu[iw]]]],CMDy[g[gall[gblu[iw]]]],s=12,color='red')
            elif ((sz[gs[galls[gblus[giw[0]]]]] > zlb[ccnt]) & (sz[gs[galls[gblus[giw[0]]]]] < zub[ccnt])):
                isgood = 2
                regcol = 'blue'
                pylab.scatter(CMDx[g[gall[gblu[iw]]]],CMDy[g[gall[gblu[iw]]]],s=12,color='green')
            else:
                isgood = 3
                regcol = 'cyan'
                pylab.scatter(CMDx[g[gall[gblu[iw]]]],CMDy[g[gall[gblu[iw]]]],s=12,color=html_teal)
            qtemp = sq[gs[galls[gblus[giw[0]]]]]
        if ((isgood == 1) | (isgood == 2)): 
            FILE2.write('point(%f,%f) # point=diamond color=%s\n'%(RA[g[gall[gblu[iw]]]],Dec[g[gall[gblu[iw]]]],regcol))
        else:
            FILE2.write('point(%f,%f) # point=x color=%s\n'%(RA[g[gall[gblu[iw]]]],Dec[g[gall[gblu[iw]]]],regcol))
    top4ar = 0
    print 'b'
    for iw in range(0,len(gars)):
        qtemp = 0
        isgood = 0
        regcol = 'yellow'
        giw = FindCloseSources(RA[g[gall[gars[iw]]]],Dec[g[gall[gars[iw]]]],0.01,sRA[gs[galls[garss]]],sDec[gs[galls[garss]]],0)
        if len(giw) > 0: 
            if ((sz[gs[galls[garss[giw[0]]]]] > centerzs[i]-0.01) & (sz[gs[galls[garss[giw[0]]]]] < centerzs[i]+0.01)):
                isgood = 1
                regcol = 'yellow'
                pylab.scatter(CMDx[g[gall[gars[iw]]]],CMDy[g[gall[gars[iw]]]],s=12,color='red')
            elif ((sz[gs[galls[garss[giw[0]]]]] > zlb[ccnt]) & (sz[gs[galls[garss[giw[0]]]]] < zub[ccnt])):
                isgood = 2
                regcol = 'yellow'
                pylab.scatter(CMDx[g[gall[gars[iw]]]],CMDy[g[gall[gars[iw]]]],s=12,color='green')
                print 'bagel'
            else:
                isgood = 3
                regcol = 'orange'
                pylab.scatter(CMDx[g[gall[gars[iw]]]],CMDy[g[gall[gars[iw]]]],s=12,color=html_teal)
            qtemp = sq[gs[galls[garss[giw[0]]]]]
        if ((top4ar < 3.4) & (isgood < 2.2) & (isgood > 0.1)):
            FILE2.write('# text(%f,%f) color=magenta font="helvetica 10 bold" text={%4.1f,%4.1f}\n'%(RA[g[gall[gars[iw]]]],Dec[g[gall[gars[iw]]]]-2.5/60/60.0,rB[g[gall[gars[iw]]]],iB[g[gall[gars[iw]]]]))
            top4ar += 1
        if ((isgood == 1) | (isgood == 2)): 
            FILE2.write('point(%f,%f) # point=diamond color=%s\n'%(RA[g[gall[gars[iw]]]],Dec[g[gall[gars[iw]]]],regcol))
        else:
            FILE2.write('point(%f,%f) # point=x color=%s\n'%(RA[g[gall[gars[iw]]]],Dec[g[gall[gars[iw]]]],regcol))
    top10 = 0
    top4 = 0
    top4cols = np.array(['red','yellow','cyan','green'])
    print 'c'
    for iw in range(0,len(garg)):
        qtemp = 0
        isgood = 0
        regcol = 'green'
        giw = FindCloseSources(RA[g[gall[grs[garg[iw]]]]],Dec[g[gall[grs[garg[iw]]]]],0.01,sRA[gs[galls[grss]]],sDec[gs[galls[grss]]],0)
        if len(giw) > 0: 
            if ((sz[gs[galls[grss[giw[0]]]]] > centerzs[i]-0.01) & (sz[gs[galls[grss[giw[0]]]]] < centerzs[i]+0.01)):
                isgood = 1
                regcol = 'red'
                pylab.scatter(CMDx[g[gall[grs[garg[iw]]]]],CMDy[g[gall[grs[garg[iw]]]]],s=12,color='red')
            elif ((sz[gs[galls[grss[giw[0]]]]] > zlb[ccnt]) & (sz[gs[galls[grss[giw[0]]]]] < zub[ccnt])):
                isgood = 2
                regcol = 'purple'
                pylab.scatter(CMDx[g[gall[grs[garg[iw]]]]],CMDy[g[gall[grs[garg[iw]]]]],s=12,color='green')
            else:
                isgood = 3
                regcol = 'brown'
                pylab.scatter(CMDx[g[gall[grs[garg[iw]]]]],CMDy[g[gall[grs[garg[iw]]]]],s=12,color=html_teal)
            qtemp = sq[gs[galls[grss[giw[0]]]]]
        FILE.write("%i  %10.8f %f %f %i %4i\n"%(isgood,iB[g[gall[grs[garg[iw]]]]],RA[g[gall[grs[garg[iw]]]]],Dec[g[gall[grs[garg[iw]]]]],qtemp,iw))
        FILE2.write('point(%f,%f) # point=x color=%s\n'%(RA[g[gall[grs[garg[iw]]]]],Dec[g[gall[grs[garg[iw]]]]],regcol))
        if ((top10 < 9.4) & (isgood < 2.2)):
            if ((i == 5) | (i == 6)):
                FILE2.write('# text(%f,%f) color=magenta font="helvetica 10 bold" text={%4.1f,%4.1f}\n'%(RA[g[gall[grs[garg[iw]]]]],Dec[g[gall[grs[garg[iw]]]]]-2.5/60/60.0,iB[g[gall[grs[garg[iw]]]]],rB[g[gall[grs[garg[iw]]]]]))
            else:
                FILE2.write('# text(%f,%f) color=magenta font="helvetica 10 bold" text={%4.1f,%4.1f}\n'%(RA[g[gall[grs[garg[iw]]]]],Dec[g[gall[grs[garg[iw]]]]]-2.5/60/60.0,iB[g[gall[grs[garg[iw]]]]],zB[g[gall[grs[garg[iw]]]]]))
            top10 += 1
        if ((top4 < 3.4) & (isgood < 2.2)):
            FILE2.write('point(%f,%f) # point=circle color=%s\n'%(RA[g[gall[grs[garg[iw]]]]],Dec[g[gall[grs[garg[iw]]]]],top4cols[top4]))
            if top4 == 0: pylab.scatter(CMDx[g[gall[grs[garg[iw]]]]],CMDy[g[gall[grs[garg[iw]]]]],s=50,marker='d',facecolors='none',color='red')
            if top4 == 1: pylab.scatter(CMDx[g[gall[grs[garg[iw]]]]],CMDy[g[gall[grs[garg[iw]]]]],s=50,marker='d',facecolors='none',color=html_brwn)
            if top4 == 2: pylab.scatter(CMDx[g[gall[grs[garg[iw]]]]],CMDy[g[gall[grs[garg[iw]]]]],s=50,marker='d',facecolors='none',color=html_teal)
            if top4 == 3: pylab.scatter(CMDx[g[gall[grs[garg[iw]]]]],CMDy[g[gall[grs[garg[iw]]]]],s=50,marker='d',facecolors='none',color='blue')
            top4 += 1
    FILE2.write('circle(%f,%f,%f") # color=blue\ncircle(%f,%f,%f")]\n'%(centerRAs[i],centerDecs[i],srchdist[i],centerRAs[i],centerDecs[i],srchdist[i]*0.5))
    FILE.close()
    FILE2.close()
    pylab.savefig('/home/rumbaugh/CMD.%s.2.8.12.png'%(names[i]))
    pylab.close('all')
      
