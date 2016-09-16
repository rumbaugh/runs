readcol, './stats/stats.clusterB.ann.dat', rlow,rhi, area_ann, cnts_ann
readcol, './stats/stats.clusterB.cum.dat', rcum,crap, area_cum, cnts_cum
rann = (rlow+rhi)/2.0
plot, rann, cnts_ann/area_ann,psym=7
g = where(rann gt 100 and rann lt 200)      
bkg = median(cnts_ann[g]/area_ann[g],/even)
;hor, bkg
     
netcnts = cnts_cum - (bkg*area_cum)   ;; subtract scaled background
netcnts_err = (1.0+sqrt(netcnts + 0.75))
plot, rcum, netcnts, psym=7
g = where(rcum ge 100 and rcum lt 180)      
maxcnts = median(netcnts[g])
;hor, maxcnts
ploterror,  rcum*0.5, netcnts, netcnts_err, psym=7, xrange=[0,85],yrange=[0,110],/xsty,/ysty, xtitle='R (arcsec)', ytitle='Counts'
;hor, maxcnts, linestyle=2
;; cnts(r<100) == 209.839, background == 132.014, maxcnts == 76.2763, sig = maxcnts / (1.0+SQRT(0.75+background)) == 6.21495

psopen, 'xgca.clusterB.ps', /landscape
ploterror,  rcum*0.5, netcnts, netcnts_err, psym=7, xrange=[0,85],yrange=[0,110],/xsty,/ysty, xtitle='R (arcsec)', ytitle='Counts', charthick=2, charsize=1.5, xthick=2, ythick=2, thick=2, symsize=1.5,errthick=2
;hor, maxcnts, linestyle=2,thick=2
psclose

end
