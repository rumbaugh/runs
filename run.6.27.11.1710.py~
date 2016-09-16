import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/plotcircle.py")
execfile("/home/rumbaugh/angconvert.py")

html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FF9900'
html_pink = '#FF00FF'

try:
    cradmult
except NameError:
    cradmult = 0.5

try:
    Ilim
except NameError:
    Ilim = 23.5

#FILEA=open('/home/rumbaugh/paperstuff/AGNlist.4.8.11.dat','w')
path = '/home/rumbaugh/LFC'
pathm = '/scratch/rumbaugh/ciaotesting'
path2 = 'opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat'
names = np.array(['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757'])
files = np.array(['FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.noheader.cat','FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.noheader.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.noheader.cat'])
mfiles = np.array(['FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat','FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat','FINAL.matched.0023.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.1604.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.N200.specnXray.nov2010.rumbaugh.noheader.cat'])
pfiles=np.array(['sc1322.lfc.newIDsandoldIds.radecmag.cat','nep5281.lfc.newIDradecmag.cat','cl0023_radecIDmags.cat','final.idradecmag.lfcpluscosmic.withsdss.cat','nep200.idradecmag.lfc.uhcorr.neat'])

zlb = np.array([0.65,0.80,0.82,0.84,0.68])
zub = np.array([0.79,0.84,0.87,0.96,0.71])

crcr = read_file('/home/rumbaugh/clusters.z+pos+mpc.5.14.11.dat')
#crcr = read_file('/home/rumbaugh/clusters.pos.5.14.11.dat')
struc = get_colvals(crcr,'col1')
cnam = get_colvals(crcr,'col2')
clusz = get_colvals(crcr,'col3')
clusRA = get_colvals(crcr,'col4')
clusDec = get_colvals(crcr,'col5')
mpc = get_colvals(crcr,'col6')
mpccm = get_colvals(crcr,'col7')
crads = cradmult*0.7*mpc/60

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
    print len(gqz)

    raA = msRA[gmsq[gmsz]]
    decA = msDec[gmsq[gmsz]]
    zA = msz[gmsq[gmsz]]
    rahA,ramA,rasA = np.zeros(len(gmsz)),np.zeros(len(gmsz)),np.zeros(len(gmsz))
    decdA,decmA,decsA = np.zeros(len(gmsz)),np.zeros(len(gmsz)),np.zeros(len(gmsz))
    garg = np.argsort(zA)
    argcnt = 0
