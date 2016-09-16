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
device,file="/home/rumbaugh/paperstuff/clus.RSwid.5.19.11.ps",/color

ystr = "Num. of galaxies"
xstr = "RS offset (r'-i')"
for i=0,4 do begin &$
if i eq 5 then xstr = "F814W Magnitude" &$
if i eq 5 then ystr = "F606W-F814W" &$
if i lt 4 then readcol,"/home/rumbaugh/LFC/FINAL.matched." + names2[i] + ".specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D' &$
if i ge 4 then readcol,"/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,mskACA,raACA,decACA,idACA,F606W,F814W,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D' &$
plot,[0,1],[0,1],/nodata,TITLE="RS Offsets - " + names[i],XTITLE=xstr,YTITLE=ystr,PSYM=3,THICK=2,SYMSIZE=0.1,XRANGE=[-1.0,0.5],YRANGE=[0,ymax[i]],xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=4,XTHICK=6,YTHICK=6 &$
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
Histoplot,rsoffset[g[gq[gc]]],MININPUT=-1.0,MAXINPUT=0.5,BINSIZE=0.025,THICK=4,/oplot,/outline &$
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
oplot,xl,yl,linestyle=3,thick=4,color=0 &$
xl = [0,0]
yl = [0,100]
oplot,xl,yl,linestyle=1,thick=7,color=0 &$
;oplot,xl,yu,linestyle=3,thick=5,color=30 &$

endfor


 h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90)) 
 hh = where((f606 gt 0.1) and (f606 lt 90) and (f814 gt 0.1) and (f814 lt 90)) 
 rsfit = 3.182-0.063*f814 
 rsoffset = f606-f814-rsfit 
hh = where((f606 gt 0.1) and (f606 lt 90) and (f814 gt 0.1) and (f814 lt 90))
rsfit = 3.182-0.063*f814
rsoffset = f606-f814-rsfit
plot,[0,1],[0,1],/nodata,TITLE="RS Offsets - 1604 - ACS only",XTITLE="RS offset (RS widths)",YTITLE="Num. of galaxies",PSYM=3,XRANGE=[-7,2],YRANGE=[0,20],xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=4,XTHICK=6,YTHICK=6
h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90))
hh = where((f606 gt 0.1) and (f606 lt 90) and (f814 gt 0.1) and (f814 lt 90))
g = where((0.96 ge rs[hh]) and (rs[hh] ge 0.84))
gq = where(sQ[hh[g]] gt 2.3) &$
;gc = where((rprime[g[gq]] gt 15) & (rprime[g[gq]] lt 30) & (iprime[g[gq]] gt 15) & (iprime[g[gq]] lt 30)) &$
rsfit = 3.182-0.063*f814
rsoffset = f606-f814-rsfit
rswid = rsoffset/(2*0.0907)
Histoplot,rswid[hh[g[gq]]],MININPUT=-6,MAXINPUT=2,BINSIZE=0.1,THICK=4,/oplot,/outline,histdata=hist1,locations=loc1
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

plot,[0,1],[0,1],/nodata,TITLE="RS Offsets - Cl0023+Cl1324",XTITLE="RS Offset (RS widths)",YTITLE="Num. of galaxies",PSYM=3,XRANGE=[-5,2],YRANGE=[0,60],xstyle=1,ystyle=1,XTHICK=6,YTHICK=6,CHARSIZE=1.3,CHARTHICK=4

Histoplot,rswidA2,MININPUT=-6,MAXINPUT=2,BINSIZE=0.1,THICK=4,/oplot,/outline

plot,[0,1],[0,1],/nodata,TITLE="RS Offsets - Cl0023+Cl1324+Cl1604",XTITLE="RS Offset (RS widths)",YTITLE="Num. of galaxies",PSYM=3,XRANGE=[-5,2],YRANGE=[0,60],xstyle=1,ystyle=1,XTHICK=6,YTHICK=6,CHARSIZE=1.3,CHARTHICK=4

Histoplot,rswidA3,MININPUT=-6,MAXINPUT=2,BINSIZE=0.1,THICK=4,/oplot,/outline


