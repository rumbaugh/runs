
rsb = [1.777,1.325,1.84,1.203,1.305,3.182,1.0]
rsm = [0.0229,0.0084,0.0319,0.0012,0.00485,0.063,0]
rsSTD = [0.0625,0.0735,0.0576,0.0413,0.0813,0.0907,0.1]
rsNSTD = [3.0,2.0,3.0,3.0,2.0,2.0,3.0]
files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
names = ['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422']
cRAh = [13,13,13,17,18,16,16,9,9]
cRAm = [24,24,24,57,21,4,4,10,10]
cRAs = [48.9,20.3,49.2,19.3,32.3,23.5,26.5,8.5,45.0]
cDd = [30,30,30,66,68,43,43,54,54]
cDm = [11,12,58,31,27,4,14,18,22]
cDs = [26,52,35,29,57,39,22,56,7]
;centerRAs = [((16+(4.0+23.5/60)/60)*360.0/24,(16+(4.0+26.5/60)/60)*360.0/24]
;centerDecs = [43+(4.0+39.0/60)/60,43+(14.0+22.0/60)/60]
centerRAs = (cRAh + (cRAm + (cRAs/60.0))/60.0)*360.0/24
centerDecs = cDd + (cDm + (cDs/60.0))/60.0
centerzs = [0.76,0.76,0.69,0.69,0.84,0.89861,0.86531,1.1,1.1]
;1 Mpc = 3.06*0.7 Arcmin
srchdist = [3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92]*0.7

ccnt = 0
veldists = make_array(n_elements(names))
for i=0,n_elements(names)-1 do begin
   if ((i ne 1) and (i ne 2) and (i ne 6) and (i ne 8)) then ccnt += 1
   if ((i ne 5) and (i ne 6)) then readcol,files[ccnt],id,mask,slit,ra,dec,rB,iB,zB,z,zerr,q,format='A,A,A,D,D,D,D,D,D,D,I'
   if ((i eq 5) or (i eq 6)) then readcol,files[ccnt],id,mask,slit,ra,dec,rB,iB,zB,z,zerr,q,oldids,pflags,acsra,acsdec,acsid,f606,f814,format='A,A,A,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D'
   gq = where((q gt 2.1) and (z gt centerzs[i]-0.01) and (z lt centerzs[i]+0.01))
   if i eq 1 then gq = where((q gt 2.1) and (z gt 0.65) and (z lt 0.79))
   gclus = FindCloseSources(centerRAs[i],centerDecs[i],srchdist[i]*60,ra[gq],dec[gq],0)
   zavg = avg(z[gq[gclus]])
   ;vels = 30000.0*((1.0+z[gq])^2-1)/((1.0+z[gq])^2+1) ;rec. vels in km/s
   vels = 300000.0*(z[gq[gclus]]-zavg)/(1+zavg)
   veldists[i] = total(vels*vels)/(n_elements(gclus)-1)-300000*300000*avg(zerr[gq[gclus]])^2/((1+zavg)^2)
   print,names[i] + ' - Avg z: ' + string(zavg) + '  Vel Disp: ' + string(sqrt(veldists[i]))
   nnarr = make_array(n_elements(gclus),11)
   delta = make_array(n_elements(gclus))
   for j=0,n_elements(gclus)-1 do begin
      diststemp = make_array(n_elements(gclus))
      for k=0,n_elements(gclus)-1 do diststemp[k] = SphDist(ra[gq[gclus[j]]],dec[gq[gclus[j]]],ra[gq[gclus[k]]],dec[gq[gclus[k]]])
      disttempsort = sort(diststemp)
      nnarr[j,0:10] = disttempsort[0:10]
      zavgt = avg(z[gq[gclus[nnarr[j,0:10]]]])
      velstemp = 300000.0*(z[gq[gclus[nnarr[j,0:10]]]]-zavgt)/(1+zavgt)
      tempsum = total(velstemp*velstemp)
      veldist = 0.1*tempsum-300000*300000*avg(zerr[gq[gclus[nnarr[j,0:10]]]])^2/((1+zavgt)^2)
      delta[j] = (sqrt(11.0)/veldists[i])*sqrt((avg(velstemp)-avg(vels))^2+(veldist-veldists[i])^2)
   endfor 
   Del = total(delta)
   print,'Del = ' + string(Del)
endfor
end


      
