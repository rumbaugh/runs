SELECT r.SP_ROWNUM,e.COADD_OBJECT_ID,e.mjd,e.RA,e.DEC,e.mag_psf,e.MAG_PSF_ERROR as MAGERR_PSF,e.band,e.flags FROM rumbaugh.sdssposs_y3a1_match r,rumbaugh.ERIC_LC_Y3A1_ABRIDGED e where e.coadd_object_id=r.coadd_objects_id; >sdssposs_lightcurve_entries_y3a1_SN_abridged.tab
