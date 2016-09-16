#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_1.6.12.11.11A-138.J0427+4133.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0427+4133.EarlySB1_1.fixpos.6.12.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_1.6.12.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB1_1.fixpos.6.12.11.mod
quit
EOF
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_1.6.12.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB1_1.fixpos.6.12.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_11.8.21.11.11A-138.J0427+4133.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0427+4133.EarlySB1_11.fixpos.8.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_11.8.21.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB1_11.fixpos.8.21.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_11.8.21.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB1_11.fixpos.8.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_13.8.29.11.11A-138.J0427+4133.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0427+4133.EarlySB1_13.fixpos.8.29.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_13.8.29.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB1_13.fixpos.8.29.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_13.8.29.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB1_13.fixpos.8.29.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_14.8.31.11.11A-138.J0427+4133.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0427+4133.EarlySB1_14.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_14.8.31.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB1_14.fixpos.8.31.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_14.8.31.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB1_14.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_15.9.2.11.11A-138.J0427+4133.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0427+4133.EarlySB1_15.fixpos.9.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_15.9.2.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB1_15.fixpos.9.2.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB1/data/EarlySB1_15.9.2.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB1_15.fixpos.9.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_2.6.20.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_2.fixpos.6.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_2.6.20.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_2.fixpos.6.20.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_2.6.20.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_2.fixpos.6.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_3.7.5.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_3.fixpos.7.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_3.7.5.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_3.fixpos.7.5.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_3.7.5.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_3.fixpos.7.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_4.7.7.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_4.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_4.7.7.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_4.fixpos.7.7.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_4.7.7.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_4.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_6.7.21.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_6.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_6.7.21.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_6.fixpos.7.21.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_6.7.21.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_6.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_7.8.4.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_7.fixpos.8.4.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_7.8.4.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_7.fixpos.8.4.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_7.8.4.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_7.fixpos.8.4.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_8.8.7.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_8.fixpos.8.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_8.8.7.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_8.fixpos.8.7.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_8.8.7.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_8.fixpos.8.7.11.mod
quit
EOF
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
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_12.8.24.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_12.fixpos.8.24.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_12.8.24.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_12.fixpos.8.24.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_12.8.24.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_12.fixpos.8.24.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_13.9.1.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_13.fixpos.9.1.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_13.9.1.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_13.fixpos.9.1.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_13.9.1.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_13.fixpos.9.1.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_15.9.5.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_15.fixpos.9.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_15.9.5.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_15.fixpos.9.5.11.mod
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
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_15.9.5.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_15.fixpos.9.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_16.9.11.11.11A-138.J0204+0903.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0204+0903.EarlySB2_16.fixpos.9.11.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_16.9.11.11.11A-138.J0754+5324.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0754+5324.EarlySB2_16.fixpos.9.11.11.mod
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
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/EarlySB2/data/EarlySB2_16.9.11.11.11A-138.B0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B0712+472.EarlySB2_16.fixpos.9.11.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_10.7.21.11.11A-138.J1414+4554.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1414+4554.LateSB1_10.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_10.7.21.11.11A-138.J1400+6210.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1400+6210.LateSB1_10.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_10.7.21.11.11A-138.J1545+4751.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1545+4751.LateSB1_10.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_10.7.21.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB1_10.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_10.7.21.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB1_10.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_10.7.21.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB1_10.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_10.7.21.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB1_10.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_11.7.26.11.11A-138.J1414+4554.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1414+4554.LateSB1_11.fixpos.7.26.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_11.7.26.11.11A-138.J1400+6210.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1400+6210.LateSB1_11.fixpos.7.26.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_11.7.26.11.11A-138.J1545+4751.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1545+4751.LateSB1_11.fixpos.7.26.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_11.7.26.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB1_11.fixpos.7.26.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_11.7.26.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB1_11.fixpos.7.26.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_11.7.26.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB1_11.fixpos.7.26.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_11.7.26.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB1_11.fixpos.7.26.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_13.8.2.11.11A-138.J1414+4554.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1414+4554.LateSB1_13.fixpos.8.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_13.8.2.11.11A-138.J1400+6210.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1400+6210.LateSB1_13.fixpos.8.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_13.8.2.11.11A-138.J1545+4751.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1545+4751.LateSB1_13.fixpos.8.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_13.8.2.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB1_13.fixpos.8.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_13.8.2.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB1_13.fixpos.8.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_13.8.2.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB1_13.fixpos.8.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_13.8.2.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB1_13.fixpos.8.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_15.8.7.11.11A-138.J1414+4554.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1414+4554.LateSB1_15.fixpos.8.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_15.8.7.11.11A-138.J1400+6210.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1400+6210.LateSB1_15.fixpos.8.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_15.8.7.11.11A-138.J1545+4751.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1545+4751.LateSB1_15.fixpos.8.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_15.8.7.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB1_15.fixpos.8.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_15.8.7.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB1_15.fixpos.8.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_15.8.7.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB1_15.fixpos.8.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_15.8.7.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB1_15.fixpos.8.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_16.8.10.11.11A-138.J1414+4554.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1414+4554.LateSB1_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_16.8.10.11.11A-138.J1400+6210.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1400+6210.LateSB1_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_16.8.10.11.11A-138.J1545+4751.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1545+4751.LateSB1_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_16.8.10.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB1_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_16.8.10.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB1_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_16.8.10.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB1_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_16.8.10.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB1_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_18.8.20.11.11A-138.J1414+4554.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1414+4554.LateSB1_18.fixpos.8.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_18.8.20.11.11A-138.J1400+6210.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1400+6210.LateSB1_18.fixpos.8.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_18.8.20.11.11A-138.J1545+4751.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1545+4751.LateSB1_18.fixpos.8.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_18.8.20.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB1_18.fixpos.8.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_18.8.20.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB1_18.fixpos.8.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_18.8.20.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB1_18.fixpos.8.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_18.8.20.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB1_18.fixpos.8.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_5.6.28.11.11A-138.J1414+4554.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1414+4554.LateSB1_5.fixpos.6.28.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_5.6.28.11.11A-138.J1400+6210.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1400+6210.LateSB1_5.fixpos.6.28.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_5.6.28.11.11A-138.J1545+4751.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1545+4751.LateSB1_5.fixpos.6.28.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_5.6.28.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB1_5.fixpos.6.28.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_5.6.28.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB1_5.fixpos.6.28.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_5.6.28.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB1_5.fixpos.6.28.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_5.6.28.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB1_5.fixpos.6.28.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_7.7.7.11.11A-138.J1414+4554.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1414+4554.LateSB1_7.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_7.7.7.11.11A-138.J1400+6210.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1400+6210.LateSB1_7.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_7.7.7.11.11A-138.J1545+4751.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1545+4751.LateSB1_7.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_7.7.7.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB1_7.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_7.7.7.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB1_7.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_7.7.7.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB1_7.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_7.7.7.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB1_7.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_9.7.16.11.11A-138.J1414+4554.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1414+4554.LateSB1_9.fixpos.7.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_9.7.16.11.11A-138.J1400+6210.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1400+6210.LateSB1_9.fixpos.7.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_9.7.16.11.11A-138.J1545+4751.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1545+4751.LateSB1_9.fixpos.7.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_9.7.16.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB1_9.fixpos.7.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_9.7.16.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB1_9.fixpos.7.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_9.7.16.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB1_9.fixpos.7.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_9.7.16.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB1_9.fixpos.7.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_X.8.15.11.11A-138.J1414+4554.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1414+4554.LateSB1_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_X.8.15.11.11A-138.J1400+6210.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1400+6210.LateSB1_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_X.8.15.11.11A-138.J1545+4751.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1545+4751.LateSB1_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_X.8.15.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB1_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_X.8.15.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB1_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_X.8.15.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB1_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_X.8.15.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB1_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_1.6.10.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB2_1.fixpos.6.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_1.6.10.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB2_1.fixpos.6.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_1.6.10.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB2_1.fixpos.6.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_1.6.10.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB2_1.fixpos.6.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_1.6.10.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB2_1.fixpos.6.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_1.6.10.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB2_1.fixpos.6.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_4.7.24.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB2_4.fixpos.7.24.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_4.7.24.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB2_4.fixpos.7.24.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_4.7.24.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB2_4.fixpos.7.24.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_4.7.24.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB2_4.fixpos.7.24.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_4.7.24.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB2_4.fixpos.7.24.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_4.7.24.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB2_4.fixpos.7.24.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_16.8.14.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB2_16.fixpos.8.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_16.8.14.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB2_16.fixpos.8.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_16.8.14.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB2_16.fixpos.8.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_16.8.14.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB2_16.fixpos.8.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_16.8.14.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB2_16.fixpos.8.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_16.8.14.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB2_16.fixpos.8.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_19.8.23.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB2_19.fixpos.8.23.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_19.8.23.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB2_19.fixpos.8.23.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_19.8.23.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB2_19.fixpos.8.23.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_19.8.23.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB2_19.fixpos.8.23.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_19.8.23.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB2_19.fixpos.8.23.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB2/data/LateSB2_19.8.23.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB2_19.fixpos.8.23.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_14.8.5.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_14.fixpos.8.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_14.8.5.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_14.fixpos.8.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_14.8.5.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_14.fixpos.8.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_14.8.5.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_14.fixpos.8.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_14.8.5.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_14.fixpos.8.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_14.8.5.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_14.fixpos.8.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_14.8.5.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_14.fixpos.8.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_16.8.10.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_16.8.10.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_16.8.10.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_16.8.10.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_16.8.10.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_16.8.10.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_16.8.10.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_17.8.16.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_17.fixpos.8.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_17.8.16.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_17.fixpos.8.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_17.8.16.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_17.fixpos.8.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_17.8.16.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_17.fixpos.8.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_17.8.16.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_17.fixpos.8.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_17.8.16.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_17.fixpos.8.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_17.8.16.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_17.fixpos.8.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_2.6.14.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_2.fixpos.6.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_2.6.14.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_2.fixpos.6.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_2.6.14.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_2.fixpos.6.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_2.6.14.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_2.fixpos.6.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_2.6.14.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_2.fixpos.6.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_2.6.14.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_2.fixpos.6.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_2.6.14.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_2.fixpos.6.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_20.9.9.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_20.fixpos.9.9.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_20.9.9.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_20.fixpos.9.9.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_20.9.9.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_20.fixpos.9.9.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_20.9.9.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_20.fixpos.9.9.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_20.9.9.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_20.fixpos.9.9.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_20.9.9.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_20.fixpos.9.9.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_20.9.9.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_20.fixpos.9.9.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_21.8.31.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_21.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_21.8.31.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_21.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_21.8.31.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_21.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_21.8.31.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_21.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_21.8.31.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_21.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_21.8.31.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_21.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_21.8.31.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_21.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_22.9.8.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_22.fixpos.9.8.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_22.9.8.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_22.fixpos.9.8.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_22.9.8.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_22.fixpos.9.8.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_22.9.8.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_22.fixpos.9.8.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_22.9.8.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_22.fixpos.9.8.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_22.9.8.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_22.fixpos.9.8.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_22.9.8.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_22.fixpos.9.8.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_3.6.21.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_3.fixpos.6.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_3.6.21.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_3.fixpos.6.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_3.6.21.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_3.fixpos.6.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_3.6.21.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_3.fixpos.6.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_3.6.21.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_3.fixpos.6.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_3.6.21.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_3.fixpos.6.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_3.6.21.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_3.fixpos.6.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_6.7.2.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_6.fixpos.7.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_6.7.2.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_6.fixpos.7.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_6.7.2.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_6.fixpos.7.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_6.7.2.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_6.fixpos.7.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_6.7.2.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_6.fixpos.7.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_6.7.2.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_6.fixpos.7.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_6.7.2.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_6.fixpos.7.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_8.7.14.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_8.fixpos.7.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_8.7.14.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_8.fixpos.7.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_8.7.14.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_8.fixpos.7.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_8.7.14.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_8.fixpos.7.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_8.7.14.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_8.fixpos.7.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_8.7.14.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_8.fixpos.7.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_8.7.14.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_8.fixpos.7.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_X.8.15.11.11A-138.J0003+4807.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J0003+4807.LateSB3_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_X.8.15.11.11A-138.J1823+7938.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1823+7938.LateSB3_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_X.8.15.11.11A-138.J1945+7055.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1945+7055.LateSB3_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_X.8.15.11.11A-138.J1816+3457.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1816+3457.LateSB3_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_X.8.15.11.11A-138.J1826+1831.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1826+1831.LateSB3_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_X.8.15.11.11A-138.J1734+0926.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.J1734+0926.LateSB3_X.fixpos.8.15.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB3/data/LateSB3_X.8.15.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit.B1938+666.LateSB3_X.fixpos.8.15.11.mod
quit
EOF
