set_dirs
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/paperstuff/RS.hists.full.4.4.11.ps',/color
path = '/home/rumbaugh/paperstuff'
;zlb = [0.66,0.808,0.82,0.84,0.68]
;zub = [0.785,0.828,0.856,0.96,0.705]
zlb = [0,0.66,0.82,0.68,0]
zub = [1.5,0.785,0.856,0.705,1.5]
names = ['Cl1324','Cl1324','Cl0023','RXJ1757','RXJ1757']
names2 = ['Cl1324','Cl1324','Cl0023','RXJ1757','RXJ1757']
ymax = [148,20,200,8,45]
bsize = [0.01,0.001,0.05,0.001,0.01]for i=0,4 do begin &$
   rfile = path + '/input.fullRShist.' + names[i] + '.dat' &$
   readcol,rfile,ra,dec,z,format='D,D,D',/silent &$
   plot,[0-1],[0-1],/nodata,title=names2[i],xtitle='Redshift',ytitle='Num. of AGN',xrange=[zlb[i],zub[i]],yrange=[0,ymax[i]],xstyle=1,ystyle=1,XTHICK=3,YTHICK=2,CHARSIZE=1.0,CHARTHICK=2 &$
   Histoplot,z,BINSIZE=bsize[i],minvalue=zlb[i],maxvalue=zub[i],/oplot &$
endfor
end

