import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/plotcircle.py")
execfile("/home/rumbaugh/angconvert.py")

html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FFCC00'

try:
    cradmult
except NameError:
    cradmult = 2

try:
    Ilim
except NameError:
    Ilim = 23.5
try:
    Imin
except NameError:
    Imin = 19.5

try:
    arstep
except NameError:
    arstep = 0.0001

def switch5(arr5):
    arr5[0],arr5[1],arr5[2],arr5[3],arr5[4] = arr5[1],arr5[3],arr5[0],arr5[4],arr5[2]
    return arr5

def LookInCluster(clustot,clustotRS,clustotNRS,Mind,Cind):
    gicStemp = np.where(intempS > 0.1)
    gictemp = np.where(intemp > 0.1)
    gictemp = gictemp[0]
    gicStemp = gicStemp[0]
    gsztemp = np.where((sz[gsI[gicStemp]] >= clusz[Cind]-0.01) & (sz[gsI[gicStemp]] <= clusz[Cind]+0.01))
    gsztemp = gsztemp[0]
    gsqtemp = np.where(sq[gsI[gicStemp[gsztemp]]] > 2.3)
    gsqtemp = gsqtemp[0]
    gRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] + rsNSTD[i]*rsSTD[i]) & (sR[gsI[gicStemp]]-sI[gsI[gicStemp]] >= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
    gNRSt1 = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]) & (sR[gsI[gicStemp]]-sI[gsI[gicStemp]] >= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - 3*rsNSTD[i]*rsSTD[i]))
    gNRSt2 = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - 3*rsNSTD[i]*rsSTD[i]))
    gRSt = gRSt[0]
    gNRSt1 = gNRSt1[0]
    gNRSt2 = gNRSt2[0]
    gRSzt = np.where((sz[gsI[gicStemp[gRSt]]] >= clusz[Cind]-0.01) & (sz[gsI[gicStemp[gRSt]]] <= clusz[Cind]+0.01))
    gRSzt = gRSzt[0]
    gRSqt = np.where(sq[gsI[gicStemp[gRSt[gRSzt]]]] > 2.3)
    gRSqt = gRSqt[0]
    gNRSzt1 = np.where((sz[gsI[gicStemp[gNRSt1]]] >= clusz[Cind]-0.01) & (sz[gsI[gicStemp[gNRSt1]]] <= clusz[Cind]+0.01))
    gNRSzt1 = gNRSzt1[0]
    gNRSqt1 = np.where(sq[gsI[gicStemp[gNRSt1[gNRSzt1]]]] > 2.3)
    gNRSqt1 = gNRSqt1[0]
    gNRSzt2 = np.where((sz[gsI[gicStemp[gNRSt2]]] >= clusz[Cind]-0.01) & (sz[gsI[gicStemp[gNRSt2]]] <= clusz[Cind]+0.01))
    gNRSzt2 = gNRSzt2[0]
    gNRSqt2 = np.where(sq[gsI[gicStemp[gNRSt2[gNRSzt2]]]] > 2.3)
    gNRSqt2 = gNRSqt2[0]
    gRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] + rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] >= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
    gNRSpt1 = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] >= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - 3*rsNSTD[i]*rsSTD[i]))
    gNRSpt2 = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - 3*rsNSTD[i]*rsSTD[i]))
    convRSt,convNRSt1,convNRSt2 = 0,0,0
    if len(gRSt) > 0: convRSt = len(gRSqt)*1.0/len(gRSt)
    if len(gNRSt1) > 0: convNRSt1 = len(gNRSqt1)*1.0/len(gNRSt1)
    if len(gNRSt2) > 0: convNRSt2 = len(gNRSqt2)*1.0/len(gNRSt2)
    totRStemp = convRSt*len(gRSpt[0])
    totNRStemp1 = convNRSt1*len(gNRSpt1[0])
    totNRStemp2 = convNRSt2*len(gNRSpt2[0])
    clustotRS += totRStemp
    clustotNRS += totNRStemp1 + totNRStemp2
    convtemp = len(gsqtemp)*1.0/len(gicStemp)
    tottemp = convtemp*len(gictemp)
    clustot += tottemp
    print '%s%s - (Good Spec,Tot.Spec,Total,Est) - (%i,%i,%i,%.1f)'%(names[Mind],cnam[Cind],len(gsqtemp),len(gicStemp),len(gictemp),tottemp)
    print '%.0f %.0f %.0f %6.4f %6.4f %6.4f'%(totRStemp,totNRStemp1,totNRStemp2,convNRSt1,convNRSt2,(len(gNRSqt1)+len(gNRSqt2))*1.0/(len(gNRSqt1)+len(gNRSqt2)+len(gRSqt)))
    plotcircle(RAcen=clusRA[Cind],DECcen=clusDec[Cind],rad=crads[Cind])
    return clustot,clustotRS,clustotNRS

def lookinreg(ralb,raub,declb,decub,chkras,chkdecs):
    glreg = np.where((chkras >= ralb) & (chkras <= raub) & (chkdecs >= declb) & (chkdecs <= decub)) 
    if len(glreg) > 0:
        glreg = glreg[0]
    numin = len(glreg)
    return numin

bgcnt = -1
numBGs = np.array([2,4,3,2,3])
BGRA1arr = np.array([201.33,201.375,275.7,275.7,275.45,274.85,5.915,6.04,6.12,241.2,241.46,269.7,268.86,269.3])
BGRA2arr = np.array([201.43,201.43,275.93,275.85,275.65,274.95,6.02,6.09,6.19,241.375,241.57,269.98,268.92,269.45])
BGDec1arr = np.array([30.32,30.735,68.38,68.5,68.66,68.58,4.55,4.205,4.425,42.87,43.0,66.44,66.44,66.68])
BGDec2arr = np.array([30.465,30.88,68.43,68.55,68.69,68.6,4.6,4.26,4.52,42.94,43.13,66.48,66.65,66.74])
#numBGs = np.array([2,4,3,2,3])
#BGRA1arr = np.array([201.35,201.375,275.7,275.7,275.45,274.85,5.925,6.04,6.12,241.2,241.46,269.7,268.86,269.3])
#BGRA2arr = np.array([201.42,201.43,275.93,275.85,275.65,274.95,6.02,6.08,6.185,241.375,241.57,269.98,268.92,269.45])
#BGDec1arr = np.array([30.325,30.735,68.38,68.5,68.66,68.58,4.57,4.21,4.425,42.87,43.0,66.44,66.44,66.68])
#BGDec2arr = np.array([30.46,30.88,68.43,68.55,68.69,68.6,4.6,4.25,4.51,42.94,43.13,66.48,66.65,66.74])
CLareas = np.zeros(5)
BGareas = np.zeros(5)
BGRSmemtot = np.zeros(5)
BGNRSmemtot = np.zeros(5)
CLRSmemtot = np.zeros(5)
CLNRSmemtot = np.zeros(5)

#masks1324 = np.array(['1322A','1322C','1322E','1322F','1322G','1322H','1322J','1322K','1322L','1322M'])#,'LRIS'])
#masks1604 = np.array(['GHF1','GHF2','FG1','FG2','16XR1','16XR2','16XR3','16CN2','16CN3','16CN4','16CN5','16CN6','16COM1','CE1','LRIS.scm1','LRIS.scm2','LRIS.scm4','LRIS.scnm2','SC1NM1','SC1NM2','SC2NM1','SC2NM2','oldLRIS','oldLRISe'])
#masks5281 = np.array(['5281M1','5281M2','5281M3'])
#masks1757 = np.array(['N200M1','N200M2'])#,'N200X1','N200X2'])
#masks0023 = np.array(['0023X1','0023X2','0023X3B','0023X4','
#masks0023 = np.array(['00DMA','00DMB','00ND1','00ND2','00ND4'])#,'LRIS'])


masks1324 = np.array(['1322A','1322C','1322E','1322G'])#,'LRIS'])
masks1604 = np.array(['GHF1','GHF2','FG1','FG2','16XR1','16XR2','16XR3','16CN2','16CN3','16CN4','16CN5','16CN6','16COM1','CE1','LRIS.scm1','LRIS.scm2','LRIS.scm4','LRIS.scnm2','SC1NM1','SC1NM2','SC2NM1','SC2NM2','oldLRIS','oldLRISe'])
masks5281 = np.array(['5281M1','5281M2'])
masks1757 = np.array(['N200M1','N200M2'])#,'N200X1','N200X2'])
#masks0023 = np.array(['0023X1','0023X2','0023X3B','0023X4','
masks0023 = np.array(['00ND1','00ND2'])#,'LRIS'])

topcolbin = np.array([1.3,1.3,1.5,1.4,1.4])
botRS = np.array([1.0,1.05,1.1,1.05,1.0])
#for CL1604 ACS data, use 2.1, but same bottom (0.0, for all fields)
convgrid = np.zeros((3,4,5))
totmemgrid = np.zeros((3,4,5))

