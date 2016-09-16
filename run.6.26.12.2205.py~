set_plot,'PS'
loadct,13
usersymfs

device,file='/home/rumbaugh/veldisp_hists.5.31.12.ps',/color


names = ['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422']
names2 = names
bounds=[2750,2250,2250,2750,2250,2250,2250,2250,2750]
;names2 = ['RXJ1757','RXJ1821','Cl0910+5422']
;names = ['nep200','nep5281','cl0910']
;ymaxes = [11,11,8]
ymaxes = [14,5,8,8,13,14,13,6,10]

for i=0,n_elements(names)-1 do begin
!p.position = square()
readcol,'/home/rumbaugh/temp/idl_clusprops.' + names2[i] + '.5.31.12.dat',sig,blusig,redsig,BCGvel,bluvelcen,redvelcen
;print,bluvelcen,redvelcen
readcol,'/home/rumbaugh/temp/idl_vels.' + names2[i] + '.4.10.12.dat',vels,deltas,isblu,format='D,D,I'

endfor
end


