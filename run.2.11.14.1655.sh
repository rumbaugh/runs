obs LateSB1_10.7.21.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 1024,0.05
rmod ../../difmap_results/fit.B1938+666.LateSB1_10.concatshift.fixpos.8.29.12.mod
modelfit 5
selfcal false,false,60
modelfit 5
selfcal false,false,60
modelfit 10
gscale
modelfit 5
selfcal false,false,20
modelfit 5
cmul = imstat(rms)
print cmul
mapsize 256,0.05
shift -1.0,-0.4
levs = 2,4,8,16,32,64,128
mapl cln
