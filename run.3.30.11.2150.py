execfile('/home/rumbaugh/FindCloseSources.py')

try:
    Ilim
except NameError:
    Ilim = 24.0

path = '/home/rumbaugh/LFC'
pathm = '/scratch/rumbaugh/ciaotesting'
path2 = 'opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat'
names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
files = np.array(['FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.noheader.cat','FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.noheader.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.noheader.cat'])
mfiles = np.array(['FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat','FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat','FINAL.matched.0023.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.1604.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.N200.specnXray.nov2010.rumbaugh.noheader.cat'])
pfiles=np.array(['sc1322.lfc.newIDsandoldIds.radecmag.cat','nep5281.lfc.newIDradecmag.cat','cl0023_radecIDmags.cat','final.idradecmag.lfcpluscosmic.withsdss.cat','nep200.idradecmag.lfc.uhcorr.neat'])

zlb = np.array([0.66,0.808,0.82,0.84,0.68])
zub = np.array([0.785,0.828,0.856,0.96,0.705])

cRA = np.array([201.166,275.375,5.975,241.033,269.37])
cDec = np.array([30.6,68.45,4.375,43.8,66.55])


for i in range(0,5):
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
    
    crs = read_file(sfile)
    sRA = get_colvals(crs,'col4')
    sDec = get_colvals(crs,'col5')
    sI = get_colvals(crs,'col7')
    sq = get_colvals(crs,'col11')
    sz = get_colvals(crs,'col9')
    
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
    
    pSphD = np.zeros(len(pRA))
    sSphD = np.zeros(len(sRA))
    for k in range(0,len(pRA)):
        pSphD[k] = SphDist(pRA[k],pDec[k],cRA[i],cDec[i])
    for k in range(0,len(sRA)):
        sSphD[k] = SphDist(sRA[k],sDec[k],cRA[i],cDec[i])

    gnm = np.where(nm > 0.4)
    gnm = gnm[0]
    pInds = np.zeros(len(gnm),dtype='int')
    pInds.fill(-1)
    mInds = np.zeros(len(gnm),dtype='int')
    mInds.fill(-1)
    msInds = np.zeros(len(gnm),dtype='int')
    msInds.fill(-1)
    for j in range(0,len(gnm)):
        cic = FindCloseSources(mRA[gnm[j]],mDec[gnm[j]],1.8,sRA,sDec,0)
        if len(cic) > 0: mInds[j] = cic[0]
        cic3 = FindCloseSources(mRA[gnm[j]],mDec[gnm[j]],1.8,pRA,pDec,0)
        if len(cic3) > 0: pInds[j] = cic3[0]
        cic2 = FindCloseSources(mRAX[gnm[j]],mDecX[gnm[j]],1.8,msRA,msDec,0)
        if len(cic2) > 0: msInds[j] = cic2[0]
    ns = np.where(mInds > -0.3)
    ns = ns[0]
    gq = np.where((sq[mInds[ns]] == -1) | (sq[mInds[ns]] > 2.7))
    gq = gq[0]
    gq2 = np.where(sq[mInds[ns]] > 2.7)
    gq2 = gq2[0]
    gqz = np.where((sz[mInds[ns[gq2]]] >= zlb[i]) & (sz[mInds[ns[gq2]]] <= zub[i]))
    gqz = gqz[0]
    nwl = 0.0
    gsq = np.where((sq == -1) | (sq > 2.3))
    gsq = gsq[0]
    gsz = np.where((sz[gsq] >= zlb[i]) & (sz[gsq] <= zub[i]))
    gsz = gsz[0]
    distMax = sSphD[gsq[gsz]].max()
    if i == 1:
        garg = np.argsort(sSphD[gsq[gsz]])
        distMax = sSphD[gsq[gsz[garg[len(garg)-3]]]]
    gsqd = np.where(sSphD[gsq] <= distMax*1.05)
    gsqd = gsqd[0]
    gqd = np.where(sSphD[mInds[ns[gq]]] <= distMax*1.05)
    gqd = gqd[0]

    gqzd = np.where(sSphD[mInds[ns[gq2[gqz]]]] <= distMax*1.05)
    gqzd = gqzd[0]
    #gszd = np.where(sSphD[gsq[gsz]] <= distMax*1.05)
    #gszd = gszd[0]
    nwl2 = 0.0

    gt = np.where((pI <= Ilim) & (pI > 0.1))
    gt = gt[0]
    gtd = np.where(pSphD[gt] <= distMax*1.05)
    gtd = gtd[0]
    gt2 = np.where((pI[pInds] <= Ilim) & (pI[pInds] > 0.1))
    gt2 = gt2[0]
    gtd2 = np.where(pSphD[pInds[gt2]] <= distMax*1.05)
    gtd2 = gtd2[0]
    gt2d = gtd2

    print '\n%s'%(names[i])
    print len(pInds),len(gt2),len(gt2d)
    #FILE = open('/home/rumbaugh/paperstuff/matchedVunmatched.%s.dat'%(names[i]),'w')
    print 'Percent of good specs that are AGN cluster members: %5.2f'%(len(gqzd)*100.0/(len(gqd)+nwl))
    print 'Percent of good specs that are any cluster members: %5.2f'%(len(gsz)*100.0/(len(gsqd)+nwl2))
    print 'Total AGN: %i'%(int(len(gt2d)*len(gqzd)*1.0/(len(gqd)+nwl)))
    print 'Total cluster members: %i'%(int(len(gtd)*len(gsz)*1.0/(len(gsqd)+nwl2)))
    AGNfrac = (len(gt2d)*len(gqzd)*1.0/(len(gqd)+nwl))/(len(gtd)*len(gsz)*1.0/(len(gsqd)+nwl2))
    fracerr = AGNfrac*m.sqrt(1.0/len(gt2d) + 1.0/len(gqzd) + 1.0/len(gqd) + 1.0/len(gtd) + 1.0/len(gsz) + 1.0/len(gsqd))
    print 'AGN Fraction: %6.3f +/- %6.3f'%(AGNfrac,fracerr)
    gnn = np.where(msInds < -0.3)
    gnn = gnn[0]
    #for kk in range(0,len(gnn)):
    #    FILE.write('%f %f %i %f %f %f %f\n'%(mRAX[gnm[gnn[kk]]],mDecX[gnm[gnn[kk]]],0,-1,pR[pInds[gnn[kk]]],pI[pInds[gnn[kk]]],pZ[pInds[gnn[kk]]]))
    #for kk in range(0,len(msRA)):
    #    FILE.write('%f %f %i %f %f %f %f\n'%(msRAX[kk],msDecX[kk],msq[kk],msz[kk],msR[kk],msI[kk],msZ[kk]))
    #FILE.close()