crxlims = read_file('/home/rumbaugh/paperstuff/xraybounds.5.3.11.dat')
limL = get_colvals(crxlims,'col2')
limU = get_colvals(crxlims,'col3')

path = '/home/rumbaugh/LFC'
pathm = '/scratch/rumbaugh/ciaotesting'
path2 = 'opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat'
names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
files = np.array(['FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.noheader.cat','FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.noheader.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.noheader.cat'])
mfiles = np.array(['FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat','FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat','FINAL.matched.0023.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.1604.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.N200.specnXray.nov2010.rumbaugh.noheader.cat'])
pfiles=np.array(['sc1322.lfc.newIDsandoldIds.radecmag.cat','nep5281.lfc.newIDradecmag.cat','cl0023_radecIDmags.cat','final.idradecmag.lfcpluscosmic.withsdss.cat','nep200.idradecmag.lfc.uhcorr.neat'])

#rsfitb = np.array([1.777,1.325,1.84,1.203,3.182])
#rsfitm = np.array([0.0229,0.0084,0.0319,0.0012,0.063])
#rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0907])
rsfitb = np.array([1.777,1.325,1.84,1.203,1.305])
rsfitm = np.array([0.0229,0.0084,0.0319,0.0012,0.00485])
rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0813])
rsfitb = switch5(rsfitb)
rsfitm = switch5(rsfitm)
rsSTD = switch5(rsSTD)

rsNSTD = np.array([2.0,3.0,3.0,2.0,3.0])

zlb = np.array([0.65,0.80,0.82,0.84,0.68])
zub = np.array([0.79,0.84,0.87,0.96,0.71])

crcr = read_file('/home/rumbaugh/clusters.z+pos+mpc.5.13.11.dat')
struc = get_colvals(crcr,'col1')
cnam = get_colvals(crcr,'col2')
clusz = get_colvals(crcr,'col3')
clusdis = get_colvals(crcr,'col14')
clusH = get_colvals(crcr,'col15')*0.7
clusRA = get_colvals(crcr,'col4')
clusDec = get_colvals(crcr,'col5')
mpc = get_colvals(crcr,'col6')
mpccm = get_colvals(crcr,'col7')
crads = cradmult*0.7*mpc/60
r200 = 2*clusdis/(m.sqrt(200)*clusH)
crads = cradmult*0.7*mpc/60

crbnds = read_file('/home/rumbaugh/CMD.regions.dat')
bounds = get_colvals(crbnds,'col2')
bgcnt2 = 0
Ilimholder = Ilim
Iminholder = Imin
for i in range(0,5):
    xpfile= '/scratch/rumbaugh/ciaotesting/%s/master/photometry/%s.xray_phot.soft_hard_full.dat'%(names[i],names[i])
    crxp = read_file(xpfile)
    xfncnts = get_colvals(crxp,'col8')
    xpra = get_colvals(crxp,'col1')
    xpdec = get_colvals(crxp,'col2')
    if i == 3: 
        Ilim = Ilimholder
        Imin = Iminholder
    else:
        Ilim = Ilimholder
        Imin = Iminholder
    rsfX = np.arange(15)+15
    rsfY1 = rsfitb[i]-rsfitm[i]*rsfX+rsNSTD[i]*rsSTD[i]
    rsfY2 = rsfitb[i]-rsfitm[i]*rsfX-rsNSTD[i]*rsSTD[i]

    master = 'master'
    if i == 2: master = '7914'
    mfile = '%s/%s/%s/%s'%(pathm,names[i],master,path2)
    sfile = '%s/%s'%(path,files[i])
    msfile = '%s/%s'%(path,mfiles[i])
    crm = read_file(mfile)
    mRAX = get_colvals(crm,'col2')
    mDecX = get_colvals(crm,'col3')
    nm = get_colvals(crm,'col5')
    mRA = get_colvals(crm,'col6')
    mDec = get_colvals(crm,'col7')

    pfile = '%s/%s'%(path,pfiles[i])
    crp = read_file(pfile)
    if i == 0:
        pRA = get_colvals(crp,'col3')
        pDec = get_colvals(crp,'col4')
        pR = get_colvals(crp,'col5')
        pI = get_colvals(crp,'col6')
        pZ = get_colvals(crp,'col7')
    else:
        pRA = get_colvals(crp,'col2')
        pDec = get_colvals(crp,'col3')
        pR = get_colvals(crp,'col4')
        pI = get_colvals(crp,'col5')
        pZ = get_colvals(crp,'col6')
#    if i == 3:
#        pfile2 = '/home/rumbaugh/LFC/ACS_merged.F606W+F814W_deep.all.coll.nh.dat'
#        crp2 = read_file(pfile2)
#        pR = get_colvals(crp2,'col3')
#        pI = get_colvals(crp2,'col4')
#        pRA = get_colvals(crp2,'col1')
#        pDec = get_colvals(crp2,'col2')
        
    
    crs = read_file(sfile)
    smask = get_colvals(crs,'col2')
    sRA = get_colvals(crs,'col4')
    sDec = get_colvals(crs,'col5')
    sI = get_colvals(crs,'col7')
    sR = get_colvals(crs,'col6')
    sq = get_colvals(crs,'col11')
    sz = get_colvals(crs,'col9')
