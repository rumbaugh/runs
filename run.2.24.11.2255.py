execfile('/home/rumbaugh/FindCloseSources.py')
import matplotlib
import matplotlib.pylab as pylab
path = '/home/rumbaugh/LFC'
pathm = '/scratch/rumbaugh/ciaotesting'
path2 = 'opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat'
names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
namesl = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','NEP200'])
files = np.array(['FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.noheader.cat','FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.noheader.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.noheader.cat'])

for i in range(0,5):
    master = 'master'
    if i == 2: master = '7914'
    mfile = '%s/%s/%s/%s'%(pathm,names[i],master,path2)
    sfile = '%s/%s'%(path,files[i])
    crm = read_file(mfile)
    mRAX = get_colvals(crm,'col2')
    mDecX = get_colvals(crm,'col3')
    nm = get_colvals(crm,'col5')
    mRA = get_colvals(crm,'col6')
    mDec = get_colvals(crm,'col7')
    
    crs = read_file(sfile)
    sRA = get_colvals(crs,'col4')
    sDec = get_colvals(crs,'col5')
    sI = get_colvals(crs,'col7')
    sq = get_colvals(crs,'col11')
    
    gnm = np.where(nm > 0.4)
    gnm = gnm[0]
    mInds = np.zeros(len(gnm),dtype='int')
    mInds.fill(-1)
    for j in range(0,len(gnm)):
        cic = FindCloseSources(mRA[gnm[j]],mDec[gnm[j]],1.8,sRA,sDec,0)
        if len(cic) > 0: mInds[j] = cic[0]
    gq = np.where((sq[mInds] == -1) | (sq[mInds] > 2.7))
    gq = gq[0]
    print '\n%s'%(names[i])
    print "Number of X-ray sources matched to opt. sources: " + str(len(mInds))
    print "Number targeted for spectroscopy (q = -1,3,4): " + str(len(gq))
    print 'Percent targeted: %5.1f'%(100.0*len(gq)/len(mInds))
    gI = np.argsort(sI[mInds[gq]])
    perctemp = np.zeros(len(gI))
    for kk in range(len(gI)-1,-1,-1):
        gnh = np.where(sI[mInds] <= sI[mInds[gq[gI[kk]]]])
        perctemp[kk] = (100.0*(kk)/(1.0*len(gnh[0])))
    pylab.plot(sI[mInds[gq[gI]]],perctemp,label=namesl[i])
pylab.xlim(15,27)
pylab.legend()
pylab.savefig('/home/rumbaugh/completeness.plot.2.24.11.png')
pylab.close('all')
