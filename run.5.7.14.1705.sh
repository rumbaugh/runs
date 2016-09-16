#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_9.8.11.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_9.fixpos.8.11.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_9.8.11.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_9.fixpos.8.11.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_9.8.11.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_9.fixpos.8.11.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_9.8.11.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_9.fixpos.8.11.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_10.8.18.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_10.fixpos.8.18.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_10.8.18.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_10.fixpos.8.18.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_10.8.18.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_10.fixpos.8.18.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_10.8.18.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_10.fixpos.8.18.11.mod
quit
EOF
