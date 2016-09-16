

names = ['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B']
ncnts = [670,298,96,212,108,219,69]

t3013 = 3

c2fH = [2.2276,2.218,2.2206,2.2199,2.2199,2.2196,2.2196]
c2fH10 = [

Temps = [4.95,3.75,4.71,3.71,t3013,3.50,1.64]
TerrU = [0.99,1.00,10,1.44,10,1.82,0.65]
TerrD = [0.74,0.68,2.95,0.94,2.99,1.08,0.45]

lineslope = (alog(1125)-alog(0.1))/(alog(20)-alog(1.333333))
lineb = alog(1125)-lineslope*alog(20)
expb = exp(lineb)
lineX = (DINDGEN(10000)+1)*(10.0/10000)
lineY = expb*lineX^lineslope

lumbol = DBLARR(n_elements(Temps))
lumbol2 = DBLARR(n_elements(Temps))
lumbol3 = DBLARR(n_elements(Temps))

readcol,'/home/rumbaugh/paperstuff/clus.lums.soft.5.24.11.dat',snames,lums,lumerrs,format='A,D,D'
readcol,'/home/rumbaugh/paperstuff/clus.lums.hard.5.24.11.dat',hnames,lumh,lumerrh,format='A,D,D'

for i=0,n_elements(lumbol)-1 do lumbol[i] = lum2lum(lums[i]/10.0,Temps[i],'0.5-2.0')
for i=0,n_elements(lumbol)-1 do lumbol2[i] = lum2lum(lumh[i]/10.0,Temps[i],'2.0-8.0')
for i=0,n_elements(lumbol)-1 do lumbol[i] = lum2lum(lums[i]/10.0,Temps[i],'0.5-2.0')

openw,1,'/home/rumbaugh/paperstuff/clus.lums.bol.5.24.11.dat'
for i=0,n_elements(lumbol)-1 do printf,1, lumbol[i]
close, 1

;set_plot,'PS'
;loadct,13
;device,file='/home/rumbaugh/paperstuff/LxT.plot.bol.5.14.11.ps',/color

;plot,[0-1],[0-1],/nodata,XRANGE=[0.8,8],YRANGE=[0.0999,105],/xlog,/ylog,XTITLE='T (keV)',YTITLE='Bolometric Luminosity (1e44 ergs/s)',xstyle=1,ystyle=1,XTHICK=4,YTHICK=4,CHARSIZE=1.3,CHARTHICK=4
;oplot,lineX,lineY,THICK=4
;oplot,Temps,

end
