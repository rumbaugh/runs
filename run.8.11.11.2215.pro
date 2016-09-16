set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/LumvsRS.nospectar.8.10.11.ps',/color

xt = [-6,-6,-3,-3,-1,-1,2,2,10,10,-20,-20,10,10,-20]
yt = [30,50,50,30,30,50,50,30,30,43.2,43.2,43.0,43.0,42.5,42.5]


rswidsYg2st = []
flumsYg2st = []
rswidsOg2st = []
flumsOg2st = []
rswidsYg3st = []
flumsYg3st = []
rswidsOg3st = []
flumsOg3st = []

rswidsYg2s = []
flumsYg2s = []
rswidsOg2s = []
flumsOg2s = []
rswidsYg3s = []
flumsYg3s = []
rswidsOg3s = []
flumsOg3s = []


rswids4g2s = []
flums4g2s = []
rswids4g3s = []
flums4g3s = []
rswids3g2s = []
flums3g2s = []
rswids3g3s = []
flums3g3s = []
rswids2g2s = []
flums2g2s = []
rswids2g3s = []
flums2g3s = []
rswids1g2s = []
flums1g2s = []
rswids1g3s = []
flums1g3s = []
rswids0g2s = []
flums0g2s = []
rswids0g3s = []
flums0g3s = []
rswids4g2st = []
flums4g2st = []
rswids4g3st = []
flums4g3st = []
rswids3g2st = []
flums3g2st = []
rswids3g3st = []
flums3g3st = []
rswids2g2st = []
flums2g2st = []
rswids2g3st = []
flums2g3st = []
rswids1g2st = []
flums1g2st = []
rswids1g3st = []
flums1g3st = []
rswids0g2st = []
flums0g2st = []
rswids0g3st = []
flums0g3st = []

rsb = [1.777,3.182,1.325,1.203,1.84]
rsm = [0.0229,0.063,0.0084,0.0012,0.0319]
rsSTD = [0.0625,0.0907,0.0735,0.0413,0.0576]
rsNSTD = [3.0,2.0,2.0,3.0,3.0]
thisletter = "162B
 
names = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
mnames = ['Cl0023','Cl1604','Cl1324','NEP5281','NEP200']
;pnames = ['/home/rumbaugh/LFC/cl0023_radecIDmags.cat',"/home/rumbaugh/LFC/final.idradecmag.lfcpluscosmic.withsdss.cat","/home/rumbaugh/LFC/sc1322.lfc.newIDsandoldIds.radecmag.cat","/home/rumbaugh/LFC/nep5281.lfc.newIDradecmag.cat","/home/rumbaugh/LFC/nep200.idradecmag.lfc.uhcorr.neat"]
pnames = ['/home/rumbaugh/LFC/cl0023_radecIDmags.cat',"/home/rumbaugh/LFC/ACS_merged.F606W+F814W_deep.all.coll.nh.dat","/home/rumbaugh/LFC/sc1322.lfc.newIDsandoldIds.radecmag.cat","/home/rumbaugh/LFC/nep5281.lfc.newIDradecmag.cat","/home/rumbaugh/LFC/nep200.idradecmag.lfc.uhcorr.neat"]
sfiles = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.wh.cat']
;sfiles = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.5281X4targetsonly.aug2011.cat','FINAL.spectroscopic.autocompile.N200.blemaux.N200XR3incomplete.aug2011.cat']
exps = [49383.247922195,49478.092354796,46103.507982594,48391.890220549,50399.00069391,49548.501183658,46451.792387024]
m1604 = (43.35861-43.28914)/(240.9075-241.19939)
y01604 = 43.28914 
x01604 = 241.19939

