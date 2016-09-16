
names = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
mnames = ['Cl0023','Cl1604','Cl1324','NEP5281','NEP200']
sfiles = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.wh.cat']
pnames = ['/home/rumbaugh/LFC/cl0023_radecIDmags.cat',"/home/rumbaugh/LFC/final.idradecmag.lfcpluscosmic.withsdss.cat","/home/rumbaugh/LFC/sc1322.lfc.newIDsandoldIds.radecmag.cat","/home/rumbaugh/LFC/nep5281.lfc.newIDradecmag.cat","/home/rumbaugh/LFC/nep200.idradecmag.lfc.uhcorr.neat"]
pACS1604 = "/home/rumbaugh/LFC/ACS_merged.F606W+F814W_deep.all.coll.nh.dat"
;pnames = ['/home/rumbaugh/LFC/cl0023_radecIDmags.cat',"/home/rumbaugh/LFC/ACS_merged.F606W+F814W_deep.all.coll.nh.dat","/home/rumbaugh/LFC/sc1322.lfc.newIDsandoldIds.radecmag.cat","/home/rumbaugh/LFC/nep5281.lfc.newIDradecmag.cat","/home/rumbaugh/LFC/nep200.idradecmag.lfc.uhcorr.neat"]
openw,2,"/home/rumbaugh/Xray_opt_spec_matching.summary.dat"
printf,2,'# Structure    sig>2    sig>3   matched2opt   mtchd2opt_>2sig   mtchd2opt_>3sig    targeted    targeted_>2sig   targeted_>3sig   goodz   goodz_>2sig   goodz_>3sig'
for i=0,4 do begin &$
if ((i ne 2)) then readcol,pnames[i],pID,pra,pdec,pR,pI,pZ,format='A,D,D,D,D,D',/silent &$
if ((i eq 2)) then readcol,pnames[i],pID,oldpID,pra,pdec,pR,pI,pZ,format='A,I,D,D,D,D,D',/silent &$
if i eq 1 then readcol,pACS1604,praACS,pdecACS,p606,p814,d606,d814,rh606,rh814,c606,c814,format='D,D,D,D,D,D,D,D,D,D',/silent &$
    sfile = '/home/rumbaugh/' + sfiles[i] &$
    if i ne 1 then readcol,sfile,LFCID,mask,slit,sra,sdec,sr,si,sz,sredshift,srerr,q,old_id,format='A,A,A,D,D,D,D,D,D,D,D,A,A',/silent &$
    if i eq 1 then readcol,sfile, LFCID,mask,slit,sra,sdec,sr,si,sz,sredshift,srerr,q,old_id,maskACS,acsRA,acsDec,acsID,f606,f814,format='A,A,A,D,D,D,D,D,D,D,D,A,A,D,D,A,D,D',/silent &$
    xpfile = '/scratch/rumbaugh/ciaotesting/' + names[i] + '/master/photometry/' + names[i] + '.xray_phot.soft_hard_full.dat' &$
    readcol,xpfile,xpRA,xpDec,sflux,hflux,fflux,sncnts,hncnts,fncnts,ssig,hsig,fsig,wssig,whsig,wfsig,wmask,wflag,format='D,D,F,F,F,D,D,D,D,D,D,D,D,D,I,I',/silent &$
    mfile = '/home/rumbaugh/' + mnames[i] + '.opt_Xray_matched_catalog_3high.corrected.twk.8.8.11.dat' &$
    if i ne 1 then readcol,mfile,XID,RAX,DecX,poserr,nm,ra_opt,dec_opt,optID,prob,rel,ra_opt2,dec_opt2,optID2,prob2,rel2,ra_opt3,dec_opt3,optID3,prob3,rel3,probnone,citemp,sigmax,format='I,D,D,D,I,D,D,A,D,D,D,D,A,D,D,D,D,A,D,D,D,D,D',/silent &$
if i eq 1 then readcol,mfile,XID,RAX,DecX,poserr,nm,ra_opt,dec_opt,optID,prob,rel,ra_opt2,dec_opt2,optID2,prob2,rel2,ra_opt3,dec_opt3,optID3,prob3,rel3,probnone,citemp,sigmax,inACS,xpID,format='I,D,D,D,I,D,D,A,D,D,D,D,A,D,D,D,D,A,D,D,D,D,D,I,I',/silent &$
        if i ne 1 then gg2s = where((ssig gt 2) or (hsig gt 2) or (fsig gt 2)) &$
        if i ne 1 then gg3s = where((ssig gt 3) or (hsig gt 3) or (fsig gt 3)) &$
        if i eq 1 then gg2s = where((ssig[xpID] gt 2) or (hsig[xpID] gt 2) or (fsig[xpID] gt 2)) &$
        if i eq 1 then gg3s = where((ssig[xpID] gt 3) or (hsig[xpID] gt 3) or (fsig[xpID] gt 3)) &$
        gnm = where(nm gt 0.1) &$
        gnt = gnm &$
        gnm2 = where(nm[gg2s] gt 0.1) &$
        gnm3 = where(nm[gg3s] gt 0.1) &$
