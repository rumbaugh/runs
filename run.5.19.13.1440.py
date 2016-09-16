execfile('/home/rumbaugh/split_off_slits.py')

masks = ['M0744_A','M0744_B','M0417_B','M1115_A','miki10.f','miki22_z','miki21_B']
split_off_slits(masks,colors=['red','blue'],sides=['top','bottom'])
split_off_slits(['1131m3','1131m4'],colors=['red','blue'],sides=['top'])
split_off_slits(['1131m3'],colors=['blue'],sides=['bottom'])