#    if i == 3:
#        sR = get_colvals(crs,'col17')
#        sI = get_colvals(crs,'col18')
    
    crms = read_file(msfile)
    msRA = get_colvals(crms,'col4')
    msDec = get_colvals(crms,'col5')
    msR = get_colvals(crms,'col6')
    msI = get_colvals(crms,'col7')
    msZ = get_colvals(crms,'col8')
    msq = get_colvals(crms,'col11')
    msz = get_colvals(crms,'col9')
    msRAX = get_colvals(crms,'col14')
    msDecX = get_colvals(crms,'col15')

    if i == 3:
        msRAX = get_colvals(crms,'col20')
        msDecX = get_colvals(crms,'col21')
        #msI = get_colvals(crms,'col18')

    gmsq2 = np.where(msq > 2.3)
    gmsq2 = gmsq2[0]
    gmsz2 = np.where((msz[gmsq2] >= zlb[i]) & (msz[gmsq2] <= zub[i]))
    gmsz2 = gmsz2[0]
    gnm = np.where(nm > 0.4)
    gnm = gnm[0]
    pInds = np.zeros(len(gnm),dtype='int')
    pInds.fill(-1)
    mInds = np.zeros(len(gnm),dtype='int')
    mInds.fill(-1)
    msInds = np.zeros(len(gnm),dtype='int')
    msInds.fill(-1)
    xInds = np.zeros(len(msRAX),dtype='int')
    xInds.fill(-1)
    for j in range(0,len(gnm)):
        cic = FindCloseSources(mRA[gnm[j]],mDec[gnm[j]],1.8,sRA,sDec,0)
        if len(cic) > 0: mInds[j] = cic[0]
        cic3 = FindCloseSources(mRA[gnm[j]],mDec[gnm[j]],1.8,pRA,pDec,0)
        if len(cic3) > 0: pInds[j] = cic3[0]
        cic2 = FindCloseSources(mRAX[gnm[j]],mDecX[gnm[j]],1.8,msRA,msDec,0)
        if len(cic2) > 0: msInds[j] = cic2[0]
    for j in range(0,len(msRAX)):
        cicx = FindCloseSources(msRAX[j],msDecX[j],1.8,xpra,xpdec,0)
        if len(cicx) > 0: xInds[j] = cicx[0]
    ns = np.where(mInds > -0.3)
    ns = ns[0]
    nsx = np.where(xInds > -0.3)
    nsx = nsx[0]

    gmxI = np.where((msI[nsx] >= Imin) & (msI[nsx] <= Ilim))
    gmxI = gmxI[0]
    gmxlum = np.where((xfncnts[xInds[nsx[gmxI]]] > limL[i]) & (xfncnts[xInds[nsx[gmxI]]] < limU[i]))
    gmxlum = gmxlum[0]
    gmsq = np.where(msq[nsx[gmxI[gmxlum]]] > 2.3)
    gmsq = gmsq[0]
    gmsz = np.where((msz[nsx[gmxI[gmxlum[gmsq]]]] >= zlb[i]) & (msz[nsx[gmxI[gmxlum[gmsq]]]] <= zub[i]))
    gmsz = gmsz[0]

    gmsq2 = np.where(msq[nsx[gmxI]] > 2.3)
    gmsq2 = gmsq2[0]
    gmsz2 = np.where((msz[nsx[gmxI[gmsq2]]] >= zlb[i]) & (msz[nsx[gmxI[gmsq2]]] <= zub[i]))
    gmsz2 = gmsz2[0]


    #print msI[gmsq2[gmsz2]]
    #print xfncnts[xInds[gmsq2[gmsz2]]]
    #print xfncnts[xInds[nsx[gmsq2[gmsz2]]]]
    #print len(xInds)-len(nsx)



    #gxI = np.where((sI[mInds[ns]] >= Imin) & (sI[mInds[ns]] <= Ilim))
    #gxI = gxI[0]
    #gxlum = np.where((xfncnts[xInds[ns[gxI]]] > limL[i]) & (xfncnts[xInds[ns[gxI]]] < limU[i]))
    #gxlum = gxlum[0]
    #gxq = np.where((sq[mInds[ns[gxI[gxlum]]]] == -1) | (sq[mInds[ns[gxI[gxlum]]]] > 2.7))
    #gxq = gxq[0]
    #gxqz = np.where((sz[mInds[ns[gxI[gxlum[gxq]]]]] >= zlb[i]) & (sz[mInds[ns[gxI[gxlum[gxq]]]]] <= zub[i]))
    #gxqz = gxqz[0]
    gq = np.where((sq[mInds[ns]] == -1) | (sq[mInds[ns]] > 2.7))
    gq = gq[0]
    gq2 = np.where(sq[mInds[ns]] > 2.7)
    gq2 = gq2[0]
    gqz = np.where((sz[mInds[ns[gq2]]] >= zlb[i]) & (sz[mInds[ns[gq2]]] <= zub[i]))
    gqz = gqz[0]
    nwl = 0.0

    raA = msRA[gmsq[gmsz]]
    decA = msDec[gmsq[gmsz]]
    zA = msz[gmsq[gmsz]]
    rahA,ramA,rasA = np.zeros(len(gmsz)),np.zeros(len(gmsz)),np.zeros(len(gmsz))
    decdA,decmA,decsA = np.zeros(len(gmsz)),np.zeros(len(gmsz)),np.zeros(len(gmsz))
    garg = np.argsort(zA)
    argcnt = 0

    gsq = np.where((sq > 2.3))
    gsq = gsq[0]
    gsz = np.where((sz[gsq] >= zlb[i]) & (sz[gsq] <= zub[i]))
    gsz = gsz[0]
    nwl2 = 0.0
    gsI = np.where((sI <= Ilim) & (sI >= Imin))
    gsI = gsI[0]
    gsI2 = np.where((sI[gsq[gsz]] <= Ilim) & (sI[gsq[gsz]] >= Imin))
    gsI2 = gsI2[0]

    gt = np.where((pI <= Ilim) & (pI >= Imin))
    gt = gt[0]
    gt2 = np.where(pI[pInds] <= Ilim)
    gt2 = gt2[0]

    FILEBG = open('/home/rumbaugh/paperstuff/compcorrcats/BG.%s.cols.6.3.11.dat'%(names[i]),'w')
    for ibg in range(0,numBGs[i]):
        bgcnt += 1
        BGareas[i] += (BGDec2arr[bgcnt]-BGDec1arr[bgcnt])*(BGRA2arr[bgcnt]-BGRA1arr[bgcnt])*m.cos(m.pi*0.5*(BGDec2arr[bgcnt]+BGDec1arr[bgcnt])/180.0)
        gbgt = np.where((pRA[gt] > BGRA1arr[bgcnt]) & (pRA[gt] < BGRA2arr[bgcnt]) & (pDec[gt] > BGDec1arr[bgcnt]) & (pDec[gt] < BGDec2arr[bgcnt]))
        gbgt = gbgt[0]
        gbgRS = np.where((pR[gt[gbgt]]-pI[gt[gbgt]]-(rsfitb[i]-rsfitm[i]*pI[gt[gbgt]]) < rsNSTD[i]*rsSTD[i]) & (pR[gt[gbgt]]-pI[gt[gbgt]]-(rsfitb[i]-rsfitm[i]*pI[gt[gbgt]]) > -rsNSTD[i]*rsSTD[i]))
        gbgRS = gbgRS[0]
        for jbg in range(0,len(gbgRS)): FILEBG.write('%f %f %f %f\n'%(pR[gt[gbgt[gbgRS[jbg]]]],pI[gt[gbgt[gbgRS[jbg]]]],pR[gt[gbgt[gbgRS[jbg]]]]-pI[gt[gbgt[gbgRS[jbg]]]],pR[gt[gbgt[gbgRS[jbg]]]]-pI[gt[gbgt[gbgRS[jbg]]]]-(rsfitb[i]-rsfitm[i]*pI[gt[gbgt[gbgRS[jbg]]]])))
        BGRSmemtot[i] += len(gbgRS)
        gbgNRS = np.where((pR[gt[gbgt]]-pI[gt[gbgt]]-(rsfitb[i]-rsfitm[i]*pI[gt[gbgt]]) < -rsNSTD[i]*rsSTD[i]))
        gbgNRS = gbgNRS[0]
        for jbg in range(0,len(gbgNRS)): FILEBG.write('%f %f %f %f\n'%(pR[gt[gbgt[gbgNRS[jbg]]]],pI[gt[gbgt[gbgNRS[jbg]]]],pR[gt[gbgt[gbgNRS[jbg]]]]-pI[gt[gbgt[gbgNRS[jbg]]]],pR[gt[gbgt[gbgNRS[jbg]]]]-pI[gt[gbgt[gbgNRS[jbg]]]]-(rsfitb[i]-rsfitm[i]*pI[gt[gbgt[gbgNRS[jbg]]]])))
        BGNRSmemtot[i] += len(gbgNRS)
    FILEBG.close()
        

    degree_symbol = unichr(176)
    indisS = np.zeros(len(gsI))
    indisS2 = np.zeros(len(gsI))
    indisS3 = np.zeros(len(gsI))
    indisX = np.zeros(len(gmxlum))

    clustot = 0.0
    clustotRS = 0.0
    clustotNRS = 0.0
    FILECL = open('/home/rumbaugh/paperstuff/compcorrcats/CL.%s.cols.6.3.11.dat'%(names[i]),'w')
    grid2masks = np.zeros((5,2))#0=RS
    if i == 0:
        #Cl1324
        inwin = np.where((pRA[gt] >= (13+(23.0+40.0/60)/60)*(360/24.0)) & (pRA[gt] <= (13+(25.0+30.0/60)/60)*(360/24.0)) & (pDec[gt] >= (30+5.0/60)) & (pDec[gt] <= 31 + 1.0/60))
        inwin = inwin[0]
        #dists = np.zeros((7,len(inwin)))
        indis = np.zeros(len(inwin))
        indis2 = np.zeros(len(inwin))
        for j in range(0,3):
            Cind = j+5
            intemp = np.zeros(len(inwin))
            intempS = np.zeros(len(indisS))
            intempX = np.zeros(len(indisX))
            for k in range(0,len(indisX)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],msRAX[nsx[gmxI[gmxlum[k]]]],msDecX[nsx[gmxI[gmxlum[k]]]])
                if diststemp < crads[Cind]*60: 
                    indisX[k] += 1
                    intempX[k] += 1
                    if ((msz[nsx[gmxI[gmxlum[k]]]] >= zlb[i]) & (msz[nsx[gmxI[gmxlum[k]]]] <= zub[i])): print '(%6.4f,%5.3f,%7.5f)'%(msz[nsx[gmxI[gmxlum[k]]]],diststemp/mpc[i],msz[nsx[gmxI[gmxlum[k]]]]-clusz[Cind])
            for k in range(0,len(indisS)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],sRA[gsI[k]],sDec[gsI[k]])
                if diststemp < crads[Cind]*60: 
                    indisS[k] += 1
                    intempS[k] += 1
                    if ((sz[gsI[k]] >= clusz[Cind]-0.01) & (sz[gsI[k]] <= clusz[Cind]+0.01)): indisS2[k] += 1
                    if ((sz[gsI[k]] >= clusz[Cind]-0.01) & (sz[gsI[k]] <= clusz[Cind]+0.01) & (clusdis[Cind] > 300)): indisS3[k] += 1
            for k in range(0,len(inwin)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],pRA[gt[inwin[k]]],pDec[gt[inwin[k]]])
                if diststemp < crads[Cind]*60: 
                    indis[k] += 1
                    intemp[k] += 1
            CLareas[i] += m.pi*crads[Cind]*crads[Cind] 
            NIR = 0
            subarea = 0.0
            R = crads[Cind]
            if clusDec[Cind] > 30.6:
                idec = clusDec[Cind]+crads[Cind]
                while NIR <= 0.1:
                    h = crads[Cind]-(idec-clusDec[Cind])
                    if h < 0: h *= -1
                    chord = 2*m.sqrt(2*h*R-h*h)
                    subarea += chord*arstep*m.cos(m.pi*idec/180.0)
                    idec -= arstep
                    NIR = lookinreg(clusRA[Cind]-0.5*chord,clusRA[Cind]+0.5*chord,idec,idec+arstep,pRA[gt[inwin]],pDec[gt[inwin]])
            else:
                idec = clusDec[Cind]-crads[Cind]
                while NIR <= 0.1:
                    h = crads[Cind]+(idec-clusDec[Cind])
                    if h < 0: h *= -1
                    chord = 2*m.sqrt(2*h*R-h*h)
                    subarea += chord*arstep
                    idec += arstep
                    NIR = lookinreg(clusRA[Cind]-0.5*chord,clusRA[Cind]+0.5*chord,idec-arstep,idec,pRA[gt[inwin]],pDec[gt[inwin]])
                if clusRA[Cind] < 201.11:
                    hy = h
                    NIR = 0
                    mcos = m.cos(m.pi*clusDec[Cind]/180.0)
                    ira = clusRA[Cind]-crads[Cind]/mcos
                    while NIR <= 0.1:
                        h = crads[Cind]/mcos+(ira-clusRA[Cind])
                        if h < 0: h *= -1
                        chord = 2*m.sqrt(2*h*R-h*h)
                        subarea += (chord-(0.5*chord-crads[Cind]/mcos+hy))*arstep*m.cos(m.pi*clusDec[Cind]/180.0)
                        ira += arstep
                        NIR = lookinreg(ira-arstep,ira,clusDec[Cind]-0.5*chord,clusDec[Cind]+0.5*chord,pRA[gt[inwin]],pDec[gt[inwin]])
            CLareas[i] -= subarea
            clustot,clustotRS,clustotNRS = LookInCluster(clustot,clustotRS,clustotNRS,i,Cind)    
        for j in range(0,len(masks1324)):
            gmask = np.where(smask[gsq[gsz[gsI2]]] == masks1324[j])
            gmask = gmask[0]
            ggRS = np.where((sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) < rsNSTD[i]*rsSTD[i]) & (sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) > -rsNSTD[i]*rsSTD[i]))
            ggNRS = np.where((sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) <= -rsNSTD[i]*rsSTD[i]))
            grid2masks[i][0],grid2masks[i][1] = len(ggRS[0]),len(ggNRS[0])
    if i == 1:
        #NEP5281
        Cind = 4
        inwin = np.where((pRA[gt] >= (18+(20.0+30.0/60)/60)*(360/24.0)) & (pRA[gt] <= (18+(22.0+30.0/60)/60)*(360/24.0)) & (pDec[gt] >= (68+22.0/60)) & (pDec[gt] <= 68 + 34.0/60))
        inwin = inwin[0]
        indis = np.zeros(len(inwin))
        indis2 = np.zeros(len(inwin))
        intemp = np.zeros(len(inwin))
        intempS = np.zeros(len(indisS))
        intempX = np.zeros(len(indisX))
        for k in range(0,len(indisX)):
            diststemp = SphDist(clusRA[Cind],clusDec[Cind],msRAX[nsx[gmxI[gmxlum[k]]]],msDecX[nsx[gmxI[gmxlum[k]]]])
            if diststemp < crads[Cind]*60: 
                indisX[k] += 1
                if ((msz[nsx[gmxI[gmxlum[k]]]] >= zlb[i]) & (msz[nsx[gmxI[gmxlum[k]]]] <= zub[i])): print '(%6.4f,%5.3f,%7.5f)'%(msz[nsx[gmxI[gmxlum[k]]]],diststemp/mpc[i],msz[nsx[gmxI[gmxlum[k]]]]-clusz[Cind])
        for k in range(0,len(indisS)):
            diststemp = SphDist(clusRA[Cind],clusDec[Cind],sRA[gsI[k]],sDec[gsI[k]])
            if diststemp < crads[Cind]*60: 
                indisS[k] += 1
                intempS[k] += 1
                if ((sz[gsI[k]] >= clusz[Cind]-0.01) & (sz[gsI[k]] <= clusz[Cind]+0.01)): indisS2[k] += 1
                if ((sz[gsI[k]] >= clusz[Cind]-0.01) & (sz[gsI[k]] <= clusz[Cind]+0.01) & (clusdis[Cind] > 300)): indisS3[k] += 1
        for k in range(0,len(inwin)):
            diststemp = SphDist(clusRA[Cind],clusDec[Cind],pRA[gt[inwin[k]]],pDec[gt[inwin[k]]])
            if diststemp < crads[Cind]*60:
                indis[k] += 1
                intemp[k] += 1
        CLareas[i] += m.pi*crads[Cind]*crads[Cind]             
        clustot,clustotRS,clustotNRS = LookInCluster(clustot,clustotRS,clustotNRS,i,4)
        for j in range(0,len(masks5281)):
            gmask = np.where(smask[gsq[gsz[gsI2]]] == masks5281[j])
            gmask = gmask[0]
            ggRS = np.where((sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) < rsNSTD[i]*rsSTD[i]) & (sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) > -rsNSTD[i]*rsSTD[i]))
            ggNRS = np.where((sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) <= -rsNSTD[i]*rsSTD[i]))
            grid2masks[i][0],grid2masks[i][1] = len(ggRS[0]),len(ggNRS[0])
    if i == 2:
        #Cl0023
        inwin = np.where((pRA[gt] >= (0+(23.0+20.0/60)/60)*(360/24.0)) & (pRA[gt] <= (0+(24.0+30.0/60)/60)*(360/24.0)) & (pDec[gt] >= (4+16.0/60)) & (pDec[gt] <= 4 + 29.0/60))
        inwin = inwin[0]
        indis = np.zeros(len(inwin))
        indis2 = np.zeros(len(inwin))
        for j in range(0,4):
            Cind = j
            intemp = np.zeros(len(inwin))
            intempS = np.zeros(len(indisS))
            intempX = np.zeros(len(indisX))
            if j != 1:
                for k in range(0,len(indisX)):
                    diststemp = SphDist(clusRA[Cind],clusDec[Cind],msRAX[nsx[gmxI[gmxlum[k]]]],msDecX[nsx[gmxI[gmxlum[k]]]])
                    if diststemp < crads[Cind]*60: indisX[k] += 1
                    if ((msz[nsx[gmxI[gmxlum[k]]]] >= zlb[i]) & (msz[nsx[gmxI[gmxlum[k]]]] <= zub[i])): print '(%6.4f,%5.3f,%7.5f)'%(msz[nsx[gmxI[gmxlum[k]]]],diststemp/mpc[i],msz[nsx[gmxI[gmxlum[k]]]]-clusz[Cind])
                for k in range(0,len(indisS)):
                    diststemp = SphDist(clusRA[Cind],clusDec[Cind],sRA[gsI[k]],sDec[gsI[k]])
                    if diststemp < crads[Cind]*60: 
                        indisS[k] += 1
                        intempS[k] += 1
                        if ((sz[gsI[k]] >= clusz[Cind]-0.01) & (sz[gsI[k]] <= clusz[Cind]+0.01)): indisS2[k] += 1
                        if ((sz[gsI[k]] >= clusz[Cind]-0.01) & (sz[gsI[k]] <= clusz[Cind]+0.01) & (clusdis[Cind] > 300)): indisS3[k] += 1
                for k in range(0,len(inwin)):
                    diststemp = SphDist(clusRA[Cind],clusDec[Cind],pRA[gt[inwin[k]]],pDec[gt[inwin[k]]])
                    if diststemp < crads[Cind]*60:
                        indis[k] += 1
                        intemp[k] += 1
                CLareas[i] += m.pi*crads[Cind]*crads[Cind]  
                clustot,clustotRS,clustotNRS = LookInCluster(clustot,clustotRS,clustotNRS,i,j)
        for j in range(0,len(masks0023)):
            gmask = np.where(smask[gsq[gsz[gsI2]]] == masks0023[j])
            gmask = gmask[0]
            ggRS = np.where((sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) < rsNSTD[i]*rsSTD[i]) & (sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) > -rsNSTD[i]*rsSTD[i]))
            ggNRS = np.where((sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) <= -rsNSTD[i]*rsSTD[i]))
            grid2masks[i][0],grid2masks[i][1] = len(ggRS[0]),len(ggNRS[0])
    if i == 3:
        #Cl1604
        inwin = np.where((pRA[gt] >= (16+(2.0+45.0/60)/60)*(360/24.0)) & (pRA[gt] <= (16+(5.0+15.0/60)/60)*(360/24.0)) & (pDec[gt] >= (43+0.0/60)) & (pDec[gt] <= 43 + 30.0/60))
        inwin = inwin[0]
        indis = np.zeros(len(inwin))
        indis2 = np.zeros(len(inwin))
        for j in range(0,7):
            Cind = j+10
            intemp = np.zeros(len(inwin))
            intempS = np.zeros(len(indisS))
            intempX = np.zeros(len(indisX))
            for k in range(0,len(indisX)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],msRAX[nsx[gmxI[gmxlum[k]]]],msDecX[nsx[gmxI[gmxlum[k]]]])
                if diststemp < crads[Cind]*60: indisX[k] += 1
                if ((msz[nsx[gmxI[gmxlum[k]]]] >= zlb[i]) & (msz[nsx[gmxI[gmxlum[k]]]] <= zub[i])): print '(%6.4f,%5.3f,%7.5f)'%(msz[nsx[gmxI[gmxlum[k]]]],diststemp/mpc[i],msz[nsx[gmxI[gmxlum[k]]]]-clusz[Cind])
            for k in range(0,len(indisS)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],sRA[gsI[k]],sDec[gsI[k]])
                if diststemp < crads[Cind]*60: 
                    indisS[k] += 1
                    intempS[k] += 1
                    if ((sz[gsI[k]] >= clusz[Cind]-0.01) & (sz[gsI[k]] <= clusz[Cind]+0.01)): indisS2[k] += 1
                    if ((sz[gsI[k]] >= clusz[Cind]-0.01) & (sz[gsI[k]] <= clusz[Cind]+0.01) & (clusdis[Cind] > 300)): indisS3[k] += 1
            for k in range(0,len(inwin)):
                diststemp = SphDist(clusRA[Cind],clusDec[Cind],pRA[gt[inwin[k]]],pDec[gt[inwin[k]]])
                if diststemp < crads[Cind]*60:
                    indis[k] += 1
                    intemp[k] += 1
                    
            CLareas[i] += m.pi*crads[Cind]*crads[Cind]  
            clustot,clustotRS,clustotNRS = LookInCluster(clustot,clustotRS,clustotNRS,i,Cind)
        dtmp = SphDist(clusRA[11],clusDec[11],clusRA[12],clusDec[12])/60.0
        if cradmult > 0.51: CLareas[i] -= 0.5*crads[11]*crads[11]*(m.acos((crads[11]*crads[11]+dtmp*dtmp-crads[12]*crads[12])/(2*dtmp*crads[11]))-m.sqrt(1-((crads[11]*crads[11]+dtmp*dtmp-crads[12]*crads[12])/(2*dtmp*crads[11]))**2))+0.5*crads[12]*crads[12]*(m.acos((crads[12]*crads[12]+dtmp*dtmp-crads[11]*crads[11])/(2*dtmp*crads[12]))-m.sqrt(1-((crads[12]*crads[12]+dtmp*dtmp-crads[11]*crads[11])/(2*dtmp*crads[12]))**2))
        ggRS = np.where((sR[gsq[gsz[gsI2]]]-sI[gsq[gsz[gsI2]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2]]]) < rsNSTD[i]*rsSTD[i]) & (sR[gsq[gsz[gsI2]]]-sI[gsq[gsz[gsI2]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2]]]) > -rsNSTD[i]*rsSTD[i]))
        ggNRS = np.where((sR[gsq[gsz[gsI2]]]-sI[gsq[gsz[gsI2]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2]]]) <= -rsNSTD[i]*rsSTD[i]))
        grid2masks[i][0],grid2masks[i][1] = len(ggRS[0]),len(ggNRS[0])
    if i == 4:
        #RXJ1757
        Cind = len(clusRA)-1
        inwin = np.where((pRA[gt] >= (17+(56.0+40.0/60)/60)*(360/24.0)) & (pRA[gt] <= (17+(58.0+0.0/60)/60)*(360/24.0)) & (pDec[gt] >= (66+27.0/60)) & (pDec[gt] <= 66 + 36.0/60))
        inwin = inwin[0]
        indis = np.zeros(len(inwin))
        indis2 = np.zeros(len(inwin))
        intemp = np.zeros(len(inwin))
        intempS = np.zeros(len(indisS))
        intempX = np.zeros(len(indisX))
        for k in range(0,len(indisX)):
            diststemp = SphDist(clusRA[Cind],clusDec[Cind],msRAX[nsx[gmxI[gmxlum[k]]]],msDecX[nsx[gmxI[gmxlum[k]]]])
            if diststemp < crads[Cind]*60: indisX[k] += 1
            if ((msz[nsx[gmxI[gmxlum[k]]]] >= zlb[i]) & (msz[nsx[gmxI[gmxlum[k]]]] <= zub[i])): print '(%6.4f,%5.3f,%7.5f)'%(msz[nsx[gmxI[gmxlum[k]]]],diststemp/mpc[i],msz[nsx[gmxI[gmxlum[k]]]]-clusz[Cind])
        for k in range(0,len(indisS)):
            diststemp = SphDist(clusRA[Cind],clusDec[Cind],sRA[gsI[k]],sDec[gsI[k]])
            if diststemp < crads[Cind]*60: 
                indisS[k] += 1
                intempS[k] += 1
                if ((sz[gsI[k]] >= clusz[Cind]-0.01) & (sz[gsI[k]] <= clusz[Cind]+0.01)): indisS2[k] += 1
                if ((sz[gsI[k]] >= clusz[Cind]-0.01) & (sz[gsI[k]] <= clusz[Cind]+0.01) & (clusdis[Cind] > 300)): indisS3[k] += 1
        for k in range(0,len(inwin)):
            diststemp = SphDist(clusRA[Cind],clusDec[Cind],pRA[gt[inwin[k]]],pDec[gt[inwin[k]]])
            if diststemp < crads[Cind]*60:
                indis[k] += 1
                intemp[k] += 1
        CLareas[i] += m.pi*crads[Cind]*crads[Cind]          
        clustot,clustotRS,clustotNRS = LookInCluster(clustot,clustotRS,clustotNRS,i,Cind)
        for j in range(0,len(masks1757)):
            gmask = np.where(smask[gsq[gsz[gsI2]]] == masks1757[j])
            gmask = gmask[0]
            ggRS = np.where((sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) < rsNSTD[i]*rsSTD[i]) & (sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) > -rsNSTD[i]*rsSTD[i]))
            ggNRS = np.where((sR[gsq[gsz[gsI2[gmask]]]]-sI[gsq[gsz[gsI2[gmask]]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2[gmask]]]]) <= -rsNSTD[i]*rsSTD[i]))
            grid2masks[i][0],grid2masks[i][1] = len(ggRS[0]),len(ggNRS[0])
    inran = np.where(indis > 0.1)
    inran = inran[0]
    inranS = np.where(indisS > 0.1)
    inranS = inranS[0]
    inranS3 = np.where(indisS3 > 0.1)
    inranS3 = inranS3[0]
    inranX = np.where(indisX > 0.1)
    inranX = inranX[0]
    pylab.scatter(pRA[gt],pDec[gt],s=0.2,color='blue')
    pylab.scatter(sRA[gsq[gsz[gsI2]]],sDec[gsq[gsz[gsI2]]],s=5,color='red')
    for ibg in range(0,numBGs[i]): 
        yplottemp = np.array([BGDec1arr[bgcnt2],BGDec2arr[bgcnt2],BGDec2arr[bgcnt2],BGDec1arr[bgcnt2],BGDec1arr[bgcnt2]])
        xplottemp = np.array([BGRA1arr[bgcnt2],BGRA1arr[bgcnt2],BGRA2arr[bgcnt2],BGRA2arr[bgcnt2],BGRA1arr[bgcnt2]])
        pylab.plot(xplottemp,yplottemp,color='black')
        bgcnt2 += 1
    pylab.savefig('/home/rumbaugh/spattest.%s.5.31.11.png'%(names[i]))

    gsqtt = np.where(sq[gsI[inranS]] > 2.3)
    gsqtt = gsqtt[0]

    onRS = np.where((sR[gsq[gsz[gsI2]]]-sI[gsq[gsz[gsI2]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2]]]) < rsNSTD[i]*rsSTD[i]) & (sR[gsq[gsz[gsI2]]]-sI[gsq[gsz[gsI2]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2]]]) > -rsNSTD[i]*rsSTD[i]))
    notonRS = np.where((sR[gsq[gsz[gsI2]]]-sI[gsq[gsz[gsI2]]]-(rsfitb[i]-rsfitm[i]*sI[gsq[gsz[gsI2]]]) < -rsNSTD[i]*rsSTD[i]))
    onRS_S = np.where((sR[gsI[inranS[gsqtt]]]-sI[gsI[inranS[gsqtt]]]-(rsfitb[i]-rsfitm[i]*sI[gsI[inranS[gsqtt]]]) < rsNSTD[i]*rsSTD[i]) & (sR[gsI[inranS[gsqtt]]]-sI[gsI[inranS[gsqtt]]]-(rsfitb[i]-rsfitm[i]*sI[gsI[inranS[gsqtt]]]) > -rsNSTD[i]*rsSTD[i]))
    notonRS_S = np.where((sR[gsI[inranS[gsqtt]]]-sI[gsI[inranS[gsqtt]]]-(rsfitb[i]-rsfitm[i]*sI[gsI[inranS[gsqtt]]]) < -rsNSTD[i]*rsSTD[i]))

    inran2 = np.where(indis2 > 0.1)
    inran2 = inran2[0]
    inranS2 = np.where(indisS2 > 0.1)
    inranS2 = inranS2[0]
    colmaggrid = np.zeros((3,4))
    colmaggridS = np.zeros((3,4,2))
    pylab.xlim(19.5,23.5)
    pylab.ylim(-0.5,2.0)
    gCtmp = np.where((pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]]-(rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]) <= -rsNSTD[i]*rsSTD[i]))
    CLNRSmemtot[i] = len(gCtmp[0])
    gCtmp = gCtmp[0]
    for jbg in range(0,len(gCtmp)): FILECL.write('%f %f %f %f\n'%(pR[gt[inwin[inran[gCtmp[jbg]]]]],pI[gt[inwin[inran[gCtmp[jbg]]]]],pR[gt[inwin[inran[gCtmp[jbg]]]]]-pI[gt[inwin[inran[gCtmp[jbg]]]]],pR[gt[inwin[inran[gCtmp[jbg]]]]]-pI[gt[inwin[inran[gCtmp[jbg]]]]]-(rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran[gCtmp[jbg]]]]])))
    for iC in range(0,3):
        if iC == 0: gCtmp = np.where((pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]]-(rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]) <= rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]]-(rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]) >= -rsNSTD[i]*rsSTD[i]))
        if iC == 1: gCtmp = np.where((pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]]-(rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]) <= -rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] > botRS[i]-0.5))
        if iC == 2: gCtmp = np.where((pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] <= botRS[i]-0.5) & (pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] > botRS[i]-1.0))
        print len(gCtmp[0])
        if len(gCtmp) > 0: 
            gCtmp = gCtmp[0]
            if iC == 0: 
                CLRSmemtot[i] += len(gCtmp)
                for jbg in range(0,len(gCtmp)): FILECL.write('%f %f %f %f\n'%(pR[gt[inwin[inran[gCtmp[jbg]]]]],pI[gt[inwin[inran[gCtmp[jbg]]]]],pR[gt[inwin[inran[gCtmp[jbg]]]]]-pI[gt[inwin[inran[gCtmp[jbg]]]]],pR[gt[inwin[inran[gCtmp[jbg]]]]]-pI[gt[inwin[inran[gCtmp[jbg]]]]]-(rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran[gCtmp[jbg]]]]])))
            for iI in range(0,4):
                gItmp = np.where((pI[gt[inwin[inran[gCtmp]]]] > 19.5+iI) & (pI[gt[inwin[inran[gCtmp]]]] <= 19.5+iI+1))
                if len(gItmp) > 0: 
                    gItmp = gItmp[0]
                    colmaggrid[iC][iI] = len(gItmp)
                    #print "Tot. phot. in Col reg. %i, Mag reg. %i: %i"%(iC,iI,len(gItmp))
                    if ((iI == 3) & (iC == 0)): 
                        pylab.scatter(pI[gt[inwin[inran[gCtmp[gItmp]]]]],pR[gt[inwin[inran[gCtmp[gItmp]]]]]-pI[gt[inwin[inran[gCtmp[gItmp]]]]],s=4,color='black',label='All Phot. Targets')
                    else:
                        if len(gItmp) > 0: pylab.scatter(pI[gt[inwin[inran[gCtmp[gItmp]]]]],pR[gt[inwin[inran[gCtmp[gItmp]]]]]-pI[gt[inwin[inran[gCtmp[gItmp]]]]],s=4,color='black',label='_nolegend_')
                #else:
                    #print "Tot. phot. in Col reg. %i, Mag regs: 0"%(iC,iI)
        #else:
           # print "Tot. phot. in Col reg. %i, all Mag regs: 0"%(iC)
        if iC == 0: gCtmp = np.where((sR[gsI[inranS]]-sI[gsI[inranS]]-(rsfitb[i]-rsfitm[i]*sI[gsI[inranS]]) <= rsNSTD[i]*rsSTD[i]) & (sR[gsI[inranS]]-sI[gsI[inranS]]-(rsfitb[i]-rsfitm[i]*sI[gsI[inranS]]) >= -rsNSTD[i]*rsSTD[i]))
        if iC == 1: gCtmp = np.where((sR[gsI[inranS]]-sI[gsI[inranS]]-(rsfitb[i]-rsfitm[i]*sI[gsI[inranS]]) <= -rsNSTD[i]*rsSTD[i]) & (sR[gsI[inranS]]-sI[gsI[inranS]] >= botRS[i]-0.5))
        if iC == 2: gCtmp = np.where((sR[gsI[inranS]]-sI[gsI[inranS]] <= botRS[i]-0.5) & (sR[gsI[inranS]]-sI[gsI[inranS]] >= botRS[i]-1.0))
        print len(gCtmp[0])
        if len(gCtmp) > 0: 
            gCtmp = gCtmp[0]
            for iI in range(0,4):
                gItmp = np.where((sI[gsI[inranS[gCtmp]]] > 19.5+iI) & (sI[gsI[inranS[gCtmp]]] <= 19.5+iI+1))
                if len(gItmp) > 0: 
                    gItmp = gItmp[0]
                    colmaggridS[iC][iI][0] = len(gItmp)
                    #print "Tot. spec. in Col reg. %i, Mag reg. %i: %i"%(iC,iI,len(gItmp))
                    if ((iI == 3) & (iC == 0)): 
                        pylab.scatter(sI[gsI[inranS[gCtmp[gItmp]]]],sR[gsI[inranS[gCtmp[gItmp]]]]-sI[gsI[inranS[gCtmp[gItmp]]]],s=4.5,color=html_teal,label='All Spec. Targets')
                    else:
                        if len(gItmp) > 0: pylab.scatter(sI[gsI[inranS[gCtmp[gItmp]]]],sR[gsI[inranS[gCtmp[gItmp]]]]-sI[gsI[inranS[gCtmp[gItmp]]]],s=4.5,color=html_teal,label='_nolegend_')
                #else:
                    #print "Tot. spec. in Col reg. %i, Mag regs: 0"%(iC,iI)
        #else:
            #print "Tot. spec. in Col reg. %i, all Mag regs: 0"%(iC)
        if iC == 0: gCtmp = np.where((sR[gsI[inranS2]]-sI[gsI[inranS2]]-(rsfitb[i]-rsfitm[i]*sI[gsI[inranS2]]) <= rsNSTD[i]*rsSTD[i]) & (sR[gsI[inranS2]]-sI[gsI[inranS2]]-(rsfitb[i]-rsfitm[i]*sI[gsI[inranS2]]) >= -rsNSTD[i]*rsSTD[i]))
        if iC == 1: gCtmp = np.where((sR[gsI[inranS2]]-sI[gsI[inranS2]]-(rsfitb[i]-rsfitm[i]*sI[gsI[inranS2]]) <= -rsNSTD[i]*rsSTD[i]) & (sR[gsI[inranS2]]-sI[gsI[inranS2]] >= botRS[i]-0.5))
        if iC == 2: gCtmp = np.where((sR[gsI[inranS2]]-sI[gsI[inranS2]] <= botRS[i]-0.5) & (sR[gsI[inranS2]]-sI[gsI[inranS2]] >= botRS[i]-1.0))
        print len(gCtmp[0])
        if len(gCtmp) > 0: 
            gCtmp = gCtmp[0]
            for iI in range(0,4):
                gItmp = np.where((sI[gsI[inranS2[gCtmp]]] > 19.5+iI) & (sI[gsI[inranS2[gCtmp]]] <= 19.5+iI+1))
                if len(gItmp) > 0: 
                    gItmp = gItmp[0]
                    gsqtmp = np.where(sq[gsI[inranS2[gCtmp[gItmp]]]] > 2.3)
                    if len(gsqtmp) > 0: colmaggridS[iC][iI][1] = len(gsqtmp[0])
                    #print "Tot. good spec. in Col reg. %i, Mag reg. %i: %i"%(iC,iI,len(gsqtmp[0]))
                    if ((iI == 3) & (iC == 0) & (len(gsqtmp[0]) > 0)): 
                        pylab.scatter(sI[gsI[inranS2[gCtmp[gItmp[gsqtmp[0]]]]]],sR[gsI[inranS2[gCtmp[gItmp[gsqtmp[0]]]]]]-sI[gsI[inranS2[gCtmp[gItmp[gsqtmp[0]]]]]],s=5,color='red',label='In cluster')
                    #else:
                        if len(gsqtmp[0]) > 0: pylab.scatter(sI[gsI[inranS2[gCtmp[gItmp[gsqtmp[0]]]]]],sR[gsI[inranS2[gCtmp[gItmp[gsqtmp[0]]]]]]-sI[gsI[inranS2[gCtmp[gItmp[gsqtmp[0]]]]]],s=5,color='red',label='_nolegend_')
                #else:
                    #print "Tot. good spec. in Col reg. %i, Mag regs: 0"%(iC,iI)
                if colmaggridS[iC][iI][0] > 0: convgrid[iC][iI][i] = colmaggridS[iC][iI][1]*1.0/colmaggridS[iC][iI][0]
                totmemgrid[iC][iI][i] = convgrid[iC][iI][i]*colmaggrid[iC][iI]
                #print "Conversion for Col reg. %i, Mag reg. %i: %7.5f"%(iC,iI,convgrid[iC][iI][i])
                #print "Tot. mem. for Col reg. %i, Mag reg. %i: %.1f"%(iC,iI,totmemgrid[iC][iI][i])
        #else:
            #print "Tot. good spec. in Col reg. %i, all Mag regs: 0"%(iC)
            #print "Conversion for Col reg. %i, all Mag regs: 0"%(iC)
            #print "Tot. mem. for Col reg. %i, all Mag regs: 0"%(iC)
    #CLRSmemtot[i] = np.sum(colmaggrid[0,:])
    #CLNRSmemtot[i] = np.sum(colmaggrid)-CLRSmemtot[i]
    leg = pylab.legend()
    for t in leg.get_texts():
        t.set_fontsize('small')
    xptmp = np.array([18,20,30])
    yptmp = rsfitb[i]-rsfitm[i]*xptmp-rsNSTD[i]*rsSTD[i]
    yptmp2 = rsfitb[i]-rsfitm[i]*xptmp+rsNSTD[i]*rsSTD[i]
    pylab.plot(xptmp,yptmp,linestyle='dashed',color='black')
    pylab.plot(xptmp,yptmp2,linestyle='dashed',color='black')
    pylab.ylabel("r'-i'")
    pylab.xlabel("i' magnitude")
    pylab.title(names[i])
    pylab.savefig('/home/rumbaugh/paperstuff/CMD.completeness.%s.r200.5.30.11.png'%(names[i]))
    pylab.close('all')

    gmsqIR = np.where(msq[nsx[gmxI[gmxlum[inranX]]]] > 2.3)
    gmsqIR = gmsqIR[0]
    gmszIR = np.where((msz[nsx[gmxI[gmxlum[inranX[gmsqIR]]]]] >= zlb[i]) & (msz[nsx[gmxI[gmxlum[inranX[gmsqIR]]]]] <= zub[i]))
    gmszIR = gmszIR[0]

    gsgd = np.where(sq[gsI[inranS]] > 2.3)
    gsgd = gsgd[0]
    gsok = np.where((sq[gsI[inranS]] > 0.3) & (sq[gsI[inranS]] < 2.3))
    gsok = gsok[0]
    gsst = np.where(sq[gsI[inranS]] < -0.3)
    gsst = gsst[0]
    gsz = np.where((sz[gsI[inranS[gsgd]]] <= zub[i]) & (sz[gsI[inranS[gsgd]]] >= zlb[i]))
    pylab.xlim(19,25)
    pylab.ylim(-0.5,2.0)
    if i == 3:
        pylab.ylim(-0.5,2.5)
    pylab.scatter(pI[gt[inwin[inran]]],pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]],s=6,color='blue')
    pylab.scatter(sI[gsI[inranS[gsst]]],sR[gsI[inranS[gsst]]]-sI[gsI[inranS[gsst]]],s=6.5,color=html_brwn)
    if len(gsok) > 0: pylab.scatter(sI[gsI[inranS[gsok]]],sR[gsI[inranS[gsok]]]-sI[gsI[inranS[gsok]]],s=6.5,color=html_teal)
    pylab.scatter(sI[gsI[inranS[gsgd]]],sR[gsI[inranS[gsgd]]]-sI[gsI[inranS[gsgd]]],s=7,color=html_orng)
    pylab.scatter(sI[gsI[inranS[gsgd[gsz]]]],sR[gsI[inranS[gsgd[gsz]]]]-sI[gsI[inranS[gsgd[gsz]]]],s=8,color='red')
    leg = pylab.legend(('No Spec','Q=-1','Q=1,2','Q=3,4','Q=3,4, in clus'),loc=4,markerscale=0.8,labelspacing=0.3)
    for t in leg.get_texts():
        t.set_fontsize('small')
    pylab.plot(rsfX,rsfY1,linestyle='dashed',color='black')
    pylab.plot(rsfX,rsfY2,linestyle='dashed',color='black')
    savname = '/home/rumbaugh/paperstuff/CMD.%s.completeness.r200.5.30.11.png'%(names[i])
    #pylab.savefig(savname)
    pylab.close('all')
    gszRS = np.where((sR[gsI[inranS[gsgd[gsz]]]]-sI[gsI[inranS[gsgd[gsz]]]] <= rsfitb[i]-rsfitm[i]*sI[gsI[inranS[gsgd[gsz]]]]+rsNSTD[i]*rsSTD[i]) & (sR[gsI[inranS[gsgd[gsz]]]]-sI[gsI[inranS[gsgd[gsz]]]] >= rsfitb[i]-rsfitm[i]*sI[gsI[inranS[gsgd[gsz]]]]-(0+rsNSTD[i])*rsSTD[i]))
    gszRS = gszRS[0]
    gsallRS = np.where((sR[gsI[inranS]]-sI[gsI[inranS]] <= rsfitb[i]-rsfitm[i]*sI[gsI[inranS]]+rsNSTD[i]*rsSTD[i]) & (sR[gsI[inranS]]-sI[gsI[inranS]] >= rsfitb[i]-rsfitm[i]*sI[gsI[inranS]]-(0+rsNSTD[i])*rsSTD[i]))
    gsallRS = gsallRS[0]
    gszNRS0 = np.where((sR[gsI[inranS[gsgd[gsz]]]]-sI[gsI[inranS[gsgd[gsz]]]] < rsfitb[i]-rsfitm[i]*sI[gsI[inranS[gsgd[gsz]]]]-rsNSTD[i]*rsSTD[i]) & (sR[gsI[inranS[gsgd[gsz]]]]-sI[gsI[inranS[gsgd[gsz]]]] >= rsfitb[i]-rsfitm[i]*sI[gsI[inranS[gsgd[gsz]]]]-(1+rsNSTD[i])*rsSTD[i]))
    gszNRS0 = gszNRS0[0]
    gsallNRS0 = np.where((sR[gsI[inranS]]-sI[gsI[inranS]] < rsfitb[i]-rsfitm[i]*sI[gsI[inranS]]-rsNSTD[i]*rsSTD[i]) & (sR[gsI[inranS]]-sI[gsI[inranS]] >= rsfitb[i]-rsfitm[i]*sI[gsI[inranS]]-(1+rsNSTD[i])*rsSTD[i]))
    gsallNRS0 = gsallNRS0[0]
    conversionRS = (len(gszRS)+len(gszNRS0))/(1.0*len(gsallRS)+len(gsallNRS0))
    gszNRS1 = np.where((sR[gsI[inranS[gsgd[gsz]]]]-sI[gsI[inranS[gsgd[gsz]]]] >= bounds[i]) & (sR[gsI[inranS[gsgd[gsz]]]]-sI[gsI[inranS[gsgd[gsz]]]] < rsfitb[i]-rsfitm[i]*sI[gsI[inranS[gsgd[gsz]]]]-(1+rsNSTD[i])*rsSTD[i]))
    gszNRS1 = gszNRS1[0]
    gsallNRS1 = np.where((sR[gsI[inranS]]-sI[gsI[inranS]] >= bounds[i]) & (sR[gsI[inranS]]-sI[gsI[inranS]] < rsfitb[i]-rsfitm[i]*sI[gsI[inranS]]-(1+rsNSTD[i])*rsSTD[i]))
    gsallNRS1 = gsallNRS1[0]
    conversionNRS1 = len(gszNRS1)/(1.0*len(gsallNRS1))
    gszNRS2 = np.where((sR[gsI[inranS[gsgd[gsz]]]]-sI[gsI[inranS[gsgd[gsz]]]] < bounds[i]))
    gszNRS2 = gszNRS2[0]
    gsallNRS2 = np.where((sR[gsI[inranS]]-sI[gsI[inranS]] < bounds[i]))
    gsallNRS2 = gsallNRS2[0]
    conversionNRS2 = len(gszNRS2)/(1.0*len(gsallNRS2))


    gpallRS = np.where((pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]+rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] >= rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]-(0+rsNSTD[i])*rsSTD[i]))
    gpallRS = gpallRS[0]
    gpallNRS0 = np.where((pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] < rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]-rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] >= rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]-(1+rsNSTD[i])*rsSTD[i]))
    gpallNRS0 = gpallNRS0[0]
    gpallNRS1 = np.where((pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] >= bounds[i]) & (pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] < rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]-(1+rsNSTD[i])*rsSTD[i]))
    gpallNRS1 = gpallNRS1[0]
    gpallNRS1A = np.where((pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] >= rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]-(2*rsNSTD[i])*rsSTD[i]) & (pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] < rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]-(1+rsNSTD[i])*rsSTD[i]))
    gpallNRS1A = gpallNRS1A[0]
    gpallNRS1B = np.where((pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] >= bounds[i]) & (pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] < rsfitb[i]-rsfitm[i]*pI[gt[inwin[inran]]]-(2*rsNSTD[i])*rsSTD[i]))
    gpallNRS1B = gpallNRS1B[0]
    gpallNRS2 = np.where((pR[gt[inwin[inran]]]-pI[gt[inwin[inran]]] < bounds[i]))
    gpallNRS2 = gpallNRS2[0]


    totalRS = conversionRS*len(gpallRS)
    totalNRS0 = conversionRS*len(gpallNRS0)
    totalNRS1 = conversionNRS1*len(gpallNRS1)
    totalNRS2 = conversionNRS2*len(gpallNRS2)
    totalNRS = totalNRS0+totalNRS1+totalNRS2
    totalNRS1A = conversionNRS1*len(gpallNRS1A)
    totalNRS1B = conversionNRS1*len(gpallNRS1B)

    AGNconv = len(gmsz)/(1.0*len(gmsq))
    #totalAGN = AGNconv*len(gmxlum)
    totalAGN = AGNconv*(len(inranX)-len(gmszIR))+len(gmszIR)

    totRS = np.sum(totmemgrid[0,:,i])
    totNRS = np.sum(totmemgrid[1:,:,i])

    totRSstat = CLRSmemtot[i]-BGRSmemtot[i]*CLareas[i]/BGareas[i]
    totNRSstat = CLNRSmemtot[i]-BGNRSmemtot[i]*CLareas[i]/BGareas[i]
    totRSstaterr = m.sqrt(CLRSmemtot[i]+BGRSmemtot[i]*CLareas[i]*CLareas[i]/BGareas[i]/BGareas[i])
    totNRSstaterr = m.sqrt(CLNRSmemtot[i]+BGNRSmemtot[i]*CLareas[i]*CLareas[i]/BGareas[i]/BGareas[i])
    NRSfracerr = m.sqrt((totRSstat+totNRSstat)**(-4)*(totNRSstaterr**2*(totNRSstat**2+(totNRSstat+totRSstat)**2)+(totRSstaterr**2*totNRSstat**2)))
    FILECL.close()
    print '\nField - %7s:'%(names[i])
    print "i' range: (%f,%f)"%(Imin,Ilim)
    print 'Counts range: (%f,%f)'%(limL[i],limU[i])
    print 'All sources within %3.1f Mpc: %i'%(cradmult,len(inranS3))
    print 'Estimated total RS members:  %.1f +/- %.1f'%(totRSstat,totRSstaterr)
    print 'Estimated total NRS members: %.1f +/- %.1f'%(totNRSstat,totNRSstaterr)
    print 'Galaxy Density, (BG,CL): (%f,%f)+/-(%.2f,%.2f)'%((BGRSmemtot[i]+BGNRSmemtot[i])/BGareas[i]/3600,(CLRSmemtot[i]+CLNRSmemtot[i])/CLareas[i]/3600,m.sqrt(BGRSmemtot[i]+BGNRSmemtot[i])/BGareas[i]/3600,m.sqrt(CLRSmemtot[i]+CLNRSmemtot[i])/CLareas[i]/3600)
    print 'Red Galaxy Density, (BG,CL): (%f,%f)+/-(%.2f,%.2f)'%((BGRSmemtot[i])/BGareas[i]/3600,(CLRSmemtot[i])/CLareas[i]/3600,m.sqrt(BGRSmemtot[i])/BGareas[i]/3600,m.sqrt(CLRSmemtot[i])/CLareas[i]/3600)
    print 'Blue Galaxy Density, (BG,CL): (%f,%f)+/-(%.2f,%.2f)'%((BGNRSmemtot[i])/BGareas[i]/3600,(CLNRSmemtot[i])/CLareas[i]/3600,m.sqrt(BGNRSmemtot[i])/BGareas[i]/3600,m.sqrt(CLNRSmemtot[i])/CLareas[i]/3600)
