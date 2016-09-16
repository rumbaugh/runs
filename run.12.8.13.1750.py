execfile('/mnt/data2/rumbaugh/LRIS/2011_01/Scripts/split_off_slits.py')

tmp_slit_dict = {'1131m1_v2': {'blue': {'top': ['1','54','80','261','490','484','564','663','678','948'], 'bottom': ['176','77']}}, '1131m2_v2': {'blue': {'top': ['1','91','121','197','227','517','600','679','786'], 'bottom': ['98','426']}}, '0435m3_v2': {'blue': {'top': ['132','450','668','604','885','849','865']}}}

indir = '/mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised'
outdir = '/mnt/data2/rumbaugh/LRIS/2011_01/reduced/0435m2_revised/slits'
infiles = {'blue': {'top': '%s/0435m2_blue_top_coadd_bgsub.fits'%indir, 'bottom': '%s/0435m2_blue_bottom_coadd_bgsub.fits'%indir}, 'red': {'top': '%s/0435m2_red_top_coadd_bgsub.fits'%indir, 'bottom': '%s/0435m2_red_bottom_coadd_bgsub.fits'%indir}}
outfiles = {'base': '%s/0435m2'%outdir, 'blue': {'top': '%s/0435m2_blue_top_coadd_bgsub.fits'%outdir, 'bottom': '%s/0435m2_blue_bottom_coadd_bgsub.fits'%outdir}, 'red': {'top': '%s/0435m2_red_top_coadd_bgsub.fits'%outdir, 'bottom': '%s/0435m2_red_bottom_coadd_bgsub.fits'%outdir}}
outwfiles = {'base': '%s/0435m2'%outdir, 'blue': {'top': '%s/0435m2_blue_top_coadd_bgsub.weight.fits'%outdir, 'bottom': '%s/0435m2_blue_bottom_coadd_bgsub.weight.fits'%outdir}, 'red': {'top': '%s/0435m2_red_top_coadd_bgsub.weight.fits'%outdir, 'bottom': '%s/0435m2_red_bottom_coadd_bgsub.weight.fits'%outdir}}


slit_name_dict = {'0435m2': {'redux_dir': '/mnt/data2/rumbaugh/LRIS/2011_01/reduced/', \
'blue': {'top': ['1','85','189','324','628'], 'bottom': ['761','167']}, \
'red': {'top': ['1','85','189','324','628'], 'bottom': ['761','455']}}}

for mask in ['0435m2']: 
    sides, colors = ['top','bottom'],['blue','red']
    split_off_slits([mask],colors=colors,sides=sides,infiles=infiles,outfiles=outfiles,outwfiles=outwfiles)