cnttar = 0 &$
cntgood = 0 &$
cnttar2 = 0 &$
cntgood2 = 0 &$
cnttar3 = 0 &$
cntgood3 = 0 &$
openw,1,'/home/rumbaugh/matched.' + names[i] + '.Xray_opt_spec.8.7.11.cat' &$
if i ne 1 then printf,1,"# Xray_ID   Xray_RA   Xray_Dec   poserr    ncnts_soft   ncnts_hard   ncnts_full flux_soft   flux_hard   flux_full   sig_soft   sig_hard   sig_full   num_opt_matches   opt_ID   mask   slit   opt_RA   opt_Dec   q      z      z_err   r'      i'      z'     prob_match   prob_no_match" &$
if i eq 1 then printf,1,"# Xray_ID   Xray_RA   Xray_Dec   poserr    ncnts_soft   ncnts_hard   ncnts_full flux_soft   flux_hard   flux_full   sig_soft   sig_hard   sig_full   num_opt_matches   opt_ID   mask   slit   opt_RA   opt_Dec   q      z      z_err   r'      i'      z'    f606    f814    prob_match   prob_no_match   isinACS" &$
for j=0,n_elements(XID)-1 do begin &$
   ; On these, the primary source had no spectroscopy,
   ; but the secondary did, and we matched to the secondary
   ;if ((i eq 3) and (XID[j] eq 103)) then optID[j] = optID2[j]
   ;if ((i eq 3) and (XID[j] eq 103)) then ra_opt[j] = ra_opt2[j]
   ;if ((i eq 3) and (XID[j] eq 103)) then dec_opt[j] = dec_opt2[j]
   ;if ((i eq 3) and (XID[j] eq 103)) then prob[j] = prob2[j]
   ;if ((i eq 1) and (XID[j] eq 231)) then optID[j] = optID2[j]
   ;if ((i eq 1) and (XID[j] eq 231)) then ra_opt[j] = ra_opt2[j]
   ;if ((i eq 1) and (XID[j] eq 231)) then dec_opt[j] = dec_opt2[j]
   ;if ((i eq 1) and (XID[j] eq 231)) then prob[j] = prob2[j]
   ;if ((i eq 0) and (XID[j] eq 88)) then optID[j] = optID2[j]
   ;if ((i eq 0) and (XID[j] eq 88)) then ra_opt[j] = ra_opt2[j]
   ;if ((i eq 0) and (XID[j] eq 88)) then dec_opt[j] = dec_opt2[j]
   ;if ((i eq 0) and (XID[j] eq 88)) then prob[j] = prob2[j]
   gid = -1 &$
   gpid = -1 &$
   gpidACS = -1 &$
   gidt2 = -1 &$
   gidt22 = -1 &$
   gid2 = -1 &$
   gpid = where(pID eq optID[j]) &$
   if ((i ne 1) and (nm[j] gt 0.1)) then gid = where(LFCID eq optID[j]) &$
   if ((i eq 1) and (nm[j] gt 0.1)) then gid = where(acsID eq optID[j]) &$
   if ((i eq 1) and (nm[j] gt 0.1)) then gidt2 = where(LFCID eq optID[j]) &$
   if ((i eq 1) and (nm[j] gt 0.1) and (gidt2[0] gt -0.1)) then gid = gidt2 &$    &$
   if ((i ne 1) and (nm[j] gt 1.1)) then gid2 = where(LFCID eq optID2[j]) &$
   if ((i eq 1) and (nm[j] gt 1.1)) then gid2 = where(acsID eq optID2[j]) &$
   if ((i eq 1) and (nm[j] gt 1.1)) then gidt22 = where(LFCID eq optID2[j]) &$
   if ((i eq 1) and (nm[j] gt 1.1) and (gidt22[0] gt -0.1)) then gid2 = gidt22 &$    &$
   if ((gid2[0] gt -0.1) and (gid[0] lt -0.1))  then optID[j] = optID2[j] &$
   if ((gid2[0] gt -0.1) and (gid[0] lt -0.1))  then ra_opt[j] = ra_opt2[j] &$
   if ((gid2[0] gt -0.1) and (gid[0] lt -0.1))  then dec_opt[j] = dec_opt2[j] &$
   if ((gid2[0] gt -0.1) and (gid[0] lt -0.1))  then prob[j] = prob2[j] &$
   if ((gid2[0] gt -0.1) and (gid[0] lt -0.1))  then gid = gid2 &$
   if ((nm[j] gt 0.1) and (gid[0] gt -0.1)) then gpid = where(pID eq optID[j]) &$
   ;print,j,' ',optID[j] &$
   if ((i eq 1) and (nm[j] gt 0.1) and (gpid[0] lt -0.1)) then gpidACS = long(float(optID[j]))-2 &$
   ;print,j,' ',optID[j] &$
   if ((nm[j] gt 0.1) and (gid[0] gt -0.1)) then cnttar++ &$
   if ((nm[j] gt 0.1) and (gid[0] gt -0.1) and ((q[gid[0]] gt 2.3) or (q[gid[0]] lt -0.3))) then cntgood++ &$
   if ((nm[j] gt 0.1) and (gid[0] gt -0.1) and (sigmax[j] gt 3.0)) then cnttar3++ &$
   if ((nm[j] gt 0.1) and (gid[0] gt -0.1) and (sigmax[j] gt 3.0) and ((q[gid[0]] gt 2.3) or (q[gid[0]] lt -0.3))) then cntgood3++ &$
   if ((nm[j] gt 0.1) and (gid[0] gt -0.1) and ((sigmax[j] gt 2.0))) then cnttar2++ &$
   if ((nm[j] gt 0.1) and (gid[0] gt -0.1) and ((q[gid[0]] gt 2.3) or (q[gid[0]] lt -0.3)) and ((sigmax[j] gt 2.0))) then cntgood2++ &$
   ;if i eq 1 then print,gid &$
   if ((nm[j] gt 0.1) and (gid[0] gt -0.1) and (n_elements(gid) gt 1.1)) then print,n_elements(gid)," ",q[gid] &$
   if ((i ne 1) and (nm[j] lt 0.1)) then printf,1,XID[j],RAX[j],DecX[j],poserr[j],sncnts[j],hncnts[j],fncnts[j],sflux[j],hflux[j],fflux[j],ssig[j],hsig[j],fsig[j],nm[j],optID[j],'N/A','N/A',ra_opt[j],dec_opt[j],'0','-1','-1','99.','99.','99.',prob[j],probnone[j],format='(1(I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",I," ",A," ",A," ",A," ",G," ",G," ",I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," "))' &$
   if ((i eq 1) and (nm[j] lt 0.1)) then printf,1,XID[j],RAX[j],DecX[j],poserr[j],sncnts[xpID[j]],hncnts[xpID[j]],fncnts[xpID[j]],sflux[xpID[j]],hflux[xpID[j]],fflux[xpID[j]],ssig[xpID[j]],hsig[xpID[j]],fsig[xpID[j]],nm[j],optID[j],'N/A','N/A',ra_opt[j],dec_opt[j],'0','-1','-1','99.','99.','99.','99.','99.',prob[j],probnone[j],inACS[j],format='(1(I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",I," ",A," ",A," ",A," ",G," ",G," ",I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," "," ",I," "))' &$
   if ((i ne 1) and (nm[j] gt 0.1) and (gid[0] lt -0.1)) then printf,1,XID[j],RAX[j],DecX[j],poserr[j],sncnts[j],hncnts[j],fncnts[j],sflux[j],hflux[j],fflux[j],ssig[j],hsig[j],fsig[j],nm[j],optID[j],'N/A','N/A',ra_opt[j],dec_opt[j],'0','-1','-1',pR[gpid[0]],pI[gpid[0]],pZ[gpid[0]],prob[j],probnone[j],format='(1(I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",I," ",A," ",A," ",A," ",G," ",G," ",I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," "))' &$
   if ((i eq 1) and (nm[j] gt 0.1) and (gid[0] lt -0.1) and (gpid[0] gt -0.1)) then printf,1,XID[j],RAX[j],DecX[j],poserr[j],sncnts[xpID[j]],hncnts[xpID[j]],fncnts[xpID[j]],sflux[xpID[j]],hflux[xpID[j]],fflux[xpID[j]],ssig[xpID[j]],hsig[xpID[j]],fsig[xpID[j]],nm[j],optID[j],'N/A','N/A',ra_opt[j],dec_opt[j],'0','-1','-1',pR[gpid[0]],pI[gpid[0]],pZ[gpid[0]],'99.','99.',prob[j],probnone[j],inACS[j],format='(1(I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",I," ",A," ",A," ",A," ",G," ",G," ",I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," "," ",I," "))' &$
   if ((i ne 1) and (nm[j] gt 0.1) and (gid[0] lt -0.1) and (gpid[0] lt -0.1)) then print,"Matched to opt source but couldn't find it in phot catalog;",i,j," ",optID[j] &$
   if ((i eq 1) and (nm[j] gt 0.1) and (gid[0] lt -0.1) and (gpid[0] lt -0.1)) then if (long(float(optID[j])) lt 0) then print,"Cl1604 - Shouldn't be able to get here" &$
   if ((i eq 1) and (nm[j] gt 0.1) and (gid[0] lt -0.1) and (gpid[0] lt -0.1)) then printf,1,XID[j],RAX[j],DecX[j],poserr[j],sncnts[xpID[j]],hncnts[xpID[j]],fncnts[xpID[j]],sflux[xpID[j]],hflux[xpID[j]],fflux[xpID[j]],ssig[xpID[j]],hsig[xpID[j]],fsig[xpID[j]],nm[j],optID[j],'N/A','N/A',ra_opt[j],dec_opt[j],'0','-1','-1','99.','99.','99.',p606[gpidACS],p814[gpidACS],prob[j],probnone[j],inACS[j],format='(1(I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",I," ",A," ",A," ",A," ",G," ",G," ",I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," "," ",I," "))' &$
   if ((i ne 1) and (nm[j] gt 0.1) and (gid[0] gt -0.1)) then printf,1,XID[j],RAX[j],DecX[j],poserr[j],sncnts[j],hncnts[j],fncnts[j],sflux[j],hflux[j],fflux[j],ssig[j],hsig[j],fsig[j],nm[j],optID[j],mask[gid[0]],slit[gid[0]],ra_opt[j],dec_opt[j],q[gid[0]],sredshift[gid[0]],srerr[gid[0]],sr[gid[0]],si[gid[0]],sz[gid[0]],prob[j],probnone[j],format='(1(I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",I," ",A," ",A," ",A," ",G," ",G," ",I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," "))' &$
   if ((i eq 1) and (nm[j] gt 0.1) and (gid[0] gt -0.1)) then printf,1,XID[j],RAX[j],DecX[j],poserr[j],sncnts[xpID[j]],hncnts[xpID[j]],fncnts[xpID[j]],sflux[xpID[j]],hflux[xpID[j]],fflux[xpID[j]],ssig[xpID[j]],hsig[xpID[j]],fsig[xpID[j]],nm[j],optID[j],mask[gid[0]],slit[gid[0]],ra_opt[j],dec_opt[j],q[gid[0]],sredshift[gid[0]],srerr[gid[0]],sr[gid[0]],si[gid[0]],sz[gid[0]],f606[gid[0]],f814[gid[0]],prob[j],probnone[j],inACS[j],format='(1(I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",I," ",A," ",A," ",A," ",G," ",G," ",I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," "," ",I," "))' &$
