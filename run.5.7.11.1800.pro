set_dirs
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/paperstuff/RS.hists.5.7.11.ps',/color
path = '/home/rumbaugh/paperstuff'
zlb = [0.65,0.80,0.82,0.84,0.68]
zub = [0.79,0.84,0.87,0.96,0.71]
names = ['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757']
names2 = ['Cl1324','RXJ1821','Cl0023','Cl1604','RXJ1757']
ymax = [20,14,20,20,7]
thicks=[4,6,5,4,6]
bsize = [0.001,0.001,0.001,0.001,0.001]
for i=0,4 do begin &$
   rfile = path + '/input.fullRShist.' + names[i] + '.dat' &$
   readcol,rfile,ra,dec,z,format='D,D,D',/silent &$
   plot,[0-1],[0-1],/nodata,title=names2[i],xtitle='Redshift',ytitle='Num. of Galaxies',xrange=[zlb[i],zub[i]],yrange=[0,ymax[i]],xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=3,XTHICK=8,YTHICK=8 &$
   Histoplot,z,maxvalue=zub[i],minvalue=zlb[i],BINSIZE=bsize[i],thick=thicks[i],datacolorname='Gray',/oplot &$
endfor
end

