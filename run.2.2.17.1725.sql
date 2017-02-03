SELECT e.mjd_obs,o.imageid,y.COADD_OBJECTS_ID,ms.SP_ROWNUM,y.RA,y.DEC,o.mag_psf+i.zeropoint as mag_psf,o.magerr_psf+i.sigma_zeropoint as magerr_psf,o.band,i.exptime,o.object_id
FROM des_admin.Y3A1_COADD_OBJECT_SUMMARY y, des_admin.y3a1_objects o, des_admin.y3a1_image i,des_admin.y3a1_exposure e,RUMBAUGH.sdssposs_y3a1_match ms 
where o.imageid=i.id 
and i.exposureid=e.id 
and ms.coadd_objects_id=y.coadd_objects_id 
and y.coadd_objects_id=o.coadd_objects_id; > SDSSPOSS_lightcurve_entries_Y3A1.tab