readcol,'/home/rumbaugh/LFC/c2f.pointings.avgz.8.4.11.dat',c2fsarr,c2fharr
;fourpiDL2 = [1.676,1.987,1.31,1.58,1.034]/(0.7*0.7) ;times 10^57 
fourpiDL2 = [1.58,1.776,0.9278,1.486,1.034]/(0.7*0.7) ;times 10^57 
cnt = 0
for i=0,4 do begin &$
if i eq 0 then time = exps[0] &$
if i eq 3 then time = exps[5] &$
if i eq 4 then time = exps[6] &$
if i eq 0 then c2fs = c2fsarr[0] &$
if i eq 0 then c2fh = c2fharr[0] &$
if i eq 3 then c2fs = c2fsarr[5] &$
if i eq 3 then c2fh = c2fharr[5] &$
if i eq 4 then c2fs = c2fsarr[6] &$
if i eq 4 then c2fh = c2fharr[6] &$
if ((i ne 1) and (i ne 2)) then readcol,pnames[i],pID,pra,pdec,pR,pI,pZ,format='A,D,D,D,D,D',/silent &$
if ((i eq 2)) then readcol,pnames[i],pID,oldpID,pra,pdec,pR,pI,pZ,format='A,I,D,D,D,D,D',/silent &$
if i eq 1 then readcol,pnames[i],pra,pdec,p606,p814,d606,d814,rh606,rh814,c606,c814,format='D,D,D,D,D,D,D,D,D,D',/silent &$
if i eq 1 then pI = p814 &$
if i eq 1 then pR = p606 &$
sfile = '/home/rumbaugh/' + sfiles[i] &$
;print,cnt &$
cnt++ &$
if i ne 1 then readcol,sfile,LFCID,mask,slit,sra,sdec,sr,si,sz,sredshift,srerr,q,old_id,format='A,A,A,D,D,D,D,D,D,D,D,A,A',/silent &$
if i eq 1 then readcol,sfile,LFCID,mask,slit,sra,sdec,sr,si,sz,sredshift,srerr,q,old_id,phot_flag,acsRA,acsDec,acsID,f606,f814,format='A,A,A,D,D,D,D,D,D,D,D,A,A,D,D,A,D,D',/silent &$
;print,cnt &$
cnt++ &$
mfile = '/home/rumbaugh/' + mnames[i] + '.opt_Xray_matched_catalog_3high.corrected.twk.8.4.11.dat' &$
if i ne 1 then readcol,mfile,XID,RAX,DecX,poserr,nm,ra_opt,dec_opt,optID,prob,rel,ra_opt2,dec_opt2,optID2,prob2,rel2,ra_opt3,dec_opt3,optID3,prob3,rel3,probnone,citemp,sigmax,format='I,D,D,D,I,D,D,A,D,D,D,D,A,D,D,D,D,A,D,D,D,D,D',/silent &$
if i eq 1 then readcol,mfile,XID,RAX,DecX,poserr,nm,ra_opt,dec_opt,optID,prob,rel,ra_opt2,dec_opt2,optID2,prob2,rel2,ra_opt3,dec_opt3,optID3,prob3,rel3,probnone,citemp,sigmax,inACS,xpID,format='I,D,D,D,I,D,D,A,D,D,D,D,A,D,D,D,D,A,D,D,D,D,D,I,I',/silent &$
xpfile = '/scratch/rumbaugh/ciaotesting/' + names[i] + '/master/photometry/' + names[i] + '.xray_phot.soft_hard_full.dat' &$
readcol,xpfile,xpRA,xpDec,sflux,hflux,fflux,sncnts,hncnts,fncnts,ssig,hsig,fsig,wssig,whsig,wfsig,wmask,wflag,format='D,D,F,F,F,D,D,D,D,D,D,D,D,D,I,I',/silent &$
if i eq 1 then sncnts = sncnts[xpID] &$
if i eq 1 then hncnts = hncnts[xpID] &$
if i eq 1 then fncnts = fncnts[xpID] &$
if i eq 1 then sflux = sflux[xpID] &$
if i eq 1 then hflux = hflux[xpID] &$
if i eq 1 then fflux = fflux[xpID] &$
if i eq 1 then ssig = ssig[xpID] &$
if i eq 1 then hsig = hsig[xpID] &$
if i eq 1 then fsig = fsig[xpID] &$
gnt = where(nm gt 0.1) &$
notarget = DBLARR(n_elements(nm)) &$
if i eq 1 then gnt = where((nm gt 0.1) and (inACS gt 0.3)) &$
for j=0,n_elements(gnt)-1 do begin &$
   gid = -1 &$
   gid2 = -1 &$
   if (((sigmax[gnt[j]] lt ssig[gnt[j]]-0.1) or (sigmax[gnt[j]] gt ssig[gnt[j]]+0.1)) and ((sigmax[gnt[j]] lt hsig[gnt[j]]-0.1) or (sigmax[gnt[j]] gt hsig[gnt[j]]+0.1)) and ((sigmax[gnt[j]] lt fsig[gnt[j]]-0.1) or (sigmax[gnt[j]] gt fsig[gnt[j]]+0.1))) then print,gnt[j],sigmax[gnt[j]],ssig[gnt[j]],hsig[gnt[j]],fsig[gnt[j]] &$
   if i ne 1 then gid = where(LFCID eq optID[gnt[j]]) &$
   if i eq 1 then gid = where(acsID eq optID[gnt[j]]) &$
   if ((i ne 1) and (nm[gnt[j]] gt 1.1)) then gid2 = where(LFCID eq optID2[gnt[j]]) &$
   if ((i eq 1) and (nm[gnt[j]] gt 1.1)) then gid2 = where(acsID eq optID2[gnt[j]]) &$
   if ((gid[0] lt -0.1) and (gid2[0] gt -0.1)) then gid = gid2 &$
   if ((gid[0] gt -0.1) and ((q[gid[0]] gt -0.3) and (q[gid[0]] lt 1.3))) then notarget[gnt[j]] = 1 &$
   if ((gid[0] gt -0.1) and ((q[gid[0]] lt -0.3) or (q[gid[0]] gt 1.3))) then notarget[gnt[j]] = -1 &$
   if (gid[0] lt -0.1) then notarget[gnt[j]] = 1 &$
   ;if i eq 1 then print,gid &$
endfor &$
gnotar = where(notarget gt 0.1) &$
gtar = where(notarget[gnt] lt -0.1) &$
gtartest = where(notarget[gnt] lt 0.1) &$
if ((i ne 1) and (n_elements(gtartest) ne n_elements(gtar))) then print,i," gtar not equal to gtartest",gtar,gtartest
;if i eq 1 then print,n_elements(gtartest),n_elements(gtar)
sfluxes = DBLARR(n_elements(gnotar)) &$
hfluxes = DBLARR(n_elements(gnotar)) &$
slums = DBLARR(n_elements(gnotar)) &$
hlums = DBLARR(n_elements(gnotar)) &$
flums = DBLARR(n_elements(gnotar)) &$
rprime = DBLARR(n_elements(gnotar)) &$
iprime = DBLARR(n_elements(gnotar)) &$
sfluxest = DBLARR(n_elements(gtar)) &$
hfluxest = DBLARR(n_elements(gtar)) &$
slumst = DBLARR(n_elements(gtar)) &$
hlumst = DBLARR(n_elements(gtar)) &$
flumst = DBLARR(n_elements(gtar)) &$
rprimet = DBLARR(n_elements(gtar)) &$
iprimet = DBLARR(n_elements(gtar)) &$
openw, 1, '/home/rumbaugh/LFC/nottargeted.' + names[i] + '.info.cat' &$
for j=0,n_elements(gnotar)-1 do begin &$
   if i eq 1 then time = exps[1] &$
   if i eq 1 then c2fs = c2fsarr[1] &$
   if i eq 1 then c2fh = c2fharr[1] &$
   if ((i eq 1) and (DecX[gnotar[j]] gt (m1604*(RaX[gnotar[j]]-x01604)+y01604))) then time = exps[2] &$
   if ((i eq 1) and (DecX[gnotar[j]] gt (m1604*(RaX[gnotar[j]]-x01604)+y01604))) then c2fs = c2fsarr[2] &$
   if ((i eq 1) and (DecX[gnotar[j]] gt (m1604*(RaX[gnotar[j]]-x01604)+y01604))) then c2fh = c2fharr[2] &$
   if i eq 2 then c2fs = c2fsarr[3] &$
   if i eq 2 then c2fh = c2fharr[3] &$
   if i eq 2 then time = exps[3] &$
   if ((i eq 2) and (DecX[gnotar[j]] lt 30.6)) then c2fs = c2fsarr[4] &$
   if ((i eq 2) and (DecX[gnotar[j]] lt 30.6)) then c2fh = c2fharr[4] &$
   if ((i eq 2) and (DecX[gnotar[j]] lt 30.6)) then time = exps[4] &$
   if i ne 1 then sfluxes[j] = sncnts[gnotar[j]]*c2fs/time &$
   if i ne 1 then hfluxes[j] = hncnts[gnotar[j]]*c2fh/time &$
   if i eq 1 then sfluxes[j] = sncnts[long(XID[gnotar[j]])]*c2fs/time &$
   if i eq 1 then hfluxes[j] = hncnts[long(XID[gnotar[j]])]*c2fh/time &$
   slums[j] = sfluxes[j]*fourpiDL2[i] &$ ;in units of 10^(-57)ergs/s
   hlums[j] = hfluxes[j]*fourpiDL2[i] &$
   flums[j] = alog10(slums[j]+hlums[j])+57 &$ ;this is log luminosity
   if i ne 1 then gli = where(pID eq optID[gnotar[j]]) &$
   if i eq 1 then gli = long(optID[gnotar[j]])-2 &$
   if i ne 1 then rprime[j] = pR[gli[0]] &$
   if i ne 1 then iprime[j] = pI[gli[0]] &$
   if i eq 1 then rprime[j] = p606[gli[0]] &$
   if i eq 1 then iprime[j] = p814[gli[0]] &$
   ;if i eq 1 then print,gli,rprime[j],iprime[j] &$
   printf, 1, XID[gnotar[j]],optID[gnotar[j]], RAX[gnotar[j]],DecX[gnotar[j]],nm[gnotar[j]],ra_opt[gnotar[j]],dec_opt[gnotar[j]],sncnts[gnotar[j]],hncnts[gnotar[j]],sflux[gnotar[j]],hflux[gnotar[j]],slums[j],hlums[j],flums[j],rprime[j],iprime[j],(rprime[j]-iprime[j]-(-1*rsm[i]*iprime[j]+rsb[i]))/(rsNSTD[i]*rsSTD[i]),sigmax[gnotar[j]],format='(1(I," ",A," ",G," ",G," ",I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," "))' &$
      endfor &$
