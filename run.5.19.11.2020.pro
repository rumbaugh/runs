set_dirs
set_plot,'PS'
loadct,13


xl = [16,18,28]
rswidA = []
rswidA2 = []
rswidA3 = []
names = ['Cl0023','Cl1324','RXJ1757','RXJ1821','Cl1604','Cl1604']
names2 = ['0023','1322','N200','N5281','1604','1604']
path = '/home/rumbaugh/'
files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat"']
;zlb = [0.82,0.655,0.68,0.808,0.84,0.84]
;zub = [0.856,0.785,0.705,0.828,0.96,0.96]
zlb = [0.82,0.65,0.68,0.80,0.84,0.84]
zub = [0.87,0.79,0.71,0.84,0.96,0.96]
rsb = [1.777,1.325,1.84,1.203,1.305,3.182]
rsm = [0.0229,0.0084,0.0319,0.0012,0.00485,0.063]
rsSTD = [0.0625,0.0735,0.0735,0.0413,0.0813,0.0907]
rsNSTD = [3.0,3.0,3.0,3.0,2.0,2.0]
ymax = [20,40,10,10,20]
device,file="/home/rumbaugh/paperstuff/clus.colvz.5.19.11.ps",/color

ystr = "Num. of galaxies"
xstr = "r'-i'"
for i=0,4 do begin &$
if i eq 5 then xstr = "F814W Magnitude" &$
if i eq 5 then ystr = "F606W-F814W" &$
if i lt 4 then readcol,"/home/rumbaugh/LFC/FINAL.matched." + names2[i] + ".specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D' &$
if i ge 4 then readcol,"/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,mskACA,raACA,decACA,idACA,F606W,F814W,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D' &$
;plot,[0,1],[0,1],/nodata,TITLE="RS Offsets - " + names[i],XTITLE=xstr,YTITLE=ystr,PSYM=3,THICK=2,SYMSIZE=0.1,XRANGE=[0,1.5],YRANGE=[0,ymax[i]],xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=4,XTHICK=6,YTHICK=6 &$
if i lt 4 then readcol,files[i],newid,mask,slit,raLFC,decLFC,rprime,iprime,zprime,rs,rserr,sQ,oldid,format="A,A,A,D,D,D,D,D,D,D,I,A" &$
if i ge 4 then readcol,"/home/rumbaugh/LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat",newid,mask,slit,raLFC,decLFC,rprime,iprime,zprime,rs,rserr,sQ,oldid,pflags,raACS,decACS,idACS,f606,f814,format="A,A,A,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D" &$
rsfit = rsb[i]-rsm[i]*iprime &$
rsoffset = rprime-iprime-rsfit &$
g = where((zub[i] ge rs) and (rs ge zlb[i]))  &$
gq = where(sQ[g] gt 2.3) &$
gc = where((rprime[g[gq]] gt 15) and (rprime[g[gq]] lt 30) and (iprime[g[gq]] gt 15) and (iprime[g[gq]] lt 30)) &$
rswid = rsoffset/(rsNSTD[i]*rsSTD[i]) &$
if i lt 4 then rswidA = [rswidA,rswid[g[gq[gc]]]] &$
if i lt 2 then rswidA2 = [rswidA2,rswid[g[gq[gc]]]] &$
if i lt 2 then rswidA3 = [rswidA3,rswid[g[gq[gc]]]] &$
plot,rs[g[gq[gc]]],rprime[g[gq[gc]]]-iprime[g[gq[gc]]],XTITLE="Redshift",YTITLE="r'-i'",SYMSIZE=0.1,XRANGE=[0.65,0.8],YRANGE=[0,1.5],PSYM=2,THICK=4,xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=4,XTHICK=6,YTHICK=6 &$
plot,rs[g[gq[gc]]],rsoffset[g[gq[gc]]],XTITLE="Redshift",YTITLE="RS Offset (r'-i')",SYMSIZE=0.1,XRANGE=[0.65,0.8],YRANGE=[-1,0.5],PSYM=2,THICK=4,xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=4,XTHICK=6,YTHICK=6 &$
;Histoplot,rprime[g[gq[gc]]]-iprime[g[gq[gc]]],MININPUT=0,MAXINPUT=1.5,BINSIZE=0.025,THICK=4,/oplot,/outline &$
;oplot,iprime[g[gq]],rprime[g[gq]]-iprime[g[gq]],PSYM=2,SYMSIZE=0.3,THICK=8,color=250 &$
;g = where((zub[i] ge z) and (z ge zlb[i])) &$
;gq = where(q[g] gt 2.3) &$
;rsoffset = rB-iB-rsfit &$
;if n_elements(gq) eq 1 then tempi = [iB[g[gq]]] &$
;if n_elements(gq) eq 1 then tempr = [rB[g[gq]]] &$
;if n_elements(gq) eq 1 then oplot,tempi,tempr-tempi,PSYM=6,SYMSIZE=1.2,THICK=5,;color=160 &$
;if n_elements(gq) gt 1 then oplot,iB[g[gq]],rB[g[gq]]-iB[g[gq]],PSYM=6,SYMSIZE=1.2,THICK=7,color=160 &$
;yu = rsNSTD[i]*rsSTD[i]+rsfit &$
;yl = -1*rsNSTD[i]*rsSTD[i]+rsfit &$
xl = [-rsNSTD[i]*rsSTD[i],-rsNSTD[i]*rsSTD[i],rsNSTD[i]*rsSTD[i],rsNSTD[i]*rsSTD[i]]
yl = [0,100,100,0]
;oplot,xl,yl,linestyle=3,thick=4,color=0 &$
xl = [0,0]
yl = [0,100]
;oplot,xl,yl,linestyle=1,thick=7,color=0 &$
;oplot,xl,yu,linestyle=3,thick=5,color=30 &$

