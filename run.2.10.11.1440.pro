set_dirs
c2f = [[5.66306511542e-11,1.66681616965e-11,1.67083124157e-11,1.71226366747e-11,1.71288816213e-11,3.58103893313e-10,1.37889668047e-10],[2.15619390269e-11,1.76555669098e-11,1.76481547625e-11,1.83530000159e-11,1.83487592541e-11,2.86905834614e-11,2.58843094352e-11]]
nh = [2.79,1.22,1.155,5.66,4.07]
ids = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
mas = ['7914','master','master','master','master']
f2l = [1.676e+12,1.987e+12,1.310e+12,1.580e+12,1.034e+12]
set_plot,'PS'
loadct,'13'
device,file="/home/rumbaugh/LFC/analysis/XrayLumPlots.test.ps",/color
totalslum = []
totalhlum = []
yslum = []
yhlum = []
oslum = []
ohlum = []
cl1324rac = 0.5*(30.86373172217+30.279328719557)
c2finds = [0,1,3,5,6]
zhb = [0.855,0.96,0.785,0.828,0.705]
zlb = [0.820,0.84,0.660,0.808,0.68]

mx = (43.2104078-43.348505)/(240.9472-241.28263)

for i=0,4 do begin &$
   fileroot = '/scratch/rumbaugh/ciaotesting/' + ids[i] + '/' + mas[i] + '/photometry/' + ids[i] + '.xray_phot.soft_hard_full.dat' &$
   readcol,fileroot,ra,dec,ff,sf,hf,ncntsf,ncntss,ncntsh,cntsf,cntss,cntsh,sf,ss,sh,mask,g,FORMAT="D,D,D,D,D,D,D,D,D,D,D,D,D,D,I,I" &$
   sqflux = ncntss*c2f[c2finds[i],0] &$
   hqflux = ncntsh*c2f[c2finds[i],1] &$
   ratemp = mx*(ra-241.28263)+43.348505 &$
   for ii=0,n_elements(ra)-1 do if (((i eq 2) and (ra[ii] lt cl1324rac)) or ((i eq 1) and (ra[ii] gt ratemp[ii]))) then sqflux = ncntss*c2f[c2finds[i+1],1] &$
   for ii=0,n_elements(ra)-1 do if (((i eq 2) and (ra[ii] lt cl1324rac)) or ((i eq 1) and (ra[ii] gt ratemp[ii]))) then hqflux = ncntsh*c2f[c2finds[i+1],1] &$
   fqflux = sqflux+hqflux &$
   slum = sqflux*f2l[i] &$
   hlum = hqflux*f2l[i] &$
   flum = slum+hlum &$
   slum = alog(slum)+42 &$
   hlum = alog(hlum)+42 &$
   flum = alog(flum)+42 &$
   totalslum = [totalslum,slum] &$
   totalhlum = [totalhlum,hlum] &$
   if i lt 2 then yslum = [yslum,slum] &$
   if i lt 2 then yhlum = [yhlum,hlum] &$
   if i ge 2 then oslum = [oslum,slum] &$
   if i ge 2 then ohlum = [ohlum,hlum] &$
   ;Histoplot,slum,TITLE=ids[i]+" - Soft Band" &$
   ;Histoplot,hlum,TITLE=ids[i]+" - Hard Band" &$
   ;Histoplot,flum,TITLE=ids[i]+" - Full Band" &$
endfor
totalflum = alog(exp(totalslum-42)+exp(totalhlum-42))+42
yflum=alog(exp(yslum-42)+exp(yhlum-42))+42
oflum=alog(exp(oslum-42)+exp(ohlum-42))+42
;plot,totalslum
;Histoplot,totalslum,TITLE="Total Soft Band"
;Histoplot,totalhlum,TITLE="Total Hard Band"
;Histoplot,totalflum,TITLE="Total Full Band"
Histoplot,yslum,TITLE="Comparison - Soft Band",/LINE_FILL,ORIENTATION=-45,SPACING=0.02,POLYCOLOR='Indian Red'
Histoplot,oslum,TITLE="Comparison - Soft Band",/LINE_FILL,POLYCOLOR='Charcoal',ORIENTATION=45,/oplot
Histoplot,yhlum,TITLE="Comparison - Hard Band",/LINE_FILL,ORIENTATION=-45,SPACING=0.02,POLYCOLOR='Indian Red'
Histoplot,ohlum,TITLE="Comparison - Hard Band",/LINE_FILL,POLYCOLOR='Charcoal',ORIENTATION=45,/oplot
Histoplot,yflum,TITLE="Comparison - Full Band",/LINE_FILL,ORIENTATION=-45,SPACING=0.02,POLYCOLOR='Indian Red'
Histoplot,oflum,TITLE="Comparison - Full Band",/LINE_FILL,POLYCOLOR='Charcoal',ORIENTATION=45,/oplot
end

