set_dirs
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/IDLcolorcode.plot.ps',/color
x = indgen(256)
plot,[0-1],[0-1],/nodata,xrange=[0,256],yrange=[0,256],xstyle=1,ystyle=1,TITLE="IDL color code - loadct,13"
for i=0,255 do begin &$
   temp = indgen(1) &$
   temp[0] = x[i] &$
   oplot,temp,temp,psym=6,symsize=0.5,thick=4,color=x[i] &$
endfor
end
