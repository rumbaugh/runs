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

rsfitb = np.array([1.777,3.182,1.325,1.48,1.84])
rsfitm = np.array([0.0229,0.063,0.0084,0.012,0.0319])
rsSTD = np.array([0.0625,0.0907,0.0735,0.0636,0.0576])
rsnstd = np.array([3.,2.,3.,3.,3.])
mx = (43.2104078-43.348505)/(240.9472-241.28263)



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
    sR = get_colvals(crs,'col6')
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
    gsqNZ = np.where((sI[gsq] > 0.1) & (sR[gsq] > 0.1))
    gsqNZ = gsqNZ[0]
    gsqRS = np.where((sR[gsq[gsqNZ]]-sI[gsq[gsqNZ]] > rsfitb[i]-rsfitm[i]*sI[gsq[gsqNZ]]-rsnstd[i]*rsSTD[i]) 
& (sR[gsq[gsqNZ]]-sI[gsq[gsqNZ]] < rsfitb[i]-rsfitm[i]*sI[gsq[gsqNZ]]+rsnstd[i]*rsSTD[i]))
    gsqRS = gsqRS[0]
    gsqNRS = np.where((sR[gsq[gsqNZ]]-sI[gsq[gsqNZ]] < rsfitb[i]-rsfitm[i]*sI[gsq[gsqNZ]]-rsnstd[i]*rsSTD[i]))
    gsqNRS = gsqNRS[0]
    gszRS = np.where((sz[gsq[gsqNZ[gsqRS]]] >= zlb[i]) & (sz[gsq[gsqNZ[gsqRS]]] <= zub[i]))
    gszRS = gszRS[0]
    gszNRS = np.where((sz[gsq[gsqNZ[gsqNRS]]] >= zlb[i]) & (sz[gsq[gsqNZ[gsqNRS]]] <= zub[i]))
    gszNRS = gszNRS[0]
    nwl2 = 0.0

    gt = np.where((pI <= Ilim) & (pI > 0.1))
    gt = gt[0]
    gtNZ = np.where((pI[gt] > 0.1) & (pR[gt] > 0.1))
    gtNZ = gtNZ[0]
    gtRS = np.where((pR[gt[gtNZ]]-pI[gt[gtNZ]] > rsfitb[i]-rsfitm[i]*pI[gt[gtNZ]]-rsnstd[i]*rsSTD[i]) & (pR[gt[gtNZ]]-pI[gt[gtNZ]] < rsfitb[i]-rsfitm[i]*sI[gt[gtNZ]]+rsnstd[i]*rsSTD[i]))
    gtRS = gtRS[0]
    gtNRS = np.where((pR[gt[gtNZ]]-pI[gt[gtNZ]] < rsfitb[i]-rsfitm[i]*pI[gt[gtNZ]]-rsnstd[i]*rsSTD[i]))
    gtNRS = gtNRS[0]
    gt2 = np.where((pI[pInds] <= Ilim) & (pI[pInds] > 0.1))
    gt2 = gt2[0]

    print '\n%s'%(names[i])
    #FILE = open('/home/rumbaugh/paperstuff/matchedVunmatched.%s.dat'%(names[i]),'w')
    print 'Percent of good specs that are AGN cluster members: %5.2f'%(len(gqz)*100.0/(len(gq)+nwl))
    print 'Percent of good specs that are any cluster members: %5.2f'%(len(gsz)*100.0/(len(gsq)+nwl2))
    print 'Total AGN: %i'%(int(len(gt2)*len(gqz)*1.0/(len(gq)+nwl)))
    print 'Total cluster members: %i'%(int(len(gt)*len(gsz)*1.0/(len(gsq)+nwl2)))
    print 'AGN Fraction: %6.3f'%((len(gt2)*len(gqz)*1.0/(len(gq)+nwl))/(len(gt)*len(gsz)*1.0/(len(gsq)+nwl2)))
    print 'Total Blue clusters: %i'%(int(len(gt[gtNZ[gtNRS]])*len(gsz[gsqNZ[gsqNRS[gszNRS]]])*1.0/(len(gsq[gsqNZ[gsqNRS]])+nwl2)))
    print 'Total Red clusters: %i'%(int(len(gt[gtNZ[gtRS]])*len(gsz[gsqNZ[gsqRS[gszRS]]])*1.0/(len(gsq[gsqNZ[gsqRS]])+nwl2)))
    print 'Blue fraction: %6.3f'%((len(gt[gtNZ[gtNRS]])*len(gsz[gsqNZ[gsqNRS[gszNRS]]])*1.0/(len(gsq[gsqNZ[gsqNRS]])+nwl2))/(len(gt[gtNZ[gtRS]])*len(gsz[gsqNZ[gsqRS[gszRS]]])*1.0/(len(gsq[gsqNZ[gsqRS]])+nwl2)))
    gnn = np.where(msInds < -0.3)
    gnn = gnn[0]
    #for kk in range(0,len(gnn)):
    #    FILE.write('%f %f %i %f %f %f %f\n'%(mRAX[gnm[gnn[kk]]],mDecX[gnm[gnn[kk]]],0,-1,pR[pInds[gnn[kk]]],pI[pInds[gnn[kk]]],pZ[pInds[gnn[kk]]]))
    #for kk in range(0,len(msRA)):
    #    FILE.write('%f %f %i %f %f %f %f\n'%(msRAX[kk],msDecX[kk],msq[kk],msz[kk],msR[kk],msI[kk],msZ[kk]))
    #FILE.close()