#    print 'Estimated total RS members:  %.1f'%(totRS)
#    print 'Estimated total NRS members: %.1f'%(totNRS)
#    print 'Estimated total RS members:  %i'%(int(totalRS))
#    print 'Estimated total NRS members: %i'%(int(totalNRS))
    print 'Estimated NRS fraction (2masks): %5.3f +/- %5.3f'%(grid2masks[i][1]*1.0/(grid2masks[i][1]+grid2masks[i][0]),m.sqrt(grid2masks[i][1]*1.0/(grid2masks[i][1]+grid2masks[i][0])**2 + grid2masks[i][1]*grid2masks[i][1]*1.0/(grid2masks[i][1]+grid2masks[i][0])**3))
    print 'Estimated NRS fraction (eff): %5.3f'%(totalNRS/(totalRS+totalNRS))
#    print 'Estimated blue fraction: %5.3f'%((totalNRS1B+totalNRS2)/(totalRS+totalNRS))
#    print 'Estimated NRS fraction: %5.3f'%(totNRS/(1.0*totRS+totNRS))
    print 'Estimated NRS fraction: %5.3f +/- %.3f'%(totNRSstat/(1.0*totRSstat+totNRSstat),NRSfracerr)
    print 'Measured NRS fraction(long way):  %5.3f'%((len(gszNRS0)+len(gszNRS1)+len(gszNRS2))*1.0/(len(gszRS)+len(gszNRS0)+len(gszNRS1)+len(gszNRS2)))
    print 'Measured NRS fraction(all): %5.3f +\- %5.3f'%((len(notonRS[0])*1.0/(len(notonRS[0])+len(onRS[0]))),m.sqrt(len(notonRS[0])*1.0/(len(notonRS[0])+len(onRS[0]))**2+len(notonRS[0])*len(notonRS[0])*1.0/(len(notonRS[0])+len(onRS[0]))**3))
    print 'Measured NRS fraction(r200): %5.3f'%((len(notonRS_S[0])*1.0/(len(notonRS_S[0])+len(onRS_S[0]))))
