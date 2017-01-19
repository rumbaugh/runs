SELECT h.coadd_object_id,y.ra,y.dec,h.hpix_16384 from DES_ADMIN.Y3A1_COADD_OBJECT_HPIX h, DES_ADMIN.Y3A1_COADD_OBJECT_SUMMARY y where h.coadd_object_id=y.coadd_object_id; >y3a1_hpix_radec.tab
