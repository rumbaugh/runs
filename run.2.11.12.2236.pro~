 
 readcol, "sources.1662.full+soft+hard.1e6.b1.1-16.wexp20.xsradecsigncnts.hdat", mask, RAf, RAs, RAh, DECf, DECs, DECh, sf, ss, sh, ncnts_f, ncnts_s, ncnts_h, xsxf, xsxs, xsxh, xsyf, xsys, xsyh,  format='I,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D,D'

 sig = dblarr(3,n_elements(ras))
 ra = dblarr(3,n_elements(ras))
 dec = dblarr(3,n_elements(ras))
 ra_out = dblarr(n_elements(ras))
 dec_out = dblarr(n_elements(ras))

 sig[0,*] = sf  &  sig[1,*] = ss  &  sig[2,*] = sh  
 ra[0,*] = raf  &  ra[1,*] = ras  &  ra[2,*] = rah  
 dec[0,*] = decf  &  dec[1,*] = decs  &  dec[2,*] = dech  

 openw, 1, "sources.1662.full+soft+hard.srclist.dat"
 for i=0, n_elements(ras)-1 do begin &$ 
     g = where(sig[*,i] eq max(sig[*,i]))  &$
     ra_out[i] = ra[g,i]  &$
     dec_out[i] = dec[g,i]  &$
     printf,1, ra_out[i], dec_out[i], mask[i], sf[i],ss[i],sh[i], ncnts_f[i], ncnts_s[i], ncnts_h[i], g &$
 endfor
 close, 1
end
