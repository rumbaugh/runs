readcol,'/home/rumbaugh/clusters.z+pos+mpc.4.18.11.dat',struc,name,z,ra,dec,mpc,mpccm,rah,ram,ras,decd,decm,decs,format='A,A,D,D,D,D,D,D,D,D,D,D,D',/silent
usethese = [1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1]

1604N = 'acis6933+7343.img.500-2000.nops.fits'
1604S = 'acis6932.img.500-2000.nops.fits'

path1 = '/home/rumbaugh/ChandraData/'
path2 = 'Cl0023/master/'
cfile = 'acis7914.img.500-2000.nops.fits'
cntsArr = DBLARR(80)
annuli = (dindgen(80)+1)*5
for i=0,n_elements(rah)-1 do begin &$
if i eq 5 then path2 = 'Cl1324/master/' &$
if i eq 9 then cfile = 'acis9404+9836.img.500-2000.nops.fits' &$
if i eq 10 then path2 = 'Cl1604/master/' &$
if i eq 10 then cfile = 1604S &$
if i eq 11 then cfile = 1604N &$
if i eq 12 then cfile = 1604S &$
if i eq 13 then cfile = 1604N &$


