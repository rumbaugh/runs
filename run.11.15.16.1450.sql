SELECT y.SP_ROWNUM,y.RA,y.DEC,t.TILENAME
from RUMBAUGH.SDSSPOSS_Y1A1_MATCH y,RUMBAUGH.SDSSPOSS_Y1A1_TILES t
where y.sp_rownum=t.sp_rownum
and y.coadd_objects_id=0
and t.TILENAME!='None'; >SDSSPOSS_INY1A1TILE.tab
