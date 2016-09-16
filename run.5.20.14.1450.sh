#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_1.6.12.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB1_1.fixpos.6.12.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_11.8.21.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB1_11.fixpos.8.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_13.8.29.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB1_13.fixpos.8.29.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_14.8.31.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB1_14.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_15.9.2.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB1_15.fixpos.9.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_2.6.20.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_2.fixpos.6.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_3.7.5.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_3.fixpos.7.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_4.7.7.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_4.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_6.7.21.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_6.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_7.8.4.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_7.fixpos.8.4.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_8.8.7.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_8.fixpos.8.7.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_12.8.24.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_12.fixpos.8.24.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_13.9.1.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_13.fixpos.9.1.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_15.9.5.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_15.fixpos.9.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_16.9.11.11.11A-138.MG0414+0534.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.MG0414+0534.EarlySB2_16.fixpos.9.11.11.mod
quit
EOF
