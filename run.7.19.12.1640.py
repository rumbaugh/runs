execfile('/home/rumbaugh/scale_estimators.py')
execfile('/home/rumbaugh/FindCloseSources.py')
execfile('/home/rumbaugh/CalcVelDisp.py')
import matplotlib
import matplotlib.pylab as pylab

def sigclip(data,mean,sig,sigthresh=3.0):
    gsc = np.where((data < mean + sigthresh*sig) & (data > mean - sigthresh*sig))
    gsc = gsc[0]
    return gsc


html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FF9900'
html_pink = '#FF00FF'
strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])
sigerrs = np.array([120,140,130,140,90,130,80,190,140])

#files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
files = ['FINAL.SG0023.deimos.lris.feb2012.nodups.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.feb2012.nh.cat','FINAL.nep5281.deimos.gioia.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectroscopic.autocompile.blemaux.sc0910.mar2012.T08needstoberedone.nodups.cat']
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
FILE=open('/home/rumbaugh/veldisps.7.19.12.dat','w')
FILE.write("# Structure  Numgals_MAD_xray Numgals_MAD_BCG Numgals_MAD_RGP  Numgals_FP_xray Numgals_FP_BCG Numgals_FP_RGP  Numgals_BW_xray Numgals_BW_BCG Numgals_BW_RGP  Numgals_gap_xray Numgals_gap_BCG Numgals_gap_RGP MAD_xray MAD_BCG MAG_RGP FP_xray FP_BCG FP_RGP BW_xray BW_BCG BW_RGP gap_xray gap_BCG gap_RGP MAD_xray_errBSlo MAD_BCG_errBSlo MAG_RGP_errBSlo FP_xray_errBSlo FP_BCG_errBSlo FP_RGP_errBSlo BW_xray_errBSlo BW_BCG_errBSlo BW_RGP_errBSlo gap_xray_errBSlo gap_BCG_errBSlo gap_RGP_errBSlo MAD_xray_errBShi MAD_BCG_errBShi MAG_RGP_errBShi FP_xray_errBShi FP_BCG_errBShi FP_RGP_errBShi BW_xray_errBShi BW_BCG_errBShi BW_RGP_errBShi gap_xray_errBShi gap_BCG_errBShi gap_RGP_errBShi MAD_xray_errJK MAD_BCG_errJK MAG_RGP_errJK FP_xray_errJK FP_BCG_errJK FP_RGP_errJK BW_xray_errJK BW_BCG_errJK BW_RGP_errJK gap_xray_errJK gap_BCG_errJK gap_RGP_errJK \n")
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
    gerrBSL,merrBSL,ferrBSL,berrBSL = np.zeros(3),np.zeros(3),np.zeros(3),np.zeros(3)
    gerrBSH,merrBSH,ferrBSH,berrBSH = np.zeros(3),np.zeros(3),np.zeros(3),np.zeros(3)
    gerrJK,merrJK,ferrJK,berrJK = np.zeros(3),np.zeros(3),np.zeros(3),np.zeros(3)
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
    prevx,prevBCG,prevRGP = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanx = biweight_loc(velsx)
    velsxtemp = np.copy(velsx)
    gxlens = np.zeros(4,dtype='int8')
    while len(gxtemp) < prevx:
        prevx = len(gxtemp)
        gxtemp = sigclip(velsxtemp,meanx,MADs[0])
        velsxtemp = (sz[g[gx]]-biweight_loc(sz[g[gx[gxtemp]]]))*(3.0*10**5)/(1+sz[g[gx]])
        meanx = biweight_loc(velsxtemp[gxtemp])
        MADs[0],merrBSL[0],merrBSH[0] = CalcVelDisp(sz[g[gx]],method='MAD',ConfInvMethod='bootstrap')
        MADs[0],merrJK[0] = CalcVelDisp(sz[g[gx]],method='MAD',ConfInvMethod='jackknife')
    gxlens[1] = len(gxtemp)
    prevx,prevBCG,prevRGP = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanx = biweight_loc(velsx)
    velsxtemp = np.copy(velsx)
    while len(gxtemp) < prevx:
        prevx = len(gxtemp)
        gxtemp = sigclip(velsxtemp,meanx,FPs[0])
        velsxtemp = (sz[g[gx]]-biweight_loc(sz[g[gx[gxtemp]]]))*(3.0*10**5)/(1+sz[g[gx]])
        meanx = biweight_loc(velsxtemp[gxtemp])
        FPs[0],ferrBSL[0],ferrBSH[0] = CalcVelDisp(sz[g[gx]],method='fpseudosigma',ConfInvMethod='bootstrap')
        FPs[0],ferrJK[0] = CalcVelDisp(sz[g[gx]],method='fpseudosigma',ConfInvMethod='jackknife')
    gxlens[2] = len(gxtemp)
    prevx,prevBCG,prevRGP = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanx = biweight_loc(velsx)
    velsxtemp = np.copy(velsx)
    while len(gxtemp) < prevx:
        prevx = len(gxtemp)
        gxtemp = sigclip(velsxtemp,meanx,biweights[0])
        velsxtemp = (sz[g[gx]]-biweight_loc(sz[g[gx[gxtemp]]]))*(3.0*10**5)/(1+sz[g[gx]])
        meanx = biweight_loc(velsxtemp[gxtemp])
        biweights[0],berrBSL[0],berrBSH[0] = CalcVelDisp(sz[g[gx]],method='biweight_scale',ConfInvMethod='bootstrap')
        biweights[0],berrJK[0] = CalcVelDisp(sz[g[gx]],method='biweight_scale',ConfInvMethod='jackknife')
    gxlens[3] = len(gxtemp)
    prevx,prevBCG,prevRGP = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanx = biweight_loc(velsx)
    velsxtemp = np.copy(velsx)
    while len(gxtemp) < prevx:
        prevx = len(gxtemp)
        gxtemp = sigclip(velsxtemp,meanx,gappers[0])
        velsxtemp = (sz[g[gx]]-biweight_loc(sz[g[gx[gxtemp]]]))*(3.0*10**5)/(1+sz[g[gx]])
        meanx = biweight_loc(velsxtemp[gxtemp])
        gappers[0],gerrBSL[0],gerrBSH[0] = CalcVelDisp(sz[g[gx]],method='gapper',ConfInvMethod='bootstrap')
        gappers[0],gerrJK[0] = CalcVelDisp(sz[g[gx]],method='gapper',ConfInvMethod='jackknife')
    gxlens[0] = len(gxtemp)

    prevx,prevBCG,prevr = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanBCG = biweight_loc(velsBCG)
    velsBCGtemp = np.copy(velsBCG)
    gBCGlens = np.zeros(4,dtype='int8')
    while len(gBCGtemp) < prevBCG:
        prevBCG = len(gBCGtemp)
        gBCGtemp = sigclip(velsBCGtemp,meanBCG,MADs[1])
        velsBCGtemp = (sz[g[gBCG]]-biweight_loc(sz[g[gBCG[gBCGtemp]]]))*(3.0*10**5)/(1+sz[g[gBCG]])
        meanBCG = biweight_loc(velsBCGtemp[gBCGtemp])
        MADs[1],merrBSL[1],merrBSH[1] = CalcVelDisp(sz[g[gBCG]],method='MAD',ConfInvMethod='bootstrap')
        MADs[1],merrJK[1] = CalcVelDisp(sz[g[gBCG]],method='MAD',ConfInvMethod='jackknife')
    gBCGlens[1] = len(gBCGtemp)
    prevx,prevBCG,prevr = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanBCG = biweight_loc(velsBCG)
    velsBCGtemp = np.copy(velsBCG)
    while len(gBCGtemp) < prevBCG:
        prevBCG = len(gBCGtemp)
        gBCGtemp = sigclip(velsBCGtemp,meanBCG,FPs[1])
        velsBCGtemp = (sz[g[gBCG]]-biweight_loc(sz[g[gBCG[gBCGtemp]]]))*(3.0*10**5)/(1+sz[g[gBCG]])
        meanBCG = biweight_loc(velsBCGtemp[gBCGtemp])
        FPs[1],ferrBSL[1],ferrBSH[1] = CalcVelDisp(sz[g[gBCG]],method='fpseudosigma',ConfInvMethod='bootstrap')
        FPs[1],ferrJK[1] = CalcVelDisp(sz[g[gBCG]],method='fpseudosigma',ConfInvMethod='jackknife')
    gBCGlens[2] = len(gBCGtemp)
    prevx,prevBCG,prevr = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanBCG = biweight_loc(velsBCG)
    velsBCGtemp = np.copy(velsBCG)
    while len(gBCGtemp) < prevBCG:
        prevBCG = len(gBCGtemp)
        gBCGtemp = sigclip(velsBCGtemp,meanBCG,biweights[1])
        velsBCGtemp = (sz[g[gBCG]]-biweight_loc(sz[g[gBCG[gBCGtemp]]]))*(3.0*10**5)/(1+sz[g[gBCG]])
        meanBCG = biweight_loc(velsBCGtemp[gBCGtemp])
        biweights[1],berrBSL[1],berrBSH[1] = CalcVelDisp(sz[g[gBCG]],method='biweight_scale',ConfInvMethod='bootstrap')
        biweights[1],berrJK[1] = CalcVelDisp(sz[g[gBCG]],method='biweight_scale',ConfInvMethod='jackknife')
    gBCGlens[3] = len(gBCGtemp)
    prevx,prevBCG,prevr = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanBCG = biweight_loc(velsBCG)
    velsBCGtemp = np.copy(velsBCG)
    while len(gBCGtemp) < prevBCG:
        prevBCG = len(gBCGtemp)
        gBCGtemp = sigclip(velsBCGtemp,meanBCG,gappers[1])
        velsBCGtemp = (sz[g[gBCG]]-biweight_loc(sz[g[gBCG[gBCGtemp]]]))*(3.0*10**5)/(1+sz[g[gBCG]])
        meanBCG = biweight_loc(velsBCGtemp[gBCGtemp])
        gappers[1],gerrBSL[1],gerrBSH[1] = CalcVelDisp(sz[g[gBCG]],method='gapper',ConfInvMethod='bootstrap')
        gappers[1],gerrJK[1] = CalcVelDisp(sz[g[gBCG]],method='gapper',ConfInvMethod='jackknife')
    gBCGlens[0] = len(gBCGtemp)


    prevx,prevBCG,prevRGP = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanRGP = biweight_loc(velsRGP)
    velsRGPtemp = np.copy(velsRGP)
    gRGPlens = np.zeros(4,dtype='int8')
    while len(gRGPtemp) < prevRGP:
        prevRGP = len(gRGPtemp)
        gRGPtemp = sigclip(velsRGPtemp,meanRGP,MADs[2])
        velsRGPtemp = (sz[g[gRGP]]-biweight_loc(sz[g[gRGP[gRGPtemp]]]))*(3.0*10**5)/(1+sz[g[gRGP]])
        meanRGP = biweight_loc(velsRGPtemp[gRGPtemp])
        MADs[2],merrBSL[2],merrBSH[2] = CalcVelDisp(sz[g[gRGP]],method='MAD',ConfInvMethod='bootstrap')
        MADs[2],merrJK[2] = CalcVelDisp(sz[g[gRGP]],method='MAD',ConfInvMethod='jackknife')
    gRGPlens[1] = len(gRGPtemp)
    prevx,prevBCG,prevRGP = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanRGP = biweight_loc(velsRGP)
    velsRGPtemp = np.copy(velsRGP)
    while len(gRGPtemp) < prevRGP:
        prevRGP = len(gRGPtemp)
        gRGPtemp = sigclip(velsRGPtemp,meanRGP,FPs[2])
        velsRGPtemp = (sz[g[gRGP]]-biweight_loc(sz[g[gRGP[gRGPtemp]]]))*(3.0*10**5)/(1+sz[g[gRGP]])
        meanRGP = biweight_loc(velsRGPtemp[gRGPtemp])
        FPs[2],ferrBSL[2],ferrBSH[2] = CalcVelDisp(sz[g[gRGP]],method='fpseudosigma',ConfInvMethod='bootstrap')
        FPs[2],ferrJK[2] = CalcVelDisp(sz[g[gRGP]],method='fpseudosigma',ConfInvMethod='jackknife')
    gRGPlens[2] = len(gRGPtemp)
    prevx,prevBCG,prevRGP = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanRGP = biweight_loc(velsRGP)
    velsRGPtemp = np.copy(velsRGP)
    while len(gRGPtemp) < prevRGP:
        prevRGP = len(gRGPtemp)
        gRGPtemp = sigclip(velsRGPtemp,meanRGP,biweights[2])
        velsRGPtemp = (sz[g[gRGP]]-biweight_loc(sz[g[gRGP[gRGPtemp]]]))*(3.0*10**5)/(1+sz[g[gRGP]])
        meanRGP = biweight_loc(velsRGPtemp[gRGPtemp])
        biweights[2],berrBSL[2],berrBSH[2] = CalcVelDisp(sz[g[gRGP]],method='biweight_scale',ConfInvMethod='bootstrap')
        biweights[2],berrJK[2] = CalcVelDisp(sz[g[gRGP]],method='biweight_scale',ConfInvMethod='jackknife')
    gRGPlens[3] = len(gRGPtemp)
    prevx,prevBCG,prevRGP = 9999,9999,9999
    gxtemp,gBCGtemp,gRGPtemp = np.arange(len(gx)),np.arange(len(gBCG)),np.arange(len(gRGP))
    meanRGP = biweight_loc(velsRGP)
    velsRGPtemp = np.copy(velsRGP)
    while len(gRGPtemp) < prevRGP:
        prevRGP = len(gRGPtemp)
        gRGPtemp = sigclip(velsRGPtemp,meanRGP,gappers[2])
        velsRGPtemp = (sz[g[gRGP]]-biweight_loc(sz[g[gRGP[gRGPtemp]]]))*(3.0*10**5)/(1+sz[g[gRGP]])
        meanRGP = biweight_loc(velsRGPtemp[gRGPtemp])
        gappers[2],gerrBSL[2],gerrBSH[2] = CalcVelDisp(sz[g[gRGP]],method='gapper',ConfInvMethod='bootstrap')
        gappers[2],gerrJK[2] = CalcVelDisp(sz[g[gRGP]],method='gapper',ConfInvMethod='jackknife')
    gRGPlens[0] = len(gRGPtemp)



    FILE.write('%13s %3i %3i %3i %3i %3i %3i %3i %3i %3i %3i %3i %3i %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f\n'%(names[i],gxlens[1],gBCGlens[1],gRGPlens[1],gxlens[2],gBCGlens[2],gRGPlens[2],gxlens[3],gBCGlens[3],gRGPlens[3],gxlens[0],gBCGlens[0],gRGPlens[0],MADs[0],MADs[1],MADs[2],FPs[0],FPs[1],FPs[2],biweights[0],biweights[1],biweights[2],gappers[0],gappers[1],gappers[2],merrBSL[0],merrBSL[1],merrBSL[2],ferrBSL[0],ferrBSL[1],ferrBSL[2],berrBSL[0],berrBSL[1],berrBSL[2],gerrBSL[0],gerrBSL[1],gerrBSL[2],merrBSH[0],merrBSH[1],merrBSH[2],ferrBSH[0],ferrBSH[1],ferrBSH[2],berrBSH[0],berrBSH[1],berrBSH[2],gerrBSH[0],gerrBSH[1],gerrBSH[2],merrJK[0],merrJK[1],merrJK[2],ferrJK[0],ferrJK[1],ferrJK[2],berrJK[0],berrJK[1],berrJK[2],gerrJK[0],gerrJK[1],gerrJK[2]))
    pylab.xlabel('Velocity Dispersion')
    pylab.ylabel('Num. Galaxies Used')
    pylab.ylim(gxlens[0]-10,gxlens[0]+10)
    pylab.xlim(0,1500)
    pylab.scatter([gappers[0]],[gxlens[0]],color='blue',marker='x')
    pylab.scatter([gappers[1]],[gBCGlens[0]],color='blue',marker='+')
    pylab.scatter([gappers[2]],[gRGPlens[0]],color='blue',marker='d',facecolor='none')
    pylab.scatter([MADs[0]],[gxlens[1]],color=html_teal,marker='x')
    pylab.scatter([MADs[1]],[gBCGlens[1]],color=html_teal,marker='+')
    pylab.scatter([MADs[2]],[gRGPlens[1]],color=html_teal,marker='d',facecolor='none')
    pylab.scatter([FPs[0]],[gxlens[2]],color=html_orng,marker='x')
    pylab.scatter([FPs[1]],[gBCGlens[2]],color=html_orng,marker='+')
    pylab.scatter([FPs[2]],[gRGPlens[2]],color=html_orng,marker='d',facecolor='none')
    pylab.scatter([biweights[0]],[gxlens[3]],color='red',marker='x')
    pylab.scatter([biweights[1]],[gBCGlens[3]],color='red',marker='+')
    pylab.scatter([biweights[2]],[gRGPlens[3]],color='red',marker='d',facecolor='none')
    pylab.errorbar([biweights[2]],[gRGPlens[3]],yerr=None,xerr=[sigerrs[i]],color='red',marker='d')
    pylab.savefig('/home/rumbaugh/veldisps.plot.%s.6.27.12.png'%(names[i]))
    pylab.close('all')
FILE.close()
                                                           
