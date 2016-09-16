
set_plot,'PS'
loadct,13

device,file="/home/rumbaugh/cmd.0910.1.13.12.ps",/color


readcol,'/home/rumbaugh/FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat',sID,mask,slit,RA,Dec,rB,iB,zB,z,zerr,flag,format='I,A,A,D,D,D,D,D,D,D,I'
