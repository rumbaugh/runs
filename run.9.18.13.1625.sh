#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.08.01.B0712.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.0131894,true,-0.0048,0.0053,varpos
addcmp 0.0106833,true,0.0504,-0.1513,varpos
addcmp 0.00553042,true,0.8129,-0.6612,varpos
addcmp 0.00132117,true,1.1557,0.4609,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.B0712.fixpos.5.08.01.mod
quit
EOF




difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.14.01.B0712.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.0131894,true,-0.0048,0.0053,varpos
addcmp 0.0106833,true,0.0504,-0.1513,varpos
addcmp 0.00553042,true,0.8129,-0.6612,varpos
addcmp 0.00132117,true,1.1557,0.4609,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.B0712.fixpos.5.14.01.mod
quit
EOF



difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.17.01.B0712.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.0131894,true,-0.0048,0.0053,varpos
addcmp 0.0106833,true,0.0504,-0.1513,varpos
addcmp 0.00553042,true,0.8129,-0.6612,varpos
addcmp 0.00132117,true,1.1557,0.4609,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.B0712.fixpos.5.17.01.mod
quit
EOF
