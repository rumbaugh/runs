
set_plot,'PS'
loadct,13

device,file="/home/rumbaugh/rshist.0910.1.11.12.ps",/color

readcol,'/home/rumbaugh/FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat',sID,mask,slit,RA,Dec,rB,iB,zB,z,zerr,flag,format='I,A,A,D,D,D,D,D,D,D,I'
gf = where(flag gt 2.2)

plot,[0,1],[0,1],/nodata,XTITLE='Redshift',YTITLE='Num. of Galaxies',THICK=2,XRANGE=[0,1.5],YRANGE=[0,40],xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=4,XTHICK=6,YTHICK=6 &$
Histoplot,z[gf],BINSIZE=0.01,MININPUT=0,MAXINPUT=2,THICK=4.5,datacolorname='black',/oplot

plot,[0,1],[0,1],/nodata,XTITLE='Redshift',YTITLE='Num. of Galaxies',THICK=2,XRANGE=[1,1.2],YRANGE=[0,30],xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=4,XTHICK=6,YTHICK=6 &$
Histoplot,z[gf],BINSIZE=0.0025,MININPUT=1,MAXINPUT=1.2,THICK=5,datacolorname='black',/oplot
end
