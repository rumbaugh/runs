set_dirs
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/paperstuff/RS.hists.full.5.7.11.ps',XSIZE=30,YSIZE=10.5,SCALE_FACTOR=1.0,/color
path = '/home/rumbaugh/paperstuff'
zlb2 = [0,0.655,0.82,0.68,0]
zub2 = [1.5,0.785,0.856,0.705,1.5]
zlb = [0,0.64,0.82,0.675,0]
zub = [1.5,0.8,0.856,0.715,1.5]
names = ['Cl1324','Cl1324','Cl0023','RXJ1757','RXJ1757']
names2 = ['Cl1324','Cl1324','Cl0023','RXJ1757','RXJ1757']
ymax = [50,20,200,8,15]
bsize = [0.0025,0.001,0.05,0.001,0.0025]
;bsize = [0.025,0.05,0.05,0.05,0.025]
thicks= [4,6,4,6,4]
for i=0,4 do begin &$
   rfile = path + '/input.fullRShist.' + names[i] + '.dat' &$
   readcol,rfile,ra,dec,z,format='D,D,D',/silent &$
   plot,[0-1],[0-1],/nodata,title=names2[i],xtitle='Redshift',ytitle='Num. of AGN',xrange=[zlb[i],zub[i]],yrange=[0,ymax[i]],xstyle=1,ystyle=1,XTHICK=3,YTHICK=3,CHARSIZE=1.3,CHARTHICK=4 &$
   Histoplot,z,BINSIZE=bsize[i],minvalue=0,maxvalue=1.5,datacolorname='Charcoal',THICK=thicks[i],/oplot &$
endfor
end

