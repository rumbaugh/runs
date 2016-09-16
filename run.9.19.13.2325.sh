#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 5
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.08.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.af377_1244+408.5.08.01.mod
quit
EOF


difmap << EOF
integer mfitniter
mfitniter = 5
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.12.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.af377_1244+408.5.12.01.mod
quit
EOF


difmap << EOF
integer mfitniter
mfitniter = 5
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.14.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.af377_1244+408.5.14.01.mod
quit
EOF


difmap << EOF
integer mfitniter
mfitniter = 5
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.17.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.af377_1244+408.5.17.01.mod
quit
EOF

difmap << EOF
integer mfitniter
mfitniter = 5
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.08.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.af377_1400+621.5.08.01.mod
quit
EOF


difmap << EOF
integer mfitniter
mfitniter = 5
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.12.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.af377_1400+621.5.12.01.mod
quit
EOF


difmap << EOF
integer mfitniter
mfitniter = 5
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.14.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.af377_1400+621.5.14.01.mod
quit
EOF


difmap << EOF
integer mfitniter
mfitniter = 5
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.17.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.af377_1400+621.5.17.01.mod
quit
EOF

