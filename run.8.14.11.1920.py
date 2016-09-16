execfile("/home/rumbaugh/get_cols_batch.py")
names = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
names2 = ['0023','1604','1322','N5281','N200']
sfiles = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat']
zlb = [0.82,0.84,0.65,0.8,0.68]
zub = [0.87,0.96,0.79,0.84,0.71]

for i in range(0,len(names)):
    FILE = open("/home/rumbaugh/ChandraData/%s/master/spectargets.reg"%(names[i]),'w')
    FILE.write('# Region file format: DS9 version 4.1\nglobal color=green dashlist=8 3 width=1 font="helvetica 10 normal" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
    sfile = '/home/rumbaugh/' + sfiles[i]
    crs = read_file(sfile)
    lid,lmask,sli,sRA,sDec,rb,ib,zb,rs,rse,sq = get_cols_batch(crs,11)
    for j in range(0,len(sq)):
        FILE.write('circle(%f,%f,4") # color=black width=4\n'%(sRA[j],sDec[j]))
    msfile = '/home/rumbaugh/LFC/FINAL.matched.%s.specnXray.nov2010.rumbaugh.noheader.cat'%(names2[i])
    crms = read_file(msfile)
    li,mask,slit,msRA,msDec,rb,ib,zb,msz,ze,msq = get_cols_batch(crms,11)
    for j in range(0,len(msq)):
        if ((msz[j] > zlb[i]) & (msz[j] < zub[i]) &(msq[j] > 2.3)): FILE.write('circle(%f,%f,5") # color=cyan width=4\ncircle(%f,%f,50") # color=cyan width=4\n'%(msRA[j],msDec[j],msRA[j],msDec[j]))
    FILE.close()
    
