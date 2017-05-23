SELECT t.thingid, t.ra, t.dec, r.ind from thingindex t, dr13_thingids r into MyDB.DR13_THINGIDS_INFO where r.thingid=t.thingid
