import easyaccess as ea
execfile('/home/rumbaugh/runs/run.10.2.16.1930.py')
cre=np.loadtxt('/home/rumbaugh/milliquas_num_epochs.dat',dtype='i8')
IDs,exps=cre[:,0],cre[:,1]

ge=np.argsort(exps)[::-1]

con=ea.connect()
idsstr=''
for s in IDs[ge[:10]]: idsstr='%s, %i'%(idsstr,s)
idsstr=idstr[1:]

query='SELECT e.mjd_obs,o.imageid,y.COADD_OBJECTS_ID,y.RA,y.DEC,o.mag_auto+i.zeropoint,o.magerr_auto,o.mag_psf+i.zeropoint,o.magerr_psf,o.band,i.exptime,i.sigma_zeropoint FROM des_admin.Y1A1_COADD_OBJECTS y, des_admin.y1a1_objects o, des_admin.y1a1_image i,des_admin.y1a1_exposure e where o.imageid=i.id and i.exposureid=e.id and y.coadd_objects_id=o.coadd_objects_id and y.coadd_objects_id in (%s)'%idsstr

DF=con.query_to_pandas(query)

