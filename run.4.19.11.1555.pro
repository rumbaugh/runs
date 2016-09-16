set_dirs

set_plot,'PS'
device,file='/home/rumbaugh/paperstuff/diffuseemission.plot.4.19.11.ps'

readcol,"/home/rumbaugh/LFC/diffuseemission.4.19.11.dat",netcnts1,counts1,netcnts2,counts2,netcnts3,counts3,netcnts4,counts4,netcnts5,counts5
names = ['NEP5281','RXJ1757','Cl1324 - 9403+9840','Cl1324 - 9404+9836','Cl1324+3013']
bins = 60
annmult = [1.0,1.0,2.0,1.5,1.5]
annulitemp = findgen(bins)
annulitemp = 10 + annulitemp*10
;print, annuli
icnt = 0


annuli = annmult[icnt]*annulitemp
icnt += 1
x = [0,1,100,119,240]
y = (findgen(5)+1)/(findgen(5)+1)
SB1 = dblarr(bins)
SB1[0] = counts1[0]/(1.0*annuli[0]*annuli[0])
for i=1,bins-1 do begin &$
   SB1[i] = (counts1[i]-counts1[i-1])/(1.0*annuli[i]*annuli[i]-annuli[i-1]*annuli[i-1]) &$
endfor
;lavg = (SB1[119]+SB1[118]+SB1[117])/3.0
;for q=0,4 do y[q] = ;lavg


plot,annuli, SB1,xtitle='Pixels',title=names[icnt-1],PSYM=4,xrange=[0,300]
g = where((annuli ge 275) and (annuli le 345))
bg = total(SB1[g])/(1.0*n_elements(g))
y = (findgen(5)+1)/(findgen(5)+1)
y *= bg
oplot,x,y,LINESTYLE=2
annuli = annmult[icnt]*annulitemp
icnt += 1
SB2 = dblarr(bins)
SB2[0] = counts2[0]/(1.0*annuli[0]*annuli[0])
for i=1,bins-1 do begin &$
   SB2[i] = (counts2[i]-counts2[i-1])/(1.0*annuli[i]*annuli[i]-annuli[i-1]*annuli[i-1]) &$
endfor
;lavg = (SB2[119]+SB2[118]+SB2[117])/3.0
;for q=0,4 do y[q] = ;lavg

plot,annuli, SB2,xtitle='Pixels',title=names[icnt-1],PSYM=4,xrange=[0,300]
g = where((annuli ge 275) and (annuli le 345))
bg = total(SB2[g])/(1.0*n_elements(g))
y = (findgen(5)+1)/(findgen(5)+1)
y *= bg
oplot,x,y,LINESTYLE=2

annuli = annmult[icnt]*annulitemp
icnt += 1
SB3 = dblarr(bins)
SB3[0] = counts3[0]/(1.0*annuli[0]*annuli[0])
for i=1,bins-1 do begin &$
   SB3[i] = (counts3[i]-counts3[i-1])/(1.0*annuli[i]*annuli[i]-annuli[i-1]*annuli[i-1]) &$
endfor
;lavg = (SB3[119]+SB3[118]+SB3[117])/3.0
;for q=0,4 do y[q] = ;lavg

plot,annuli, SB3,xtitle='Pixels',title=names[icnt-1],PSYM=4,xrange=[0,300]
g = where((annuli ge 275) and (annuli le 345))
bg = total(SB3[g])/(1.0*n_elements(g))
y = (findgen(5)+1)/(findgen(5)+1)
y *= bg
oplot,x,y,LINESTYLE=2

annuli = annmult[icnt]*annulitemp
icnt += 1
SB4 = dblarr(bins)
SB4[0] = counts4[0]/(1.0*annuli[0]*annuli[0])
for i=1,bins-1 do begin &$
   SB4[i] = (counts4[i]-counts4[i-1])/(1.0*annuli[i]*annuli[i]-annuli[i-1]*annuli[i-1]) &$
endfor
;lavg = (SB4[119]+SB4[118]+SB4[117])/3.0
;for q=0,4 do y[q] = ;lavg

plot,annuli, SB4,xtitle='Pixels',title=names[icnt-1],PSYM=4,xrange=[0,300]
g = where((annuli ge 275) and (annuli le 345))
bg = total(SB4[g])/(1.0*n_elements(g))
y = (findgen(5)+1)/(findgen(5)+1)
y *= bg
oplot,x,y,LINESTYLE=2

annuli = annmult[icnt]*annulitemp
icnt += 1
SB5 = dblarr(bins)
SB5[0] = counts5[0]/(1.0*annuli[0]*annuli[0])
for i=1,bins-1 do begin &$
   SB5[i] = (counts5[i]-counts5[i-1])/(1.0*annuli[i]*annuli[i]-annuli[i-1]*annuli[i-1]) &$
endfor
;lavg = (SB5[119]+SB5[118]+SB5[117])/3.0
;for q=0,5 do y[q] = ;lavg

plot,annuli, SB5,xtitle='Pixels',title=names[icnt-1],PSYM=4,xrange=[0,300]
g = where((annuli ge 275) and (annuli le 345))
bg = total(SB5[g])/(1.0*n_elements(g))
y = (findgen(5)+1)/(findgen(5)+1)
y *= bg
oplot,x,y,LINESTYLE=2

end
