declare -a slits=(761 85 324 628)
for i in ${slits[*]}
do
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/spec_output/outspec.0435m2_${i}_coadd_bgsub.dat /home/rumbaugh/tmp0435/outspec.0435m2_${i}.dat
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/spec_output/outspec.0435m2_${i}_red_bottom_coadd_bgsub.dat /home/rumbaugh/tmp0435/outspec.0435m2_${i}_red.dat
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/spec_output/outspec.0435m2_${i}_red_top_coadd_bgsub.dat /home/rumbaugh/tmp0435/outspec.0435m2_${i}_red.dat
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/spec_output/outspec.0435m2_${i}_blue_bottom_coadd_bgsub.dat /home/rumbaugh/tmp0435/outspec.0435m2_${i}_blue.dat
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/spec_output/outspec.0435m2_${i}_blue_top_coadd_bgsub.dat /home/rumbaugh/tmp0435/outspec.0435m2_${i}_blue.dat
done

declare -a slits=(211)
for i in ${slits[*]}
do
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m3_v2/spec_output/outspec.0435m3_v2_${i}_coadd_bgsub.dat /home/rumbaugh/tmp0435/outspec.0435m3_v2_${i}.dat
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m3_v2/spec_output/outspec.0435m3_v2_${i}_red_bottom_coadd_bgsub.dat /home/rumbaugh/tmp0435/outspec.0435m3_v2_${i}_red.dat
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m3_v2/spec_output/outspec.0435m3_v2_${i}_red_top_coadd_bgsub.dat /home/rumbaugh/tmp0435/outspec.0435m3_v2_${i}_red.dat
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m3_v2/spec_output/outspec.0435m3_v2_${i}_blue_bottom_coadd_bgsub.dat /home/rumbaugh/tmp0435/outspec.0435m3_v2_${i}_blue.dat
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m3_v2/spec_output/outspec.0435m3_v2_${i}_blue_top_coadd_bgsub.dat /home/rumbaugh/tmp0435/outspec.0435m3_v2_${i}_blue.dat
done
