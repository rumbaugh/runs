set_dirs
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/control.anal.plot.2.24.11.ps',/color

sSTD = [9.08,5.41,4.24, 5.41,6.06,6.70,4.03, 4.86,4.94, 5.95,6.66,3.47, 7.02,6.12]
mSTD = [7.10,3.76, 2.85,3.44,3.77,4.99,2.98,3.12,2.99,4.39,4.37,2.66,5.72,4.58]
lSTD = [5.68,3.21,2.40,2.68,2.79,4.39,2.38,2.64,2.38,3.49,3.52,2.27,5.02,3.75]

x = MAKE_ARRAY(n_elements(sSTD),value=18.83/2.0)

plot,[0-1],[0-1],/nodata,xrange=[6.5,19],yrange=[0,11],xstyle=1,ystyle=1,XTITLE='Core Radius (Arcseconds)',YTITLE='Height of Peak Above Mean (Std. Deviations)',CHARTHICK=1.5,YTHICK=2,XTHICK=2,CHARSIZE=1.3

oplot,x,sSTD,PSYM=4,color=250,SYMSIZE=2.5,THICK=2

x = x*27.27/18.83

oplot,x,mSTD,PSYM=4,color=160,SYMSIZE=2.5,THICK=2

x = x*35.1/27.27

oplot,x,lSTD,PSYM=4,color=65,SYMSIZE=2.5,THICK=2

t = [20,35.1/2.0,27.27/2.0,18.83/2.0,0]
y = [5.0,5.0,5.0,6.0,5.0+27.27/(27.27-18.83)]
oplot,t,y,LINESTYLE=2,THICK=2
end