close, 1 &$
rsoffset = rprime-iprime-(-1*rsm[i]*iprime+rsb[i]) &$
rswids = rsoffset/(rsNSTD[i]*rsSTD[i]) &$
g3s = where(sigmax[gnotar] ge 3) &$
g2s = where((sigmax[gnotar] ge 2)) &$
;if (i eq 2) then for j=0,n_elements(rswids)-1 do print,rsoffset[j],rswids[j],rprime[j],iprime[j],(-1*rsm[i]*iprime[j]+rsb[i]),flums[j] &$
plot,[0-1],[0-1],/nodata,YRANGE=[41.5,44.5],XRANGE=[-7.5,2],/xstyle,/ystyle,XTITLE='RS Offsets (RS Wids)',YTITLE='Log Luminosity',TITLE=names[i] + " - Not Targeted for Spectroscopy",XTHICK=4,YTHICK=4,CHARTHICK=3 &$
oplot,rswids[g2s],flums[g2s],PSYM=4,THICK=2,color=80 &$
oplot,rswids[g3s],flums[g3s],PSYM=6,THICK=2,color=255 &$
oplot,xt,yt,linestyle=1 &$
legend,['>3!4' + String(thisletter) + '!X','>2!4' + String(thisletter) + '!X and <3!4' + String(thisletter) + '!X'],PSYM=[6,4],color=[255,80],/bottom &$
if i lt 1.3 then flumsYg2s = [flumsYg2s,flums[g2s]] &$
if i lt 1.3 then flumsYg3s = [flumsYg3s,flums[g3s]] &$
if i gt 1.3 then flumsOg2s = [flumsOg2s,flums[g2s]] &$
if i gt 1.3 then flumsOg3s = [flumsOg3s,flums[g3s]] &$
if i lt 1.3 then rswidsYg2s = [rswidsYg2s,rswids[g2s]] &$
if i lt 1.3 then rswidsYg3s = [rswidsYg3s,rswids[g3s]] &$
if i gt 1.3 then rswidsOg2s = [rswidsOg2s,rswids[g2s]] &$
if i gt 1.3 then rswidsOg3s = [rswidsOg3s,rswids[g3s]] &$
if i eq 0 then flums0g2s = [flums0g2s,flums[g2s]] &$
if i eq 0 then flums0g3s = [flums0g3s,flums[g3s]] &$
if i eq 0 then rswids0g2s = [rswids0g2s,rswids[g2s]] &$
if i eq 0 then rswids0g3s = [rswids0g3s,rswids[g3s]] &$
if i eq 1 then flums1g2s = [flums1g2s,flums[g2s]] &$
if i eq 1 then flums1g3s = [flums1g3s,flums[g3s]] &$
if i eq 1 then rswids1g2s = [rswids1g2s,rswids[g2s]] &$
if i eq 1 then rswids1g3s = [rswids1g3s,rswids[g3s]] &$
if i eq 2 then flums2g2s = [flums2g2s,flums[g2s]] &$
if i eq 2 then flums2g3s = [flums2g3s,flums[g3s]] &$
if i eq 2 then rswids2g2s = [rswids2g2s,rswids[g2s]] &$
if i eq 2 then rswids2g3s = [rswids2g3s,rswids[g3s]] &$
if i eq 3 then flums3g2s = [flums3g2s,flums[g2s]] &$
if i eq 3 then flums3g3s = [flums3g3s,flums[g3s]] &$
if i eq 3 then rswids3g2s = [rswids3g2s,rswids[g2s]] &$
if i eq 3 then rswids3g3s = [rswids3g3s,rswids[g3s]] &$
if i eq 4 then flums4g2s = [flums4g2s,flums[g2s]] &$
if i eq 4 then flums4g3s = [flums4g3s,flums[g3s]] &$
if i eq 4 then rswids4g2s = [rswids4g2s,rswids[g2s]] &$
if i eq 4 then rswids4g3s = [rswids4g3s,rswids[g3s]] &$
print,names[i]   
print, '> 2s'
gtt = where((flums[g2s] gt 43.2) and (rswids[g2s] gt -6) and (rswids[g2s] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -6>C>-3: ',n_elements(gtt)
gtt = where((flums[g2s] gt 43.2) and (rswids[g2s] gt -3) and (rswids[g2s] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -3>C>-1: ',n_elements(gtt)
gtt = where((flums[g2s] gt 43.2) and (rswids[g2s] gt -1) and (rswids[g2s] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -1>C>-2: ',n_elements(gtt)
gtt = where((flums[g2s] gt 42.5) and (flums[g2s] lt 43.2) and (rswids[g2s] gt -6) and (rswids[g2s] lt -3))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flums[g2s] gt 42.5) and (flums[g2s] lt 43.2) and (rswids[g2s] gt -3) and (rswids[g2s] lt -1))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flums[g2s] gt 42.5) and (flums[g2s] lt 43.2) and (rswids[g2s] gt -1) and (rswids[g2s] lt 2))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -1>C>-2: ',n_elements(gtt)
gtt = where((flums[g2s] gt 43.0) and (rswids[g2s] gt -6) and (rswids[g2s] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -6>C>-3: ',n_elements(gtt)
gtt = where((flums[g2s] gt 43.0) and (rswids[g2s] gt -3) and (rswids[g2s] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -3>C>-1: ',n_elements(gtt)
gtt = where((flums[g2s] gt 43.0) and (rswids[g2s] gt -1) and (rswids[g2s] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -1>C>-2: ',n_elements(gtt)
gtt = where((flums[g2s] gt 42.5) and (flums[g2s] lt 43.0) and (rswids[g2s] gt -6) and (rswids[g2s] lt -3))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flums[g2s] gt 42.5) and (flums[g2s] lt 43.0) and (rswids[g2s] gt -3) and (rswids[g2s] lt -1))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flums[g2s] gt 42.5) and (flums[g2s] lt 43.0) and (rswids[g2s] gt -1) and (rswids[g2s] lt 2))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -1>C>-2: ',n_elements(gtt)
gtt = where((flums[g2s] lt 42.5) and (rswids[g2s] gt -6) and (rswids[g2s] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flums[g2s] lt 42.5) and (rswids[g2s] gt -3) and (rswids[g2s] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flums[g2s] lt 42.5) and (rswids[g2s] gt -1) and (rswids[g2s] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -1>C>-2: ',n_elements(gtt)

print, '> 3s'
gtt = where((flums[g3s] gt 43.2) and (rswids[g3s] gt -6) and (rswids[g3s] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -6>C>-3: ',n_elements(gtt)
gtt = where((flums[g3s] gt 43.2) and (rswids[g3s] gt -3) and (rswids[g3s] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -3>C>-1: ',n_elements(gtt)
gtt = where((flums[g3s] gt 43.2) and (rswids[g3s] gt -1) and (rswids[g3s] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -1>C>-2: ',n_elements(gtt)
gtt = where((flums[g3s] gt 42.5) and (flums[g3s] lt 43.2) and (rswids[g3s] gt -6) and (rswids[g3s] lt -3))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flums[g3s] gt 42.5) and (flums[g3s] lt 43.2) and (rswids[g3s] gt -3) and (rswids[g3s] lt -1))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flums[g3s] gt 42.5) and (flums[g3s] lt 43.2) and (rswids[g3s] gt -1) and (rswids[g3s] lt 2))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -1>C>-2: ',n_elements(gtt)
gtt = where((flums[g3s] gt 43.0) and (rswids[g3s] gt -6) and (rswids[g3s] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -6>C>-3: ',n_elements(gtt)
gtt = where((flums[g3s] gt 43.0) and (rswids[g3s] gt -3) and (rswids[g3s] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -3>C>-1: ',n_elements(gtt)
gtt = where((flums[g3s] gt 43.0) and (rswids[g3s] gt -1) and (rswids[g3s] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -1>C>-2: ',n_elements(gtt)
gtt = where((flums[g3s] gt 42.5) and (flums[g3s] lt 43.0) and (rswids[g3s] gt -6) and (rswids[g3s] lt -3))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flums[g3s] gt 42.5) and (flums[g3s] lt 43.0) and (rswids[g3s] gt -3) and (rswids[g3s] lt -1))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flums[g3s] gt 42.5) and (flums[g3s] lt 43.0) and (rswids[g3s] gt -1) and (rswids[g3s] lt 2))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -1>C>-2: ',n_elements(gtt)
gtt = where((flums[g3s] lt 42.5) and (rswids[g3s] gt -6) and (rswids[g3s] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flums[g3s] lt 42.5) and (rswids[g3s] gt -3) and (rswids[g3s] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flums[g3s] lt 42.5) and (rswids[g3s] gt -1) and (rswids[g3s] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -1>C>-2: ',n_elements(gtt)

   openw, 2, '/home/rumbaugh/LFC/targeted.' + names[i] + '.info.cat' &$
   for j=0,n_elements(gtar)-1 do begin &$
   if i eq 1 then time = exps[1] &$
   if i eq 1 then c2fs = c2fsarr[1] &$
   if i eq 1 then c2fh = c2fharr[1] &$
   if ((i eq 1) and (DecX[gnt[gtar[j]]] gt (m1604*(RaX[gnt[gtar[j]]]-x01604)+y01604))) then time = exps[2] &$
   if ((i eq 1) and (DecX[gnt[gtar[j]]] gt (m1604*(RaX[gnt[gtar[j]]]-x01604)+y01604))) then c2fs = c2fsarr[2] &$
   if ((i eq 1) and (DecX[gnt[gtar[j]]] gt (m1604*(RaX[gnt[gtar[j]]]-x01604)+y01604))) then c2fh = c2fharr[2] &$
   if i eq 2 then c2fs = c2fsarr[3] &$
   if i eq 2 then c2fh = c2fharr[3] &$
   if i eq 2 then time = exps[3] &$
   if ((i eq 2) and (DecX[gnt[gtar[j]]] lt 30.6)) then c2fs = c2fsarr[4] &$
   if ((i eq 2) and (DecX[gnt[gtar[j]]] lt 30.6)) then c2fh = c2fharr[4] &$
   if ((i eq 2) and (DecX[gnt[gtar[j]]] lt 30.6)) then time = exps[4] &$
   if i ne 1 then sfluxest[j] = sncnts[gnt[gtar[j]]]*c2fs/time &$
   if i ne 1 then hfluxest[j] = hncnts[gnt[gtar[j]]]*c2fh/time &$
   if i eq 1 then sfluxest[j] = sncnts[long(XID[gnt[gtar[j]]])]*c2fs/time &$
   if i eq 1 then hfluxest[j] = hncnts[long(XID[gnt[gtar[j]]])]*c2fh/time &$
   slumst[j] = sfluxest[j]*fourpiDL2[i] &$ ;in units of 10^(-57)ergs/s
   hlumst[j] = hfluxest[j]*fourpiDL2[i] &$
   flumst[j] = alog10(slumst[j]+hlumst[j])+57 &$ ;this is log luminosity
   if i ne 1 then gli = where(pID eq optID[gnt[gtar[j]]]) &$
   if i eq 1 then gli = long(optID[gnt[gtar[j]]])-2 &$
   if i ne 1 then rprimet[j] = pR[gli[0]] &$
   if i ne 1 then iprimet[j] = pI[gli[0]] &$
   if i eq 1 then rprimet[j] = p606[gli[0]] &$
   if i eq 1 then iprimet[j] = p814[gli[0]] &$
   ;if i eq 1 then print,gli,rprime[j],iprimet[j] &$
   printf, 2, XID[gnt[gtar[j]]], optID[gnt[gtar[j]]], RAX[gnt[gtar[j]]],DecX[gnt[gtar[j]]],nm[gnt[gtar[j]]],ra_opt[gnt[gtar[j]]],dec_opt[gnt[gtar[j]]],sncnts[gnt[gtar[j]]],hncnts[gnt[gtar[j]]],sflux[gnt[gtar[j]]],hflux[gnt[gtar[j]]],slumst[j],hlumst[j],flumst[j],rprimet[j],iprimet[j],(rprimet[j]-iprimet[j]-(-1*rsm[i]*iprimet[j]+rsb[i]))/(rsNSTD[i]*rsSTD[i]),sigmax[gnt[gtar[j]]],format='(1(I," ",A," ",G," ",G," ",I," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," "))' &$ 
      endfor &$
close, 2 &$
rsoffsett = rprimet-iprimet-(-1*rsm[i]*iprimet+rsb[i]) &$
rswidst = rsoffsett/(rsNSTD[i]*rsSTD[i]) &$
g3st = where(sigmax[gnt[gtar]] ge 3) &$
g2st = where((sigmax[gnt[gtar]] ge 2)) &$
;if (i eq 2) then for j=0,n_elements(rswids)-1 do print,rsoffset[j],rswids[j],rprime[j],iprime[j],(-1*rsm[i]*iprime[j]+rsb[i]),flums[j] &$
plot,[0-1],[0-1],/nodata,YRANGE=[41.5,44.5],XRANGE=[-7.5,2],/xstyle,/ystyle,XTITLE='RS Offsets (RS Wids)',YTITLE='Log Luminosity',TITLE=names[i] + ' - Targeted for Spectroscopy',XTHICK=4,YTHICK=4,CHARTHICK=3 &$

oplot,xt,yt,linestyle=1 &$
oplot,rswidst[g2st],flumst[g2st],PSYM=4,THICK=2,color=80 &$
oplot,rswidst[g3st],flumst[g3st],PSYM=6,THICK=2,color=255 &$
legend,['>3!4' + String(thisletter) + '!X','>2!4' + String(thisletter) + '!X and <3!4' + String(thisletter) + '!X'],PSYM=[6,4],color=[255,80],/bottom &$
if i lt 1.3 then flumsYg2st = [flumsYg2st,flumst[g2st]] &$
if i lt 1.3 then flumsYg3st = [flumsYg3st,flumst[g3st]] &$
if i gt 1.3 then flumsOg2st = [flumsOg2st,flumst[g2st]] &$
if i gt 1.3 then flumsOg3st = [flumsOg3st,flumst[g3st]] &$
if i lt 1.3 then rswidsYg2st = [rswidsYg2st,rswidst[g2st]] &$
if i lt 1.3 then rswidsYg3st = [rswidsYg3st,rswidst[g3st]] &$
if i gt 1.3 then rswidsOg2st = [rswidsOg2st,rswidst[g2st]] &$
if i gt 1.3 then rswidsOg3st = [rswidsOg3st,rswidst[g3st]] &$
if i eq 0 then flums0g2st = [flums0g2st,flums[g2st]] &$
if i eq 0 then flums0g3st = [flums0g3st,flums[g3st]] &$
if i eq 0 then rswids0g2st = [rswids0g2st,rswids[g2st]] &$
if i eq 0 then rswids0g3st = [rswids0g3st,rswids[g3st]] &$
if i eq 1 then flums1g2st = [flums1g2st,flums[g2st]] &$
if i eq 1 then flums1g3st = [flums1g3st,flums[g3st]] &$
if i eq 1 then rswids1g2st = [rswids1g2st,rswids[g2st]] &$
if i eq 1 then rswids1g3st = [rswids1g3st,rswids[g3st]] &$
if i eq 2 then flums2g2st = [flums2g2st,flums[g2st]] &$
if i eq 2 then flums2g3st = [flums2g3st,flums[g3st]] &$
if i eq 2 then rswids2g2st = [rswids2g2st,rswids[g2st]] &$
if i eq 2 then rswids2g3st = [rswids2g3st,rswids[g3st]] &$
if i eq 3 then flums3g2st = [flums3g2st,flums[g2st]] &$
if i eq 3 then flums3g3st = [flums3g3st,flums[g3st]] &$
if i eq 3 then rswids3g2st = [rswids3g2st,rswids[g2st]] &$
if i eq 3 then rswids3g3st = [rswids3g3st,rswids[g3st]] &$
if i eq 4 then flums4g2st = [flums4g2st,flums[g2st]] &$
if i eq 4 then flums4g3st = [flums4g3st,flums[g3st]] &$
if i eq 4 then rswids4g2st = [rswids4g2st,rswids[g2st]] &$
if i eq 4 then rswids4g3st = [rswids4g3st,rswids[g3st]] &$
print, '> 2s'
gtt = where((flumst[g2st] gt 43.2) and (rswidst[g2st] gt -6) and (rswidst[g2st] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -6>C>-3: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 43.2) and (rswidst[g2st] gt -3) and (rswidst[g2st] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -3>C>-1: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 43.2) and (rswidst[g2st] gt -1) and (rswidst[g2st] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -1>C>-2: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 42.5) and (flumst[g2st] lt 43.2) and (rswidst[g2st] gt -6) and (rswidst[g2st] lt -3))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 42.5) and (flumst[g2st] lt 43.2) and (rswidst[g2st] gt -3) and (rswidst[g2st] lt -1))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 42.5) and (flumst[g2st] lt 43.2) and (rswidst[g2st] gt -1) and (rswidst[g2st] lt 2))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -1>C>-2: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 43.0) and (rswidst[g2st] gt -6) and (rswidst[g2st] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -6>C>-3: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 43.0) and (rswidst[g2st] gt -3) and (rswidst[g2st] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -3>C>-1: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 43.0) and (rswidst[g2st] gt -1) and (rswidst[g2st] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -1>C>-2: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 42.5) and (flumst[g2st] lt 43.0) and (rswidst[g2st] gt -6) and (rswidst[g2st] lt -3))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 42.5) and (flumst[g2st] lt 43.0) and (rswidst[g2st] gt -3) and (rswidst[g2st] lt -1))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flumst[g2st] gt 42.5) and (flumst[g2st] lt 43.0) and (rswidst[g2st] gt -1) and (rswidst[g2st] lt 2))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -1>C>-2: ',n_elements(gtt)
gtt = where((flumst[g2st] lt 42.5) and (rswidst[g2st] gt -6) and (rswidst[g2st] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flumst[g2st] lt 42.5) and (rswidst[g2st] gt -3) and (rswidst[g2st] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flumst[g2st] lt 42.5) and (rswidst[g2st] gt -1) and (rswidst[g2st] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -1>C>-2: ',n_elements(gtt)

print, '> 3s'
gtt = where((flumst[g3st] gt 43.2) and (rswidst[g3st] gt -6) and (rswidst[g3st] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -6>C>-3: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 43.2) and (rswidst[g3st] gt -3) and (rswidst[g3st] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -3>C>-1: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 43.2) and (rswidst[g3st] gt -1) and (rswidst[g3st] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.2, -1>C>-2: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 42.5) and (flumst[g3st] lt 43.2) and (rswidst[g3st] gt -6) and (rswidst[g3st] lt -3))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 42.5) and (flumst[g3st] lt 43.2) and (rswidst[g3st] gt -3) and (rswidst[g3st] lt -1))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 42.5) and (flumst[g3st] lt 43.2) and (rswidst[g3st] gt -1) and (rswidst[g3st] lt 2))
if gtt[0] eq -1 then gtt = []
print,'43.2 > Lum > 42.5, -1>C>-2: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 43.0) and (rswidst[g3st] gt -6) and (rswidst[g3st] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -6>C>-3: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 43.0) and (rswidst[g3st] gt -3) and (rswidst[g3st] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -3>C>-1: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 43.0) and (rswidst[g3st] gt -1) and (rswidst[g3st] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum > 43.0, -1>C>-2: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 42.5) and (flumst[g3st] lt 43.0) and (rswidst[g3st] gt -6) and (rswidst[g3st] lt -3))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 42.5) and (flumst[g3st] lt 43.0) and (rswidst[g3st] gt -3) and (rswidst[g3st] lt -1))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flumst[g3st] gt 42.5) and (flumst[g3st] lt 43.0) and (rswidst[g3st] gt -1) and (rswidst[g3st] lt 2))
if gtt[0] eq -1 then gtt = []
print,'43.0 > Lum > 42.5, -1>C>-2: ',n_elements(gtt)
gtt = where((flumst[g3st] lt 42.5) and (rswidst[g3st] gt -6) and (rswidst[g3st] lt -3))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -6>C>-3: ',n_elements(gtt)
gtt = where((flumst[g3st] lt 42.5) and (rswidst[g3st] gt -3) and (rswidst[g3st] lt -1))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -3>C>-1: ',n_elements(gtt)
gtt = where((flumst[g3st] lt 42.5) and (rswidst[g3st] gt -1) and (rswidst[g3st] lt 2))
if gtt[0] eq -1 then gtt = []
print,'Lum < 42.5, -1>C>-2: ',n_elements(gtt)

   endfor
