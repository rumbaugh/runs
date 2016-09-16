echo ' '
echo 'Needs to be run on Gallifrey'
echo ' '
declare -a z=(soft hard full)
declare -a el=(0.5 2.0 0.5)
declare -a eu=(2.0 8.0 8.0)
declare -a nl=(500 2000 500)
declare -a nu=(2000 8000 8000)
declare -a n=(500-2000 2000-8000 500-8000)
declare -a nn=(500:2000 2000:8000 500:8000)
declare -a nd=(0.5,2.0 2.0,8.0)
declare -a ndL=(0.5 2.0)
declare -a ndH=(2.0 8.0)
declare -a nq=(0.5:2.0 2.0:8.0)
declare -a nh=(0.58 1.93 3.71)


for i in 927 1708
do
cd /mnt/data2/rumbaugh/dump/ChandraData/$i
punlearn ardlib
acis_set_ardlib acis$i.bpix.fits
for j in 1 2 3
do
get_sky_limits acis$i.evt2.${n[$j]}.fits verbose=0
set xy = `pget get_sky_limits xygrid`
merge_all evtfile="acis$i.evt2.${n[$j]}.fits" asol="acis$i.asol.fits" chip="0,1,2,3" refcoord="acis$i.evt2.${n[$j]}.fits" xygrid="$xy" energy="/home/rumbaugh/Chandra_ORELSE_Notes/expmap_weights/weights.${z[$j]}.gamma=1.4.txt" expmap="acis$i.expmap_${z[$j]}.fits" dtffile='' merged='' expcorr='' clobber=yes
done
done
for i in 927 1708
do
cd /mnt/data2/rumbaugh/dump/ChandraData/$i
punlearn ardlib
acis_set_ardlib acis$i.bpix.fits
for j in 1 2 3
do
wavdetect infile="acis$i.img.${n[$j]}.fits" outfile="sources.$i.${z[$j]}.1e6.b1.1-16.wexp20.fits" scellfile="./temp/sources_scell.$i.${z[$j]}.1e6.wexp20.fits" imagefile="./temp/sources_image.$i.${z[$j]}.1e6.wexp20.fits" defnbkgfile="./temp/sources_bkg.$i.${z[$j]}.1e6.wexp20.fits" regfile="./regions/sources.$i.${z[$j]}.1e6.b1.1-16.wexp20.reg" scales="1.0 1.414 2.0 2.828 4.0 5.657 8.0 11.314 16.0" sigthresh=1.0e-6 ellsigma=4 expthresh=0.2 expfile="acis$i.expmap_${z[$j]}.fits" clob+
rm temp/*
cd regions
rm bkg*${z[$j]}*reg
mkBgRegScript sources.$i.${z[$j]}.1e6.b1.1-16.wexp20.reg 2 bkg.$i.${z[$j]}.reg
mkSubSuperBgRegScript sources.$i.${z[$j]}.1e6.b1.1-16.wexp20.reg bkg.$i.${z[$j]}.reg bkg_sub.$i.${z[$j]}.reg
sed -i 's/[0-9]e-[0-9][0-9]/0/g' bkg_sub.$i.${z[$j]}.reg
sed -i 's/[0-9]e-[0-9][0-9]/0/g' sources.$i.${z[$j]}.1e6.b1.1-16.wexp20.reg
cd ..
set num = `stats -v max < acis$i.expmap_${z[$j]}.fits`
dmimgcalc acis$i.img.${n[$j]}.fits acis$i.expmap_${z[$j]}.fits acis$i.img.${n[$j]}.vig_corr.fits div weight=$num clob+
dmfilth infile=acis$i.img.${n[$j]}.vig_corr.fits outfile=acis$i.img.${n[$j]}.nops.fits method=POISSON srclist=@./regions/sources.$i.${z[$j]}.1e6.b1.1-16.wexp20.reg bkglist=@./regions/bkg_sub.$i.${z[$j]}.reg randseed=0 clob+
done
done
done
