readcol,'/home/rumbaugh/LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat',phot_id,mask,slit,ra,dec,rB,iB,zB,rs,rserr,q,oldid,pflags,acsra,acsdec,acsID,f606,f814,format='A,A,A,D,D,D,D,D,D,D,I,A,A,D,D,D,D,D'

srchdist = 3.09*0.7

cRAh = 16
cRAm = 4
cRAs = 26.5
cDd = 43
cDm = 14
cDs = 22

centerRA = (cRAh + (cRAm + (cRAs/60.0))/60.0)*360.0/24
centerDec = cDd + (cDm + (cDs/60.0))/60.0

g = FindCloseSources(centerRA,centerDec,srchdist*60,ra,dec,0)
dists = make_array(n_elements(g))
for ig = 0,n_elements(g)-1 do dists[ig] = SphDist(centerRA,centerDec,ra[g[ig]],dec[g[ig]])
sdist = sort(dists)

set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/testsrch.ps',/color
plot,[0,1],[0,1],/nodata,XRANGE=[241.135,241.085],YRANGE=[43.22625,43.25375],/xsty,/ysty
oplot,ra,dec,PSYM=2,SYMSIZE=0.3
oplot,ra[g[sdist[0:9]]],dec[g[sdist[0:9]]],PSYM=4,color=155
x1 = make_array(1)
x1[0] = centerRA
y1 = make_array(1)
y1[0] = centerDec
oplot,x1,y1,PSYM=7,color=255

end