plot,[0-1],[0-1],/nodata,YRANGE=[41.5,44.5],XRANGE=[-15,6],/xsty,/ysty,XTITLE='RS Offsets (RS Wids)',YTITLE='Log Luminosity',TITLE='All Fields - Not Targeted for Spectroscopy',XTHICK=4,YTHICK=4,CHARTHICK=3

oplot,xt,yt,linestyle=1 &$
oplot,rswidsYg2s,flumsYg2s,PSYM=4,THICK=2,color=180
oplot,rswidsYg3s,flumsYg3s,PSYM=6,THICK=2,color=255
oplot,rswidsOg2s,flumsOg2s,PSYM=5,THICK=2,color=110
oplot,rswidsOg3s,flumsOg3s,PSYM=7,THICK=2,color=70
legend,['Unevolved - >3!4' + String(thisletter) + '!X','Unevolved - >2!4' + String(thisletter) + '!X and <3!4' + String(thisletter) + '!X','Evolved - >3!4' + String(thisletter) + '!X','Evolved - >2!4' + String(thisletter) + '!X and <3!4' + String(thisletter) + '!X'],PSYM=[6,4,7,5],color=[255,180,70,110],/bottom,/right

plot,[0-1],[0-1],/nodata,YRANGE=[41.5,44.5],XRANGE=[-15,6],/xsty,/ysty,XTITLE='RS Offsets (RS Wids)',YTITLE='Log Luminosity',TITLE='All Fields - Targeted for Spectroscopy',XTHICK=4,YTHICK=4,CHARTHICK=3