endfor


 h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90)) 
 hh = where((f606 gt 0.1) and (f606 lt 90) and (f814 gt 0.1) and (f814 lt 90)) 
 rsfit = 3.182-0.063*f814 
 rsoffset = f606-f814-rsfit 
hh = where((f606 gt 0.1) and (f606 lt 90) and (f814 gt 0.1) and (f814 lt 90))
rsfit = 3.182-0.063*f814
rsoffset = f606-f814-rsfit
;plot,[0,1],[0,1],/nodata,TITLE="RS Offsets - 1604 - ACS only",XTITLE="RS offset (RS widths)",YTITLE="Num. of galaxies",PSYM=3,XRANGE=[-7,2],YRANGE=[0,20],xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=4,XTHICK=6,YTHICK=6
h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90))
hh = where((f606 gt 0.1) and (f606 lt 90) and (f814 gt 0.1) and (f814 lt 90))
g = where((0.96 ge rs[hh]) and (rs[hh] ge 0.84))
gq = where(sQ[hh[g]] gt 2.3) &$
;gc = where((rprime[g[gq]] gt 15) & (rprime[g[gq]] lt 30) & (iprime[g[gq]] gt 15) & (iprime[g[gq]] lt 30)) &$
rsfit = 3.182-0.063*f814
rsoffset = f606-f814-rsfit
rswid = rsoffset/(2*0.0907)
;Histoplot,rswid[hh[g[gq]]],MININPUT=-6,MAXINPUT=2,BINSIZE=0.1,THICK=4,/oplot,/outline,histdata=hist1,locations=loc1
rswidA = [rswidA,rswid[hh[g[gq]]]]
rswidA3 = [rswidA3,rswid[hh[g[gq]]]]
;oplot,f814[hh[g[gq]]],f606[hh[g[gq]]]-f814[hh[g[gq]]],PSYM=2,SYMSIZE=0.3,THICK=8,color=250
g = where((z[h] le 0.96) and (z[h] ge 0.84))
gq = where(q[h[g]] gt 2.3) &$
rsfit = 3.182-0.063*f814
rsoffset = F606W-F814W-rsfit
;oplot,F814W[h[g[gq]]],F606W[h[g[gq]]]-F814W[h[g[gq]]],color=160,PSYM=6,SYMSIZE=1.2,THICK=7
yl = -2*0.0907+rsfit
yu = 2*0.0907+rsfit
;oplot,xl,yl,linestyle=3,thick=5,color=30
;oplot,xl,yu,linestyle=3,thick=5,color=30

;plot,[0,1],[0,1],/nodata,TITLE="RS Offsets - Cl0023+Cl1324",XTITLE="RS Offset (RS widths)",YTITLE="Num. of galaxies",PSYM=3,XRANGE=[-5,2],YRANGE=[0,60],xstyle=1,ystyle=1,XTHICK=6,YTHICK=6,CHARSIZE=1.3,CHARTHICK=4

;Histoplot,rswidA2,MININPUT=-6,MAXINPUT=2,BINSIZE=0.1,THICK=4,/oplot,/outline

;plot,[0,1],[0,1],/nodata,TITLE="RS Offsets - Cl0023+Cl1324+Cl1604",XTITLE="RS Offset (RS widths)",YTITLE="Num. of galaxies",PSYM=3,XRANGE=[-5,2],YRANGE=[0,60],xstyle=1,ystyle=1,XTHICK=6,YTHICK=6,CHARSIZE=1.3,CHARTHICK=4

;Histoplot,rswidA3,MININPUT=-6,MAXINPUT=2,BINSIZE=0.1,THICK=4,/oplot,/outline


;plot,[0,1],[0,1],/nodata,TITLE="RS Offsets - Combined",XTITLE="RS Offset (RS widths)",YTITLE="Num. of galaxies",PSYM=3,XRANGE=[-5,2],YRANGE=[0,60],xstyle=1,ystyle=1,XTHICK=6,YTHICK=6,CHARSIZE=1.3,CHARTHICK=4

;Histoplot,rswidA,MININPUT=-6,MAXINPUT=2,BINSIZE=0.1,THICK=4,locations=loca,histdata=hista,/oplot,/outline


xl = [16,18,28]

hist_mag = []
y_RSO = []
o_RSO = []


bndX = [-2*0.0907,-2*0.0907,2*0.0907,2*0.0907]
bndY = [0,1000,1000,0]

end
