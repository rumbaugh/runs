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
rsSTD = [0.0625,0.0735,0.0576,0.0413,0.0813]
rsNSTD = [3.,3.,3.,3.,2.]

device,file="/home/rumbaugh/paperstuff/RSoffset.hist.sig.4.11.11.ps",/color

for i=0,3 do begin &$
readcol,rfiles[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D' &$
g = where((zub[i] ge z) and (z ge zlb[i])) &$
rsfit = rsfitb[i]-rsfitm[i]*iB &$
rsoffset = (rB-iB-rsfit)/rsSTD[i] &$
if i lt 0.1 then y_RSO = [y_RSO,rsoffset[g]] &$
if i gt 0.1 then o_RSO = [o_RSO,rsoffset[g]] &$
endfor

readcol,rfiles[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,mskACA,raACA,decACA,idACA,F606W,F814W,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D'
h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90))
g = where((z[h] le 0.96) and (z[h] ge 0.84))
rsfit = 3.182-0.063*iB
rsoffset = 1.5*(F606W-F814W-rsfit)/rsSTD[i]
y_RSO = [y_RSO,rsoffset[h[g]]]


plot,[0,1],[0,1],/nodata,XTITLE='Red Sequence Offset(!7r!3)',YTITLE='Num. of AGN',XRANGE=[-10,5],YRANGE=[0,4.1],/xstyle,/ystyle,XTHICK=2.5,YTHICK=2,CHARTHICK=2
HISTOPLOT,y_RSO,BINSIZE=0.125,MININPUT=-10,MAXINPUT=5,xstyle=1,ystyle=1,/LINE_FILL,polycolor='Indian Red',spacing=0.02,orientation=-45,THICK=2,/oplot
HISTOPLOT,o_RSO,BINSIZE=0.125,MININPUT=-19,MAXINPUT=5,xstyle=1,ystyle=1,/LINE_FILL,polycolor='Charcoal',spacing=0.2,orientation=45,THICK=1.5,datacolorname='Charcoal',/oplot

end