oplot,xt,yt,linestyle=1 &$
oplot,rswidsYg2st,flumsYg2st,PSYM=4,THICK=2,color=180
oplot,rswidsYg3st,flumsYg3st,PSYM=6,THICK=2,color=255
oplot,rswidsOg2st,flumsOg2st,PSYM=5,THICK=2,color=110
oplot,rswidsOg3st,flumsOg3st,PSYM=7,THICK=2,color=70
legend,['Unevolved - >3!4' + String(thisletter) + '!X','Unevolved - >2!4' + String(thisletter) + '!X and <3!4' + String(thisletter) + '!X','Evolved - >3!4' + String(thisletter) + '!X','Evolved - >2!4' + String(thisletter) + '!X and <3!4' + String(thisletter) + '!X'],PSYM=[6,4,7,5],color=[255,180,70,110],/bottom,/right

plot,[0-1],[0-1],/nodata,YRANGE=[41.5,44.5],XRANGE=[-7.5,2],/xsty,/ysty,XTITLE='RS Offsets (RS Wids)',YTITLE='Log Luminosity',TITLE='All Fields - Not Targeted for Spectroscopy',XTHICK=4,YTHICK=4,CHARTHICK=3

oplot,xt,yt,linestyle=1 &$
oplot,rswidsYg2s,flumsYg2s,PSYM=4,THICK=2,color=180
oplot,rswidsYg3s,flumsYg3s,PSYM=6,THICK=2,color=255
oplot,rswidsOg2s,flumsOg2s,PSYM=5,THICK=2,color=110
oplot,rswidsOg3s,flumsOg3s,PSYM=7,THICK=2,color=70
legend,['Unevolved - >3!4' + String(thisletter) + '!X','Unevolved - >2!4' + String(thisletter) + '!X and <3!4' + String(thisletter) + '!X','Evolved - >3!4' + String(thisletter) + '!X','Evolved - >2!4' + String(thisletter) + '!X and <3!4' + String(thisletter) + '!X'],PSYM=[6,4,7,5],color=[255,180,70,110],/bottom,/right

