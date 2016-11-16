SELECT y.RA,y.DEC
from RUMBAUGH.MILLIQUAS_Y1A1_MATCH y,RUMBAUGH.MILLIQUAS_Y1A1_TILES t
where y.mq_rownum=t.mq_rownum
and y.coadd_objects_id=0
and t.TILENAME!='None'; >MILLIQUAS_INY1A1TILE_RADEC.csv
