set_dirs
set_plot,'PS'
device,file="/home/rumbaugh/LFC/LxoverSM.ps",/color
loadct,13


readcol,"/home/rumbaugh/Download/Xray.AGN.hoststellarmasses.sc1604.cat",ID,mask,slit,z,massK,massKerr,massSED,massSEDerr,format="A,A,I,D,D,D,D"

readcol,"/home/rumbaugh/LFC/XrayLums.Cl1604.soft.dat",Xlums,flux,cnts,z2,ra,dec
Xlumslog = alog10(Xlums) + 42

Lsun = 3.839e33

refBLumlog = findgen(2000)
refBLumlog = refBLumlog*(45.7-43.7)/1000.0 + 43.7
refBLum = 10^(refBLumlog)

;refXLum = refBLum/(17.87*(refBLum/(10^10*Lsun))^(0.28)+10.03*(refBLum/(10^10*Lsun))^(-0.02))
refXLumlog = refBLumlog-alog10((17.87*(10^(refBLumlog-alog10(3.839)-43))^(0.28)+10.03*(10^(refBLumlog-alog10(3.839)-43))^(-0.02)))
;refXLumlog = alog10(refXLum)

BLum = findgen(n_elements(z))
Edd = findgen(n_elements(z))
for i=0,n_elements(z)-1 do begin &$
   gz = where((z2-z[i] ge -0.00001) and (z2-z[i] le 0.00001)) &$
   Xlumtemp = Xlumslog[gz[0]] &$
   gtemp = where(refXLumlog > Xlumtemp) &$
   LBoltemplog = (Xlumtemp-refXlumlog[gtemp[0]-1])*(refBlumlog[gtemp[0]]-refBlumlog[gtemp[0]-1])/(refXlumlog[gtemp[0]]-refXlumlog[gtemp[0]-1]) + refBlumlog[gtemp[0]-1] &$
   Edd[i] = LBoltemplog-alog10(massK[i]) &$
   endfor
;print,mask
;print,Xlumslog
;print,"\n"
;print,Edd

Histoplot,Edd,MAXINPUT=36,MININPUT=31,BINSIZE=0.5,/LINE_FILL,POLYCOLOR='Indian Red',SPACING=0.02



readcol,"/home/rumbaugh/Download/Xray.AGN.hoststellarmasses.sc1324.cat",ID,mask,slit,z,massK,massKerr,format="A,A,I,D,D"

readcol,"/home/rumbaugh/LFC/XrayLums.Cl1324.soft.dat",Xlums,flux,cnts,z2,ra,dec
;Xlums = Xlums*10^42
Xlumslog = alog10(Xlums) + 42

Lsun = 3.839e33

refBLumlog = findgen(2000)
refBLumlog = refBLumlog*(45.7-43.7)/1000.0 + 43.7
refBLum = 10^(refBLumlog)

;refXLum = refBLum/(17.87*(refBLum/(10^10*Lsun))^(0.28)+10.03*(refBLum/(10^10*Lsun))^(-0.02))
;refXLumlog = alog10(refXLum)

refXLumlog = refBLumlog-alog10((17.87*(10^(refBLumlog-alog10(3.839)-43))^(0.28)+10.03*(10^(refBLumlog-alog10(3.839)-43))^(-0.02)))


BLum = findgen(n_elements(z))
Edd = findgen(n_elements(z))
for i=0,n_elements(z)-1 do begin &$
   gz = where((z2-z[i] ge -0.00001) and (z2-z[i] le 0.00001)) &$
   Xlumtemp = Xlumslog[gz[0]] &$
   gtemp = where(refXLumlog > Xlumtemp) &$
   LBoltemplog = (Xlumtemp-refXlumlog[gtemp[0]-1])*(refBlumlog[gtemp[0]]-refBlumlog[gtemp[0]-1])/(refXlumlog[gtemp[0]]-refXlumlog[gtemp[0]-1]) + refBlumlog[gtemp[0]-1] &$
   Edd[i] = LBoltemplog-alog10(massK[i])  &$
endfor

readcol,"/home/rumbaugh/LFC/XrayLums.Cl1324.hard.dat",Xlums,flux,cnts,z2,ra,dec
;Xlums = Xlums*10^42
Xlumslog = alog10(Xlums) + 42
Xtemp = Xlumslog[3] 

tryBL = 44 + alog10(2)
tempXL = 0.0
while tempXL lt Xtemp do begin &$
   lastXL = tempXL &$
   tryBL += 0.00025 &$
   tempXL = tryBL - alog10(10.83*(10^0.28)^(tryBL-43-alog10(3.839))+6.08*(10^(-0.02))^(tryBL-43-alog10(3.839))) &$
endwhile
BL = (Xtemp - lastXL)*0.00025/(tempXL-lastXL) + tryBL-0.00025
Edd = [Edd,BL-alog10(massK[1])]

g = where(Edd*0 eq 0)
Histoplot,Edd[g],MAXINPUT=36,MININPUT=31,BINSIZE=0.5,/LINE_FILL,POLYCOLOR='Charcoal',ORIENTATION=-45,/OPLOT




end


