set_plot,'PS'
loadct,13

device,file='/home/rumbaugh/veldisp_hists.5.2.12.ps',/color


names = ['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422']
names2 = names
;names2 = ['RXJ1757','RXJ1821','Cl0910+5422']
;names = ['nep200','nep5281','cl0910']
;ymaxes = [11,11,8]
ymaxes = [14,5,8,8,13,14,13,6,10]

for i=0,n_elements(names)-1 do begin
readcol,'/home/rumbaugh/temp/idl_clusprops.' + names2[i] + '.4.10.12.dat',sig,blusig,redsig,BCGvel
readcol,'/home/rumbaugh/temp/idl_vels.' + names2[i] + '.4.10.12.dat',vels,deltas,isblu,format='D,D,I'
plot,[0-1],[0-1],/nodata,xrange=[-2250,2250],yrange=[0,ymaxes[i]],XTITLE='Relative Recessional Velocity (km s!E-1!N)',YTITLE='Num. of Galaxies',TITLE=names2[i],xstyle=1,ystyle=1,XTHICK=4,YTHICK=4,CHARSIZE=1.3,CHARTHICK=4
gblu = where((isblu gt 0.5) and (isblu lt 1.5))
gred = where(isblu lt 0.5)
;if ((n_elements(gred) gt 8) and (n_elements(gblu) gt 8)) then begin
Histoplot,vels[gblu],BINSIZE=500,MININPUT=-2250,MAXINPUT=2250,THICK=2,datacolorname='Royal Blue',/LINE_FILL,POLYCOLOR='Royal Blue',ORIENTATION=0,spacing=0.2,/OPLOT
Histoplot,vels[gred],BINSIZE=500,MININPUT=-2250,MAXINPUT=2250,THICK=2,datacolorname='Red',/LINE_FILL,POLYCOLOR='Red',ORIENTATION=90,spacing=0.2,/OPLOT
Histoplot,vels,BINSIZE=500,MININPUT=-2250,MAXINPUT=2250,THICK=4.5,datacolorname='Black',/OPLOT
tempgaussx = MAKE_ARRAY(2000,/INDEX)*bounds[i]/1000.0-2250
tempgaussy = MAKE_ARRAY(2000)
for j=0,n_elements(tempgaussx)-1 do tempgaussy[j] = 500*(n_elements(vels)/(sig*sqrt(2*!PI)))*exp(-0.5*(tempgaussx[j]/sig)^2)
oplot,tempgaussx,tempgaussy,color=115,THICK=4
if ((n_elements(gred) ge 10) and (n_elements(gblu) ge 10)) then begin
for j=0,n_elements(tempgaussx)-1 do tempgaussy[j] = 500*(n_elements(gblu)/(blusig*sqrt(2*!PI)))*exp(-0.5*(tempgaussx[j]/blusig)^2)
oplot,tempgaussx,tempgaussy,color=80,THICK=5,LINESTYLE=1
for j=0,n_elements(tempgaussx)-1 do tempgaussy[j] = 500*(n_elements(gred)/(redsig*sqrt(2*!PI)))*exp(-0.5*(tempgaussx[j]/redsig)^2)
oplot,tempgaussx,tempgaussy,color=255,THICK=4,LINESTYLE=5
endif 
BCGx = [BCGvel,BCGvel,BCGvel+100,BCGvel,BCGvel-100,BCGvel,BCGvel]
ymax = ymaxes[i]
BCGy = [ymax*0.9,ymax*0.8,ymax*0.83,ymax*0.8,ymax*0.83,ymax*0.8,ymax*0.9]
oplot,BCGx,BCGy,color=240,THICK=5
endfor
end


