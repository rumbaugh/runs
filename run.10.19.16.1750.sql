SELECT ms.numrow,y.COADD_OBJECTS_ID,ms.MQ_ROWNUM,y.RA as ra_y1a1,y.DEC as dec_y1a1,dr.objid as objid_SDSS,dr.thingid,dr.mjd_g,dr.ra, dr.dec,dr.run,dr.rerun,dr.stripe,dr.psfmag_u as SDSS_psfmag_u,dr.psfmag_g as SDSS_psfmag_g,dr.psfmag_r as SDSS_psfmag_r,dr.psfmag_i as SDSS_psfmag_i,dr.psfmag_z as SDSS_psfmag_z,dr.psfmagerr_u as SDSS_psfmagerr_u,dr.psfmagerr_g as SDSS_psfmagerr_g,dr.psfmagerr_r as SDSS_psfmagerr_r,dr.psfmagerr_i as SDSS_psfmagerr_i,dr.psfmagerr_z as SDSS_psfmagerr_z
FROM des_admin.Y1A1_COADD_OBJECTS y,milliquas_y1a1_match_only ms,mq_sdss_dr13_match dr 
where ms.coadd_objects_id=y.coadd_objects_id 
and ms.numrow=dr.numrow; > milliquas_lightcurve_entries_SDSS.tab
