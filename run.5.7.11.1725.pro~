set_dirs
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/paperstuff/RS.hists.full.4.4.11.ps',/color
path = '/home/rumbaugh/paperstuff'
zlb = [0.64,0.808,0.82,0.84,0.685]
zub = [0.8,0.828,0.856,0.96,0.715]
names = ['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757']
names2 = ['Cl1324','RXJ1821','Cl0023','Cl1604','RXJ1757']
ymax = [200,100,200,200,100]
bsize = [0.025,0.05,0.05,0.05,0.025]
for i=0,4 do begin &$
   rfile = path + '/input.fullRShist.' + names[i] + '.dat' &$
   readcol,rfile,ra,dec,z,format='D,D,D',/silent &$
   plot,[0-1],[0-1],/nodata,title=names2[i],xtitle='Redshift',ytitle='Num. of AGN',xrange=[0,1.5],yrange=[0,ymax[i]],xstyle=1,ystyle=1,XTHICK=3,YTHICK=3,CHARSIZE=1.3,CHARTHICK=4 &$
   Histoplot,z,BINSIZE=bsize[i],minvalue=0,maxvalue=1.5,datacolorname='Charcoal',THICK=6,/oplot &$
endfor
end

