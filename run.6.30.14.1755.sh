#!/bin/csh
difmap << EOF
obs /mnt/data2/rumbaugh/VLA/AF377/data/af377_10.25.00.0414+573.uvfits
select I
mapunits arcsec
mapsize 256,0.03125
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g.mod
modelfit 7
selfcal false,false,60
modelfit 7
selfcal false,false,60
modelfit 7
shift 0.472,1.277
wmap /mnt/data2/rumbaugh/VLA/AF377/data/af377_10.25.00.0414+573.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/model_wrms.0414.10.25.00.mod
quit
EOF
difmap << EOF
obs /mnt/data2/rumbaugh/VLA/AF377/data/af377_10.25.00.0712+472.uvfits
select I
mapunits arcsec
mapsize 256,0.03125
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0712_g.mod
modelfit 7
selfcal false,false,60
modelfit 7
selfcal false,false,60
modelfit 7
shift -0.793,-0.156
wmap /mnt/data2/rumbaugh/VLA/AF377/data/af377_10.25.00.0712+472.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/model_wrms.0712.10.25.00.mod
quit
EOF
difmap << EOF
obs /mnt/data2/rumbaugh/VLA/AF377/data/af377_10.25.00.1030+074.uvfits
select I
mapunits arcsec
mapsize 256,0.03125
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1030_g.mod
modelfit 7
selfcal false,false,60
modelfit 7
selfcal false,false,60
modelfit 7
shift -0.878,1.143
wmap/mnt/data2/rumbaugh/VLA/AF377/data/af377_10.25.00.1030+074.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/model_wrms.1030.10.25.00.mod
quit
EOF
difmap << EOF
obs /mnt/data2/rumbaugh/VLA/AF377/data/af377_10.25.00.1127+385.uvfits
select I
mapunits arcsec
mapsize 256,0.03125
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1127_g.mod
modelfit 7
selfcal false,false,60
modelfit 7
selfcal false,false,60
modelfit 7
shift -0.276,0.048
wmap /mnt/data2/rumbaugh/VLA/AF377/data/af377_10.25.00.1127+385.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/model_wrms.1127.10.25.00.mod
quit
EOF
difmap << EOF
obs /mnt/data2/rumbaugh/VLA/AF377/data/af377_10.25.00.1152+199.uvfits
select I
mapunits arcsec
mapsize 256,0.03125
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_1152_g.mod
modelfit 7
selfcal false,false,60
modelfit 7
selfcal false,false,60
modelfit 7
shift -0.549,0.978
wmap /mnt/data2/rumbaugh/VLA/AF377/data/af377_10.25.00.1152+199.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/model_wrms.1152.10.25.00.mod
quit
EOF
