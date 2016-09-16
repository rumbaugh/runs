execfile("/home/rumbaugh/get_cols_batch.py")


names = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
mnames = ['Cl0023','Cl1604','Cl1324','NEP5281','NEP200']
sfiles = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.wh.cat']

for i in range(0,5):
    sfile = '/home/rumbaugh/' + sfiles[i]
    crs = read_file(sfile)
    if i != 1: LFCID,mask,slit,sra,sdec,sr,si,sz,sredshift,srerr,q,old_id = get_cols_batch(crs,12)
    if i == 1: LFCID,mask,slit,sra,sdec,sr,si,sz,sredshift,srerr,q,old_id,phot_flag,acsRA,acsDec,acsID,f606,f814 = get_cols_batch(crs,18)
    xpfile = '/scratch/rumbaugh/ciaotesting/' + names[i] + '/master/photometry/' + names[i] + '.xray_phot.soft_hard_full.dat'
    crxp = read_file(xpfile)
    xpRA,xpDec,sflux,hflux,fflux,sncnts,hncnts,fncnts,ssig,hsig,fsig,wssig,whsig,wfsig,wmask,wflag = get_cols_batch(crxp,16)
    mfile = '/home/rumbaugh/' + mnames[i] + '.opt_Xray_matched_catalog_3high.corrected.twk.8.4.11.dat'
    crm = read_file(mfile)
    XID,RAX,DecX,poserr,nm,ra_opt,dec_opt,optID,prob,rel,ra_opt2,dec_opt2,optID2,prob2,rel2,ra_opt3,dec_opt3,optID3,prob3,rel3,probnone,citemp,sigmax = get_cols_batch(crm,23)
    if i == 1: 
        isACS = get_colvals(crm,'col24')
        xpID = get_colvals(crm,'col25')
        xpIDt = np.zeros(len(xpID),dtype='int')
        for j in range(0,len(xpID)): xpIDt[j] = int(xpID[j])
        xpID = np.zeros(len(xpID),dtype='int')
        for j in range(0,len(xpID)): xpID[j] = int(xpIDt[j])
    XIDt = np.zeros(len(XID),dtype='int')
    for j in range(0,len(XID)): XIDt[j] = int(XID[j])
    XID = np.zeros(len(XID),dtype='int')
    for j in range(0,len(XID)): XID[j] = int(XIDt[j])
    if i != 1:
        gg2s = np.where((ssig > 2) | (hsig > 2) | (fsig > 2))
        gg3s = np.where((ssig > 3) | (hsig > 3) | (fsig > 3))
        gg2s = gg2s[0]
        gg3s = gg3s[0]
        gnm = np.where(nm > 0.1)
        gnm = gnm[0]
        gnm2 = np.where(nm[gg2s] > 0.1)
        gnm2 = gnm2[0]
        gnm3 = np.where(nm[gg3s] > 0.1)
        gnm3 = gnm3[0]
    else:
        gg2s = np.where((ssig[xpID] > 2) | (hsig[xpID] > 2) | (fsig[xpID] > 2))
        gg3s = np.where((ssig[xpID] > 3) | (hsig[xpID] > 3) | (fsig[xpID] > 3))
        gg2s = gg2s[0]
        gg3s = gg3s[0]
        gnm = np.where(nm > 0.1)
        gnm = gnm[0]
        gnm2 = np.where(nm[gg2s] > 0.1)
        gnm2 = gnm2[0]
        gnm3 = np.where(nm[gg3s] > 0.1)
        gnm3 = gnm3[0]
    cnt = 0
    cntq = 0
    for j in range(0,len(XID)):
        if nm[j] > 0.1: 
            if ((i == 1) | (i == 2) | (i == 3)): gid = np.where(LFCID == str(optID[j]))
            if ((i == 0) | (i == 4)): gid = np.where(LFCID == int(optID[j]))
            if len(gid[0]) > 0.1: 
                cnt += 1
                gid = gid[0]
                if ((q[gid[0]] > 2.3) or (q[gid[0]] < -0.2)): cntq += 1
            elif ((i == 1) & (str(optID[j]) != '0.0')):
                if isACS == 1: gid = np.where(acsID == int(float(optID[j])))
                if isACS == 0: gid = np.where(acsID == optID[j])
                if len(gid) > 0.1:
                    if len(gid[0]) > 0.1: 
                        cnt += 1
                        gid = gid[0]
                        if ((q[gid[0]] > 2.3) or (q[gid[0]] < -0.2)): cntq += 1
            
    cnt2 = 0
    cntq2 = 0
    for j in range(0,len(gg2s)):
        if nm[gg2s[j]] > 0.1: 
            if ((i == 1) | (i == 2) | (i == 3)): gid = np.where(LFCID == str(optID[gg2s[j]]))
            if ((i == 0) | (i == 4)): gid = np.where(LFCID == int(optID[gg2s[j]]))
            if len(gid[0]) > 0.1: 
                cnt2 += 1
                gid = gid[0]
                if ((q[gid[0]] > 2.3) or (q[gid[0]] < -0.2)): cntq2 += 1
            elif ((i == 1) & (str(optID[gg2s[j]]) != '0.0')):
                gid = np.where(acsID == int(float(optID[gg2s[j]])))
                if len(gid) > 0.1:
                    if len(gid[0]) > 0.1: 
                        cnt2 += 1
                        gid = gid[0]
                        if ((q[gid[0]] > 2.3) or (q[gid[0]] < -0.2)): cntq2 += 1
    cnt3 = 0
    cntq3 = 0
    for j in range(0,len(gg3s)):
        if nm[j] > 0.1: 
            if ((i == 1) | (i == 2) | (i == 3)): gid = np.where(LFCID == str(optID[gg3s[j]]))
            if ((i == 0) | (i == 4)): gid = np.where(LFCID == int(optID[gg3s[j]]))
            if len(gid[0]) > 0.1: 
                cnt3 += 1
                gid = gid[0]
                if ((q[gid[0]] > 2.3) or (q[gid[0]] < -0.2)): cntq3 += 1
            elif ((i == 1) & (str(optID[gg3s[j]]) != '0.0')):
                gid = np.where(acsID == int(float(optID[gg3s[j]])))
                if len(gid) > 0.1:
                    if len(gid[0]) > 0.1: 
                        cnt3 += 1
                        gid = gid[0]
                        if ((q[gid[0]] > 2.3) or (q[gid[0]] < -0.2)): cntq3 += 1
        
        
        
    print '%s:\nX-ray sources with det. sig. > 2sig: %i\nX-ray sources with det. sig. > 3sig: %i\nX-ray sources match to opt. sources: %i\nX-ray sources match to opt. sources (> 2s): %i\nX-ray sources match to opt. sources( > 3s): %i\nAttempted Redshifts: %i\nAttempted Redshifts(>2s): %i\nAttempted Redshifts(>3s): %i\nConfirmed Redshifts: %i\nConfirmed Redshifts(>2s): %i\nConfirmed Redshifts(>3s): %i\n'%(names[i],len(gg2s),len(gg3s),len(gnm),len(gnm2),len(gnm3),cnt,cntq,cnt2,cntq2,cnt3,cntq3)
