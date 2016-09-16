set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/paperstuff/fluxlimitplots.7.16.ps',/color

names = ['Cl0023','RXJ1757','Cl1604','NEP5281','Cl1324']
names2 = ['Cl0023','RXJ1757','Cl1604','RXJ1821','Cl1324']
c2fS = 10^(-12)*[6.3657,6.5997,0.5*(6.1157+6.1178),8.2274,0.5*(6.1569+6.1593)]
c2fH = 10^(-11)*[2.2252,2.218,0.5*(2.2196+2.2185),2.2276,0.5*(2.2206+2.2199)]
times = [49383.247922195,46451.792387024,0.5*(48391.890220549+50399.00069391),49548.501183658,0.5*(46103.507982594+49478.092354796)]
arr4piDl2 = [1.676,1.034,1.987,1.580,1.310]/(0.7*0.7)
;times 10^57
bsizes=[30,19,18,20,40,25,25,15,40,30]
bi = 0
x = [0.001,100]
y1 = [1,1]
for i=0,4 do begin &$
filename = '/scratch/rumbaugh/ciaotesting/' + names[i] + '/master/photometry/' + names[i] + '.xray_phot.soft_hard_full.dat' &$
readcol,filename,ra,dec,fluxS,fluxH,fluxF,ncntsS,ncntsH,ncntsF,sigS,sigH,sigF,wss,wsh,wsf,wmask,wflag,format='D,D,D,D,D,D,D,D,D,D,D,D,D,D,A,I' &$
if ((i eq 4)) then gN = where(ra gt 30.6) &$
if ((i eq 4)) then gS = where(ra lt 30.6) &$
lnlumsS = alog10(fluxS)+57+alog10(arr4piDl2[i]) &$
lnlumsH = alog10(fluxH)+57+alog10(arr4piDl2[i]) &$
lnlumsF = alog10(fluxF)+57+alog10(arr4piDl2[i]) &$
plot,[0-1],[0-1],/nodata,xrange=[40,45],yrange=[0,bsizes[bi]],XTITLE='Log Luminosity',YTITLE='Num. of Point Sources',TITLE=names2[i] + ' Point Sources - Soft Band',xstyle=1,ystyle=1 &$
bi++ &$
Histoplot,lnlumsS,binsize=0.125,mininput=40,maxinput=45,/OPLOT &$
plot,lnlumsS,sigS,PSYM=7,SYMSIZE=0.5,XTITLE='Log Luminosity',YTITLE='Detection Significance (Sigma)',TITLE=names2[i] + ' Point Sources - Soft Band',/ylog &$
oplot,x,y1,LINESTYLE=1 &$
oplot,x,2*y1,LINESTYLE=1 &$
oplot,x,3*y1,LINESTYLE=1 &$
lnsig = alog10(sigS) &$
gf = where((finite(lnlumsS) eq 1) and (finite(lnsig) eq 1)) &$
lnlumsS = lnlumsS[gf] &$
lnsig = lnsig[gf] &$
Del = n_elements(lnlumsS)*total(lnlumsS*lnlumsS)-(total(lnlumsS))^2 &$
A = (total(lnlumsS*lnlumsS)*total(lnsig)-(total(lnlumsS))*total(lnsig*lnlumsS))/Del &$
B = (n_elements(lnlumsS)*total(lnlumsS*lnsig)-(total(lnlumsS))*total(lnsig))/Del &$
print,Del,A,B &$
yt = 10^(A+B*x) &$
oplot,x,yt,THICK=2.5 &$
plot,[0-1],[0-1],/nodata,xrange=[40,45],yrange=[0,bsizes[bi]],XTITLE='Log Luminosity',YTITLE='Num. of Point Sources',TITLE=names2[i] + ' Point Sources - Hard Band',xstyle=1,ystyle=1 &$
Histoplot,lnlumsH,binsize=0.125,mininput=40,maxinput=45,/OPLOT &$
plot,lnlumsH,sigH,PSYM=7,SYMSIZE=0.5,XTITLE='Log Luminosity',YTITLE='Detection Significance (Sigma)',TITLE=names2[i] + ' Point Sources - Hard Band',/ylog &$
bi++ &$
oplot,x,y1,LINESTYLE=1 &$
oplot,x,2*y1,LINESTYLE=1 &$
oplot,x,3*y1,LINESTYLE=1 &$
lnsig = alog10(sigH) &$
gf = where((finite(lnlumsH) eq 1) and (finite(lnsig) eq 1)) &$
lnlumsH = lnlumsH[gf] &$
lnsig = lnsig[gf] &$
Del = n_elements(lnlumsH)*total(lnlumsH*lnlumsH)-(total(lnlumsH))^2 &$
A = (total(lnlumsH*lnlumsH)*total(lnsig)-(total(lnlumsH))*total(lnsig*lnlumsH))/Del &$
B = (n_elements(lnlumsH)*total(lnlumsH*lnsig)-(total(lnlumsH))*total(lnsig))/Del &$
yt = 10^(A+B*x) &$
oplot,x,yt,THICK=2.5 &$
print,Del,A,B &$
endfor

end


