execfile('/home/rumbaugh/FindCloseSources.py')
path = '/home/rumbaugh/LFC'
pathm = '/scratch/rumbaugh/ciaotesting'
path2 = 'opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat'
names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
files = np.array(['FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.noheader.cat','FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.noheader.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.noheader.cat'])
mfiles = np.array(['FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat','FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat','FINAL.matched.0023.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.1604.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.N200.specnXray.nov2010.rumbaugh.noheader.cat'])
pfiles=np.array(['sc1322.lfc.newIDsandoldIds.radecmag.cat','nep5281.lfc.newIDradecmag.cat','cl0023_radecIDmags.cat','final.idradecmag.lfcpluscosmic.withsdss.cat','nep200.idradecmag.lfc.uhcorr.neat'])

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
    gq = np.where((sq[mInds[ns]] == -1) | (sq[mInds[ns]] > 2.7))
    gq = gq[0]
    print '\n%s'%(names[i])
    print "Number of X-ray sources matched to opt. sources: " + str(len(gnm))
    print "Number targeted for spectroscopy: " + str(len(ns[0]))
    print "Number targeted for spectroscopy (q = -1,3,4): " + str(len(gq))
    print 'Percent targetd: %5.1f'%(100.0*len(gq)/len(mInds))
    print 'Number matched: %i'%(len(msq))
    gg = np.where((msq == -1) | (msq > 2.5))
    print 'Number with q=-1,3,4: %i'%(len(gg[0]))
    print 'Percent targetd: %5.1f'%(100.0*len(msq)/len(mInds))
    print 'Percent good: %5.1f'%(100.0*len(gg[0])/len(mInds))
    print 'Spect. Targets: %i'%(len(sq))
    gsq = np.where((sq == -1) | (sq > 2.3))
    print 'Spect. Redshifts (q=-1,3,4): %i'%(len(gsq[0]))
    #gI = np.argsort(sI[mInds])
    #perctemp = np.zeros(len(gI))
    #for kk in range(0,len(gI)):
    FILE = open('/home/rumbaugh/paperstuff/matchedVunmatched.%s.dat'%(names[i]),'w')
    gnn = np.where(msInds < -0.3)
    gnn = gnn[0]
    for kk in range(0,len(gnn)):
        FILE.write('%f %f %i %f %f %f %f\n'%(mRAX[gnm[gnn[kk]]],mDecX[gnm[gnn[kk]]],0,-1,pR[pInds[gnn[kk]]],pI[pInds[gnn[kk]]],pZ[pInds[gnn[kk]]]))
    for kk in range(0,len(msRA)):
        FILE.write('%f %f %i %f %f %f %f\n'%(msRAX[kk],msDecX[kk],msq[kk],msz[kk],msR[kk],msI[kk],msZ[kk]))
    FILE.close()
