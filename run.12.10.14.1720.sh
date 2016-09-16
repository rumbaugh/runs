#!/bin/bash
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB1_10.7.21.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB1_10.fixpos.7.21.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB1_10.fixpos.7.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB1_11.7.26.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB1_11.fixpos.7.26.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB1_11.fixpos.7.26.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB1_13.8.2.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB1_13.fixpos.8.2.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB1_13.fixpos.8.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB1_15.8.7.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB1_15.fixpos.8.7.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB1_15.fixpos.8.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB1_16.8.10.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB1_16.fixpos.8.10.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB1_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB1_18.8.20.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB1_18.fixpos.8.20.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB1_18.fixpos.8.20.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB1_5.6.28.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB1_5.fixpos.6.28.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB1_5.fixpos.6.28.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB1_7.7.7.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB1_7.fixpos.7.7.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB1_7.fixpos.7.7.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB1_9.7.16.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB1_9.fixpos.7.16.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB1_9.fixpos.7.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB1_X.8.15.11.11A-138.B1938+666.uvfits
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
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB2_1.6.10.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB2_1.fixpos.6.10.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB2_1.fixpos.6.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB2_4.7.24.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB2_4.fixpos.7.24.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB2_4.fixpos.7.24.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB2_16.8.14.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB2_16.fixpos.8.14.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB2_16.fixpos.8.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB2_19.8.23.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB2_19.fixpos.8.23.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB2_19.fixpos.8.23.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_14.8.5.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB3_14.fixpos.8.5.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB3_14.fixpos.8.5.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_16.8.10.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB3_16.fixpos.8.10.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB3_16.fixpos.8.10.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_17.8.16.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB3_17.fixpos.8.16.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB3_17.fixpos.8.16.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_2.6.14.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB3_2.fixpos.6.14.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB3_2.fixpos.6.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_20.9.9.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB3_20.fixpos.9.9.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB3_20.fixpos.9.9.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_21.8.31.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB3_21.fixpos.8.31.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB3_21.fixpos.8.31.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_22.9.8.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB3_22.fixpos.9.8.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB3_22.fixpos.9.8.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_3.6.21.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB3_3.fixpos.6.21.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB3_3.fixpos.6.21.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_6.7.2.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB3_6.fixpos.7.2.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB3_6.fixpos.7.2.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_8.7.14.11.11A-138.B1938+666.uvfits
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
shift 0.1,-0.3
wmap  /home/rumbaugh/B1938+666_files/B1938+666.LateSB3_8.fixpos.7.14.11.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /home/rumbaugh/B1938+666_files/difmap_results/fit_wrms.B1938+666.LateSB3_8.fixpos.7.14.11.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /home/rumbaugh/B1938+666_files/LateSB3_X.8.15.11.11A-138.B1938+666.uvfits
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
quit
EOF
