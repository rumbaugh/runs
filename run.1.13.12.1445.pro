
set_plot,'PS'
loadct,13

device,file="/home/rumbaugh/CMD.0910.1.13.12.ps",/color


readcol,'/home/rumbaugh/FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat',sID,mask,slit,RA,Dec,rB,iB,zB,z,zerr,flag,format='I,A,A,D,D,D,D,D,D,D,I'

g = where((flag gt 2.2) and (z lt 1.13) and (z gt 1.05))

plot,iB[g],rB[g]-iB[g],XTITLE="i'",YTITLE="r'-i'",PSYM=4,SYMSIZE=1,THICK=2,XRANGE=[19,26],YRANGE=[-1,2],xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=4,XTHICK=6,YTHICK=6

end
