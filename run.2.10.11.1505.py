set_dirs
c2f = [[5.66306511542e-11,1.66681616965e-11,1.67083124157e-11,1.71226366747e-11,1.71288816213e-11,3.58103893313e-10,1.37889668047e-10],[2.15619390269e-11,1.76555669098e-11,1.76481547625e-11,1.83530000159e-11,1.83487592541e-11,2.86905834614e-11,2.58843094352e-11]]
nh = [2.79,1.22,1.155,5.66,4.07]
ids = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
mas = ['7914','master','master','master','master']
f2l = [1.676e+57,1.987e+57,1.310e+57,1.580e+57,1.034e+57]
zhb = [0.855,0.96,0.785,0.828,0.705]
zlb = [0.820,0.84,0.660,0.808,0.68]
set_plot,'PS'
loadct,'13'
device,file="/home/rumbaugh/LFC/analysis/XlumvsHRPlots.ps",/color
totalslum = []
totalhlum = []
yslum = []
yhlum = []
oslum = []
ohlum = []
yHR = []
oHR = []
ic = []
yIC = []
oIC = []
cl1324rac = 0.5*(30.86373172217+30.279328719557)
c2finds = [0,1,3,5,6]

mx = (43.2104078-43.348505)/(240.9472-241.28263)

for i=0,4 do begin &$
   fileroot = '/home/rumbaugh/LFC/XrayLums.' + ids[i] + '.soft.dat' &$
   readcol,fileroot,slum,sflux,sncnts,sz,sra,sdec &$
   fileroot = '/home/rumbaugh/LFC/XrayLums.' + ids[i] + '.hard.dat' &$
   readcol,fileroot,hlum,hflux,hncnts,hz,hra,hdec &$
   ictemp = make_array(n_elements(sz),value=0) &$
   gic = where((sz ge zlb[i]) and (sz le zhb[i])) &$
   ictemp[gic] = 1 &$
   ic = [ic,ictemp] &$
   ghr = where(sncnts+hncnts gt 0) &$
   HRt = (hncnts[ghr]-sncnts[ghr])/(hncnts[ghr]+sncnts[ghr]) &$
   ratemp = mx*(sra-241.28263)+43.348505 &$
   flum = slum+hlum &$
   totalslum = [totalslum,slum] &$
   totalhlum = [totalhlum,hlum] &$
   if i lt 2 then yIC = [yIC,ictemp[ghr]] &$
   if i ge 2 then oIC = [oIC,ictemp[ghr]] &$
   if i lt 2 then yslum = [yslum,slum[ghr]] &$
   if i lt 2 then yhlum = [yhlum,hlum[ghr]] &$
   if i ge 2 then oslum = [oslum,slum[ghr]] &$
   if i ge 2 then ohlum = [ohlum,hlum[ghr]] &$
   if i lt 2 then yHR = [yHR,HRt] &$
   if i ge 2 then oHR = [oHR,HRt] &$
   ;Histoplot,slum,TITLE=ids[i]+" - Soft Band" &$
   ;Histoplot,hlum,TITLE=ids[i]+" - Hard Band" &$
   ;Histoplot,flum,TITLE=ids[i]+" - Full Band" &$
endfor
totalflum = totalslum+totalhlum
yflum=yslum+yhlum
oflum=oslum+ohlum
plot,/nodata,[0,1],[0,1],TITLE="HR vs Full Band Rest Frame Luminosity",XTITLE="Log Luminosity - Full Band",ytitle="Hardness Ratio",xrange=[41.75,44],YRANGE=[-1.5,1.1],xstyle=1,ystyle=1
g = where((yflum gt 0) and (yIC gt 0.5))
oplot,alog10(yflum[g])+42,yHR[g],PSYM=4,THICK=2,color=250
oplot,alog10(oflum[g])+42,oHR[g],PSYM=6,THICK=2,color=80
legend,['NEP+1324','1604+0023'],PSYM=[6,4],THICK=[2,2],color=[80,250]
plot,/nodata,[0,1],[0,1],TITLE="HR vs Soft Band Rest Frame Luminosity",XTITLE="Log Luminosity - Soft Band",ytitle="Hardness Ratio",xrange=[41.0,43.5],YRANGE=[-1.5,1.1],xstyle=1,ystyle=1
g = where((yslum gt 0) and (yIC gt 0.5))
oplot,alog10(yslum[g])+42,yHR[g],PSYM=4,THICK=2,color=250
oplot,alog10(oslum[g])+42,oHR[g],PSYM=6,THICK=2,color=80
legend,['NEP+1324','1604+0023'],PSYM=[6,4],THICK=[2,2],color=[80,250]
plot,/nodata,[0,1],[0,1],TITLE="HR vs Hard Band Rest Frame Luminosity",XTITLE="Log Luminosity - Hard Band",ytitle="Hardness Ratio",xrange=[41.75,44],YRANGE=[-1.5,1.1],xstyle=1,ystyle=1
g = where((yhlum gt 0) and (yIC gt 0.5))
oplot,alog10(yhlum[g])+42,yHR[g],PSYM=4,THICK=2,color=250
oplot,alog10(ohlum[g])+42,oHR[g],PSYM=6,THICK=2,color=80
legend,['NEP+1324','1604+0023'],PSYM=[6,4],THICK=[2,2],color=[80,250]

end
