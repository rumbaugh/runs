execfile('/home/rumbaugh/file_dict_1131.py')
execfile('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa/lris_reduce_longslit.py')


for mask in ['Feige110_1','Feige110_2','AGY_GRB_SN','HE0435-1223_1','HE0435-1223_2']:
    lris_reduce_longslit(indir,outdir,files_dict[mask]['prefix'],files_dict[mask],colors='both')
