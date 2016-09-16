execfile("/home/rumbaugh/get_cols_batch.py")
execfile("/home/rumbaugh/FindCloseSources.py")
names = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
names2 = ['0023','1604','1322','N5281','N200']
sfiles = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat']
pfiles = ['/home/rumbaugh/LFC/cl0023_radecIDmags.cat',"/home/rumbaugh/LFC/final.idradecmag.lfcpluscosmic.withsdss.cat","/home/rumbaugh/LFC/sc1322.lfc.newIDsandoldIds.radecmag.cat","/home/rumbaugh/LFC/nep5281.lfc.newIDradecmag.cat","/home/rumbaugh/LFC/nep200.idradecmag.lfc.uhcorr.neat"]
pACS = '/home/rumbaugh/LFC/ACS_merged.F606W+F814W_deep.all.coll.nh.dat'
zlb = [0.82,0.84,0.65,0.8,0.68]
zub = [0.87,0.96,0.79,0.84,0.71]
FILE2 = open('/home/rumbaugh/zs.temp.8.16.11.dat','w')
crcc = read_file("/home/rumbaugh/cout.temp.8.16.11.nh.dat")
oneAS = get_colvals(crcc,'col11')/0.7

AGNcnt = 0

for i in range(0,len(names)):
    crp = read_file(pfiles[i])
    if i != 2: pID,pra,pdec,pR,pI,pZ = get_cols_batch(crp,6)
    if i == 2: pID,oldpID,pra,pdec,pR,pI,pZ = get_cols_batch(crp,7)
    if i == 1:
        crpACS = read_file(pACS)
        praACS,pdecACS,p606,p814,d606,d814,rh606,rh814,c606,c814 = get_cols_batch(crpACS,10)
    FILE = open("/home/rumbaugh/ChandraData/%s/master/photsources_spectargets.reg"%(names[i]),'w')
    FILE.write('# Region file format: DS9 version 4.1\nglobal color=green dashlist=8 3 width=1 font="helvetica 10 normal" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
    sfile = '/home/rumbaugh/' + sfiles[i]
    crs = read_file(sfile)
    lid,lmask,sli,sRA,sDec,rb,ib,zb,rs,rse,sq = get_cols_batch(crs,11)
    for j in range(0,len(pra)):
        FILE.write('circle(%f,%f,2") # color=white width=2\n'%(pra[j],pdec[j]))
    if i == 1:
        for j in range(0,len(praACS)):
            FILE.write('circle(%f,%f,2.2") # color=blue width=2\n'%(praACS[j],pdecACS[j]))
    for j in range(0,len(sq)):
        FILE.write('circle(%f,%f,4") # color=black width=4\n'%(sRA[j],sDec[j]))
    msfile = '/home/rumbaugh/LFC/FINAL.matched.%s.specnXray.nov2010.rumbaugh.noheader.cat'%(names2[i])
    crms = read_file(msfile)
    li,mask,slit,msRA,msDec,rb,ib,zb,msz,ze,msq = get_cols_batch(crms,11)
    for j in range(0,len(msq)):
        if ((msz[j] > zlb[i]) & (msz[j] < zub[i]) &(msq[j] > 2.3)): 
            numphots = np.zeros(5)
            numphotsACS = np.zeros(5)
            numphotstot = np.zeros(5)
            radii = [25.0,50,100,200,300,400,500,750,1000]/oneAS[AGNcnt]
            cis = FindCloseSources(msRA[j],msDec[j],radii[4],sRA,sDec,0)
            print "\n"
            dists = np.zeros(len(cis))
            for k in range(0,len(cis)):
                dists[k] = SphDist(msRA[j],msDec[j],sRA[cis[k]],sDec[cis[k]])
            cissort = np.argsort(dists)
            for k in range(0,len(cis)):
                print '%7.5f  %i  %9.5f %8.5f  %5.1f  %s'%(rs[cis[cissort[k]]],sq[cis[cissort[k]]],sRA[cis[cissort[k]]],sDec[cis[cissort[k]]],dists[cissort[k]]*60*oneAS[AGNcnt],lid[cis[cissort[k]]])
            for k in radii: FILE.write('circle(%f,%f,%f") # color=cyan width=4\n'%(msRA[j],msDec[j],k))
            FILE2.write('%f\n'%(msz[j]))
            ci = FindCloseSources(msRA[j],msDec[j],radii[4],pra,pdec,0)
            for k in range(0,len(ci)):
                sdtemp = SphDist(pra[ci[k]],pdec[ci[k]],msRA[j],msDec[j])*60
                for l in range(0,5): 
                    if sdtemp < radii[l]: numphots[l] += 1
                if i == 1:
                    ciACS = FindCloseSources(pra[ci[k]],pdec[ci[k]],2,praACS,pdecACS,0)
                    if len(ciACS) == 0: 
                        for l in range(0,5): 
                            if sdtemp < radii[l]: numphotstot[l] += 1
            if i == 1: 
                ci = FindCloseSources(msRA[j],msDec[j],radii[4],praACS,pdecACS,0)
                for k in range(0,len(ci)):
                    sdtemp = SphDist(praACS[ci[k]],pdecACS[ci[k]],msRA[j],msDec[j])*60
                    for l in range(0,5): 
                        if sdtemp < radii[l]: 
                            numphotsACS[l] += 1
                            numphotstot[l] += 1
            #print '%7.5f  Num. within (kpc):\n25:  %i\n50:  %i\n100:  %i\n200:  %i\n300:  %i\n'%(msz[j],numphots[0]-1,numphots[1]-1,numphots[2]-1,numphots[3]-1,numphots[4]-1)
            #if i == 1:
                #print '%7.5f  Num. within (ACS):\n25:  %i\n50:  %i\n100:  %i\n200:  %i\n300:  %i\n'%(msz[j],numphotsACS[0]-1,numphotsACS[1]-1,numphotsACS[2]-1,numphotsACS[3]-1,numphotsACS[4]-1)
                #print '%7.5f  Num. within (tot):\n25:  %i\n50:  %i\n100:  %i\n200:  %i\n300:  %i\n'%(msz[j],numphotstot[0]-1,numphotstot[1]-1,numphotstot[2]-1,numphotstot[3]-1,numphotstot[4]-1)
            AGNcnt += 1
    FILE.close()
FILE2.close()
    
