import numpy as np
import math as m
import sys 
execfile("/home/rumbaugh/FindCloseSources.py")

C = 300000.0

rsb = np.array([1.777,1.325,1.84,1.203,1.305,3.182,1.0])
rsm = np.array([0.0229,0.0084,0.0319,0.0012,0.00485,0.063,0])
rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0813,0.0907,0.1])
rsNSTD = np.array([3.0,2.0,3.0,3.0,2.0,2.0,3.0])
files = np.array(['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])
cRAh = np.array([13,13,13,17,18,16,16,9,9])
cRAm = np.array([24,24,24,57,21,4,4,10,10])
cRAs = np.array([48.9,20.3,49.2,19.3,32.3,23.5,26.5,8.5,45.0])
cDd = np.array([30,30,30,66,68,43,43,54,54])
cDm = np.array([11,12,58,31,27,4,14,18,22])
cDs = np.array([26,52,35,29,57,39,22,56,7])
#centerRAs = np.array([((16+(4.0+23.5/60)/60)*360.0/24,(16+(4.0+26.5/60)/60)*360.0/24])
#centerDecs = np.array([43+(4.0+39.0/60)/60,43+(14.0+22.0/60)/60])
centerRAs = (cRAh + (cRAm + (cRAs/60.0))/60.0)*360.0/24
centerDecs = cDd + (cDm + (cDs/60.0))/60.0
centerzs = np.array([0.76,0.76,0.69,0.69,0.82,0.89861,0.86531,1.1,1.1])
#1 Mpc = 3.06*0.7 Arcmin
srchdist = np.array([3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92])*0.7

ccnt = 0
veldists = np.zeros(len(names))
veldists2 = np.zeros(len(names))
for i in range(0,len(names)-1):
   if ((i != 1) & (i != 2) & (i != 6) & (i != 8)): ccnt += 1
   if i == 7: 
       ccnt += 1
       i += 1
   sfile = '/home/rumbaugh/%s'%(files[ccnt])
   cr = read_file(sfile)
   ra,dec,z,zerr,q = get_colvals(cr,'col4'),get_colvals(cr,'col5'),get_colvals(cr,'col9'),get_colvals(cr,'col10'),get_colvals(cr,'col11')
   #if ((i != 5) & (i != 6)): readcol,files[ccnt],id,mask,slit,ra,dec,rB,iB,zB,z,zerr,q,format='A,A,A,D,D,D,D,D,D,D,I'
   #if ((i == 5) | (i == 6)): readcol,files[ccnt],id,mask,slit,ra,dec,rB,iB,zB,z,zerr,q,oldids,pflags,acsra,acsdec,acsid,f606,f814,format='A,A,A,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D'
   gerr = np.where(zerr < 0)
   gerr = gerr[0]
   z[gerr] = 0.0
   gq = np.where((q > 2.1) & (z > centerzs[i]-0.01) & (z < centerzs[i]+0.01))
   if i == 1: gq = np.where((q > 2.1) & (z > 0.65) & (z < 0.79))
   gq = gq[0]
   gclus = FindCloseSources(centerRAs[i],centerDecs[i],srchdist[i]*60,ra[gq],dec[gq],0)
   zavg = np.average(z[gq[gclus]])
   #avgvel = C*((1.0+zavg)**2-1)/((1.0+zavg)**2+1)
   avgvel = C*zavg
   #vels = C*((1.0+z[gq[gclus]])**2-1)/((1.0+z[gq[gclus]])**2+1) #rec. vels in km/s
   vels = C*(z[gq[gclus]]-zavg)/(1+zavg)
   #veldists[i] = m.sqrt(1)*m.sqrt(np.sum(vels*vels)/(len(gclus)-1)-C*C*np.average(zerr[gq[gclus]])**2/((1+zavg)**2))
   veldists[i] = m.sqrt(1)*m.sqrt(np.sum(vels*vels)/(len(gclus)-1))
   #relvels = (avgvel-vels)/(1-avgvel*vels/(C*C))
   #relvels2 = avgvel-vels
   #veldists[i],veldists2[i] = np.std(relvels),np.std(relvels2)
   print '%s - Avg z: %f  Vel Disp:  %f\n'%(names[i],zavg,m.sqrt(1)*veldists[i])
   nnarr = np.zeros((len(gclus),11))
   delta = np.zeros(len(gclus))
   for j in range(0,len(gclus)):
      diststemp = np.zeros(len(gclus))
      for k in range(0,len(gclus)): diststemp[k] = SphDist(ra[gq[gclus[j]]],dec[gq[gclus[j]]],ra[gq[gclus[k]]],dec[gq[gclus[k]]])
      disttempsort = np.argsort(diststemp)
      for k in range(0,11): nnarr[j,k] = disttempsort[k]
      tempinds = np.zeros(11,dtype=np.int8)
      for k in range(0,11): tempinds[k] = int(nnarr[j,k])
      zavgt = np.average(z[gq[gclus[tempinds]]])
      #avgvelt = C*((1.0+zavgt)**2-1)/((1.0+zavgt)**2+1)
      avgvelt = C*zavgt
      velstemp = C*(z[gq[gclus[tempinds]]]-zavgt)/(1+zavgt)
      #velst = C*((1.0+z[gq[gclus[tempinds]]])**2-1)/((1.0+z[gq[gclus[tempinds]]])**2+1) #rec. vels in km/s
      #relvelst = (avgvelt-velst)/(1-avgvelt*velst/(C*C))
      tempsum = np.sum(velstemp*velstemp)
      #veldist = m.sqrt(1)*m.sqrt(0.1*tempsum-C*C*np.average(zerr[gq[gclus[tempinds]]])**2/((1+zavgt)**2))
      veldist = m.sqrt(1)*m.sqrt(0.1*tempsum)
      #veldist = np.std(relvelst)
      #delta[j] = (m.sqrt(11.0)/veldists[i])*m.sqrt((np.average(velstemp))**2+(veldist-veldists[i])**2)
      delta[j] = (m.sqrt(11.0)/veldists[i])*m.sqrt(C**2*(zavg-zavgt)**2+(veldist-veldists[i])**2)
   Del = np.sum(delta)
   print 'Gals = %i    Del = %4.1f\n'%(len(gclus),Del)



      
