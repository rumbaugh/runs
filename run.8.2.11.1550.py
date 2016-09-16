execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/get_cols_batch.py")

msfiles = np.array(['FINAL.matched.0023.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat','FINAL.matched.1604.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.N200.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat'])
names = np.array(['Cl0023','Cl1324','Cl1604','RXJ1757','NEP5281'])
mpath = '/scratch/rumbaugh/ciaotesting/'
pname = '.xray_phot.soft_hard_full.dat'


for i in range(0,5):
    FILE = open('/home/rumbaugh/%s.Xray_phot_spec_matched.cat'%names[i],'w')
    if i != 2: FILE.write("# LFC_ID    mask    slit    RA_opt    Dec_opt    r'    i'    z'    z    zerr    q    oldID    Xray_ID    RA_Xray    Dec_Xray    Xray_poserr    Num_opt_matches    Rel    Xflux_soft    Xflux_hard    Xflux_full    Xnetcnts_soft    Xnetcnt_hard    Xnetcnt_full    sig_soft    sig_hard    sig_full    wavdetsig_soft    wavdetsig_hard    wavdetsig_full    wmask    wflag\n")
    if i == 2: FILE.write("# LFC_ID    mask    slit    RA_opt    Dec_opt    r'    i'    z'    z    zerr    q    oldID    maskACS    RA_ACS  	dec_ACS 	ACS_ID  F606W      F814W     Xray_ID    RA_Xray    Dec_Xray    Xray_poserr    Num_opt_matches    Rel    Xflux_soft    Xflux_hard    Xflux_full    Xnetcnts_soft    Xnetcnt_hard    Xnetcnt_full    sig_soft    sig_hard    sig_full    wavdetsig_soft    wavdetsig_hard    wavdetsig_full    wmask    wflag\n")
    mfile = mpath + names[i] + '/master/opt_match/opt_Xray_matched_catalog_3high.corrected.twk.dat'
    crms = read_file('/home/rumbaugh/LFC/' + msfiles[i])
    if i != 2: LFC_ID,mask,slit,RA_opt,Dec_opt,rb,ib,zb,z,zerr,q,oldID,XID,msRAX,msDecX,poserr,Num_opt,Rel,Sig = get_cols_batch(crms,19)
    if i == 2: LFC_ID,mask,slit,RA_opt,Dec_opt,rb,ib,zb,z,zerr,q,oldID,maskACS,RA_ACS,dec_ACS,ACS_ID,F606W,F814W,XID,msRAX,msDecX,poserr,Num_opt,Rel,Sig = get_cols_batch(crms,25)
    pfile = mpath + names[i] + '/master/photometry/' + names[i] + pname
    crp = read_file(pfile)
    RAX,DecX,sflux,hflux,fflux,ncnts,ncnth,ncntf,sigs,sigh,sigf,wsigs,wsigh,wsigf,wmask,wflag = get_cols_batch(crp,16)
    for j in range(0,len(msRAX)):
        g = FindCloseSources(msRAX[j],msDecX[j],1,RAX,DecX,0)
        if len(g) < 0.5: sys.exit("No match")
        g = g[0]
        if g == -1: sys.exit("No match (-1)")
        if i == 2: FILE.write(str(LFC_ID[j]) + '  ' + str(mask[j]) + '  ' + str(slit[j]) + '  ' + str(RA_opt[j]) + '  ' + str(Dec_opt[j]) + '  ' + str(rb[j]) + '  ' + str(ib[j]) + '  ' + str(zb[j]) + '  ' + str(z[j]) + '  ' + str(zerr[j]) + '  ' + str(q[j]) + '  ' + str(oldID[j]) + '  ' + str(maskACS[j]) + '  ' + str(RA_ACS[j]) + '  ' + str(dec_ACS[j]) + '  ' + str(ACS_ID[j]) + '  ' + str(F606W[j]) + '  ' + str(F814W[j]) + '  ' + str(XID[j]) + '  ' + str(msRAX[j]) + '  ' + str(msDecX[j]) + '  ' + str(poserr[j]) + '  ' + str(Num_opt[j]) + '  ' + str(Rel[j]) + '  ' + str(sflux[g]) + '  ' + str(hflux[g]) + '  ' + str(fflux[g]) + '  ' + str(ncnts[g]) + '  ' + str(ncnth[g]) + '  ' + str(ncntf[g]) + '  ' + str(sigs[g]) + '  ' + str(sigh[g]) + '  ' + str(sigf[g]) + '  ' + str(wsigs[g]) + '  ' + str(wsigh[g]) + '  ' + str(wsigf[g]) + '  ' + str(wmask[g]) + '  ' + str(wflag[g]) + '\n')
        if i != 2: FILE.write(str(LFC_ID[j]) + '  ' + str(mask[j]) + '  ' + str(slit[j]) + '  ' + str(RA_opt[j]) + '  ' + str(Dec_opt[j]) + '  ' + str(rb[j]) + '  ' + str(ib[j]) + '  ' + str(zb[j]) + '  ' + str(z[j]) + '  ' + str(zerr[j]) + '  ' + str(q[j]) + '  ' + str(oldID[j]) + '  ' + str(XID[j]) + '  ' + str(msRAX[j]) + '  ' + str(msDecX[j]) + '  ' + str(poserr[j]) + '  ' + str(Num_opt[j]) + '  ' + str(Rel[j]) + '  ' + str(sflux[g]) + '  ' + str(hflux[g]) + '  ' + str(fflux[g]) + '  ' + str(ncnts[g]) + '  ' + str(ncnth[g]) + '  ' + str(ncntf[g]) + '  ' + str(sigs[g]) + '  ' + str(sigh[g]) + '  ' + str(sigf[g]) + '  ' + str(wsigs[g]) + '  ' + str(wsigh[g]) + '  ' + str(wsigf[g]) + '  ' + str(wmask[g]) + '  ' + str(wflag[g]) + '\n')
    FILE.close()
    
    

    
    
    
