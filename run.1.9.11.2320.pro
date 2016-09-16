set_dirs

set_plot,'PS'
device,file='/home/rumbaugh/LFC/diffuseemission.plot.ps'

readcol,"/home/rumbaugh/LFC/diffuseemission.dat",netcnts1,counts1,netcnts2,counts2,netcnts3,counts3,netcnts4,counts4


annuli = findgen(120)
annuli = 2 + annuli*3
print, annuli

x = [0,1,100,119,240]
y = findgen(5)
SB1 = dblarr(120)
SB1[0] = counts1[0]/(1.0*annuli[0]*annuli[0])
for i=1,119 do begin &$
   SB1[i] = (counts1[i]-counts1[i-1])/(1.0*annuli[i]*annuli[i]-annuli[i-1]*annuli[i-1]) &$
endfor
lavg = (SB1[119]+SB1[118]+SB1[117])/3.0
for q=0,4 do y[q] = lavg


plot,annuli, SB1,PSYM=4
oplot,x,y,LINESTYLE=2
SB2 = dblarr(120)
SB2[0] = counts2[0]/(1.0*annuli[0]*annuli[0])
for i=1,119 do begin &$
   SB2[i] = (counts2[i]-counts2[i-1])/(1.0*annuli[i]*annuli[i]-annuli[i-1]*annuli[i-1]) &$
endfor
lavg = (SB2[119]+SB2[118]+SB2[117])/3.0
for q=0,4 do y[q] = lavg

plot,annuli, SB2,PSYM=4
oplot,x,y,LINESTYLE=2

SB3 = dblarr(120)
SB3[0] = counts3[0]/(1.0*annuli[0]*annuli[0])
for i=1,119 do begin &$
   SB3[i] = (counts3[i]-counts3[i-1])/(1.0*annuli[i]*annuli[i]-annuli[i-1]*annuli[i-1]) &$
endfor
lavg = (SB3[119]+SB3[118]+SB3[117])/3.0
for q=0,4 do y[q] = lavg

plot,annuli, SB3,PSYM=4
oplot,x,y,LINESTYLE=2

SB4 = dblarr(120)
SB4[0] = counts4[0]/(1.0*annuli[0]*annuli[0])
for i=1,119 do begin &$
   SB4[i] = (counts4[i]-counts4[i-1])/(1.0*annuli[i]*annuli[i]-annuli[i-1]*annuli[i-1]) &$
endfor
lavg = (SB4[119]+SB4[118]+SB4[117])/3.0
for q=0,4 do y[q] = lavg

plot,annuli, SB4,PSYM=4
oplot,x,y,LINESTYLE=2

end
