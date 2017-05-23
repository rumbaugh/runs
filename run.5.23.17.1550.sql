SELECT y.COADD_OBJECT_ID, y.ra, y.dec, r.ind from Y3A1_COADD_OBJECT_SUMMARY y, RUMBAUGH.all_coadd_object_ids r where r.cid=y.coadd_object_id; > all_coadd_object_ids_info.tab