plot,[0,1],[0,1],/nodata,TITLE="RS Offsets - Combined",XTITLE="RS Offset (RS widths)",YTITLE="Num. of galaxies",PSYM=3,XRANGE=[-5,2],YRANGE=[0,60],xstyle=1,ystyle=1,XTHICK=6,YTHICK=6,CHARSIZE=1.3,CHARTHICK=4

Histoplot,rswidA,MININPUT=-6,MAXINPUT=2,BINSIZE=0.1,THICK=4,locations=loca,histdata=hista,/oplot,/outline


xl = [16,18,28]

hist_mag = []
y_RSO = []
o_RSO = []


bndX = [-2*0.0907,-2*0.0907,2*0.0907,2*0.0907]
bndY = [0,1000,1000,0]


readcol,"/home/rumbaugh/LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat",newid,mask,slit,raLFC,decLFC,rprime,iprime,zprime,rs,rserr,Q,oldid,pflags,raACS,decACS,idACS,f606,f814,format="A,A,A,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D"
g = where((0.96 ge rs) and (rs ge 0.84))
rsfit = 3.182-0.063*f814
rsoffset = f606-f814-rsfit
rsoNorm = rsoffset/(4.0*0.0907)
plot,[0-1],[0-1],/nodata,XRANGE=[-1.85,0.5],YRANGE=[0,0.105],xstyle=1,ystyle=1,XTITLE='RS Offset (F606W-F814W)',YTITLE='Fraction of galaxies',CHARSIZE=1.1,CHARTHICK=1.5,XTHICK=1.5,YTHICK=1.5
histoplot,rsoffset[g],BINSIZE=0.05,MININPUT=-1.85,MAXINPUT=0.5,THICK=2,/outline,/frequency,/oplot,histdata=hist1,locations=loc1
oplot,bndX,bndY,linestyle=1,THICK=3


names = ['Cl0023','Cl1324','RXJ1757','RXJ1821','Cl1604']
rfiles = ['/home/rumbaugh/LFC/FINAL.matched.0023.specnXray.nov2010.rumbaugh.cat','/home/rumbaugh/LFC/FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat','/home/rumbaugh/LFC/FINAL.matched.N200.specnXray.nov2010.rumbaugh.cat','/home/rumbaugh/LFC/FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat','/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat']
zub = [0.856,0.785,0.705,0.828,0.96]
zlb = [0.82,0.655,0.68,0.808,0.84]
rsfitb = [1.777,1.325,1.84,1.203,3.182]
rsfitm = [0.0229,0.0084,0.0319,0.0012,0.063]
rsSTD = [0.0625,0.0735,0.0576,0.0413,0.0907]
rsNSTD = [3.,3.,3.,3.,2.]

for i=0,3 do begin &$
readcol,rfiles[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D' &$
g = where((zub[i] ge z) and (z ge zlb[i])) &$
h = where(q[g] gt 2.1) &$
rsfit = rsfitb[i]-rsfitm[i]*iB &$
rsoffset = (rB-iB-rsfit) &$
if i lt 0.1 then y_RSO = [y_RSO,rsoffset[g[h]]] &$
if i gt 0.1 then o_RSO = [o_RSO,rsoffset[g[h]]] &$
endfor

readcol,rfiles[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,mskACA,raACA,decACA,idACA,F606W,F814W,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D'
h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90))
g = where((z[h] le 0.96) and (z[h] ge 0.84))
rsfit = 3.182-0.063*iB
rsoffset = (F606W-F814W-rsfit)
y_RSO2 = rsoffset[h[g]]


;plot,[0,1],[0,1],/nodata,XTITLE="Red Sequence Offset(r'-i')",YTITLE='Num. of AGN',XRANGE=[-1.375,0.5],YRANGE=[0,3.5],/xstyle,/ystyle,XTHICK=4.5,YTHICK=4,CHARTHICK=4,YTICKS=3,YTICKV=[0,1,2,3],XMINOR=4,CHARSIZE=1.3
;HISTOPLOT,y_RSO,BINSIZE=0.25,MININPUT=-1.375,MAXINPUT=0.5,xstyle=1,ystyle=1,/LINE_FILL,polycolor='Charcoal',datacolorname='Charcoal',spacing=0.4,orientation=-45,THICK=6,/oplot
;HISTOPLOT,o_RSO,BINSIZE=0.25,MININPUT=-1.375,MAXINPUT=0.5,xstyle=1,ystyle=1,polycolor='Indian Red',THICK=8,datacolorname='Indian Red',/oplot
;legend,['Cl0023','Cl1324,RXJ1821,RXJ1757'],color=['0','255'],PSYM=[6,6],SYMSIZE=[0.8,0.8],CHARTHICK=4,CHARSIZE=1,THICK=18,/left

