#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/test_out.9.12.13.MG0414.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.189252,true,0.445,-2.058,varpos
addcmp 0.167601,true,0.573,-1.662,varpos
addcmp 0.0719098,true,-0.136,-0.135,varpos
addcmp 0.0278541,true,-1.508,-1.761,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.MG0414.fixpos.9.14.13.mod
quit
EOF
