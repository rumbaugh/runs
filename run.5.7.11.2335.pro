set_dirs
set_plot,'PS'
loadct,13

xl = [16,18,28]

hist_mag = []
y_RSO = []
o_RSO = []

names = ['Cl0023','Cl1324','RXJ1757','RXJ1821','Cl1604']
rfiles = ['/home/rumbaugh/LFC/FINAL.matched.0023.specnXray.nov2010.rumbaugh.cat','/home/rumbaugh/LFC/FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat','/home/rumbaugh/LFC/FINAL.matched.N200.specnXray.nov2010.rumbaugh.cat','/home/rumbaugh/LFC/FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat','/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat']
zub = [0.856,0.785,0.705,0.828,0.96]
zlb = [0.82,0.66,0.68,0.808,0.84]
rsfitb = [1.777,1.325,1.84,1.203,3.182]
rsfitm = [0.0229,0.0084,0.0319,0.0012,0.063]
rsSTD = [0.0625,0.0735,0.0576,0.0413,0.0907]
rsNSTD = [3.,3.,3.,3.,2.]

device,file="/home/rumbaugh/paperstuff/RSoffset.hist.all.5.7.11.ps",/color

for i=0,3 do begin &$
readcol,rfiles[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D' &$
g = where((zub[i] ge z) and (z ge zlb[i])) &$
rsfit = rsfitb[i]-rsfitm[i]*iB &$
rsoffset = (rB-iB-rsfit) &$
if i lt 0.1 then y_RSO = [y_RSO,rsoffset[g]] &$
if i gt 0.1 then o_RSO = [o_RSO,rsoffset[g]] &$
endfor

readcol,rfiles[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,mskACA,raACA,decACA,idACA,F606W,F814W,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D'
h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90))
g = where((z[h] le 0.96) and (z[h] ge 0.84))
rsfit = 3.182-0.063*iB
rsoffset = (F606W-F814W-rsfit)
y_RSO2 = rsoffset[h[g]]


plot,[0,1],[0,1],/nodata,XTITLE="Red Sequence Offset(r'-i')",YTITLE='Num. of AGN',XRANGE=[-1.375,0.5],YRANGE=[0,3.5],/xstyle,/ystyle,XTHICK=2.5,YTHICK=2,CHARTHICK=2,YTICKS=3,YTICKV=[0,1,2,3],XMINOR=4
HISTOPLOT,y_RSO,BINSIZE=0.125,MININPUT=-1.375,MAXINPUT=0.5,xstyle=1,ystyle=1,/LINE_FILL,polycolor='Charcoal',datacolorname='Charcoal',spacing=0.1,orientation=-45,THICK=2,/oplot
HISTOPLOT,o_RSO,BINSIZE=0.125,MININPUT=-1.375,MAXINPUT=0.5,xstyle=1,ystyle=1,polycolor='Indian Red',THICK=8,datacolorname='Indian Red',/oplot
legend,['Cl0023','Cl1324,RXJ1821,RXJ1757'],color=['0','255'],PSYM=[6,6],SYMSIZE=[0.8,0.8],CHARTHICK=2,CHARSIZE=1,THICK=18,/left

plot,[0,1],[0,1],/nodata,XTITLE="Red Sequence Offset(F606W-F814W)",YTITLE='Num. of AGN',XRANGE=[-1.375,0.5],YRANGE=[0,3.5],/xstyle,/ystyle,XTHICK=2.5,YTHICK=2,CHARTHICK=2,YTICKS=3,YTICKV=[0,1,2,3],XMINOR=4
HISTOPLOT,y_RSO2,BINSIZE=0.125,MININPUT=-1.375,MAXINPUT=0.5,xstyle=1,ystyle=1,/LINE_FILL,polycolor='Charcoal',datacolorname='Charcoal',spacing=0.4,orientation=-45,THICK=2,/oplot



bndX = [-2*0.0907,-2*0.0907,2*0.0907,2*0.0907]
bndY = [0,1000,1000,0]


readcol,"/home/rumbaugh/LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat",newid,mask,slit,raLFC,decLFC,rprime,iprime,zprime,rs,rserr,Q,oldid,pflags,raACS,decACS,idACS,f606,f814,format="A,A,A,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D"
g = where((0.96 ge rs) and (rs ge 0.84))
rsfit = 3.182-0.063*f814
rsoffset = f606-f814-rsfit
rsoNorm = rsoffset/(4.0*0.0907)
histoplot,rsoffset[g],BINSIZE=0.05,MINVALUE=-1.85,MAXVALUE=0.5,THICK=2,/outline,/frequency,/oplot
oplot,bndX,bndY,linestyle=1,THICK=3

legend,['Cl1604'],color=['0'],PSYM=[6],SYMSIZE=[0.8],CHARTHICK=2,CHARSIZE=1,THICK=18,/left

;device,file="/home/rumbaugh/paperstuff/RSoffset.hist.RSwid.4.30.11.ps",/color

for i=0,3 do begin &$
readcol,rfiles[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D' &$
g = where((zub[i] ge z) and (z ge zlb[i])) &$
rsfit = rsfitb[i]-rsfitm[i]*iB &$
rsoffset = (rB-iB-rsfit)/(2.0*rsNSTD[i]*rsSTD[i]) &$
if i lt 0.1 then y_RSO = [y_RSO,rsoffset[g]] &$
if i gt 0.1 then o_RSO = [o_RSO,rsoffset[g]] &$
endfor

readcol,rfiles[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,mskACA,raACA,decACA,idACA,F606W,F814W,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D'
h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90))
g = where((z[h] le 0.96) and (z[h] ge 0.84))
rsfit = 3.182-0.063*iB
rsoffset = (F606W-F814W-rsfit)/(2.0*rsNSTD[i]*rsSTD[i])
y_RSO = [y_RSO,rsoffset[h[g]]]

plot,[0,1],[0,1],/nodata,XTITLE='Red Sequence Offset(RS widths)',YTITLE='Num. of AGN',XRANGE=[-3.5,1],YRANGE=[0,3.5],/xstyle,/ystyle,XTHICK=2.5,YTHICK=2,CHARTHICK=2,YTICKS=3,YTICKV=[0,1,2,3],XMINOR=4
HISTOPLOT,y_RSO,BINSIZE=0.25,MININPUT=-3.5,MAXINPUT=1,xstyle=1,ystyle=1,/LINE_FILL,polycolor='Charcoal',datacolorname='Charcoal',spacing=0.1,orientation=-45,THICK=2,/oplot
HISTOPLOT,o_RSO,BINSIZE=0.25,MININPUT=-3.5,MAXINPUT=1,xstyle=1,ystyle=1,datacolorname='Indian Red',THICK=4,/oplot
legend,['Cl1604,Cl0023','Cl1324,RXJ1821,RXJ1757'],color=['0','255'],PSYM=[6,6],SYMSIZE=[0.8,0.8],CHARTHICK=2,CHARSIZE=1,THICK=18,/left
oplot,bndsX,bndsY,linestyle=1

end
