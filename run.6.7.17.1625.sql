select s.SDSS_NAME, s.ra, s.dec, s.HPIX o.objID, o.raMean, o.decMean,
   o.nDetections, o.ng, o.nr, o.ni, o.nz, o.ny,
   m.gMeanPSFMag, m.rMeanPSFMag, m.iMeanPSFMag, m.zMeanPSFMag, m.yMeanPSFMag
from MyDB.DR12_notingDR7_SNRADECTID s
  cross apply fGetNearbyObjEq(s.ra,s.dec,0.03) nb
  inner join Y3A1_COADD_OBJECT_SUMMARY y on o.objid=nb.objid and o.nDetections>1
