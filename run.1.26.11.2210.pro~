set_dirs
set_plot,'PS'
loadct,13

xl = [16,18,28]

device,file="/home/rumbaugh/LFC/analysis/RSoffset.plot_all+clust.1.24.11.ps",/color
readcol,"/home/rumbaugh/LFC/FINAL.matched.0023.specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D'
readcol,"/home/rumbaugh/LFC/cl0023_radecIDmags.cat",newid,raLFC,decLFC,rprime,iprime,zprime
rsfit = 1.777-0.0229*iprime
rsoffset = rprime-iprime-rsfit
plot,iprime,rsoffset,TITLE="AGN Color-Magnitude Diagram - 0023",XTITLE="i'-Band Magnitude",YTITLE="Red Sequence Offset",PSYM=3,THICK=2,SYMSIZE=0.1,XRANGE=[17,27],YRANGE=[-3,3],xstyle=1,ystyle=1
readcol,"FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat",newid,mask,slit,raLFC,decLFC,rprime,iprime,zprime,rs,rserr,Q,oldid,format="A,A,A,D,D,D,D,D,D,D,I,A"
rsfit = 1.777-0.0229*iprime
rsoffset = rprime-iprime-rsfit
g = where((0.856 ge rs) and (rs ge 0.82))
oplot,iprime[g],rsoffset[g],PSYM=2,THICK=2,SYMSIZE=0.2,color=250
g = where((0.856 ge z) and (z ge 0.82))
rsfit = 1.777-0.0229*iB
rsoffset = rB-iB-rsfit
oplot,iB[g],rsoffset[g],PSYM=6,THICK=2,SYMSIZE=1,color=180
;legend,['All LFC sources','All Spectrally Matched X-ray
;Sources','0023 Members'],PSYM=[3,4,6],colors=[0,120,250]
;yl = 1.777-0.0229*xl
yl = -3*0.0625*[1,1,1]
oplot,xl,yl,linestyle=3,thick=1.7



readcol,"/home/rumbaugh/LFC/FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,A,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D'
readcol,"/home/rumbaugh/LFC/sc1322.lfc.newIDsandoldIds.radecmag.cat",newid,id2,raLFC,decLFC,rprime,iprime,zprime,format='A,I,D,D,D,D,D'
rsfit = 1.325-0.0084*iprime
rsoffset = rprime-iprime-rsfit
plot,iprime,rsoffset,TITLE="AGN Color-Magnitude Diagram - 1324",XTITLE="i'-Band Magnitude",YTITLE="Redshift Sequence Offset",PSYM=3,XRANGE=[17,27],YRANGE=[-3,3],xstyle=1,ystyle=1
readcol,"FINAL.cl1322.lrisplusdeimos.cat",newid,mask,slit,raLFC,decLFC,rprime,iprime,zprime,rs,rserr,Q,oldid,format="A,A,A,D,D,D,D,D,D,D,I,A"
g = where((0.785 ge rs) and (rs ge 0.67))
rsfit = 1.325-0.0084*iprime
rsoffset = rprime-iprime-rsfit
oplot,iprime[g],rsoffset[g],PSYM=2,SYMSIZE=0.2,THICK=2,color=250
g = where((0.785 ge z) and (z ge 0.67))
rsfit = 1.325-0.0084*iB
rsoffset = rB-iB-rsfit
oplot,iB[g],rsoffset[g],PSYM=6,THICK=2,SYMSIZE=1,color=180
;legend,['All LFC sources','All Spectrally Matched X-ray Sources','0023 Members'],PSYM=[3,4,6],colors=[0,120,250]
;yl = 1.325-0.0084*xl
yl = -3*0.0735*[1,1,1]
oplot,xl,yl,linestyle=3,thick=1.7


readcol,"/home/rumbaugh/LFC/FINAL.matched.N200.specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D'
readcol,"/home/rumbaugh/LFC/nep200.idradecmag.lfc.uhcorr.neat",newid,raLFC,decLFC,rprime,iprime,zprime,format='A,D,D,D,D,D'
rsfit = 1.84-0.0319*iprime
rsoffset = rprime-iprime-rsfit
plot,iprime,rsoffset,TITLE="AGN Color-Magnitude Diagram - NEP200",XTITLE="i'-Band Magnitude",YTITLE="Redshift Sequence Offset",PSYM=3,XRANGE=[17,27],YRANGE=[-3,3],xstyle=1,ystyle=1
readcol,"FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat",newid,mask,slit,raLFC,decLFC,rprime,iprime,zprime,rs,rserr,Q,oldid,format="A,A,A,D,D,D,D,D,D,D,I,A"
rsfit = 1.84-0.0319*iprime
rsoffset = rprime-iprime-rsfit
g = where((0.705 ge rs) and (rs ge 0.68))
oplot,iprime[g],rsoffset[g],PSYM=2,SYMSIZE=0.2,THICK=2,color=250
g = where((0.705 ge z) and (z ge 0.68))
rsfit = 1.84-0.0319*iB
rsoffset = rB-iB-rsfit
oplot,iB[g],rsoffset[g],PSYM=6,THICK=2,SYMSIZE=1,color=180
;legend,['All LFC sources','All Spectrally Matched X-ray Sources','NEP200 Members'],PSYM=[3,4,6],colors=[0,120,250]
;yl = 1.84-0.0319*xl
yl = -3*0.0576*[1,1,1]
oplot,xl,yl,linestyle=3,thick=1.7


readcol,"/home/rumbaugh/LFC/FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,I,D,D,D,D,D'
readcol,"/home/rumbaugh/LFC/nep5281.lfc.newIDradecmag.cat",newid,raLFC,decLFC,rprime,iprime,zprime
rsfit = 1.48-0.012*iprime
rsoffset = rprime-iprime-rsfit
plot,iprime,rsoffset,TITLE="AGN Color-Magnitude Diagram - NEP5281",XTITLE="i'-Band Magnitude",YTITLE="Redshift Sequence Offset",PSYM=3,XRANGE=[17,27],YRANGE=[-3,3],xstyle=1,ystyle=1
readcol,"FINAL.nep5281.deimos.gioia.feb2010.cat",newid,mask,slit,raLFC,decLFC,rprime,iprime,zprime,rs,rserr,Q,oldid,format="A,A,A,D,D,D,D,D,D,D,I,A"
g = where((0.828 ge rs) and (rs ge 0.808))
rsfit = 1.48-0.012*iprime
rsoffset = rprime-iprime-rsfit
oplot,iprime[g],rsoffset[g],PSYM=2,SYMSIZE=0.2,THICK=2,color=250
g = where((0.828 ge z) and (z ge 0.808))
rsfit = 1.48-0.012*iB
rsoffset = rB-iB-rsfit
oplot,iB[g],rsoffset[g],PSYM=6,THICK=2,SYMSIZE=1,color=180
;legend,['All LFC sources','All Spectrally Matched X-ray Sources','NEP5281 Members'],PSYM=[3,4,6],colors=[0,120,250]
;yl = 1.48-0.012*xl
yl = -3*0.0636*[1,1,1]
oplot,xl,yl,linestyle=3,thick=1.7

readcol,"/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,mskACA,raACA,decACA,idACA,F606W,F814W,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D'
readcol,"/home/rumbaugh/LFC/final.idradecmag.lfcpluscosmic.withsdss.cat",newid,raLFC,decLFC,rprime,iprime,zprime,format='A,D,D,D,D,D'
rsfit = 1.305-0.00485*iprime
rsoffset = rprime-iprime-rsfit
plot,iprime,rsoffset,TITLE="AGN Color-Magnitude Diagram - 1604 - LFC only",XTITLE="i'-Band Magnitude",YTITLE="Redshift Sequence Offset",PSYM=3,XRANGE=[17,27],YRANGE=[-3,3],xstyle=1,ystyle=1
readcol,"FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat",newid,mask,slit,raLFC,decLFC,rprime,iprime,zprime,rs,rserr,Q,oldid,pflags,raACS,decACS,idACS,f606,f814,format="A,A,A,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D"
g = where((0.96 ge rs) and (rs ge 0.84))
rsfit = 1.305-0.00485*iprime
rsoffset = rprime-iprime-rsfit
oplot,iprime[g],rsoffset[g],PSYM=2,SYMSIZE=0.2,THICK=2,color=250
g = where((0.96 ge z) and (z ge 0.84))
rsfit = 1.305-0.00485*iB
rsoffset = rB-iB-rsfit
oplot,iB[g],rsoffset[g],PSYM=6,THICK=2,SYMSIZE=1,color=180
;yl = 1.305-0.00485*xl
yl = -2*0.0813*[1,1,1]
oplot,xl,yl,linestyle=3,thick=1.7
;legend,['All LFC sources','LFC Spectrally Matched X-ray Sources','Supercluster Members'],PSYM=[3,4,6],colors=[0,120,250]
;device,file="/home/rumbaugh/LFC/analysis/colorVr.plot_all+clust.1604.11.20.10.ACS.ps",/color
readcol,"/home/rumbaugh/LFC/ACS_merged.F606W+F814W_deep.all.coll.dat",raACS,decACS,m606,m814,sh1,sh2,sh3,sh4,sh5,sh6
hh = where((f606 gt 0.1) and (f606 lt 90) and (f814 gt 0.1) and (f814 lt 90))
rsfit = 3.182-0.063*f814
rsoffset = f606-f814-rsfit
plot,f814[hh],rsoffset[hh],TITLE="AGN Color-Magnitude Diagram - 1604 - ACS only",XTITLE="F814W Magnitude",YTITLE="F606W-F814W",PSYM=3,XRANGE=[17,27],YRANGE=[-3,3],xstyle=1,ystyle=1
g = where((0.96 ge rs[hh]) and (rs[hh] ge 0.84))
h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90))
hh = where((f606 gt 0.1) and (f606 lt 90) and (f814 gt 0.1) and (f814 lt 90))
rsfit = 3.182-0.063*f814
rsoffset = f606-f814-rsfit
oplot,f814[hh[g]],rsoffset[hh[g]],PSYM=2,SYMSIZE=0.2,THICK=2,color=250
g = where((z[h] le 0.96) and (z[h] ge 0.84))
rsfit = 3.182-0.063*F814W
rsoffset = F606W-F814W-rsfit
oplot,F814W[h[g]],rsoffset[h[g]],color=180,PSYM=6
;F814W[h[g]] = 99
;h = where((F606W lt 90) and (F606W gt 0.1) and (F814W gt 0.1) and (F814W lt 90))

;oplot,F814W[h],F606W[h]-F814W[h],color=120,PSYM=4
yl = -2*0.0907*[1,1,1]
oplot,xl,yl,linestyle=3,thick=1.7
;legend,['All ACS sources','ACS Spectrally Matched X-ray
;Sources','Supercluster Members'],PSYM=[3,4,6],colors=[0,120,250]


end
