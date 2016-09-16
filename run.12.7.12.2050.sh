#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_2.6.14.11.11A-138.B1938+666.uvfits
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
print "Late SB3.2 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_3.6.21.11.11A-138.B1938+666.uvfits
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
print "Late SB3.3 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB2/data/LateSB2_4.6.24.11.11A-138.B1938+666.uvfits
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
print "Late SB2.4 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_5.6.28.11.11A-138.B1938+666.uvfits
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
print "Late SB1.5 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_6.7.2.11.11A-138.B1938+666.uvfits
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
print "Late SB3.6 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_7.7.7.11.11A-138.B1938+666.uvfits
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
print "Late SB1.7 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_8.7.14.11.11A-138.B1938+666.uvfits
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
print "Late SB3.8 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_10.7.21.11.11A-138.B1938+666.uvfits
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
print "Late SB1.10 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_11.7.26.11.11A-138.B1938+666.uvfits
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
print "Late SB1.11 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB1/data/LateSB1_13.8.2.11.11A-138.B1938+666.uvfits
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
print "Late SB1.13 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/LateSB3/data/LateSB3_14.8.5.11.11A-138.B1938+666.uvfits
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
print "Late SB3.14 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/EarlySB1/data/EarlySB1_1.6.12.11.11A-138.B1938+666.uvfits
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
print "Early SB1.1 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/EarlySB2/data/EarlySB2_2.6.20.11.11A-138.B1938+666.uvfits
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
print "Early SB2.2 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/EarlySB2/data/EarlySB2_3.7.5.11.11A-138.B1938+666.uvfits
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
print "Early SB2.3 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/EarlySB2/data/EarlySB2_4.7.7.11.11A-138.B1938+666.uvfits
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
print "Early SB2.4 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/EarlySB2/data/EarlySB2_6.7.21.11.11A-138.B1938+666.uvfits
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
print "Early SB2.6 - Image rms = ", imstat(rms)
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /local3/rumbaugh/EVLA/data/11A-138/EarlySB2/data/EarlySB2_7.8.4.11.11A-138.B1938+666.uvfits
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
print "Early SB2.7 - Image rms = ", imstat(rms)
quit
EOF
