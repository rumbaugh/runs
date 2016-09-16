execfile('/mnt/data2/rumbaugh/LRIS/2011_01/Scripts/split_off_slits.py')

masks = ['M0744_A','M0744_B','M0417_B','M1115_A','miki10.f','miki22_z','miki21_B','miki21D.','bc3.file','bc3B.fil','miki21C.']
split_off_slits(masks,colors=['red','blue'],sides=['top','bottom'])
split_off_slits(['1131m3','1131m4','miki16B.'],colors=['red','blue'],sides=['top'])
#split_off_slits(['miki16B.'],colors=['red'],sides=['bottom'])
masks = ['miki22.f','miki21.f','miki04_A','miki03_B','miki03_A']
split_off_slits(masks,colors=['red'],sides=['top'])
masks = ['miki22.f','miki21.f','miki04.f','miki04_B','miki04_A','miki03_A']
split_off_slits(masks,colors=['blue'],sides=['bottom'])
masks = ['miki22.f','miki21.f','miki04_A','miki03_A']
split_off_slits(masks,colors=['red'],sides=['bottom'])