endfor &$
close,1 &$
 print,names[i] + ':  ' &$
print, "X-ray sources with det. sig. > 2sig:",n_elements(gg2s) &$
print, "X-ray sources with det. sig. > 3sig:",n_elements(gg3s) &$
print, "X-ray sources matched to opt. sources:",n_elements(gnm) &$
print,"X-ray sources match to opt. sources (> 2s):",n_elements(gnm2) &$
print,"X-ray sources match to opt. sources( > 3s):",n_elements(gnm3) &$
print,"Attempted Redshifts:",cnttar &$
print,"Attempted Redshifts(>2s):",cnttar2 &$
print,"Attempted Redshifts(>3s):",cnttar3 &$
print,"Confirmed Redshifts:",cntgood &$
print,"Confirmed Redshifts(>2s):",cntgood2 &$
print,"Confirmed Redshifts(>3s):",cntgood3 &$
print," " &$

printf,2,names[i],n_elements(gg2s),n_elements(gg3s),n_elements(gnm),n_elements(gnm2),n_elements(gnm3),cnttar,cnttar2,cnttar3,cntgood ,cntgood2,cntgood3,format='(1(A," ",I," ",I," ",I," ",I," ",I," ",I," ",I," ",I," ",I," ",I," ",I," "))' &$


   endfor
close,2
end
