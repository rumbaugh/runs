set_dirs
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/FP.spat.plot.2.2.11.ps',/color

readcol,"/home/rumbaugh/COSMOS/full.spat.anal.2.2.11.dat",ann,SB,format="I,D"
readcol,"/home/rumbaugh/ChandraData/4199/psSB.2.23.11.dat",annps,SBps,format="I,D"

r = ann

cnt = SB*3.141592637
cnt[0] *= r[0]*r[0]
for i=1,n_elements(SB)-1 do cnt[i] *= (r[i]*r[i]-r[i-1]*r[i-1])


SB2 = sqrt(cnt)/3.141592637
SB2[0] /= r[0]*r[0]
for i=1,n_elements(SB)-1 do SB2[i] /= (r[i]*r[i]-r[i-1]*r[i-1])

ploterror,r,SB,SB2,PSYM=6,SYMSIZE=1,THICK=2,CHARTHICK=1.8,XTITLE="Radius(arcseconds)",YTITLE="Surface Brightness(counts arcseconds!E-2)",ystyle=1,xstyle=1,yrange=[0,0.32],xrange=[0,61]
g = where((r ge 50) and (r le 60))
bg = total(SB[g])/n_elements(g)
bgx = [0,10,50,62]
bgy = [1,1,1,1]*bg
oplot,bgx,bgy,linestyle=2,THICK=2


r = annps

cnt = SBps*3.141592637
cnt[0] *= r[0]*r[0]
for i=1,n_elements(SB)-1 do cnt[i] *= (r[i]*r[i]-r[i-1]*r[i-1])


SB2 = sqrt(cnt)/3.141592637
SB2[0] /= r[0]*r[0]
for i=1,n_elements(SB)-1 do SB2[i] /= (r[i]*r[i]-r[i-1]*r[i-1])
oploterror,r,SBps,SB2,PSYM=4,SYMSIZE=1,THICK=2


end
