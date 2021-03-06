set_dirs
usersymfs
c2f = [[5.66306511542e-11,1.66681616965e-11,1.67083124157e-11,1.71226366747e-11,1.71288816213e-11,3.58103893313e-10,1.37889668047e-10],[2.15619390269e-11,1.76555669098e-11,1.76481547625e-11,1.83530000159e-11,1.83487592541e-11,2.86905834614e-11,2.58843094352e-11]]
nh = [2.79,1.22,1.155,5.66,4.07]
ids = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
mas = ['7914','master','master','master','master']
f2l = [1.676e+57,1.987e+57,1.310e+57,1.580e+57,1.034e+57]
zhb = [0.855,0.96,0.785,0.828,0.705]
zlb = [0.820,0.84,0.655,0.808,0.68]
set_plot,'PS'
loadct,'13'
device,file="/home/rumbaugh/XrayLums.8.3.11.ps",/color
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
   gic = where((sz ge zlb[i]) and (sz le zhb[i]) and ((sz lt 0.8125) or (sz ge 0.8135)) and ((sz lt 0.8295) or (sz ge 0.8305)) and ((sz lt 0.6955) or (sz ge 0.6965)) and ((sz lt 0.9) or (sz ge 0.901))) &$
   ictemp[gic] = 1 &$
   ic = [ic,ictemp] &$
   flum = slum+hlum &$
   slum += 0.0000000001
   hlum += 0.0000000001
   slum = alog10(slum)+42
   hlum = alog10(hlum)+42
   totalslum = [totalslum,slum] &$
   totalhlum = [totalhlum,hlum] &$
   for ii=0,n_elements(gic)-1 do print,sra[gic[ii]],sdec[gic[ii]],sz[gic[ii]],alog10(10^(slum[gic[ii]]-42)+10^(hlum[gic[ii]]-42))+42 &$
   if i eq 2 then gcl = where(sz[gic] lt 0.66) &$
   if i eq 2 then print,alog10(10^(slum[gic[gcl]]-42)+10^(hlum[gic[gcl]]-42))+42 &$
   if i lt 2 then yslum = [yslum,slum[gic]] &$
   if i lt 2 then yhlum = [yhlum,hlum[gic]] &$
   if i ge 2 then oslum = [oslum,slum[gic]] &$
   if i ge 2 then ohlum = [ohlum,hlum[gic]] &$
   ;Histoplot,slum,TITLE=ids[i]+" - Soft Band" &$
   ;Histoplot,hlum,TITLE=ids[i]+" - Hard Band" &$
   ;Histoplot,flum,TITLE=ids[i]+" - Full Band" &$
endfor

totalflum = alog10(10^(totalslum-42)+10^(totalhlum-42))+42
yflum=alog10(10^(yslum-42)+10^(yhlum-42))+42
oflum=alog10(10^(oslum-42)+10^(ohlum-42))+42
;plot,totalslum
;Histoplot,totalslum,TITLE="Total Soft Band"
;Histoplot,totalhlum,TITLE="Total Hard Band"
;Histoplot,totalflum,TITLE="Total Full Band"

!p.position = square()
plot,[0,1],[0,1],/nodata,XTITLE='Log Luminosity',YTITLE='Num. of AGN',XRANGE=[41.5,44.5],YRANGE=[0,5.2],XSTYLE=1,YSTYLE=1,XTHICK=4,YTHICK=4,CHARSIZE=1.3,CHARTHICK=4
;Histoplot,yslum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Soft Band",THICK=4
;Histoplot,oslum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Soft Band",/LINE_FILL,POLYCOLOR='Royal Blue',ORIENTATION=45,/oplot
;legend,['Cl1604,Cl0023','Cl1324,NEP5281,NEP200'],color=['255','70']
;Histoplot,yhlum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Hard Band",THICK=4
;Histoplot,ohlum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Hard Band",/LINE_FILL,POLYCOLOR='Royal Blue',ORIENTATION=45,/oplot
;legend,['Cl1604,Cl0023','Cl1324,NEP5281,NEP200'],color=['255','70']
Histoplot,yflum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Full Band",datacolorname='Navy Blue',/LINE_FILL,THICK=2,POLYCOLOR='Navy Blue',ORIENTATION=45,spacing=0.25,LINESTYLE=2,/oplot
Histoplot,oflum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Full Band",THICK=10,datacolorname='Red',/oplot
legend,['Cl1324,RXJ1821,RXJ1757','Cl1604,Cl0023'],color=['255','50'],PSYM=[6,8],SYMSIZE=[1.5,1.5],CHARTHICK=4,CHARSIZE=1,THICK=[10,2],/right
end
