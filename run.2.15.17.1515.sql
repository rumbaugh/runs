SELECT bh.numrow,y.COADD_OBJECT_ID,bh.SDSS_NAME,y.RA as ra_y3a1,y.DEC as dec_y3a1,dr.objid as objid_SDSS,dr.thingid,dr.mjd_g,dr.ra, dr.dec,dr.run,dr.rerun,dr.stripe,dr.psfmag_u as SDSS_psfmag_u,dr.psfmag_g as SDSS_psfmag_g,dr.psfmag_r as SDSS_psfmag_r,dr.psfmag_i as SDSS_psfmag_i,dr.psfmag_z as SDSS_psfmag_z,dr.psfmagerr_u as SDSS_psfmagerr_u,dr.psfmagerr_g as SDSS_psfmagerr_g,dr.psfmagerr_r as SDSS_psfmagerr_r,dr.psfmagerr_i as SDSS_psfmagerr_i,dr.psfmagerr_z as SDSS_psfmagerr_z
FROM des_admin.Y3A1_COADD_OBJECT_SUMMARY y,RUMBAUGH.dr7_bh_match_only bh,dr7_bh_sdss_match2 dr 
where bh.coadd_objects_id=y.coadd_object_id 
and bh.numrow=dr.numrow; > dr7_bh_lightcurve_entries_SDSS.y3a1.tab
