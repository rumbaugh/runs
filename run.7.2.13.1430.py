execfile('/mnt/data2/rumbaugh/LRIS/2011_01/Scripts/split_off_slits.py')

tmp_slit_dict = {'1131m1_v2': {'blue': {'top': ['1','54','80','261','490','484','564','663','678','948'], 'bottom': ['176','77']}}, '1131m2_v2': {'blue': {'top': ['1','91','121','197','227','517','600','679','786'], 'bottom': ['98','426']}}, '0435m3_v2': {'blue': {'top': ['132','450','668','604','885','849','865']}}}

for mask in ['0435m2','0435m3_v2','1131m1_v2','1131m2_v2']: 
    sides, colors = ['top','bottom'],['blue','red']
    if mask in ['1131m2_v2','0435m3_v2']: colors = ['red']
    split_off_slits([mask],colors=colors,sides=sides)
    if (mask in ['1131m1_v2','0435m3_v2']): split_off_slits([mask],colors=['blue'],sides=['bottom'])

for mask in ['0435m3_v2','1131m1_v2','1131m2_v2']:
    sides, colors = ['top','bottom'],['blue','red']
    if mask in ['1131m1_v2','1131m2_v2']: colors = ['blue']
    if mask in ['1131m1_v2']: sides = ['top']
    if mask in ['0435m3_v2']: colors,sides = ['blue'],['top']
    for color in color:
        for side in sides:
            for slit in tmp_slit_dict[mask][color][side]:
                osv = os.system("mv /mnt/data2/rumbaugh/LRIS/2011_01/reduced/%s%s_%s_%s_%s_coadd_bgsub*fits /mnt/data2/rumbaugh/LRIS/2011_01/reduced/%s/."%(mask,slit,color,side,mask))
