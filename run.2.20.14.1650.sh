declare -a slits=(761 85 324 628)
for i in ${slits[*]}
do
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/plots/lineplot.0435m2_${i}_coadd_bgsub.png /home/rumbaugh/tmp0435/lineplot.0435m2_${i}.png
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/plots/lineplot.0435m2_${i}_red_bottom_coadd_bgsub.png /home/rumbaugh/tmp0435/lineplot.0435m2_${i}_red.png
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/plots/lineplot.0435m2_${i}_red_top_coadd_bgsub.png /home/rumbaugh/tmp0435/lineplot.0435m2_${i}_red.png
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/plots/lineplot.0435m2_${i}_blue_bottom_coadd_bgsub.png /home/rumbaugh/tmp0435/lineplot.0435m2_${i}_blue.png
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits/plots/lineplot.0435m2_${i}_blue_top_coadd_bgsub.png /home/rumbaugh/tmp0435/lineplot.0435m2_${i}_blue.png
done

declare -a slits=(211)
for i in ${slits[*]}
do
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m3_v2/plots/lineplot.0435m3_v2_${i}_coadd_bgsub.png /home/rumbaugh/tmp0435/lineplot.0435m3_v2_${i}.png
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m3_v2/plots/lineplot.0435m3_v2_${i}_red_bottom_coadd_bgsub.png /home/rumbaugh/tmp0435/lineplot.0435m3_v2_${i}_red.png
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m3_v2/plots/lineplot.0435m3_v2_${i}_red_top_coadd_bgsub.png /home/rumbaugh/tmp0435/lineplot.0435m3_v2_${i}_red.png
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m3_v2/plots/lineplot.0435m3_v2_${i}_blue_bottom_coadd_bgsub.png /home/rumbaugh/tmp0435/lineplot.0435m3_v2_${i}_blue.png
cp /mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m3_v2/plots/lineplot.0435m3_v2_${i}_blue_top_coadd_bgsub.png /home/rumbaugh/tmp0435/lineplot.0435m3_v2_${i}_blue.png
done
