set_dirs
set_plot,'PS'
loadct,13

xl = [16,18,28]
rsb = [1.777,1.325,1.84,1.48,1.305]
rsm = [0.0229,0.0084,0.0319,0.012,0.00485]
rsstd = [0.0625,0.0735,0.0576,0.0636,0.0813]
nstd = [3,3,3,3,2]
names = ['Cl0023','Cl1324','RXJ1757','NEP5281','Cl1604']
pfiles = ['cl0023_radecIDmags.cat','sc1322.lfc.newIDsandoldIds.radecmag.cat','nep200.idradecmag.lfc.uhcorr.neat','nep5281.lfc.newIDradecmag.cat','final.idradecmag.lfcpluscosmic.withsdss.cat']
mfiles = ['FINAL.matched.0023.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat','FINAL.matched.N200.specnXray.nov2010.rumbaugh.noheader.cat','FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat','FINAL.matched.1604.specnXray.nov2010.rumbaugh.noheader.cat']
path = "/home/rumbaugh/LFC/"
zlb = [0.82,0.66,0.68,0.808,0.84]
zub = [0.856,0.785,0.705,0.828,0.96]

device,file="/home/rumbaugh/colVr.plot.completeness.3.8.11.ps",/color
for i=0,4 do begin &$
ptitle = 'AGN Color-Magnitude Diagram - ' + names[i] &$
plot,[0,1],[0,1],/nodata,TITLE=ptitle,XTITLE="i'-Band Magnitude",YTITLE="r'-i'",PSYM=3,THICK=2,SYMSIZE=0.1,XRANGE=[19,26],YRANGE=[-0.5,1.9],xstyle=1,ystyle=1 &$
pfile = path + pfiles[i] &$
mfile = path + mfiles[i] &$
cfile = '/home/rumbaugh/paperstuff/matchedVunmatched.' + names[i] + '.dat' &$
readcol,cfile,ra,dec,q,z,rB,iB,zB,format='D,D,I,D,D,D,D' &$
rsfit = rsb[i]-rsm[i]*xl &$
gg = where((q eq -1) or (q gt 2.5)) &$
g = where((z[gg] ge zlb[i]) and (z[gg] le zub[i])) &$
oplot,iB[gg[g]],rB[gg[g]]-iB[gg[g]],PSYM=4,SYMSIZE=1.5,THICK=2,color=160 &$
oplot,iB,rB-iB,PSYM=2,SYMSIZE=0.3,THICK=8,color=10 &$
oplot,iB[gg],rB[gg]-iB[gg],PSYM=2,SYMSIZE=0.3,THICK=8.5,color=250 &$
gg = where((q eq 1) or (q eq 2)) &$
oplot,iB[gg],rB[gg]-iB[gg],PSYM=2,SYMSIZE=0.3,THICK=8.7,color=110 &$
yu = nstd[i]*rsstd[i]+rsfit &$
yl = -nstd[i]*rsstd[i]+rsfit &$
oplot,xl,yl,linestyle=3,thick=1.7,color=30 &$
oplot,xl,yu,linestyle=3,thick=1.7,color=30 &$
endfor



end
