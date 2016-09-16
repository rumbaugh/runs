names = ['cl0023','cl1604','cl1324','nep200','nep5281']
path = '/home/rumbaugh/LFC/'
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/paperstuff/magerrors.plot.7.9.11.ps',/color

for i=0,4 do begin &$
filename = path + names[i] + '.photcat' &$
readcol,filename,idn,x,y,ra,dec,rmag,rerr,imag,ierr,zmag,zerr,format='A,D,D,D,D,D,D,D,D,D,D' &$
plot,rmag,rerr,PSYM=3,TITLE=names[i] + ' - R Band',XTITLE='R Magnitude',YTITLE='R Error',yrange=[0.19,0.21],xrange=[20,30] &$
plot,imag,ierr,PSYM=3,TITLE=names[i] + ' - I Band',XTITLE='I Magnitude',YTITLE='I Error',yrange=[0.19,0.21],xrange=[20,30] &$
plot,zmag,zerr,PSYM=3,TITLE=names[i] + ' - Z Band',XTITLE='Z Magnitude',YTITLE='Z Error',yrange=[0.19,0.21],xrange=[20,30] &$
g = where((rmag gt 20) and (rmag lt 30) and (rerr gt 0.19) and (rerr lt 0.21)) &$
print,names[i] &$
print,'R Mag Avg = ' + string(mean(rmag[g])) &$
g = where((imag gt 20) and (imag lt 30) and (ierr gt 0.19) and (ierr lt 0.21)) &$
print,'I Mag Avg = ' + string(mean(imag[g])) &$
g = where((zmag gt 20) and (zmag lt 30) and (zerr gt 0.19) and (zerr lt 0.21)) &$
print,'Z Mag Avg = ' + string(mean(zmag[g])) &$
endfor 
end
