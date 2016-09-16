
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/paperstuff/compcorr.coldists.hist.ps',/color

names = ['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757']

;rsfitb = [1.777,1.325,1.84,1.203,1.305]
;rsfitm = [0.0229,0.0084,0.0319,0.0012,0.00485]
;rsSTD = [0.0625,0.0735,0.0576,0.0413,0.0813]

rsfitb = [ 1.325,  1.203,  1.777,  1.305,  1.84 ]
rsfitm = [ 0.0084 ,  0.0012 ,  0.0229 ,  0.00485,  0.0319 ]
rsSTD = [ 0.0735,  0.0413,  0.0625,  0.0813,  0.0576]
rsNSTD = [2,3,3,2,3]*1.0

BGareas = [ 0.01935708,  0.00989024,  0.01460552,  0.01942021,  0.01304679]
CLareas = [ 0.01508725,  0.00588442,  0.00329585,  0.01428435,  0.00389747]

ymax  = [80,30,60,60,50]
ymax2 = [80,30,20,60,20]

yt = [0,1000]

for i=0,4 do begin &$
   avgRSbnd = 0.5*((rsfitb[i]-rsfitm[i]*20.5-rsNSTD[i]*rsSTD[i])+(rsfitb[i]-rsfitm[i]*23.5-rsNSTD[i]*rsSTD[i])) &$
   readcol,'/home/rumbaugh/paperstuff/compcorrcats/BG.' + names[i] + '.cols.6.3.11.dat',BGr,BGi,BGrmi,BGrsoff,format='D,D,D,D',/silent &$
   readcol,'/home/rumbaugh/paperstuff/compcorrcats/CL.' + names[i] + '.cols.6.3.11.dat',CLr,CLi,CLrmi,CLrsoff,format='D,D,D,D',/silent &$
   plot,[0-1],[0-1],/nodata,XRANGE=[-0.5,2.0],YRANGE=[0,ymax[i]],TITLE='Color Distributions - ' + names[i],XTITLE="r'-i'",YTITLE='Num. of galaxies',xstyle=1,ystyle=1,XTHICK=4,YTHICK=4,CHARTHICK=2,CHARSIZE=1.2  &$
   Histoplot,CLrmi,mininput=-0.5,maxinput=2.0,binsize=0.05,/LINE_FILL,polycolor='Indian Red',spacing=0.2,orientation=-45,THICK=5,/oplot &$
   Histoplot,BGrmi,mininput=-0.5,maxinput=2.0,binsize=0.05,datacolorname='Royal Blue',THICK=8,histdata=histt,locations=locst,/oplot &$
   xt = [1,1]*avgRSbnd &$
   oplot,xt,yt,LINESTYLE=3,THICK=3 &$
   plot,[0-1],[0-1],/nodata,XRANGE=[-0.5,2.0],YRANGE=[0,ymax2[i]],TITLE='Color Distributions - ' + names[i],XTITLE="r'-i'",YTITLE='Scaled Num. of Galaxies',xstyle=1,ystyle=1,XTHICK=4,YTHICK=4,CHARTHICK=2,CHARSIZE=1.2  &$
   Histoplot,CLrmi,mininput=-0.5,maxinput=2.0,binsize=0.05,/LINE_FILL,polycolor='Indian Red',spacing=0.2,orientation=-45,THICK=5,/oplot &$
   oplot,locst-0.025,histt*CLareas[i]/BGareas[i],THICK=8,color=60,PSYM=10 &$
   xt = [1,1]*avgRSbnd &$
   oplot,xt,yt,LINESTYLE=3,THICK=3 &$
   plot,[0-1],[0-1],/nodata,XRANGE=[-2,0.5],YRANGE=[0,ymax[i]],TITLE='Color Distributions - ' + names[i],XTITLE="RS offset",YTITLE='Num. of galaxies',xstyle=1,ystyle=1,XTHICK=4,YTHICK=4,CHARTHICK=2,CHARSIZE=1.2  &$
   Histoplot,CLrsoff,mininput=-2,maxinput=0.5,binsize=0.05,THICK=5,/LINE_FILL,polycolor='Indian Red',spacing=0.2,orientation=-45,histdata=histt,locations=locst,/oplot &$
   Histoplot,BGrsoff,mininput=-2,maxinput=0.5,binsize=0.05,datacolorname='Royal Blue',THICK=8,histdata=histt,locations=locst,/oplot &$
   xt = [1,1]*(-1)*rsSTD[i]*rsNSTD[i] &$
   oplot,xt,yt,LINESTYLE=3,THICK=3 &$
   plot,[0-1],[0-1],/nodata,XRANGE=[-2,0.5],YRANGE=[0,ymax2[i]],TITLE='Color Distributions - ' + names[i],XTITLE="RS offset",YTITLE='Scaled Num. of galaxies',xstyle=1,ystyle=1,XTHICK=4,YTHICK=4,CHARTHICK=2,CHARSIZE=1.2  &$
   Histoplot,CLrsoff,mininput=-2,maxinput=0.5,binsize=0.05,THICK=5,/LINE_FILL,polycolor='Indian Red',spacing=0.2,orientation=-45,/oplot &$
   oplot,locst-0.025,histt*CLareas[i]/BGareas[i],THICK=8,color=60,PSYM=10 &$
   xt = [1,1]*(-1)*rsSTD[i]*rsNSTD[i] &$
   oplot,xt,yt,LINESTYLE=3,THICK=3 &$
   endfor

end
   
   
