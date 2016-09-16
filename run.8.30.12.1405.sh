#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_16.8.10.11.11A-138.B1938+666.uvfits
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
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/fit.B1938+666.LateSB1_16.concatshift.fixpos.8.30.12.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_16.8.10.11.11A-138.B1938+666.uvfits
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
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/fit.B1938+666.LateSB3_16.concatshift.fixpos.8.30.12.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB2/data/LateSB2_16.8.14.11.11A-138.B1938+666.uvfits
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
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/fit.B1938+666.LateSB2_16.concatshift.fixpos.8.30.12.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_17.8.16.11.11A-138.B1938+666.uvfits
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
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/fit.B1938+666.LateSB3_17.concatshift.fixpos.8.30.12.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_18.8.20.11.11A-138.B1938+666.uvfits
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
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/fit.B1938+666.LateSB1_18.concatshift.fixpos.8.30.12.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB2/data/LateSB2_19.8.23.11.11A-138.B1938+666.uvfits
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
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/fit.B1938+666.LateSB2_19.concatshift.fixpos.8.30.12.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_21.8.31.11.11A-138.B1938+666.uvfits
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
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/fit.B1938+666.LateSB3_21.concatshift.fixpos.8.30.12.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_20.9.9.11.11A-138.B1938+666.uvfits
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
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/fit.B1938+666.LateSB3_20.concatshift.fixpos.8.30.12.mod
quit
EOF
