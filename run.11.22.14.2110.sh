#!/bin/bash
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/concatvis.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.03125
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
selfcal false,false, 60
modelfit mfitniter
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/concat.B1938+666.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.concat.mod
quit
EOF
