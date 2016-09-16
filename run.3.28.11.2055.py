execfile('/home/rumbaugh/FindCloseSources.py')
import matplotlib
import matplotlib.pylab as pylab
execfile("angconvert.py")

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


for i in range(2,3):
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

    gmsq = np.where(msq > 2.3)
    gmsq = gmsq[0]
    gmsz = np.where((msz[gmsq] >= zlb[i]) & (msz[gmsq] <= zub[i]))
    gmsz = gmsz[0]

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

    gsq = np.where((sq > 2.3))
    gsq = gsq[0]
    gsz = np.where((sz[gsq] >= zlb[i]) & (sz[gsq] <= zub[i]))
    gsz = gsz[0]
    nwl2 = 0.0

    gt = np.where(pI <= Ilim)
    gt = gt[0]
    gt2 = np.where(pI[pInds] <= Ilim)
    gt2 = gt2[0]

    degree_symbol = unichr(176)

    if i == 4:
        pylab.xlim(269.725,269.125)
        xlocs = np.array([269.625,269.5,269.375,269.25,269.125])
        xlabs = np.array(['30$^{s}$','58$^{m}$00$^{s}$','30$^{s}$','57$^{m}$00$^{s}$','17$^{h}$56$^{m}$30$^{s}$'])
        ylocs = np.array([66.4,66.45,66.5,66.55,66.6,66])
        ylabels = np.array(['65' + degree_symbol + "40'","45'","50'","55'","60'","65'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
    pylab.scatter(sRA[gsq[gsz]],sDec[gsq[gsz]],s=12)
    FILE = open('/home/rumbaugh/paperstuff/input.RShist.%s.dat'%(names[i]),'w')
    for j in range(0,len(gsz)): FILE.write('%f %f %f\n'%(sRA[gsq[gsz[j]]],sDec[gsq[gsz[j]]],sz[gsq[gsz[j]]]))
    FILE.close()
    pylab.scatter(msRA[gmsq[gmsz]],msDec[gmsq[gmsz]],marker = 'd',s=30,c='red')
    FILE = open('/home/rumbaugh/paperstuff/AGN.locs.%s.dat'%(names[i]),'w')
    gzsort = np.argsort(msz[gmsq[gmsz]])
    for j in range(0,len(gmsz)):
        FILE.write('%2i %f %f %f\n'%(1+j,msRA[gmsq[gmsz[gzsort[j]]]],msDec[gmsq[gmsz[gzsort[j]]]],msz[gmsq[gmsz[gzsort[j]]]]))
        AGNstr = str(1+j)
        pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.003/m.cos(msDec[gmsq[gmsz[gzsort[j]]]]),msDec[gmsq[gmsz[gzsort[j]]]]+0.003,AGNstr,color='red')  
    FILE.close()
    pylab.title('%s'%(names[i]))
    pylab.xlabel('Right Ascension (J2000)')
    pylab.ylabel('Declination (J2000)')
    savfile = 'AGN.spatmap.%s.png'%(names[i])
    pylab.savefig(savfile)
    pylab.close('all')
    
