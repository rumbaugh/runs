execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/get_cols_batch.py")

crWN = read_file("/home/rumbaugh/LFC/ACSboundaries.dat")
boundRAs = get_colvals(crWN,'col1')
boundDecs = get_colvals(crWN,'col2')
boundRAs = np.append(boundRAs,boundRAs[0])
boundDecs = np.append(boundDecs,boundDecs[0])

cr = read_file("/home/rumbaugh/Cl1604.opt_Xray_matched_catalog_3high.corrected.twk.8.4.11.dat.backup")
XID,RAX,DecX,poserr,nm,ra_opt,dec_opt,optID,prob,rel,ra_opt2,dec_opt2,optID2,prob2,rel2,ra_opt3,dec_opt3,optID3,prob3,rel3,probnone,citemp,sigmax = get_cols_batch(cr,23)
cr2 = read_file("/home/rumbaugh/Cl1604.opt_Xray_matched_catalog_3high.corrected.twk.8.4.11.dat")
inACS = get_colvals(cr2,'col24')
FILE = open("/home/rumbaugh/Cl1604.opt_Xray_matched_catalog_3high.corrected.twk.8.4.11.dat.test",'w')
cnt = 0
xpfile = '/scratch/rumbaugh/ciaotesting/Cl1604/master/photometry/Cl1604.xray_phot.soft_hard_full.dat'
crxp = read_file(xpfile)
xpRA,xpDec,sflux,hflux,fflux,sncnts,hncnts,fncnts,ssig,hsig,fsig,wssig,whsig,wfsig,wmask,wflag = get_cols_batch(crxp,16)
for i in range(0,len(XID)):
    #WN = WindingNum(RAX[i],DecX[i],boundRAs,boundDecs)
    #WNflag = 0
    #if ((WN < -0.1) | (WN > 0.1)): WNflag = 1
    while (SphDist(xpRA[cnt],xpDec[cnt],RAX[i],DecX[i])*60 > 1.0): cnt += 1
    smt = ssig[cnt]
    if hsig[cnt] > smt: smt = hsig[cnt]
    if fsig[cnt] > smt: smt = fsig[cnt]
    FILE.write('%3i %9.5f %9.5f %8.5f %2i %9.5f %9.5f %15s %6.3f %7.1f %9.5f %9.5f %15s %6.3f %7.1f %9.5f %9.5f %15s %6.3f %7.1f %6.3f %3i %3.1f %1i %3i\n'%(int(XID[i]),RAX[i],DecX[i],poserr[i],int(nm[i]),ra_opt[i],dec_opt[i],optID[i],prob[i],rel[i],ra_opt2[i],dec_opt2[i],optID2[i],prob2[i],rel2[i],ra_opt3[i],dec_opt3[i],optID3[i],prob3[i],rel3[i],probnone[i],int(citemp[i]),smt,inACS[i],cnt))
    cnt += 1
    #cnt tells you what line in the Xray phot cat this source corresponds to
FILE.close()
