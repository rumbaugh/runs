#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001008
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.10.08.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001008
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.10.08.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001008
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.10.08.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001008
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.10.08.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001008
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.10.08.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001008
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.10.08.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001008
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.10.08.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001008
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.10.08.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001010
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.10.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001010
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.10.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001010
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.10.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001010
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.10.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001010
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.10.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001010
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.10.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001010
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.10.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001010
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.10.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001015
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.10.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001015
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.10.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001015
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.10.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001015
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.10.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001015
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.10.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001015
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.10.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001015
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.10.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001015
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.10.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001017
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.10.17.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001017
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.10.17.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001017
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.10.17.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001017
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.10.17.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001017
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.10.17.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001017
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.10.17.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001017
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.10.17.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001017
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.10.17.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001021
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.10.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001021
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.10.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001021
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.10.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001021
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.10.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001021
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.10.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001021
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.10.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001021
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.10.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001021
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.10.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001022
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.10.22.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001022
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.10.22.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001022
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.10.22.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001022
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.10.22.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001022
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.10.22.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001022
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.10.22.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001022
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.10.22.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001022
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.10.22.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001025
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.10.25.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001025
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.10.25.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001025
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.10.25.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001025
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.10.25.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001025
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.10.25.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001025
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.10.25.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001025
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.10.25.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001025
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.10.25.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001028
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.10.28.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001028
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.10.28.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001028
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.10.28.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001028
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.10.28.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001028
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.10.28.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001028
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.10.28.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001028
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.10.28.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001028
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.10.28.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001031
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.10.31.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001031
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.10.31.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001031
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.10.31.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001031
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.10.31.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001031
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.10.31.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001031
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.10.31.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001031
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.10.31.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001031
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.10.31.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001102
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.11.02.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001102
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.11.02.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001102
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.11.02.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001102
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.11.02.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001102
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.11.02.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001102
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.11.02.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001102
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.11.02.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001102
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.11.02.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001104
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.11.04.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001104
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.11.04.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001104
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.11.04.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001104
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.11.04.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001104
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.11.04.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001104
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.11.04.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001104
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.11.04.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001104
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.11.04.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.11.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.11.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.11.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.11.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.11.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001107
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.11.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001107
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.11.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001107
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.11.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001109
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.11.09.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001109
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.11.09.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001109
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.11.09.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001109
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.11.09.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001109
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.11.09.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001109
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.11.09.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001109
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.11.09.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001109
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.11.09.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.11.18.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.11.18.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.11.18.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.11.18.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.11.18.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001118
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.11.18.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001118
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.11.18.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001118
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.11.18.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001120
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.11.20.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001120
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.11.20.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001120
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.11.20.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001120
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.11.20.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001120
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.11.20.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001120
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.11.20.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001126
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.11.26.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001126
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.11.26.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001126
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.11.26.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001126
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.11.26.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001126
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.11.26.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001126
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.11.26.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001126
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.11.26.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.11.30.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.11.30.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.11.30.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.11.30.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.11.30.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001130
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.11.30.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001130
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.11.30.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001130
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.11.30.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001203
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.12.03.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001203
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.12.03.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001203
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.12.03.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001203
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.12.03.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001203
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.12.03.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001203
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.12.03.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001203
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.12.03.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.12.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.12.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.12.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.12.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001207
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.12.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001207
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.12.07.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001210
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.12.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001210
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.12.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001210
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.12.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001210
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.12.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001210
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.12.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001210
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.12.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001210
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.12.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001210
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.12.10.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001215
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.12.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001215
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.12.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001215
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.12.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001215
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.12.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001215
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.12.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001215
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.12.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001215
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.12.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001215
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.12.15.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.12.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.12.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.12.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.12.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.12.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001221
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.12.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001221
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.12.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001221
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.12.21.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001227
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.12.27.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001227
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.12.27.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001227
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.12.27.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001227
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.12.27.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001227
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.12.27.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001227
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.12.27.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001227
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.12.27.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001227
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.12.27.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001229
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.12.29.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20001229
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.12.29.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20001229
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.12.29.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20001229
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.12.29.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20001229
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.12.29.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20001229
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.12.29.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20001229
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.12.29.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20001229
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.12.29.00.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010103
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.1.03.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010103
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.1.03.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010103
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.1.03.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010103
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.1.03.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010103
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.1.03.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010103
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.1.03.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010103
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.1.03.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010103
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.1.03.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010105
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.1.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010105
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.1.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010105
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.1.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010105
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.1.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010105
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.1.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010105
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.1.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010105
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.1.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010105
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.1.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.1.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.1.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.1.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.1.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.1.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010107
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.1.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010107
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.1.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010107
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.1.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010110
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.1.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010110
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.1.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010110
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.1.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010110
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.1.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010110
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.1.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010110
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.1.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010110
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.1.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010110
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.1.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010113
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.1.13.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010113
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.1.13.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010113
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.1.13.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010113
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.1.13.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010113
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.1.13.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010113
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.1.13.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010113
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.1.13.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010113
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.1.13.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010115
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.1.15.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010115
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.1.15.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010115
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.1.15.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010115
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.1.15.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010115
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.1.15.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010115
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.1.15.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.1.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.1.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.1.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.1.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.1.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010118
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.1.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010118
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.1.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010118
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.1.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010123
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.1.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010123
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.1.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010123
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.1.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010123
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.1.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010123
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.1.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010123
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.1.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010123
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.1.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010123
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.1.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010127
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.1.27.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010127
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.1.27.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010127
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.1.27.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010127
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.1.27.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010127
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.1.27.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010127
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.1.27.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010127
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.1.27.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010127
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.1.27.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.1.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.1.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.1.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.1.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.1.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010130
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.1.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010130
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.1.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010130
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.1.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010201
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010201
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010201
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010201
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010201
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010201
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010201
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010201
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010205
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010205
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010205
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010205
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010205
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010205
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010205
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010205
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010207
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010207
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010207
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.07.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010208
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010208
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010208
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010208
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010208
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010208
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010208
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010208
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010212
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010212
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010212
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010212
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010212
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010212
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010212
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010212
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010214
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010214
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010214
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010214
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010214
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010214
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010214
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010214
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010216
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010216
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010216
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010216
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010216
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010216
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010216
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010216
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.16.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010218
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010218
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010218
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010218
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010218
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010218
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010218
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010218
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010221
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010221
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010221
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010222
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010222
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010222
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010222
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010222
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010222
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010222
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010222
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.22.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010226
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010226
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010226
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010226
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010226
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010226
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010226
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010226
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.2.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010301
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010301
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010301
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010301
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010301
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010301
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010301
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010301
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.01.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010304
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.04.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010304
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.04.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010304
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.04.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010304
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.04.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010304
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.04.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010304
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.04.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010304
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.04.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010304
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.04.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010306
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010306
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010306
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010306
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010306
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.06.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010310
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010310
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010310
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010310
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010310
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010310
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010310
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010310
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010314
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010314
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010314
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010314
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010314
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010314
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010314
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010314
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010318
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010318
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010318
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010318
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010318
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010318
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010318
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010318
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.18.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010321
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010321
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010321
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010321
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010321
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010321
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010321
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010321
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.21.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010323
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010323
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010323
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010323
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010323
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010323
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010323
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010323
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.23.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010326
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010326
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010326
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010326
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010326
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010326
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010326
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010326
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010328
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010328
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010328
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010328
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010328
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010328
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010328
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010328
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010330
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010330
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010330
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010330
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010330
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010330
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010330
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010330
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010331
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.3.31.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010331
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.3.31.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010331
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.3.31.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010331
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.3.31.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010331
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.3.31.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010331
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.3.31.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010331
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.3.31.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010331
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.3.31.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010402
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010402
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010402
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010402
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010402
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010402
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010402
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010402
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.4.02.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010405
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010405
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010405
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010405
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010405
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010405
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010405
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010405
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.4.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010409
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010409
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010409
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010409
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010409
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010409
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010409
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010409
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.4.09.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010410
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010410
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010410
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010410
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010410
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.4.10.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010414
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010414
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010414
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010414
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010414
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010414
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010414
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010414
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.4.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010417
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010417
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010417
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010417
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010417
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010417
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010417
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010417
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.4.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010419
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010419
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010419
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010419
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010419
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010419
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010419
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010419
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.4.19.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010424
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010424
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010424
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010424
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010424
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010424
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010424
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010424
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.4.24.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010426
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010426
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010426
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010426
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010426
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010426
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010426
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010426
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.4.26.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010430
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010430
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010430
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010430
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010430
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010430
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010430
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010430
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.4.30.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010505
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010505
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010505
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010505
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010505
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010505
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010505
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010505
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.5.05.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010508
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010508
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010508
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010508
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010508
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010508
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010508
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010508
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.5.08.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010512
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010512
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010512
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010512
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010512
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010512
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010512
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010512
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.5.12.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010514
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010514
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010514
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010514
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010514
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010514
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010514
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010514
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.5.14.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010517
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010517
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010517
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010517
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010517
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010517
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010517
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010517
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.5.17.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010520
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010520
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010520
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010520
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010520
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010520
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010520
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010520
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.5.20.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010525
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010525
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010525
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010525
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010525
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010525
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010525
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010525
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.5.25.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010528
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0414+573.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1030+074_20010528
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1030+074.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1127+385_20010528
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1127+385.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1152+199_20010528
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.1152+199.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0712+472_20010528
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR_4.5.14.0712+472.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1244+408_20010528
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1244+408.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1400+621_20010528
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1400+621.fixpos.5.28.01.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_1035+564_20010528
select I
mapunits arcsec
mapsize 256,0.05
addcmp 0.1,true,0,0,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_LR.1035+564.fixpos.5.28.01.mod
quit
EOF
