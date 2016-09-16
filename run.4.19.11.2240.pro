readcol,'/home/rumbaugh/LFC/diffuse.stacked.4.19.11.dat',ann,dfsdf,cnts,/silent
bg = (cnts[67]-cnts[62])/(ann[67]*ann[67]-ann[62]*ann[62])

cnts2 = DBLARR(40)
ann2 = DBLARR(40)
for i=0,39 do cnts2[i] = cnts[2*i]+cnts[2*i+1]
for i=0,39 do ann2[i] = ann[2*i+1]

tcnts = DBLARR(80)
for i=0,79 do tcnts[i] = cnts[i]-bg*ann[i]*ann[i]
SB = DBLARR(80)
SB[0] = cnts[0]/(ann[0]*ann[0])
for i=1,79 do SB[i] = (cnts[i]-cnts[i-1])/(ann[i]*ann[i]-ann[i-1]*ann[i-1])
SB2 = DBLARR(40)
SB2[0] = cnts2[0]/(ann2[0]*ann2[0])
for i=1,39 do SB2[i] = (cnts2[i]-cnts2[i-1])/(ann2[i]*ann2[i]-ann2[i-1]*ann2[i-1])
SB2err = DBLARR(40)
SB2err[0] = cnts2[0]^0.5/(ann2[0]*ann2[0])
for i=1,39 do SB2err[i] = (cnts2[i]+cnts2[i-1])^0.5/(ann2[i]*ann2[i]-ann2[i-1]*ann2[i-1])
set_plot,'PS'
device,file='/home/rumbaugh/LFC/diffuse.stacked.plot.4.19.11.ps'
plot,ann,tcnts,Ytitle='Stacked Net Counts',XTITLE='Pixels',PSYM=4
plot,ann,SB,Ytitle='Stacked Surface Brightness',XTITLE='Pixels',PSYM=4
ploterror,ann2,SB2,SB2err,Ytitle='Stacked Surface Brightness',XTITLE='Pixels',PSYM=4

end
