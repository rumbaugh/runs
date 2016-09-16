#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 5
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.19.01_BU.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.af377_1400+621.4.19.01_BU.mod
quit
EOF


difmap << EOF
integer mfitniter
mfitniter = 5
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.19.01_BX.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.af377_1400+621.4.19.01_BX.mod
quit
EOF