plot,[0,1],[0,1],/nodata,XTITLE="Red Sequence Offset(F606W-F814W)",YTITLE='Num. of AGN',XRANGE=[-1.375,0.5],YRANGE=[0,3.5],/xstyle,/ystyle,XTHICK=4.5,YTHICK=4,CHARTHICK=4,YTICKS=3,YTICKV=[0,1,2,3],XMINOR=4,CHARSIZE=1.3
HISTOPLOT,y_RSO2,BINSIZE=0.125,MININPUT=-1.375,MAXINPUT=0.5,xstyle=1,ystyle=1,/LINE_FILL,polycolor='Charcoal',datacolorname='Charcoal',spacing=0.4,orientation=-45,THICK=6,/oplot

oplot,loc1,hist1*40,PSYM=10,color=60,THICK=3
oplot,bndX,bndY,linestyle=1,THICK=3

legend,['Cl1604 AGN','All Cl1604 Sources'],color=[0,60],PSYM=[6,0],SYMSIZE=[0.8,1],CHARTHICK=4,CHARSIZE=1.3,THICK=[18,2],/left

y_RSO = []
o_RSO = []

for i=0,3 do begin &$
readcol,rfiles[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D' &$
g = where((zub[i] ge z) and (z ge zlb[i])) &$
h = where(q[g] gt 2.1) &$
rsfit = rsfitb[i]-rsfitm[i]*iB &$
rsoffset = (rB-iB-rsfit)/(2.0*rsNSTD[i]*rsSTD[i]) &$
;if i eq 1 then print,z[g[h]] &$
if i lt 0.1 then y_RSO = [y_RSO,rsoffset[g[h]]] &$
if i gt 0.1 then o_RSO = [o_RSO,rsoffset[g[h]]] &$
endfor

readcol,rfiles[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,mskACA,raACA,decACA,idACA,F606W,F814W,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D'
h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90))
g = where((z[h] le 0.96) and (z[h] ge 0.84))
rsfit = 3.182-0.063*iB
rsoffset = (F606W-F814W-rsfit)/(2.0*rsNSTD[i]*rsSTD[i])
y_RSO = [y_RSO,rsoffset[h[g]]]

plot,[0,1],[0,1],/nodata,XTITLE='Red Sequence Offset(RS widths)',YTITLE='Num. of AGN',XRANGE=[-7,2],YRANGE=[0,3.5],/xstyle,/ystyle,XTHICK=4.5,YTHICK=4,CHARTHICK=4,CHARSIZE=1.3,YTICKS=3,YTICKV=[0,1,2,3],XMINOR=4
HISTOPLOT,y_RSO,BINSIZE=0.25,MININPUT=-7,MAXINPUT=2,xstyle=1,ystyle=1,/LINE_FILL,polycolor='Charcoal',datacolorname='Charcoal',spacing=0.4,orientation=-45,THICK=6,/oplot
HISTOPLOT,o_RSO,BINSIZE=0.25,MININPUT=-7,MAXINPUT=2,xstyle=1,ystyle=1,datacolorname='Indian Red',THICK=8,/oplot
oplot,loca,hista/17.0,PSYM=10,color=60,THICK=3
legend,['All Spec. Sources','Cl1604,Cl0023','Cl1324,RXJ1821,RXJ1757'],color=['60','0','255'],PSYM=[0,6,6],SYMSIZE=[0.8,0.8,0.8],CHARTHICK=4,CHARSIZE=1,THICK=[2,18,18],/left
bndsX = [-0.5,-0.5,0.5,0.5]
bndsY = [0,1000,1000,0]
oplot,bndsX,bndsY,linestyle=1,THICK=3


end
