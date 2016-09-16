#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.01.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.01.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.01.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.01.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.01.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.01.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.01.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.05.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.05.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.05.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.05.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.05.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.05.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.05.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.07.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.07.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.07.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.07.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.07.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.07.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.07.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.08.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.08.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.08.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.08.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.08.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.08.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.08.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.12.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.12.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.12.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.12.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.12.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.12.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.12.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.14.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.14.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.14.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.14.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.14.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.14.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.14.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.16.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.16.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.16.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.16.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.16.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.16.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.16.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.18.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.18.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.18.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.18.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.18.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.18.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.18.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.21.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.21.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.21.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.21.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.21.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.21.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.21.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.22.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.22.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.22.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.22.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.22.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.22.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.22.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.26.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.26.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.26.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.26.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.26.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.26.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_2.26.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.06.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.06.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.06.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.06.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.06.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.06.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.06.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.14.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.14.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.14.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.14.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.14.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.14.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.14.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.16.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.3.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.16.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.3.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.16.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.3.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.16.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.3.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.16.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.3.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.16.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.3.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.16.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.3.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.18.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.18.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.18.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.18.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.18.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.18.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.18.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.21.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.21.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.21.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.21.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.21.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.21.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.21.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.23.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.23.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.23.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.23.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.23.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.23.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.23.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.26.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.26.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.26.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.26.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.26.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.26.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.26.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.28.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.28.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.28.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.28.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.28.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.28.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.28.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.30.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.30.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.30.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.30.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.30.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.30.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_3.30.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.02.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.02.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.02.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.02.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.02.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.02.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.02.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.05.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.05.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.05.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.05.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.05.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.05.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.05.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.09.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.09.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.09.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.09.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.09.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.09.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.09.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.10.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.10.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.10.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.10.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.10.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.10.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.10.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.14.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.14.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.14.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.14.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.14.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.14.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.14.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.17.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.17.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.17.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.17.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.17.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.17.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.17.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.19.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.19.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.19.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.19.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.19.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.19.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.19.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.24.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.24.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.24.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.24.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.24.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.24.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.24.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.26.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.26.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.26.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.26.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.26.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.26.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.26.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.30.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.30.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.30.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.30.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.30.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.30.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_4.30.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.05.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.05.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.05.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.05.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.05.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.05.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.05.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.08.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.08.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.08.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.08.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.08.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
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
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
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
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.12.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.12.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.12.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.12.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.12.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
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
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
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
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.14.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.14.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.14.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.14.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.14.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
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
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
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
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.17.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.17.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.17.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.17.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.17.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
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
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
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
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.20.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.20.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.20.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.20.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.20.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.20.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.20.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.25.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.25.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.25.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.25.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.25.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.25.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.25.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.28.01.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0414+573.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.28.01.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1030+074.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.28.01.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1127+385.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.28.01.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1152+199.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.28.01.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data3/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.0712+472.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.28.01.1244+408.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1244+408.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data3/rumbaugh/VLA/AF377/data/af377_5.28.01.1400+621.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data3/rumbaugh/VLA/AF377/difmap_results/fit.1400+621.fixpos.5.28.01.mod
quit
EOF
