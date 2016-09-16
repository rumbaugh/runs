#!/bin/csh
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB2/data/LateSB2_1.6.10.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB2_1.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_2.6.14.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB3_2.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_3.6.21.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB3_3.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB2/data/LateSB2_4.6.24.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB2_4.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_5.6.28.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB1_5.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_6.7.2.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB3_6.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_8.7.14.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB3_8.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_9.7.16.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB1_9.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_10.7.21.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB1_10.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_11.7.26.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB1_11.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_13.8.2.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB1_13.8.25.12.mod
quit
EOF
difmap << EOF
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_14.8.5.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.05
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
selfcal false,false,60
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 5
addcmp peak(flux,max),true,peak(x,max),peak(y,max),true
modelfit 30
wmod /local3/rumbaugh/EVLA/data/11A-138/difmap_results/prelim_fit.B1938+666.LateSB3_14.8.25.12.mod
quit
EOF