#    print 'Conversions: %7.5f  %7.5f  %7.5f'%(conversionRS,conversionNRS1,conversionNRS2)
    print 'AGN conversion: %7.5f'%(AGNconv)
    print 'Estimated Total AGN: %.1f'%((totalAGN))
    #print 'Estimated AGN fraction: %7.5f'%(totalAGN/(totalRS+totalNRS))
    print 'Estimated AGN fraction: %7.5f'%(totalAGN/(1.0*(totRS+totNRS)))
    print '(Tot. AGN,(In Range),Tot. good Xray sources): (%f,%f,%f)'%(len(gmsz),len(gmszIR),len(gmsq))
    print 'Total eligible Xray Sources: %5.1f\n'%(len(gmxlum))
BGRSdens = np.sum(BGRSmemtot)/np.sum(BGareas)
BGNRSdens = np.sum(BGNRSmemtot)/np.sum(BGareas)
BGRSdenserr = m.sqrt(np.sum(BGRSmemtot))/np.sum(BGareas)
BGNRSdenserr = m.sqrt(np.sum(BGNRSmemtot))/np.sum(BGareas)
print "Using combined BGs"
for i in range(0,5):
    totRSstat = CLRSmemtot[i]-BGRSdens*CLareas[i]
    totNRSstat = CLNRSmemtot[i]-BGNRSdens*CLareas[i]
    totRSstaterr = m.sqrt(CLRSmemtot[i]+BGRSdenserr*BGRSdenserr*CLareas[i]*CLareas[i])
    totNRSstaterr = m.sqrt(CLNRSmemtot[i]+BGNRSdenserr*BGNRSdenserr*CLareas[i]*CLareas[i])
    print '%s - Estimated Total (RS,NRS) - (%.1f,%.1f)+/-(%.1f,%.1f)'%(names[i],totRSstat,totNRSstat,totRSstaterr,totNRSstaterr)
    print '%s - Estimated NRS fraction - %f'%(names[i],(totNRSstat/(totNRSstat+totRSstat)))
