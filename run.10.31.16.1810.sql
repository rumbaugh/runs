SELECT r.COADD_OBJECTS_ID,y.MAG_PSF_Y,y.MAG_PSF_G,y.MAG_PSF_R,y.MAG_PSF_I,y.MAG_PSF_Z
FROM DES_ADMIN.Y1A1_COADD_OBJECTS y, RUMBAUGH.MILLIQUAS_Y1A1_MATCH_ONLY r
where y.COADD_OBJECTS_ID=r.COADD_OBJECTS_ID; >milliquas_y1a1_coadd_mags.tab
