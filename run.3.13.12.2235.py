execfile('/home/rumbaugh/scale_estimators.py')
execfile('/home/rumbaugh/FindCloseSources.py')
import matplotlib
import matplotlib.pylab as pylab
html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FF9900'
html_pink = '#FF00FF'
strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
RGalPeakRA = np.array([201.20353640,201.09003360,201.20748930,(17+(57+18.769/60)/60)*360/24.0,275.3801,241.08946,241.09890,(360.0/24)*(9+(10+(4.168/60))/60.0),(360.0/24)*(9+(10+(47.686/60))/60.0)])
RGalPeakDec = np.array([30.19424680,30.21497820,30.97371310,66+(31+37.46/60)/60.0,68.4651,43.07613,43.23550,(54+(18+(54.21/60))/60.0),(54+(22+(13.82/60))/60.0)])

zlb = [0.82,0.65,0.68,0.80,0.84,0.84,1.0]
zub = [0.87,0.79,0.71,0.84,0.96,0.96,1.2]

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
srchdist = np.array([3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92])*0.7
ccnt = 0
FILE=open('/home/rumbaugh/veldisps.3.13.12.dat','w')
FILE.write("# Structure  Numgals_xray Numgals_BCG Numgals_RGP MAD_xray MAD_BCG MAG_RGP FP_xray FP_BCG FP_RGP BW_xray BW_BCG BW_RGP gap_xray gap_BCG gap_RGP\n")
for i in range(0,len(names)):
    if ((i != 1) & (i != 2) & (i != 6) & (i != 8)): ccnt += 1
    if i == 5: ccnt += 1
    sfile = '/home/rumbaugh/%s'%(files[ccnt])
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
    #vels = sz*3*10**5
    sq = copy_colvals(crs,'col11')
    g = np.where((sq > 2.2) & (sz > zlb[ccnt]) & (sz < zub[ccnt]))
    g = g[0]
    gappers,MADs,FPs,biweights = np.zeros(3),np.zeros(3),np.zeros(3),np.zeros(3)
    distsx,distsBCG,distsRGP = np.zeros(len(g)),np.zeros(len(g)),np.zeros(len(g))
    for j in range(0,len(g)):
        distsx[j] = SphDist(sRA[g[j]],sDec[g[j]],centerRAs[i],centerDecs[i])
        distsBCG[j] = SphDist(sRA[g[j]],sDec[g[j]],BCGRA[i],BCGDec[i])
        distsRGP[j] = SphDist(sRA[g[j]],sDec[g[j]],RGalPeakRA[i],RGalPeakDec[i])
    gx = np.where(distsx < srchdist[i])
    gx = gx[0]
    gBCG = np.where(distsBCG < srchdist[i])
    gBCG = gBCG[0]
    gRGP = np.where(distsRGP < srchdist[i])
    gRGP = gRGP[0]
    velsx = (sz[g[gx]]-biweight_loc(sz[g[gx]]))*(3.0*10**5)/(1+sz[g[gx]])
    velsBCG = (sz[g[gBCG]]-biweight_loc(sz[g[gBCG]]))*3*10**5/(1+sz[g[gBCG]])
    velsRGP = (sz[g[gRGP]]-biweight_loc(sz[g[gRGP]]))*3*10**5/(1+sz[g[gRGP]])
    gappers[0],gappers[1],gappers[2] = gapper(velsx),gapper(velsBCG),gapper(velsRGP)
    MADs[0],MADs[1],MADs[2] = MAD(velsx),MAD(velsBCG),MAD(velsRGP)
    FPs[0],FPs[1],FPs[2] = fpseudosigma(velsx),fpseudosigma(velsBCG),fpseudosigma(velsRGP)
    biweights[0],biweights[1],biweights[2] = biweight_scale(velsx),biweight_scale(velsBCG),biweight_scale(velsRGP)
    FILE.write('%13s %3i %3i %3i %f %f %f %f %f %f %f %f %f %f %f %f\n'%(names[i],len(gx),len(gBCG),len(gRGP),gappers[0],gappers[1],gappers[2],MADs[0],MADs[1],MADs[2],FPs[0],FPs[1],FPs[2],biweights[0],biweights[1],biweights[2]))
    pylab.xlabel('Velocity Dispersion')
    pylab.ylabel('Num. Galaxies Used')
    pylab.ylim(len(gx)-5,len(gx)+5)
    pylab.xlim(0,2000)
    pylab.scatter([gappers[0]],[len(gx)],color='blue',marker='x')
    pylab.scatter([gappers[1]],[len(gBCG)],color='blue',marker='o')
    pylab.scatter([gappers[2]],[len(gRGP)],color='blue',marker='d')
    pylab.scatter([MADs[0]],[len(gx)],color=html_teal,marker='x')
    pylab.scatter([MADs[1]],[len(gBCG)],color=html_teal,marker='o')
    pylab.scatter([MADs[2]],[len(gRGP)],color=html_teal,marker='d')
    pylab.scatter([FPs[0]],[len(gx)],color=html_orng,marker='x')
    pylab.scatter([FPs[1]],[len(gBCG)],color=html_orng,marker='o')
    pylab.scatter([FPs[2]],[len(gRGP)],color=html_orng,marker='d')
    pylab.scatter([biweights[0]],[len(gx)],color='red',marker='x')
    pylab.scatter([biweights[1]],[len(gBCG)],color='red',marker='o')
    pylab.scatter([biweights[2]],[len(gRGP)],color='red',marker='d')
    pylab.savefig('/home/rumbaugh/veldisps.plot.%s.3.13.12.png'%(names[i]))
    pylab.close('all')
FILE.close()
                                                           