print,'>2 sig'
gtemp = where((flumsYg2s gt 43.2) and (rswidsYg2s gt -6) and (rswidsYg2s lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -6>C>-3, young: ',n_elements(gtemp)
gtemp = where((flumsOg2s gt 43.2) and (rswidsOg2s gt -6) and (rswidsOg2s lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -6>C>-3, old: ',n_elements(gtemp)
gtemp = where((flumsYg2s gt 43.2) and (rswidsYg2s gt -3) and (rswidsYg2s lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -3>C>-1, young: ',n_elements(gtemp)
gtemp = where((flumsOg2s gt 43.2) and (rswidsOg2s gt -3) and (rswidsOg2s lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -3>C>-1, old: ',n_elements(gtemp)
gtemp = where((flumsYg2s gt 43.2) and (rswidsYg2s gt -1) and (rswidsYg2s lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -1>C>+2, young: ',n_elements(gtemp)
gtemp = where((flumsOg2s gt 43.2) and (rswidsOg2s gt -1) and (rswidsOg2s lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -1>C>+2, old: ',n_elements(gtemp)
gtemp = where((flumsYg2s lt 43.2) and (rswidsYg2s gt -6) and (rswidsYg2s lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -6>C>-3, young: ',n_elements(gtemp)
gtemp = where((flumsOg2s lt 43.2) and (rswidsOg2s gt -6) and (rswidsOg2s lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -6>C>-3, old: ',n_elements(gtemp)
gtemp = where((flumsYg2s lt 43.2) and (rswidsYg2s gt -3) and (rswidsYg2s lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -3>C>-1, young: ',n_elements(gtemp)
gtemp = where((flumsOg2s lt 43.2) and (rswidsOg2s gt -3) and (rswidsOg2s lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -3>C>-1, old: ',n_elements(gtemp)
gtemp = where((flumsYg2s lt 43.2) and (rswidsYg2s gt -1) and (rswidsYg2s lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -1>C>+2, young: ',n_elements(gtemp)
gtemp = where((flumsOg2s lt 43.2) and (rswidsOg2s gt -1) and (rswidsOg2s lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -1>C>+2, old: ',n_elements(gtemp)
print,'>3 sig'
gtemp = where((flumsYg3s gt 43.2) and (rswidsYg3s gt -6) and (rswidsYg3s lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -6>C>-3, young: ',n_elements(gtemp)
gtemp = where((flumsOg3s gt 43.2) and (rswidsOg3s gt -6) and (rswidsOg3s lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -6>C>-3, old: ',n_elements(gtemp)
gtemp = where((flumsYg3s gt 43.2) and (rswidsYg3s gt -3) and (rswidsYg3s lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -3>C>-1, young: ',n_elements(gtemp)
gtemp = where((flumsOg3s gt 43.2) and (rswidsOg3s gt -3) and (rswidsOg3s lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -3>C>-1, old: ',n_elements(gtemp)
gtemp = where((flumsYg3s gt 43.2) and (rswidsYg3s gt -1) and (rswidsYg3s lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -1>C>+2, young: ',n_elements(gtemp)
gtemp = where((flumsOg3s gt 43.2) and (rswidsOg3s gt -1) and (rswidsOg3s lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -1>C>+2, old: ',n_elements(gtemp)
gtemp = where((flumsYg3s lt 43.2) and (rswidsYg3s gt -6) and (rswidsYg3s lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -6>C>-3, young: ',n_elements(gtemp)
gtemp = where((flumsOg3s lt 43.2) and (rswidsOg3s gt -6) and (rswidsOg3s lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -6>C>-3, old: ',n_elements(gtemp)
gtemp = where((flumsYg3s lt 43.2) and (rswidsYg3s gt -3) and (rswidsYg3s lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -3>C>-1, young: ',n_elements(gtemp)
gtemp = where((flumsOg3s lt 43.2) and (rswidsOg3s gt -3) and (rswidsOg3s lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -3>C>-1, old: ',n_elements(gtemp)
gtemp = where((flumsYg3s lt 43.2) and (rswidsYg3s gt -1) and (rswidsYg3s lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -1>C>+2, young: ',n_elements(gtemp)
gtemp = where((flumsOg3s lt 43.2) and (rswidsOg3s gt -1) and (rswidsOg3s lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -1>C>+2, old: ',n_elements(gtemp)


plot,[0-1],[0-1],/nodata,YRANGE=[41.5,44.5],XRANGE=[-7.5,2],/xsty,/ysty,XTITLE='RS Offsets (RS Wids)',YTITLE='Log Luminosity',TITLE='All Fields - Targeted for Spectroscopy',XTHICK=4,YTHICK=4,CHARTHICK=3

oplot,xt,yt,linestyle=1 &$
oplot,rswidsYg2st,flumsYg2st,PSYM=4,THICK=2,color=180
oplot,rswidsYg3st,flumsYg3st,PSYM=6,THICK=2,color=255
oplot,rswidsOg2st,flumsOg2st,PSYM=5,THICK=2,color=110
oplot,rswidsOg3st,flumsOg3st,PSYM=7,THICK=2,color=70
legend,['Unevolved - >3!4' + String(thisletter) + '!X','Unevolved - >2!4' + String(thisletter) + '!X and <3!4' + String(thisletter) + '!X','Evolved - >3!4' + String(thisletter) + '!X','Evolved - >2!4' + String(thisletter) + '!X and <3!4' + String(thisletter) + '!X'],PSYM=[6,4,7,5],color=[255,180,70,110],/bottom,/right

print,'>2 sig'
gtemp = where((flumsYg2st gt 43.2) and (rswidsYg2st gt -6) and (rswidsYg2st lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -6>C>-3, young: ',n_elements(gtemp)
gtemp = where((flumsOg2st gt 43.2) and (rswidsOg2st gt -6) and (rswidsOg2st lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -6>C>-3, old: ',n_elements(gtemp)
gtemp = where((flumsYg2st gt 43.2) and (rswidsYg2st gt -3) and (rswidsYg2st lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -3>C>-1, young: ',n_elements(gtemp)
gtemp = where((flumsOg2st gt 43.2) and (rswidsOg2st gt -3) and (rswidsOg2st lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -3>C>-1, old: ',n_elements(gtemp)
gtemp = where((flumsYg2st gt 43.2) and (rswidsYg2st gt -1) and (rswidsYg2st lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -1>C>+2, young: ',n_elements(gtemp)
gtemp = where((flumsOg2st gt 43.2) and (rswidsOg2st gt -1) and (rswidsOg2st lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -1>C>+2, old: ',n_elements(gtemp)
gtemp = where((flumsYg2st lt 43.2) and (rswidsYg2st gt -6) and (rswidsYg2st lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -6>C>-3, young: ',n_elements(gtemp)
gtemp = where((flumsOg2st lt 43.2) and (rswidsOg2st gt -6) and (rswidsOg2st lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -6>C>-3, old: ',n_elements(gtemp)
gtemp = where((flumsYg2st lt 43.2) and (rswidsYg2st gt -3) and (rswidsYg2st lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -3>C>-1, young: ',n_elements(gtemp)
gtemp = where((flumsOg2st lt 43.2) and (rswidsOg2st gt -3) and (rswidsOg2st lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -3>C>-1, old: ',n_elements(gtemp)
gtemp = where((flumsYg2st lt 43.2) and (rswidsYg2st gt -1) and (rswidsYg2st lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -1>C>+2, young: ',n_elements(gtemp)
gtemp = where((flumsOg2st lt 43.2) and (rswidsOg2st gt -1) and (rswidsOg2st lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -1>C>+2, old: ',n_elements(gtemp)
print,'>3 sig'
gtemp = where((flumsYg3st gt 43.2) and (rswidsYg3st gt -6) and (rswidsYg3st lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -6>C>-3, young: ',n_elements(gtemp)
gtemp = where((flumsOg3st gt 43.2) and (rswidsOg3st gt -6) and (rswidsOg3st lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -6>C>-3, old: ',n_elements(gtemp)
gtemp = where((flumsYg3st gt 43.2) and (rswidsYg3st gt -3) and (rswidsYg3st lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -3>C>-1, young: ',n_elements(gtemp)
gtemp = where((flumsOg3st gt 43.2) and (rswidsOg3st gt -3) and (rswidsOg3st lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -3>C>-1, old: ',n_elements(gtemp)
gtemp = where((flumsYg3st gt 43.2) and (rswidsYg3st gt -1) and (rswidsYg3st lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -1>C>+2, young: ',n_elements(gtemp)
gtemp = where((flumsOg3st gt 43.2) and (rswidsOg3st gt -1) and (rswidsOg3st lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum > 43.2, -1>C>+2, old: ',n_elements(gtemp)
gtemp = where((flumsYg3st lt 43.2) and (rswidsYg3st gt -6) and (rswidsYg3st lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -6>C>-3, young: ',n_elements(gtemp)
gtemp = where((flumsOg3st lt 43.2) and (rswidsOg3st gt -6) and (rswidsOg3st lt -3))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -6>C>-3, old: ',n_elements(gtemp)
gtemp = where((flumsYg3st lt 43.2) and (rswidsYg3st gt -3) and (rswidsYg3st lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -3>C>-1, young: ',n_elements(gtemp)
gtemp = where((flumsOg3st lt 43.2) and (rswidsOg3st gt -3) and (rswidsOg3st lt -1))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -3>C>-1, old: ',n_elements(gtemp)
gtemp = where((flumsYg3st lt 43.2) and (rswidsYg3st gt -1) and (rswidsYg3st lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -1>C>+2, young: ',n_elements(gtemp)
gtemp = where((flumsOg3st lt 43.2) and (rswidsOg3st gt -1) and (rswidsOg3st lt 2))
if gtemp[0] eq -1 then gtemp = []
print,'Lum < 43.2, -1>C>+2, old: ',n_elements(gtemp)


end
