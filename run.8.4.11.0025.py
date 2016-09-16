execfile("FindCloseSources.py")
execfile("get_cols_batch.py")

names = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
msfiles = ['FINAL.matched.0023.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.1604.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat','FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat','FINAL.matched.N200.specnXray.nov2010.rumbaugh.noheader.cat']
#mfiles = ['Cl0023.opt_Xray_matched_catalog_3high.corrected.twk.11.16.10.dat','public_html/outgoing/Cl1604.opt_Xray_matched_catalog_3high.corrected.twk.11.16.10.dat','public_html/outgoing/Cl1324.opt_Xray_matched_catalog_3high.corrected.twk.11.22.10.dat','public_html/outgoing/NEP5281.opt_Xray_matched_catalog_3high.corrected.twk.11.22.10.dat','public_html/outgoing/NEP200.opt_Xray_matched_catalog_3high.corrected.twk.11.19.10.dat']
mfiles = ['Cl0023.opt_match.correct1.dat','public_html/outgoing/Cl1604.opt_Xray_matched_catalog_3high.corrected.twk.11.16.10.dat','Cl1324.opt_Xray_matched_catalog_3high.corrected.twk.11.22.10.dat','public_html/outgoing/NEP5281.opt_Xray_matched_catalog_3high.corrected.twk.11.22.10.dat','public_html/outgoing/NEP200.opt_Xray_matched_catalog_3high.corrected.twk.11.19.10.dat']

for i in range(0,5):
    crm = read_file("/home/rumbaugh/" + mfiles[i])
    crms = read_file("/home/rumbaugh/LFC/" + msfiles[i])
    XrayID,RAX,DecX,poserr,nm = get_cols_batch(crm,5)
    if i != 1: LFC_ID,mask,slit,RA_opt,dec_opt,rb, ib,zb,rs, z_err,q,old_ID, Xray_ID,RA_Xray,dec_Xray,poserr,Num_opt,Rel,Sig = get_cols_batch(crms,19)
    if i == 1: LFC_ID,mask,slit,RA_opt,dec_opt,rb, ib,zb,rs, z_err,q,old_ID, maskACS,RA_ACS,dec_ACS,ACS_ID, F606W,F814W,Xray_ID,RA_Xray,dec_Xray,poserr,Num_opt,Rel,Sig = get_cols_batch(crms,25)
    for j in range(0,len(LFC_ID)):
        g = FindCloseSources(RA_Xray[j],dec_Xray[j],0.5,RAX,DecX,0)
        if len(g) > 1: sys.exit("len(g) > 1")
        g = g[0]
        if g == -1: sys.exit("g = -1")
        #print nm[g]
        if nm[g] < 0.1: print names[i],LFC_ID[j],RAX[g],RA_Xray[j],DecX[g],dec_Xray[j],XrayID[g],Xray_ID[j],rs[j],Num_opt[j],nm[g]
        print RA_Xray[j]-RAX[g]
