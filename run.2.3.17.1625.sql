SELECT r.SP_ROWNUM,y.COADD_OBJECT_ID,e.mjd_obs,o.RA,o.DEC,o.expnum,o.filename,o.object_number,z.mag_zero-2.5*log(10,o.flux_psf) as mag_psf,SQRT(POWER(z.SIGMA_MAG_ZERO, 2)+ POWER(o.FLUXERR_PSF / o.FLUX_PSF, 2)) as MAGERR_PSF,z.mag_zero-2.5*log(10,o.flux_auto) as mag_auto,SQRT(POWER(z.SIGMA_MAG_ZERO,2) + POWER(o.FLUXERR_AUTO / o.FLUX_AUTO, 2)) as MAGERR_AUTO,o.band,o.flags,o.flags_detmodel,o.flags_model,o.flags_weight FROM rumbaugh.sdssposs_y3a1_match r,des_admin.Y3A1_COADD_OBJECT_SUMMARY y, des_admin.y3a1_finalcut_object o,des_admin.y3a1_exposure e,des_admin.y3a1_wavg_oclink l,des_admin.y3a1_zeropoint z where o.expnum=e.expnum and y.coadd_object_id=r.coadd_objects_id and y.coadd_object_id=l.coadd_object_id and o.filename=l.se_object_filename and o.object_number=l.se_object_number and e.expnum=z.expnum and z.source='FGCM' and z.version='v2.0' and z.CATALOGNAME=o.FILENAME; >SDSSPOSS_lightcurve_entries_y3a1.tab
