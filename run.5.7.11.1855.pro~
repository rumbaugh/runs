set_dirs
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/paperstuff/RS.hists.Cl1324.4.30.11.ps',/color
path = '/home/rumbaugh/paperstuff'
zlb = [0.66,0.808,0.82,0.84,0.68]
zub = [0.785,0.828,0.856,0.96,0.705]
names = ['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757']
names2 = ['Cl1324','RXJ1821','Cl0023','Cl1604','RXJ1757']
ymax = [20,11,20,20,7]
bsize = [0.001,0.001,0.001,0.001,0.001]
for i=0,0 do begin &$
   rfile = path + '/input.RShist.' + names[i] + '.4.30.11.dat' &$
   readcol,rfile,ra,dec,z,format='D,D,D',/silent &$
   plot,[0-1],[0-1],/nodata,title=names2[i],xtitle='Redshift',ytitle='Num. of Galaxies',xrange=[0.655,zub[i]],yrange=[0,ymax[i]],xstyle=1,ystyle=1,XTHICK=3,YTHICK=2,CHARSIZE=1.0,CHARTHICK=2 &$
   Histoplot,z,maxvalue=zub[i],minvalue=0.655,BINSIZE=bsize[i],/oplot &$
endfor
device,file='/home/rumbaugh/paperstuff/RS.hists.Cl1604.4.30.11.ps',XSIZE=22,YSIZE=10.5,SCALE_FACTOR=1.0,/color
for i=3,3 do begin &$
   rfile = path + '/input.RShist.' + names[i] + '.dat' &$
   readcol,rfile,ra,dec,z,format='D,D,D',/silent &$
   plot,[0-1],[0-1],/nodata,title=names2[i],xtitle='Redshift',ytitle='Num. of Galaxies',xrange=[zlb[i],zub[i]],yrange=[0,ymax[i]],xstyle=1,ystyle=1,XTHICK=3,YTHICK=2,CHARSIZE=1.0,CHARTHICK=2 &$
   Histoplot,z,maxvalue=zub[i],minvalue=zlb[i],BINSIZE=bsize[i],/oplot &$
endfor
end

