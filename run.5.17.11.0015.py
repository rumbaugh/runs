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

def switch5(arr5):
    arr5[0],arr5[1],arr5[2],arr5[3],arr5[4] = arr5[1],arr5[3],arr5[0],arr5[4],arr5[2]
    return arr5

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

rsNSTD = np.array([3.0,3.0,3.0,2.0,3.0])

zlb = np.array([0.655,0.808,0.82,0.84,0.68])
zub = np.array([0.785,0.828,0.856,0.96,0.705])

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
crads = r200*0.7*mpc/60

crbnds = read_file('/home/rumbaugh/CMD.regions.dat')
bounds = get_colvals(crbnds,'col2')

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


    print msI[gmsq2[gmsz2]]
    print xfncnts[xInds[gmsq2[gmsz2]]]
    print xfncnts[xInds[nsx[gmsq2[gmsz2]]]]
    print len(xInds)-len(nsx)



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

    gt = np.where((pI <= Ilim) & (pI >= Imin))
    gt = gt[0]
    gt2 = np.where(pI[pInds] <= Ilim)
    gt2 = gt2[0]

    degree_symbol = unichr(176)
    indisS = np.zeros(len(gsI))
    indisX = np.zeros(len(gmxlum))

    clustot = 0.0
    clustotRS = 0.0
    clustotNRS = 0.0
    if i == 0:
        #Cl1324
        inwin = np.where((pRA[gt] >= (13+(23.0+40.0/60)/60)*(360/24.0)) & (pRA[gt] <= (13+(25.0+30.0/60)/60)*(360/24.0)) & (pDec[gt] >= (30+5.0/60)) & (pDec[gt] <= 31 + 1.0/60))
        inwin = inwin[0]
        #dists = np.zeros((7,len(inwin)))
        indis = np.zeros(len(inwin))
        for j in range(0,5):
            intemp = np.zeros(len(inwin))
            intempS = np.zeros(len(indisS))
            intempX = np.zeros(len(indisX))
            for k in range(0,len(indisX)):
                diststemp = SphDist(clusRA[j+5],clusDec[j+5],msRAX[nsx[gmxI[gmxlum[k]]]],msDecX[nsx[gmxI[gmxlum[k]]]])
                if diststemp < crads[j+5]*60: 
                    indisX[k] += 1
                    intempX[k] += 17
            for k in range(0,len(indisS)):
                diststemp = SphDist(clusRA[j+5],clusDec[j+5],sRA[gsI[k]],sDec[gsI[k]])
                if diststemp < crads[j+5]*60: 
                    indisS[k] += 1
                    intempS[k] += 1
            for k in range(0,len(inwin)):
                diststemp = SphDist(clusRA[j+5],clusDec[j+5],pRA[gt[inwin[k]]],pDec[gt[inwin[k]]])
                if diststemp < crads[j+5]*60: 
                    indis[k] += 1
                    intemp[k] += 1
            gicStemp = np.where(intempS > 0.1)
            gictemp = np.where(intemp > 0.1)
            gictemp = gictemp[0]
            gicStemp = gicStemp[0]
            gsztemp = np.where((sz[gsI[gicStemp]] >= clusz[j+5]-0.01) & (sz[gsI[gicStemp]] <= clusz[j+5]+0.01))
            gsztemp = gsztemp[0]
            gsqtemp = np.where(sq[gsI[gicStemp[gsztemp]]] > 2.3)
            gsqtemp = gsqtemp[0]
            gRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] + rsNSTD[i]*rsSTD[i]) & (sR[gsI[gicStemp]]-sI[gsI[gicStemp]] >= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
            gNRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
            gRSt = gRSt[0]
            gNRSt = gNRSt[0]
            gRSzt = np.where((sz[gsI[gicStemp[gRSt]]] >= clusz[j+5]-0.01) & (sz[gsI[gicStemp[gRSt]]] <= clusz[j+5]+0.01))
            gRSzt = gRSzt[0]
            gRSqt = np.where(sq[gsI[gicStemp[gRSt[gRSzt]]]] > 2.3)
            gRSqt = gRSqt[0]
            gNRSzt = np.where((sz[gsI[gicStemp[gNRSt]]] >= clusz[j+5]-0.01) & (sz[gsI[gicStemp[gNRSt]]] <= clusz[j+5]+0.01))
            gNRSzt = gNRSzt[0]
            gNRSqt = np.where(sq[gsI[gicStemp[gNRSt[gNRSzt]]]] > 2.3)
            gNRSqt = gNRSqt[0]
            gRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] + rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] >= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
            gNRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
            convRST,convNRST = 0,0
            if len(gRSt) > 0: convRSt = len(gRSqt)*1.0/len(gRSt)
            if len(gNRSt) > 0:
                convNRSt = len(gNRSqt)*1.0/len(gNRSt)
            totRStemp = convRSt*len(gRSpt[0])
            totNRStemp = convNRSt*len(gNRSpt[0])
            clustotRS += totRStemp
            clustotNRS += totNRStemp
            convtemp = len(gsqtemp)*1.0/len(gicStemp)
            tottemp = convtemp*len(gictemp)
            clustot += tottemp
            print '%s%s - (Good Spec,Tot.Spec,Total,Est) - (%i,%i,%i,%.1f)\n'%(names[i],cnam[j+5],len(gsqtemp),len(gicStemp),len(gictemp),tottemp)
    if i == 1:
        #NEP5281
        inwin = np.where((pRA[gt] >= (18+(20.0+30.0/60)/60)*(360/24.0)) & (pRA[gt] <= (18+(22.0+30.0/60)/60)*(360/24.0)) & (pDec[gt] >= (68+22.0/60)) & (pDec[gt] <= 68 + 34.0/60))
        inwin = inwin[0]
        indis = np.zeros(len(inwin))
        intemp = np.zeros(len(inwin))
        intempS = np.zeros(len(indisS))
        intempX = np.zeros(len(indisX))
        for k in range(0,len(indisX)):
            diststemp = SphDist(clusRA[4],clusDec[4],msRAX[nsx[gmxI[gmxlum[k]]]],msDecX[nsx[gmxI[gmxlum[k]]]])
            if diststemp < crads[4]*60: indisX[k] += 1
        for k in range(0,len(indisS)):
            diststemp = SphDist(clusRA[4],clusDec[4],sRA[gsI[k]],sDec[gsI[k]])
            if diststemp < crads[4]*60: 
                indisS[k] += 1
                intempS[k] += 1
        for k in range(0,len(inwin)):
            diststemp = SphDist(clusRA[4],clusDec[4],pRA[gt[inwin[k]]],pDec[gt[inwin[k]]])
            if diststemp < crads[4]*60:
                indis[k] += 1
                intemp[k] += 1
        gicStemp = np.where(intempS > 0.1)
        gictemp = np.where(intemp > 0.1)
        gictemp = gictemp[0]
        gicStemp = gicStemp[0]
        gsztemp = np.where((sz[gsI[gicStemp]] >= clusz[4]-0.01) & (sz[gsI[gicStemp]] <= clusz[4]+0.01))
        gsztemp = gsztemp[0]
        gsqtemp = np.where(sq[gsI[gicStemp[gsztemp]]] > 2.3)
        gsqtemp = gsqtemp[0]
        gRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] + rsNSTD[i]*rsSTD[i]) & (sR[gsI[gicStemp]]-sI[gsI[gicStemp]] >= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
        gNRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
        gRSt = gRSt[0]
        gNRSt = gNRSt[0]
        gRSzt = np.where((sz[gsI[gicStemp[gRSt]]] >= clusz[4]-0.01) & (sz[gsI[gicStemp[gRSt]]] <= clusz[4]+0.01))
        gRSzt = gRSzt[0]
        gRSqt = np.where(sq[gsI[gicStemp[gRSt[gRSzt]]]] > 2.3)
        gRSqt = gRSqt[0]
        gNRSzt = np.where((sz[gsI[gicStemp[gNRSt]]] >= clusz[4]-0.01) & (sz[gsI[gicStemp[gNRSt]]] <= clusz[4]+0.01))
        gNRSzt = gNRSzt[0]
        gNRSqt = np.where(sq[gsI[gicStemp[gNRSt[gNRSzt]]]] > 2.3)
        gNRSqt = gNRSqt[0]
        gRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] + rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] >= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
        gNRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
        convRST,convNRST = 0,0
        if len(gRSt) > 0: convRSt = len(gRSqt)*1.0/len(gRSt)
        if len(gNRSt) > 0:
            convNRSt = len(gNRSqt)*1.0/len(gNRSt)
        totRStemp = convRSt*len(gRSpt[0])
        totNRStemp = convNRSt*len(gNRSpt[0])
        clustotRS += totRStemp
        clustotNRS += totNRStemp
        convtemp = len(gsqtemp)*1.0/len(gicStemp)
        tottemp = convtemp*len(gictemp)
        clustot += tottemp
        print '%s%s - (Good Spec,Tot.Spec,Total,Est) - (%i,%i,%i,%.1f)\n'%(names[i],cnam[4],len(gsqtemp),len(gicStemp),len(gictemp),tottemp)
    if i == 2:
        #Cl0023
        inwin = np.where((pRA[gt] >= (0+(23.0+20.0/60)/60)*(360/24.0)) & (pRA[gt] <= (0+(24.0+30.0/60)/60)*(360/24.0)) & (pDec[gt] >= (4+16.0/60)) & (pDec[gt] <= 4 + 29.0/60))
        inwin = inwin[0]
        indis = np.zeros(len(inwin))
        for j in range(0,4):
            intemp = np.zeros(len(inwin))
            intempS = np.zeros(len(indisS))
            intempX = np.zeros(len(indisX))
            for k in range(0,len(indisX)):
                diststemp = SphDist(clusRA[j],clusDec[j],msRAX[nsx[gmxI[gmxlum[k]]]],msDecX[nsx[gmxI[gmxlum[k]]]])
                if diststemp < crads[j]*60: indisX[k] += 1
            for k in range(0,len(indisS)):
                diststemp = SphDist(clusRA[j],clusDec[j],sRA[gsI[k]],sDec[gsI[k]])
                if diststemp < crads[j]*60: 
                    indisS[k] += 1
                    intempS[k] += 1
            for k in range(0,len(inwin)):
                diststemp = SphDist(clusRA[j],clusDec[j],pRA[gt[inwin[k]]],pDec[gt[inwin[k]]])
                if diststemp < crads[j]*60:
                    indis[k] += 1
                    intemp[k] += 1
            gicStemp = np.where(intempS > 0.1)
            gictemp = np.where(intemp > 0.1)
            gictemp = gictemp[0]
            gicStemp = gicStemp[0]
            gsztemp = np.where((sz[gsI[gicStemp]] >= clusz[j]-0.01) & (sz[gsI[gicStemp]] <= clusz[j]+0.01))
            gsztemp = gsztemp[0]
            gsqtemp = np.where(sq[gsI[gicStemp[gsztemp]]] > 2.3)
            gsqtemp = gsqtemp[0]
            gRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] + rsNSTD[i]*rsSTD[i]) & (sR[gsI[gicStemp]]-sI[gsI[gicStemp]] >= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
            gNRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
            gRSt = gRSt[0]
            gNRSt = gNRSt[0]
            gRSzt = np.where((sz[gsI[gicStemp[gRSt]]] >= clusz[j]-0.01) & (sz[gsI[gicStemp[gRSt]]] <= clusz[j]+0.01))
            gRSzt = gRSzt[0]
            gRSqt = np.where(sq[gsI[gicStemp[gRSt[gRSzt]]]] > 2.3)
            gRSqt = gRSqt[0]
            gNRSzt = np.where((sz[gsI[gicStemp[gNRSt]]] >= clusz[j]-0.01) & (sz[gsI[gicStemp[gNRSt]]] <= clusz[j]+0.01))
            gNRSzt = gNRSzt[0]
            gNRSqt = np.where(sq[gsI[gicStemp[gNRSt[gNRSzt]]]] > 2.3)
            gNRSqt = gNRSqt[0]
            gRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] + rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] >= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
            gNRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
            convRST,convNRST = 0,0
            if len(gRSt) > 0: convRSt = len(gRSqt)*1.0/len(gRSt)
            if len(gNRSt) > 0:
                convNRSt = len(gNRSqt)*1.0/len(gNRSt)
            totRStemp = convRSt*len(gRSpt[0])
            totNRStemp = convNRSt*len(gNRSpt[0])
            clustotRS += totRStemp
            clustotNRS += totNRStemp
            convtemp = len(gsqtemp)*1.0/len(gicStemp)
            tottemp = convtemp*len(gictemp)
            clustot += tottemp
            print '%s%s - (Good Spec,Tot.Spec,Total,Est) - (%i,%i,%i,%.1f)\n'%(names[i],cnam[j],len(gsqtemp),len(gicStemp),len(gictemp),tottemp)
    if i == 3:
        #Cl1604
        inwin = np.where((pRA[gt] >= (16+(2.0+45.0/60)/60)*(360/24.0)) & (pRA[gt] <= (16+(5.0+15.0/60)/60)*(360/24.0)) & (pDec[gt] >= (43+0.0/60)) & (pDec[gt] <= 43 + 30.0/60))
        inwin = inwin[0]
        indis = np.zeros(len(inwin))
        for j in range(0,7):
            intemp = np.zeros(len(inwin))
            intempS = np.zeros(len(indisS))
            intempX = np.zeros(len(indisX))
            for k in range(0,len(indisX)):
                diststemp = SphDist(clusRA[j+10],clusDec[j+10],msRAX[nsx[gmxI[gmxlum[k]]]],msDecX[nsx[gmxI[gmxlum[k]]]])
                if diststemp < crads[j+10]*60: indisX[k] += 1
            for k in range(0,len(indisS)):
                diststemp = SphDist(clusRA[j+10],clusDec[j+10],sRA[gsI[k]],sDec[gsI[k]])
                if diststemp < crads[j+10]*60: 
                    indisS[k] += 1
                    intempS[k] += 1
            for k in range(0,len(inwin)):
                diststemp = SphDist(clusRA[j+10],clusDec[j+10],pRA[gt[inwin[k]]],pDec[gt[inwin[k]]])
                if diststemp < crads[j+10]*60:
                    indis[k] += 1
                    intemp[k] += 1
            gicStemp = np.where(intempS > 0.1)
            gictemp = np.where(intemp > 0.1)
            gictemp = gictemp[0]
            gicStemp = gicStemp[0]
            gsztemp = np.where((sz[gsI[gicStemp]] >= clusz[j+10]-0.01) & (sz[gsI[gicStemp]] <= clusz[j+10]+0.01))
            gsztemp = gsztemp[0]
            gsqtemp = np.where(sq[gsI[gicStemp[gsztemp]]] > 2.3)
            gsqtemp = gsqtemp[0]
            gRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] + rsNSTD[i]*rsSTD[i]) & (sR[gsI[gicStemp]]-sI[gsI[gicStemp]] >= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
            gNRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
            gRSt = gRSt[0]
            gNRSt = gNRSt[0]
            gRSzt = np.where((sz[gsI[gicStemp[gRSt]]] >= clusz[j+10]-0.01) & (sz[gsI[gicStemp[gRSt]]] <= clusz[j+10]+0.01))
            gRSzt = gRSzt[0]
            gRSqt = np.where(sq[gsI[gicStemp[gRSt[gRSzt]]]] > 2.3)
            gRSqt = gRSqt[0]
            gNRSzt = np.where((sz[gsI[gicStemp[gNRSt]]] >= clusz[j+10]-0.01) & (sz[gsI[gicStemp[gNRSt]]] <= clusz[j+10]+0.01))
            gNRSzt = gNRSzt[0]
            gNRSqt = np.where(sq[gsI[gicStemp[gNRSt[gNRSzt]]]] > 2.3)
            gNRSqt = gNRSqt[0]
            gRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] + rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] >= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
            gNRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
            convRST,convNRST = 0,0
            if len(gRSt) > 0: convRSt = len(gRSqt)*1.0/len(gRSt)
            if len(gNRSt) > 0:
                convNRSt = len(gNRSqt)*1.0/len(gNRSt)
            totRStemp = convRSt*len(gRSpt[0])
            totNRStemp = convNRSt*len(gNRSpt[0])
            clustotRS += totRStemp
            clustotNRS += totNRStemp
            convtemp = len(gsqtemp)*1.0/len(gicStemp)
            tottemp = convtemp*len(gictemp)
            clustot += tottemp
            print '%s%s - (Good Spec,Tot.Spec,Total,Est) - (%i,%i,%i,%.1f)\n'%(names[i],cnam[j+10],len(gsqtemp),len(gicStemp),len(gictemp),tottemp)
    if i == 4:
        #RXJ1757
        inwin = np.where((pRA[gt] >= (17+(56.0+40.0/60)/60)*(360/24.0)) & (pRA[gt] <= (17+(58.0+0.0/60)/60)*(360/24.0)) & (pDec[gt] >= (66+27.0/60)) & (pDec[gt] <= 66 + 36.0/60))
        inwin = inwin[0]
        indis = np.zeros(len(inwin))
        intemp = np.zeros(len(inwin))
        intempS = np.zeros(len(indisS))
        intempX = np.zeros(len(indisX))
        for k in range(0,len(indisX)):
            diststemp = SphDist(clusRA[len(clusRA)-1],clusDec[len(clusRA)-1],msRAX[nsx[gmxI[gmxlum[k]]]],msDecX[nsx[gmxI[gmxlum[k]]]])
            if diststemp < crads[len(clusRA)-1]*60: indisX[k] += 1
        for k in range(0,len(indisS)):
            diststemp = SphDist(clusRA[len(clusRA)-1],clusDec[len(clusRA)-1],sRA[gsI[k]],sDec[gsI[k]])
            if diststemp < crads[len(clusRA)-1]*60: 
                indisS[k] += 1
                intempS[k] += 1
        for k in range(0,len(inwin)):
            diststemp = SphDist(clusRA[len(clusRA)-1],clusDec[len(clusRA)-1],pRA[gt[inwin[k]]],pDec[gt[inwin[k]]])
            if diststemp < crads[len(clusRA)-1]*60:
                indis[k] += 1
                intemp[k] += 1
        gicStemp = np.where(intempS > 0.1)
        gictemp = np.where(intemp > 0.1)
        gictemp = gictemp[0]
        gicStemp = gicStemp[0]
        gsztemp = np.where((sz[gsI[gicStemp]] >= clusz[len(clusRA)-1]-0.01) & (sz[gsI[gicStemp]] <= clusz[len(clusRA)-1]+0.01))
        gsztemp = gsztemp[0]
        gsqtemp = np.where(sq[gsI[gicStemp[gsztemp]]] > 2.3)
        gsqtemp = gsqtemp[0]
        gRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] + rsNSTD[i]*rsSTD[i]) & (sR[gsI[gicStemp]]-sI[gsI[gicStemp]] >= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
        gNRSt = np.where((sR[gsI[gicStemp]]-sI[gsI[gicStemp]] <= rsfitb[i]-rsfitm[i]*sI[gsI[gicStemp]] - rsNSTD[i]*rsSTD[i]))
        gRSt = gRSt[0]
        gNRSt = gNRSt[0]
        gRSzt = np.where((sz[gsI[gicStemp[gRSt]]] >= clusz[len(clusRA)-1]-0.01) & (sz[gsI[gicStemp[gRSt]]] <= clusz[len(clusRA)-1]+0.01))
        gRSzt = gRSzt[0]
        gRSqt = np.where(sq[gsI[gicStemp[gRSt[gRSzt]]]] > 2.3)
        gRSqt = gRSqt[0]
        gNRSzt = np.where((sz[gsI[gicStemp[gNRSt]]] >= clusz[len(clusRA)-1]-0.01) & (sz[gsI[gicStemp[gNRSt]]] <= clusz[len(clusRA)-1]+0.01))
        gNRSzt = gNRSzt[0]
        gNRSqt = np.where(sq[gsI[gicStemp[gNRSt[gNRSzt]]]] > 2.3)
        gNRSqt = gNRSqt[0]
        gRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] + rsNSTD[i]*rsSTD[i]) & (pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] >= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
        gNRSpt = np.where((pR[gt[inwin[gictemp]]]-pI[gt[inwin[gictemp]]] <= rsfitb[i]-rsfitm[i]*pI[gt[inwin[gictemp]]] - rsNSTD[i]*rsSTD[i]))
        convRSt,convNRSt = 0,0
        if len(gRSt) > 0: convRSt = len(gRSqt)*1.0/len(gRSt)
        if len(gNRSt) > 0:
            convNRSt = len(gNRSqt)*1.0/len(gNRSt)
        totRStemp = convRSt*len(gRSpt[0])
        totNRStemp = convNRSt*len(gNRSpt[0])
        clustotRS += totRStemp
        clustotNRS += totNRStemp
        convtemp = len(gsqtemp)*1.0/len(gicStemp)
        tottemp = convtemp*len(gictemp)
        clustot += tottemp
        print '%s%s - (Good Spec,Tot.Spec,Total,Est) - (%i,%i,%i,%.1f)\n'%(names[i],cnam[len(clusRA)-1],len(gsqtemp),len(gicStemp),len(gictemp),tottemp)
    inran = np.where(indis > 0.1)
    inran = inran[0]
    inranS = np.where(indisS > 0.1)
    inranS = inranS[0]
    inranX = np.where(indisX > 0.1)
    inranX = inranX[0]

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
    pylab.plot(rsfX,rsfY1,linestyle='dashed')
    pylab.plot(rsfX,rsfY2,linestyle='dashed')
    savname = '/home/rumbaugh/paperstuff/CMD.%s.completeness.rad_%3.1f.4.20.11.png'%(names[i],cradmult)
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
    totalAGN = AGNconv*len(inranX-len(gmszIR))+len(gmszIR)

    print '\nField - %7s:\n'%(names[i])
    print "i' range: (%f,%f)\n"%(Imin,Ilim)
    print 'Counts range: (%f,%f)\n'%(limL[i],limU[i])
    print 'Estimated total RS members:  %i\n'%(int(clustotRS))
    print 'Estimated total NRS members: %i\n'%(int(clustotNRS))
