readcol,'/home/rumbaugh/kinematic_pairs.8.16.11.dat',dist,z,q,kID,format='D,D,I,A'


sfiles = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat']
openw,1,'/home/rumbaugh/kinematic_pairs.ra_dec.8.17.11.dat'
for i=0,4 do begin &$
   sfile = '/home/rumbaugh/' + sfiles[i] &$
   readcol,sfile,lid,lmask,sli,sRA,sDec,rb,ib,zb,rs,rse,sq,format='A,A,A,D,D,D,D,D,D,D,I',/silent &$
   for j=0,n_elements(kID)-1 do begin &$
   if ((i eq 1)) then gid = where(lid eq kID[j]) &$
   if ((i eq 0) and (j lt 25)) then gid = where(lid eq kID[j]) &$
   if ((i eq 2) and (j lt n_elements(kID)-10)) then gid = where(lid eq kID[j]) &$
   if ((i eq 3) and (j gt 30)) then gid = where(lid eq kID[j]) &$
   if ((i eq 4) and (j gt n_elements(kID)-12)) then gid = where(lid eq kID[j]) &$
   if gid[0] gt -0.1 then printf,1,dist[j],z[j],q[j],sRA[gid[0]],sDec[gid[0]],kID[j],format='(1(D5.1,"   ",D7.5,"  ",I1,"      ",D10.6,"  ",D9.6,"  ",A," "))' &$
   endfor &$
   endfor
close,1
end
