execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/get_cols_batch.py")

crWN = read_file("/home/rumbaugh/LFC/ACSboundaries.dat")
boundRAs = get_colvals(crWN,'col1')
boundDecs = get_colvals(crWN,'col2')
boundRAs = np.append(boundRAs,boundRAs[0])
boundDecs = np.append(boundDecs,boundDecs[0])

crp = read_file("/scratch/rumbaugh/ciaotesting/Cl1604/master/photometry/Cl1604.xray_phot.soft_hard_full.dat")
pRA,pDec = get_cols_batch(crp,2)
pcnt = 0
cr = read_file("/home/rumbaugh/Cl1604.opt_Xray_matched_catalog_3high.corrected.twk.8.4.11.dat")
XID,RAX,DecX,poserr,nm,ra_opt,dec_opt,optID,prob,rel,ra_opt2,dec_opt2,optID2,prob2,rel2,ra_opt3,dec_opt3,optID3,prob3,rel3,probnone,citemp,sigmax = get_cols_batch(cr,23)
FILE = open("/home/rumbaugh/Cl1604.opt_Xray_matched_catalog_3high.corrected.twk.8.4.11.dat.test",'w')
for i in range(0,len(XID)):
    WN = WindingNum(RAX[i],DecX[i],boundRAs,boundDecs)
    WNflag = 0
    if ((WN < -0.1) | (WN > 0.1)): WNflag = 1
    while ((pRA[pcnt] > RAX[pcnt] + 0.00001))L:
    FILE.write('%3i %9.5f %9.5f %8.5f %2i %9.5f %9.5f %15s %6.3f %7.1f %9.5f %9.5f %15s %6.3f %7.1f %9.5f %9.5f %15s %6.3f %7.1f %6.3f %3i %3.1f %i\n'%(int(XID[i]),RAX[i],DecX[i],poserr[i],int(nm[i]),ra_opt[i],dec_opt[i],optID[i],prob[i],rel[i],ra_opt2[i],dec_opt2[i],optID2[i],prob2[i],rel2[i],ra_opt3[i],dec_opt3[i],optID3[i],prob3[i],rel3[i],probnone[i],int(citemp[i]),sigmax[i],WNflag))
    pcnt += 1
FILE.close()