#    print 'Estimated total RS members:  %i\n'%(int(totalRS))
#    print 'Estimated total NRS members: %i\n'%(int(totalNRS))
#    print 'Estimated NRS fraction: %5.3f\n'%(totalNRS/(totalRS+totalNRS))
#    print 'Estimated blue fraction: %5.3f\n'%((totalNRS1B+totalNRS2)/(totalRS+totalNRS))
    print 'Estimated NRS fraction: %5.3f\n'%(clustotNRS/(1.0*clustotRS+clustotNRS))
    print 'Measured NRS fraction:  %5.3f\n'%((len(gszNRS0)+len(gszNRS1)+len(gszNRS2))*1.0/(len(gszRS)+len(gszNRS0)+len(gszNRS1)+len(gszNRS2)))
#    print 'Conversions: %7.5f  %7.5f  %7.5f\n'%(conversionRS,conversionNRS1,conversionNRS2)
    print 'AGN conversion: %7.5f\n'%(AGNconv)
    print 'Estimated Total AGN: %4.1f\n'%((totalAGN))
    #print 'Estimated AGN fraction: %7.5f\n'%(totalAGN/(totalRS+totalNRS))
    print 'Estimated AGN fraction: %7.5f\n'%(totalAGN/(1.0*clustot))
    print '(Tot. AGN,(In Range),Tot. good Xray sources): (%f,%f,%f)\n'%(len(gmsz),len(gmszIR),len(gmsq))
    print 'Total eligible Xray Sources: %5.1f\n'%(len(gmxlum))
    
    