#    for jj in garg:
#        argcnt += 1
#        rahA[jj],ramA[jj],rasA[jj] = dec2hms(raA[jj])
#        decdA[jj],decmA[jj],decsA[jj] = dec2dms(decA[jj])
#        FILEA.write('%s & %2i & %2i\\ %2i\\ %4.1f & +%2i\\ %2i\\ %2i & %5.3f\\\\ \n'%(names[i],argcnt,rahA[jj],ramA[jj],rasA[jj],decdA[jj],decmA[jj],decsA[jj],zA[jj]))
        #FILEA.write('%s %9.7f %9.7f %2i %2i %4.1f %2i %2i %2i %5.3f\n'%(names[i],raA[jj],decA[jj],rahA[jj],ramA[jj],rasA[jj],decdA[jj],decmA[jj],decsA[jj],zA[jj]))

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


    if i == 0:
        #Cl1324
        pylab.ylim(30.0 + 6.0/60,31 + 2.0/60)
        pylab.xlim(201.55185,200.81315)
        xlocs = np.array([201.5,201.375,201.25,201.125,201.0,200.875])
        xlabs = np.array(['26$^{m}$00$^{s}$','30$^{s}$','25$^{m}$00$^{s}$','30$^{s}$','24$^{m}$00$^{s}$','13$^{h}$23$^{m}$30$^{s}$'])
        ylocs = np.array([30 + 10.0/60,30 + 15.0/60,30 + 20.0/60,30 + 25.0/60,30 + 30.0/60,30 + 35.0/60,30 + 40.0/60,30 + 45.0/60,30 + 50.0/60,30 + 55.0/60,31.0])
        ylabels = np.array(['30' + degree_symbol + "10'","15'","20'","25'","30'","35'","40'","45'","50'","55'",'31' + degree_symbol + "00'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
        g = np.where(sz[gsq[gsz]] < 0.68)
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color=html_pink)
        g = np.where((sz[gsq[gsz]] > 0.68) & (sz[gsq[gsz]] <= 0.725))
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color='blue')
        g = np.where((sz[gsq[gsz]] > 0.725) & (sz[gsq[gsz]] <= 0.765))
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color=html_teal)
        g = np.where((sz[gsq[gsz]] > 0.765))
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color=html_orng)
        leg = pylab.legend(('0.65 < z < 0.68','0.68 < z < 0.725','0.725 < z < 0.765','0.765 < z < 0.79'),loc=7,markerscale=0.8,labelspacing=0.3)
        icoff = 5
        F = pylab.gcf()
        DefaultSize = F.get_size_inches()
        F.set_size_inches( (DefaultSize[0]*0.9, DefaultSize[1]*1.5))
        for ic in range(0,10):
            plotcircle(RAcen=clusRA[ic+icoff],DECcen = clusDec[ic+icoff],rad=crads[ic+icoff])
            if ic == 0: pylab.text(clusRA[ic+icoff]-0.025,clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 1: pylab.text(clusRA[ic+icoff]+0.04,clusDec[ic+icoff]-0.009,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 2: pylab.text(clusRA[ic+icoff]+0.045,clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 3: pylab.text(clusRA[ic+icoff]-0.025,clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 4: pylab.text(clusRA[ic+icoff]+0.048,clusDec[ic+icoff]-0.01,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 5: pylab.text(clusRA[ic+icoff]+0.04,clusDec[ic+icoff]-0.02,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 6: pylab.text(clusRA[ic+icoff]-0.028,clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 7: pylab.text(clusRA[ic+icoff]-0.025,clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 8: pylab.text(clusRA[ic+icoff]-0.021,clusDec[ic+icoff]-0.027,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 9: pylab.text(clusRA[ic+icoff]-0.028,clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
        #2 Extra
        #plotcircle(RAcen=(13+(24.0+40.0/60)/60)*360/24.0,DECcen = 30.0+49.0/60,rad=crads[0+icoff]*1.9)
        #plotcircle(RAcen=(13+(24.0+43.0/60)/60)*360/24.0,DECcen = 30.0+23.0/60,rad=crads[0+icoff]*1.3)
        for t in leg.get_texts():
            t.set_fontsize('small') 
    if i == 1:
        #NEP5281
        pylab.xlim(275.797,274.953)
        pylab.ylim(68+19.5/60.0,68+34.0/60)
        xlocs = np.array([275.75,275.625,275.5,275.375,275.25,275.125,275])
        xlabs = np.array(['23$^{m}$00$^{s}$','30$^{s}$','22$^{m}$00$^{s}$','30$^{s}$','21$^{m}$00$^{s}$','30$^{s}$','18$^{h}$20$^{m}$00$^{s}$'])
        ylocs = np.array([68 + 20.0/60,68 + 25.0/60,68 + 30.0/60])
        ylabels = np.array(['68' + degree_symbol + "20'","25'","30'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
        icoff = 4
        for ic in range(0,1):
            plotcircle(RAcen=clusRA[ic+icoff],DECcen = clusDec[ic+icoff],rad=crads[ic+icoff])
            #pylab.text(clusRA[ic+icoff],clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold')
    if i == 2:
        #Cl0023
        pylab.xlim(6.17,5.77)
        pylab.ylim(4 + 13.6/60,4 + 32.36/60)
        xlocs = np.array([5.875,6.0,6.125])
        xlabs = np.array(['0$^{h}$23$^{m}$30$^{s}$','24$^{m}$00$^{s}$','30$^{s}$'])
        ylocs = np.array([4 + 15.0/60,4 + 20.0/60,4 + 25.0/60,4 + 30.0/60])
        ylabels = np.array(['4' + degree_symbol + "15'","20'","25'","30'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
        g = np.where(sz[gsq[gsz]] < 0.832)
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color=html_orng)
        g = np.where((sz[gsq[gsz]] >= 0.832) & (sz[gsq[gsz]] < 0.841))
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color='blue')
        g = np.where((sz[gsq[gsz]] >= 0.841) & (sz[gsq[gsz]] <= 0.855))
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color=html_teal)
        g = np.where(sz[gsq[gsz]] >= 0.855)
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color=html_pink)
        leg = pylab.legend(('0.82 < z < 0.832','0.832 < z < 0.841','0.841 < z < 0.855','0.855 < z < 0.87'),loc=3,markerscale=0.8,labelspacing=0.3)
        for t in leg.get_texts():
            t.set_fontsize('small') 
        icoff = 0
        for ic in range(0,4):
            plotcircle(RAcen=clusRA[ic+icoff],DECcen = clusDec[ic+icoff],rad=crads[ic+icoff])
            if ic == 0: pylab.text(clusRA[ic+icoff]+0.027,clusDec[ic+icoff]-0.01,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 1: pylab.text(clusRA[ic+icoff]+0.0,clusDec[ic+icoff]+0.02,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 2: pylab.text(clusRA[ic+icoff]+0.0,clusDec[ic+icoff]-0.03,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 3: pylab.text(clusRA[ic+icoff]-0.02,clusDec[ic+icoff]-0.0,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
    if i == 3:
        #Cl1604
        pylab.xlim(241.4,240.68)
        pylab.ylim(43+2.0/60,43+27.0/60)
        xlocs = np.array([240.75,240.875,241,241.125,241.25,241.375])
        xlabs = np.array(['16$^{h}$03$^{m}$00$^{s}$','30$^{s}$','04$^{m}$00$^{s}$','30$^{s}$','05$^{m}$00$^{s}$','30$^{s}$'])
        ylocs = np.array([43 + 5.0/60,43 + 10.0/60,43 + 15.0/60,43 + 20.0/60,43 + 25.0/60])
        ylabels = np.array(['43' + degree_symbol + "05'","10'","15'","20'","25'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
        g = np.where(sz[gsq[gsz]] < 0.857)
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color=html_pink)
        g = np.where((sz[gsq[gsz]] >= 0.857) & (sz[gsq[gsz]] < 0.885))
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color='blue')
        g = np.where((sz[gsq[gsz]] >= 0.885) & (sz[gsq[gsz]] < 0.91))
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color=html_teal)
        g = np.where((sz[gsq[gsz]] >= 0.91) & (sz[gsq[gsz]] < 0.93))
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color='green')
        g = np.where((sz[gsq[gsz]] >= 0.93) & (sz[gsq[gsz]] < 0.942))
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color=html_orng)
        g = np.where(sz[gsq[gsz]] >= 0.942)
        pylab.scatter(sRA[gsq[gsz[g]]],sDec[gsq[gsz[g]]],s=10,color=html_brwn)
        leg = pylab.legend(('0.84 < z < 0.857','0.857 < z < 0.885','0.885 < z < 0.91','0.91 < z < 0.93','0.93 < z < 0.942','0.942 < z < 0.96'),loc=4,markerscale=0.8,labelspacing=0.3)
        F = pylab.gcf()
        DefaultSize = F.get_size_inches()
        F.set_size_inches( (DefaultSize[0]*1.5, DefaultSize[1]*1.5))
        for t in leg.get_texts():
            t.set_fontsize('small')
        icoff = 15
        for ic in range(0,9):
            plotcircle(RAcen=clusRA[ic+icoff],DECcen = clusDec[ic+icoff],rad=crads[ic+icoff])
            if ic == 0: pylab.text(clusRA[ic+icoff]-0.03,clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
            if ic == 1: pylab.text(clusRA[ic+icoff]-0.017,clusDec[ic+icoff]-0.025,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19) 
            if ic == 2: pylab.text(clusRA[ic+icoff]-0.03,clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19) 
            if ic == 3: pylab.text(clusRA[ic+icoff],clusDec[ic+icoff]+0.018,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19) 
            if ic == 4: pylab.text(clusRA[ic+icoff]-0.003,clusDec[ic+icoff]-0.006,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19) 
            if ic == 5: pylab.text(clusRA[ic+icoff]+0.017,clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19) 
            if ic == 6: pylab.text(clusRA[ic+icoff]+0.012,clusDec[ic+icoff]+0.005,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19) 
            if ic == 7: pylab.text(clusRA[ic+icoff],clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19) 
            if ic == 8: pylab.text(clusRA[ic+icoff]-0.008,clusDec[ic+icoff]+0.004,str(cnam[ic+icoff]),color='black',weight='extra bold',size=19) 
            if ic == 9: pylab.text(clusRA[ic+icoff]-0.03,clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold',size=19)
    if i == 4:
        #RXJ1757
        pylab.xlim(269.75,269.0)
        pylab.ylim(66 + 24.0/60, 66+38.0/60)
        xlocs = np.array([269.625,269.5,269.375,269.25,269.125,269])
        xlabs = np.array(['30$^{s}$','58$^{m}$00$^{s}$','30$^{s}$','57$^{m}$00$^{s}$','30$^{s}$','17$^{h}$56$^{m}$00$^{s}$'])
        ylocs = np.array([66 + 25.0/60,66.5,66 + 35.0/60])
        ylabels = np.array(['66' + degree_symbol + "25'","30'","35'"])
        pylab.yticks(ylocs,ylabels)
        pylab.xticks(xlocs,xlabs)
        icoff = len(cnam)-1
        for ic in range(0,1):
            plotcircle(RAcen=clusRA[ic+icoff],DECcen = clusDec[ic+icoff],rad=crads[ic+icoff])
            #pylab.text(clusRA[ic+icoff],clusDec[ic+icoff],str(cnam[ic+icoff]),color='black',weight='extra bold')
    if ((i == 1) | (i > 3.1)) : pylab.scatter(sRA[gsq[gsz]],sDec[gsq[gsz]],s=10)
    FILE = open('/home/rumbaugh/paperstuff/input.RShist.%s.5.7.11.dat'%(names[i]),'w')
    for j in range(0,len(gsz)): FILE.write('%f %f %f\n'%(sRA[gsq[gsz[j]]],sDec[gsq[gsz[j]]],sz[gsq[gsz[j]]]))
    FILE.close()
    pylab.scatter(msRA[gmsq[gmsz]],msDec[gmsq[gmsz]],marker = 'd',s=40,c='red')
    FILE = open('/home/rumbaugh/paperstuff/AGN.locs.%s.5.7.11.dat'%(names[i]),'w')
    gzsort = np.argsort(msz[gmsq[gmsz]])
    for j in range(0,len(gmsz)):
        FILE.write('%2i %f %f %f\n'%(1+j,msRA[gmsq[gmsz[gzsort[j]]]],msDec[gmsq[gmsz[gzsort[j]]]],msz[gmsq[gmsz[gzsort[j]]]]))
        AGNstr = str(1+j)
        if ((i == 2) & ((j == 2) | (j == 6) | (j == 5) | (j == 4))):
            #Cl0023
            if j == 2: pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.000,msDec[gmsq[gmsz[gzsort[j]]]]+0.005,AGNstr,color='red',weight='extra bold',size=16)
            if j == 6: pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.003,msDec[gmsq[gmsz[gzsort[j]]]]-0.011,AGNstr,color='red',weight='extra bold',size=16)
            if j == 5: pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]+0.004,msDec[gmsq[gmsz[gzsort[j]]]]+0.005,AGNstr,color='red',weight='extra bold',size=16)
            if j == 4: pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]+0.003,msDec[gmsq[gmsz[gzsort[j]]]]-0.012,AGNstr,color='red',weight='extra bold',size=16)
        elif ((i == 0)):
            #Cl1324
            #AGNstr = str(j)
            if j == 0: pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.003,msDec[gmsq[gmsz[gzsort[j]]]]+0.003,AGNstr,color='red',weight='extra bold',size=16)
            if j == 1: pylab.text(msRA[gmsq[gmsz[gzsort[j]]]],msDec[gmsq[gmsz[gzsort[j]]]]+0.008,AGNstr,color='red',weight='extra bold',size=16)
            if j == 3: pylab.text(msRA[gmsq[gmsz[gzsort[j]]]],msDec[gmsq[gmsz[gzsort[j]]]]+0.008,AGNstr,color='red',weight='extra bold',size=16)
            if j == 4: pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]+0.004,msDec[gmsq[gmsz[gzsort[j]]]]-0.036,AGNstr,color='red',weight='extra bold',size=16)
            if j == 2: pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.011,msDec[gmsq[gmsz[gzsort[j]]]]-0.013,AGNstr,color='red',weight='extra bold',size=16)
            if j == 5: pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]+0.024,msDec[gmsq[gmsz[gzsort[j]]]]-0.008,AGNstr,color='red',weight='extra bold',size=16)
        elif i == 3:
            #Cl1604
            if j == 1:
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]+0.013,msDec[gmsq[gmsz[gzsort[j]]]]-0.006,AGNstr,color='red',weight='extra bold',size=16)
            elif (j == 9):
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]+0.022,msDec[gmsq[gmsz[gzsort[j]]]]-0.007,AGNstr,color='red',weight='extra bold',size=16)  
            elif (j == 2):
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.004,msDec[gmsq[gmsz[gzsort[j]]]]-0.009,AGNstr,color='red',weight='extra bold',size=16) 
            elif (j == 4):
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.008,msDec[gmsq[gmsz[gzsort[j]]]]-0.001,AGNstr,color='red',weight='extra bold',size=16) 
            elif (j == 5):
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]+0.004,msDec[gmsq[gmsz[gzsort[j]]]]+0.006,AGNstr,color='red',weight='extra bold',size=16) 
            elif (j == 6):
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.007,msDec[gmsq[gmsz[gzsort[j]]]]-0.00,AGNstr,color='red',weight='extra bold',size=16)
            elif (j == 7):
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.005,msDec[gmsq[gmsz[gzsort[j]]]]-0.00,AGNstr,color='red',weight='extra bold',size=16)
            elif (j == 8):
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.00,msDec[gmsq[gmsz[gzsort[j]]]]+0.006,AGNstr,color='red',weight='extra bold',size=16)
            else:
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.003,msDec[gmsq[gmsz[gzsort[j]]]]+0.003,AGNstr,color='red',weight='extra bold',size=16)
        elif (i == 1):
            #NEP5281
            if (j == 0): 
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]+0.008,msDec[gmsq[gmsz[gzsort[j]]]]+0.003,AGNstr,color='red',weight='extra bold',size=16) 
            if (j == 2): 
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]+0.011,msDec[gmsq[gmsz[gzsort[j]]]]+0.003,AGNstr,color='red',weight='extra bold',size=16)
            if (j == 1):
                pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.006,msDec[gmsq[gmsz[gzsort[j]]]]+0.001,AGNstr,color='red',weight='extra bold',size=16)
        elif (i == 4):
            #RXJ1757
            pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]+0.009,msDec[gmsq[gmsz[gzsort[j]]]]-0.013,AGNstr,color='red',weight='extra bold',size=16)
        else:
            pylab.text(msRA[gmsq[gmsz[gzsort[j]]]]-0.003,msDec[gmsq[gmsz[gzsort[j]]]]+0.003,AGNstr,color='red',weight='extra bold',size=16)  
    FILE.close()
    pylab.title('%s'%(names[i]))
    pylab.xlabel('Right Ascension (J2000)')
    pylab.ylabel('Declination (J2000)')
    savfile = '/home/rumbaugh/paperstuff/AGN.spatmap.color.%s.r_%3.1fMpc_nb.6.16.11.png'%(names[i],cradmult)
    pylab.savefig(savfile)
    pylab.close('all')
#FILEA.close()
    
