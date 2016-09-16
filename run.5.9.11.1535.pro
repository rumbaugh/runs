; IDL script to construct the logN-logS plot for Cl0023

mkct
 
loadct,13
set_plot,'PS'
device,file="/home/rumbaugh/paperstuff/logNlogSplot.combined.hard.paper.5.9.11.ps",/color

;; Set counts to flux conversion
;k = 0.0000000000278179021615
k = 0.0000000000278875534235
k2 = 0.0000000000222524348045

;; Set sigma above background to use in constructing logN-logS
sigma = 3.0


;; First get amount of sky covered at a given flux (6932)

rdfloat, "/scratch/rumbaugh/ciaotesting/Cl0023/7914/acis7914.img.2000-8000.nops.bin64.dat", x, y, counts
rdfloat, "/scratch/rumbaugh/ciaotesting/Cl0023/7914/acis7914.bin64.offaxis_angle.dat", x_theta, y_theta, theta

rdfloat, "/scratch/rumbaugh/Chandra_ORELSE_Notes/psfsize_4.51_90perc.dat", arcsec_offset, perc95_radius
r95a = interpol(perc95_radius, arcsec_offset, theta)
d95a = 2*r95a

rdfloat, "/scratch/rumbaugh/ciaotesting/Cl0023/7914/acis7914.expmap_hard.bin64.dat", x_exp, y_exp, exp_map
EA = exp_map         ; cm^2 * sec
V = max(exp_map) / exp_map
g1a = where(EA gt 0)
g2a = where(finite(V))

; imhead -v LIVETME < acisf06932_img.500-2000.fits
t = 49383.247922195 ; seconds
pix_area = 31.488^2.0      ; arcsec^2

flux = sigma * (1.0+SQRT(0.75 + ((counts/pix_area)*(!PI*r95a^2.0) ))) * V/t     ; / EA
flux_finite = flux(where(finite(flux)))

sky_cov = make_array(10001)
farr = make_array(10001)
farr[0] = 0.00001
fmax =  0.004   ; 
df = (fmax-farr[0])/double(n_elements(sky_cov))
for i=1L, n_elements(sky_cov)-1 do begin  &$
    farr[i] = farr[i-1] + df  &$
    Nf = n_elements(where(flux_finite le farr[i]))  &$
    sky_cov[i] = Nf * pix_area / (3600.0^2.0)  &$     ; N pixels * pixel area in degrees
endfor

i = n_elements(sky_cov)-1 
while sky_cov[i] GT 0.2*max(sky_cov) do begin &$
    i-- &$
endwhile
inds = indgen(n_elements(sky_cov))
i_lim = interpol(sky_cov, inds, i + 0.5)
j_lim = interpol(farr, inds, i + 0.5)
;print, j_lim
;j_lim = farr[i]
limitingX = dindgen(4)
limitingX[0] = j_lim*k
limitingX[1] = j_lim*k
limitingX[2] = j_lim*k
limitingX[3] = j_lim*k
limitingY = dindgen(4)
limitingY[0] = 30
limitingY[1] = 100
limitingY[2] = 1000
limitingY[3] = 2000

; Plot sky coverage vs flux
;plot, farr*k, sky_cov, /xlog, /ylog,xrange=[3E-15,5E-14],yrange=[0.001,0.5],/xstyle,/ystyle



;; Now construct logN-logS 

; Read in photometery
photcat1 = '/scratch/rumbaugh/ciaotesting/Cl0023/7914/stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat'
readcol, photcat1, id_all,ra_all,dec_all,netcnts_corr_all,netcnts_all,counts_all,sig_all,offaxis_all,src_flux_all,wmask_all,wsigf_all,wsigs_all,wsigh_all, format='I,D,D,D,D,D,D,D,D,D,D,D,D'

; Fluxes for sources 30 and 40 are overestimated.  Not sure by how much, so lets just bring it down a little.
; src_flux_all[71] = src_flux_all[71]*0.9
; src_flux_all[87] = src_flux_all[87]*0.9

src_flux_all = src_flux_all*k/k2

g = where(sig_all gt sigma)
print, n_elements(g)
ra = ra_all[g]
dec = dec_all[g]
sig = sig_all[g]
src_flux = src_flux_all[g]
netcnts = netcnts_all[g]  

src_sky_cov = interp1(farr*k,sky_cov,src_flux)
src_sky_cov_inv = 1.0/src_sky_cov 

N = make_array(n_elements(src_flux))
Nerr = make_array(n_elements(src_flux))
src_flux_sort = src_flux[reverse(sort(src_flux))]
src_sky_cov_inv_sort = src_sky_cov_inv[reverse(sort(src_flux))] 

for i=0L, n_elements(src_flux_sort)-1 do begin  &$
    g = where(src_flux_sort ge src_flux_sort[i],count) &$
    if (count gt 0) then N[i] = total(src_sky_cov_inv_sort[g]) &$
    if (count gt 0) then Nerr[i] = sqrt(total(((src_sky_cov_inv_sort[g])^2.0))) &$
;    if (count eq 0) then N[i] = 0 &$
endfor

; Plot logN-logS
; window, 1
;plot, src_flux_sort, N, /xlog, /ylog, psym=7,xrange=[6E-16,2E-14],yrange=[50,2000],/ysty,/xsty
plot, src_flux_sort, N, /xlog, /ylog, psym=7,xrange=[3E-15,5E-14],yrange=[30,2000],XTITLE="S (erg s!E-1!N cm!E-2!N)", YTITLE = "N(>S) (deg!E-2!N)",/ysty,/xsty,SYMSIZE=1,THICK=2,XTHICK=2,YTHICK=2,CHARSIZE=1.6,CHARTHICK=2

;; Optional Output
;openw, 1, "src_flux_sort.N_sort.6932_6933+7343.lst"
;for i=0, n_elements(N)-1 do printf, 1, src_flux_sort[i], N[i]
;close, 1

;Overplot Cosmos Data

COSMOS_S = make_array(4)
COSMOS_S[0] = 10^(-13.0)
COSMOS_S[1] = 10^(-13.5)
COSMOS_S[2] = 10^(-14.0)
COSMOS_S[3] = 10^(-14.3)
COSMOS_N = make_array(4)
COSMOS_N[3] = 600.1
COSMOS_N[2] = 258.9
COSMOS_N[1] = 57.0
COSMOS_N[0] = 8.6


;; NOTE: These COSMOS values are for 2-10 keV and for pow-law slope=1.7
;;       I've noticed going from 1.7 to 1.4 tends to DECREASE k by 6.96%
COSMOS_S2 = COSMOS_S*1.11404

oplot, COSMOS_S2, COSMOS_N, PSYM=0,LINESTYLE=5,THICK=2

;oplot, limitingX, limitingY, PSYM=0, LINESTYLE=2


;; Set counts to flux conversion
k = 0.5*(0.0000000000278030236628+0.0000000000278166819506)
k2 = 0.5*(0.0000000000221956802628+0.0000000000221849856109)

;; Set sigma above background to use in constructing logN-logS
sigma = 3.0

;; First get amount of sky covered at a given flux (6932)
rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1604/master/acis6933+7343.img.2000-8000.nops.bin64.dat", xN, yN, countsN
rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1604/master/acis6933+7343.hard.bin64.offaxis_angle.dat", x_thetaN, y_thetaN, thetaN

;rdfloat,"/scratch/rumbaugh/Chandra_ORELSE_Notes/psfsize_4.51_95perc.dat",
;arcsec_offsetN, perc95_radiusN
rdfloat, "/scratch/rumbaugh/Chandra_ORELSE_Notes/psfsize_4.51_90perc.dat", arcsec_offsetN, perc95_radiusN
r95aN = interpol(perc95_radiusN, arcsec_offsetN, thetaN)

rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1604/master/../6932/acis6932.img.2000-8000.nops.bin64.dat", xS, yS, countsS
rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1604/master/../6932/acis6932.bin64.offaxis_angle.dat", x_thetaS, y_thetaS, thetaS

;rdfloat,"/scratch/rumbaugh/Chandra_ORELSE_Notes/psfsize_4.51_95perc.dat",
;arcsec_offsetS, perc95_radiusS
rdfloat, "/scratch/rumbaugh/Chandra_ORELSE_Notes/psfsize_4.51_90perc.dat", arcsec_offsetS, perc95_radiusS
r95aS = interpol(perc95_radiusS, arcsec_offsetS, thetaS)
d95aS = 2*r95aS

rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1604/master/acis6933+7343.expmap_hard.bin64.dat", x_expN, y_expN, exp_mapN
rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1604/master/../6932/acis6932.expmap_hard.bin64.dat", x_expS, y_expS, exp_mapS
EAS = exp_mapS         ; cm^2 * sec
VS = max(exp_mapS) / exp_mapS
g1aS = where(EAS gt 0)
g2aS = where(finite(VS))
EAN = exp_mapN         ; cm^2 * sec
VN = max(exp_mapN) / exp_mapN
g1aN = where(EAN gt 0)
g2aN = where(finite(VN))


; imhead -v LIVETME < acisf06932_img.2000-8000.fits
tS =  49478.092354796; seconds
tN =  46103.507982594; seconds
pix_area = 31.488^2.0      ; arcsec^2

fluxS = sigma * (1.0+SQRT(0.75 + ((countsS/pix_area)*(!PI*r95aS^2.0) ))) * VS/tS     ; / EA
flux_finiteS = fluxS(where(finite(fluxS)))


fluxN = sigma * (1.0+SQRT(0.75 + ((countsN/pix_area)*(!PI*r95aN^2.0) ))) * VN/tN     ; / EA
flux_finiteN = fluxN(where(finite(fluxN)))

sky_cov = make_array(10001)
farr = make_array(10001)
farr[0] = 0.00001
fmax =  0.004   ; 
df = (fmax-farr[0])/double(n_elements(sky_cov))
for i=1L, n_elements(sky_cov)-1 do begin  &$
    farr[i] = farr[i-1] + df  &$
    Nf = n_elements(where(flux_finiteN le farr[i])) + n_elements(where(flux_finiteS le farr[i]))  &$
    sky_cov[i] = Nf * pix_area / (3600.0^2.0)  &$     ; N pixels * pixel area in degrees
endfor

i = n_elements(sky_cov)-1 
while sky_cov[i] GT 0.2*max(sky_cov) do begin &$
    i-- &$
endwhile
inds = indgen(n_elements(sky_cov))
i_lim = interpol(sky_cov, inds, i + 0.5)
j_lim = interpol(farr, inds, i + 0.5)
;print, j_lim
;j_lim = farr[i]
limitingX = dindgen(4)
limitingX[0] = j_lim*k
limitingX[1] = j_lim*k
limitingX[2] = j_lim*k
limitingX[3] = j_lim*k
limitingY = dindgen(4)
limitingY[0] = 30
limitingY[1] = 100
limitingY[2] = 1000
limitingY[3] = 2000

; Plot sky coverage vs flux
;plot, farr*k, sky_cov, /xlog,xrange=[3E-15,5E-14],yrange=[0.001,0.5],/xstyle

;plot, farr*k, sky_cov, /xlog,/ylog,xrange=[3E-15,5E-14],yrange=[0.0001,0.2],/xstyle,/ystyle



;; Now construct logN-logS 

photcat1 = '/scratch/rumbaugh/ciaotesting/Cl1604/master/stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat'
readcol, photcat1, id_all1,ra_all1,dec_all1,netcnts_corr_all,netcnts_all1,counts_all,sig_all1,offaxis_all,src_flux_all1,wmask_all,wsigf_all,wsigs_all,wsigh_all, format='I,D,D,D,D,D,D,D,D,D,D,D,D'

photcat2 = '/scratch/rumbaugh/ciaotesting/Cl1604/master/../6932/CALDB_PHOT/6932_caldb_phot/hard/stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat'
readcol, photcat2, id_all2,ra_all2,dec_all2,netcnts_corr_all,netcnts_all2,counts_all,sig_all2,offaxis_all,src_flux_all2,wmask_all,wsigf_all,wsigs_all,wsigh_all, format='I,D,D,D,D,D,D,D,D,D,D,D,D'

; Fluxes for sources 30 and 40 are overestimated.  Not sure by how much, so lets just bring it down a little.
; src_flux_all[71] = src_flux_all[71]*0.9
; src_flux_all[87] = src_flux_all[87]*0.9

;fluxes are in 2-8 kev range. Need to extrapolate to 2-10 kev
src_flux_all1 = src_flux_all1*k/k2
src_flux_all2 = src_flux_all2*k/k2

len1 = n_elements(id_all1)
len2 = n_elements(id_all2)
len = len1 + len2
ra_all = dindgen(len)
dec_all = dindgen(len)
netcnts_all = dindgen(len)
sig_all = dindgen(len)
src_flux_all = dindgen(len)
for i = 0L,len-1 do begin
   if i lt len1 then begin
      ra_all[i] = ra_all1[i]
      dec_all[i] = dec_all1[i]
      netcnts_all[i] = netcnts_all1[i]
      sig_all[i] = sig_all1[i]
      src_flux_all[i] = src_flux_all1[i]
   endif else begin
      ra_all[i] = ra_all2[i-len1]
      dec_all[i] = dec_all2[i-len1]
      netcnts_all[i] = netcnts_all2[i-len1]
      sig_all[i] = sig_all2[i-len1]
      src_flux_all[i] = src_flux_all2[i-len1]
   endelse   
endfor


g = where(sig_all gt sigma)
ra = ra_all[g]
dec = dec_all[g]
sig = sig_all[g]
src_flux = src_flux_all[g]
netcnts = netcnts_all[g]  

src_sky_cov = interp1(farr*k,sky_cov,src_flux)
src_sky_cov_inv = 1.0/src_sky_cov 

N = make_array(n_elements(src_flux))
Nerr = make_array(n_elements(src_flux))
src_flux_sort = src_flux[reverse(sort(src_flux))]
src_sky_cov_inv_sort = src_sky_cov_inv[reverse(sort(src_flux))] 

for i=0L, n_elements(src_flux_sort)-1 do begin  &$
    g = where(src_flux_sort ge src_flux_sort[i],count) &$
    if (count gt 0) then N[i] = total(src_sky_cov_inv_sort[g]) &$
    if (count gt 0) then Nerr[i] = sqrt(total(((src_sky_cov_inv_sort[g])^2.0))) &$
;    if (count eq 0) then N[i] = 0 &$
endfor

; Plot logN-logS
; window, 1
;plot, src_flux_sort, N,  psym=7,xrange=[6E-16,2E-14],yrange=[50,2000]
oplot, src_flux_sort, N,  psym=4,color=255,SYMSIZE=1,THICK=2



;; Set counts to flux conversion
k = 0.5*(0.0000000000278290277327+0.000000000027821073278)
k2 = 0.5*(0.0000000000222057351496+0.0000000000221993880176)
;; Set sigma above background to use in constructing logN-logS
sigma = 3.0

;; First get amount of sky covered at a given flux (9404+9836)
rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1324/master/acis9403+9840.img.2000-8000.nops.bin64.dat", xN, yN, countsN
rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1324/master/acis9403+9840.bin64.offaxis_angle.dat", x_thetaN, y_thetaN, thetaN

rdfloat, "/scratch/rumbaugh/Chandra_ORELSE_Notes/psfsize_4.51_90perc.dat", arcsec_offsetN, perc95_radiusN
r95aN = interpol(perc95_radiusN, arcsec_offsetN, thetaN)

rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1324/master/acis9404+9836.img.2000-8000.nops.bin64.dat", xS, yS, countsS
rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1324/master/acis9404+9836.bin64.offaxis_angle.dat", x_thetaS, y_thetaS, thetaS

rdfloat, "/scratch/rumbaugh/Chandra_ORELSE_Notes/psfsize_4.51_90perc.dat", arcsec_offsetS, perc95_radiusS
r95aS = interpol(perc95_radiusS, arcsec_offsetS, thetaS)
d95aS = 2*r95aS

rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1324/master/acis9403+9840.expmap_hard.bin64.dat", x_expN, y_expN, exp_mapN
rdfloat, "/scratch/rumbaugh/ciaotesting/Cl1324/master/acis9404+9836.expmap_hard.bin64.dat", x_expS, y_expS, exp_mapS
EAS = exp_mapS         ; cm^2 * sec
VS = max(exp_mapS) / exp_mapS
g1aS = where(EAS gt 0)
g2aS = where(finite(VS))
EAN = exp_mapN         ; cm^2 * sec
VN = max(exp_mapN) / exp_mapN
g1aN = where(EAN gt 0)
g2aN = where(finite(VN))


; imhead -v LIVETME < acisf09404+9836_img.2000-8000.fits
tS =  49478.092354796; seconds
tN =  46103.507982594; seconds
pix_area = 31.488^2.0      ; arcsec^2

fluxS = sigma * (1.0+SQRT(0.75 + ((countsS/pix_area)*(!PI*r95aS^2.0) ))) * VS/tS     ; / EA
flux_finiteS = fluxS(where(finite(fluxS)))


fluxN = sigma * (1.0+SQRT(0.75 + ((countsN/pix_area)*(!PI*r95aN^2.0) ))) * VN/tN     ; / EA
flux_finiteN = fluxN(where(finite(fluxN)))

sky_cov = make_array(10001)
farr = make_array(10001)
farr[0] = 0.00001
fmax =  0.004   ; 
df = (fmax-farr[0])/double(n_elements(sky_cov))
for i=1L, n_elements(sky_cov)-1 do begin  &$
    farr[i] = farr[i-1] + df  &$
    Nf = n_elements(where(flux_finiteN le farr[i])) + n_elements(where(flux_finiteS le farr[i]))  &$
    sky_cov[i] = Nf * pix_area / (3600.0^2.0)  &$     ; N pixels * pixel area in degrees
endfor

i = n_elements(sky_cov)-1 
while sky_cov[i] GT 0.2*max(sky_cov) do begin &$
    i-- &$
endwhile
inds = indgen(n_elements(sky_cov))
i_lim = interpol(sky_cov, inds, i + 0.5)
j_lim = interpol(farr, inds, i + 0.5)
;print, j_lim
;j_lim = farr[i]
limitingX = dindgen(4)
limitingX[0] = j_lim*k
limitingX[1] = j_lim*k
limitingX[2] = j_lim*k
limitingX[3] = j_lim*k
limitingY = dindgen(4)
limitingY[0] = 30
limitingY[1] = 100
limitingY[2] = 1000
limitingY[3] = 2000
; Plot sky coverage vs flux
;plot, farr*k, sky_cov, xrange=[1e-16,5.5e-15],yrange=[0.001,0.5],/xstyle,/ystyle



;; Now construct logN-logS 

photcat1 = '/scratch/rumbaugh/ciaotesting/Cl1324/master/CALDB_PHOT/9403+9840_caldb_phot/hard/stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat'
readcol, photcat1, id_all1,ra_all1,dec_all1,netcnts_corr_all,netcnts_all1,counts_all,sig_all1,offaxis_all,src_flux_all1,wmask_all,wsigf_all,wsigs_all,wsigh_all, format='I,D,D,D,D,D,D,D,D,D,D,D,D,D'
;readcol, photcat1, id_all1,ra_all1,dec_all1,netcnts_corr_all,netcnts_all1,counts_all,sig_all1,offaxis_all,src_flux_all1,wmask_all,wflag_all,wsigf_all,wsigs_all,wsigh_all, format='I,D,D,D,D,D,D,D,D,D,D,D,D,D,D'

photcat2 = '/scratch/rumbaugh/ciaotesting/Cl1324/master/CALDB_PHOT/9404+9836_caldb_phot/hard/stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat'
readcol, photcat2, id_all2,ra_all2,dec_all2,netcnts_corr_all,netcnts_all2,counts_all,sig_all2,offaxis_all,src_flux_all2,wmask_all,wsigf_all,wsigs_all,wsigh_all, format='I,D,D,D,D,D,D,D,D,D,D,D,D,D'
;readcol, photcat2, id_all2,ra_all2,dec_all2,netcnts_corr_all,netcnts_all2,counts_all,sig_all2,offaxis_all,src_flux_all2,wmask_all,wflag_all,wsigf_all,wsigs_all,wsigh_all, format='I,D,D,D,D,D,D,D,D,D,D,D,D,D,D'

; Fluxes for sources 30 and 40 are overestimated.  Not sure by how much, so lets just bring it down a little.
; src_flux_all[71] = src_flux_all[71]*0.9
; src_flux_all[87] = src_flux_all[87]*0.9
src_flux_all1 = src_flux_all1*k/k2
src_flux_all2 = src_flux_all2*k/k2


len1 = n_elements(id_all1)
len2 = n_elements(id_all2)
len = len1 + len2
ra_all = dindgen(len)
dec_all = dindgen(len)
netcnts_all = dindgen(len)
sig_all = dindgen(len)
src_flux_all = dindgen(len)
for i = 0L,len-1 do begin
   if i lt len1 then begin
      ra_all[i] = ra_all1[i]
      dec_all[i] = dec_all1[i]
      netcnts_all[i] = netcnts_all1[i]
      sig_all[i] = sig_all1[i]
      src_flux_all[i] = src_flux_all1[i]
   endif else begin
      ra_all[i] = ra_all2[i-len1]
      dec_all[i] = dec_all2[i-len1]
      netcnts_all[i] = netcnts_all2[i-len1]
      sig_all[i] = sig_all2[i-len1]
      src_flux_all[i] = src_flux_all2[i-len1]
   endelse   
endfor


g = where(sig_all gt sigma)
ra = ra_all[g]
dec = dec_all[g]
sig = sig_all[g]
src_flux = src_flux_all[g]
netcnts = netcnts_all[g]  

src_sky_cov = interp1(farr*k,sky_cov,src_flux)
src_sky_cov_inv = 1.0/src_sky_cov 

N = make_array(n_elements(src_flux))
Nerr = make_array(n_elements(src_flux))
src_flux_sort = src_flux[reverse(sort(src_flux))]
src_sky_cov_inv_sort = src_sky_cov_inv[reverse(sort(src_flux))] 

for i=0L, n_elements(src_flux_sort)-1 do begin  &$
    g = where(src_flux_sort ge src_flux_sort[i],count) &$
    if (count gt 0) then N[i] = total(src_sky_cov_inv_sort[g]) &$
    if (count gt 0) then Nerr[i] = sqrt(total(((src_sky_cov_inv_sort[g])^2.0))) &$
;    if (count eq 0) then N[i] = 0 &$
endfor

; Plot logN-logS
; window, 1
;plot, src_flux_sort, N,  psym=7,xrange=[6E-16,2E-14],yrange=[50,2000]
oplot, src_flux_sort, N,  psym=2,color=60,SYMSIZE=1,THICK=2



;; Set counts to flux conversion
k = 0.0000000000279176013033
k2 = 0.0000000000222764110378

;; Set sigma above background to use in constructing logN-logS
sigma = 3.0


;; First get amount of sky covered at a given flux (6932)

rdfloat, "/scratch/rumbaugh/ciaotesting/NEP5281/master/acis10444+10924.img.2000-8000.nops.bin64.dat", x, y, counts
rdfloat, "/scratch/rumbaugh/ciaotesting/NEP5281/master/acis10444+10924.bin64.offaxis_angle.dat", x_theta, y_theta, theta

rdfloat, "/scratch/rumbaugh/Chandra_ORELSE_Notes/psfsize_4.51_90perc.dat", arcsec_offset, perc95_radius
r95a = interpol(perc95_radius, arcsec_offset, theta)
d95a = 2*r95a

rdfloat, "/scratch/rumbaugh/ciaotesting/NEP5281/master/acis10444+10924.expmap_hard.bin64.dat", x_exp, y_exp, exp_map
EA = exp_map         ; cm^2 * sec
V = max(exp_map) / exp_map
g1a = where(EA gt 0)
g2a = where(finite(V))

; imhead -v LIVETME < acisf06932_img.500-2000.fits
t = 49548.501183658  ; seconds
pix_area = 31.488^2.0      ; arcsec^2

flux = sigma * (1.0+SQRT(0.75 + ((counts/pix_area)*(!PI*r95a^2.0) ))) * V/t     ; / EA
flux_finite = flux(where(finite(flux)))

sky_cov = make_array(10001)
farr = make_array(10001)
farr[0] = 0.00001
fmax =  0.004   ; 
df = (fmax-farr[0])/double(n_elements(sky_cov))
for i=1L, n_elements(sky_cov)-1 do begin  &$
    farr[i] = farr[i-1] + df  &$
    Nf = n_elements(where(flux_finite le farr[i]))  &$
    sky_cov[i] = Nf * pix_area / (3600.0^2.0)  &$     ; N pixels * pixel area in degrees
endfor

i = n_elements(sky_cov)-1 
while sky_cov[i] GT 0.2*max(sky_cov) do begin &$
    i-- &$
endwhile
inds = indgen(n_elements(sky_cov))
i_lim = interpol(sky_cov, inds, i + 0.5)
j_lim = interpol(farr, inds, i + 0.5)
;print, j_lim
;j_lim = farr[i]
limitingX = dindgen(4)
limitingX[0] = j_lim*k
limitingX[1] = j_lim*k
limitingX[2] = j_lim*k
limitingX[3] = j_lim*k
limitingY = dindgen(4)
limitingY[0] = 30
limitingY[1] = 100
limitingY[2] = 1000
limitingY[3] = 2000
; Plot sky coverage vs flux
;plot, farr*k, sky_cov, xrange=[1e-16,5.5e-15],yrange=[0.001,0.5],/xstyle,/ystyle



;; Now construct logN-logS 

; Read in photometery
photcat1 = '/scratch/rumbaugh/ciaotesting/NEP5281/master/stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat'
;readcol, photcat1, id_all,ra_all,dec_all,netcnts_corr_all,netcnts_all,counts_all,sig_all,offaxis_all,src_flux_all,wmask_all,wflag_all,wsigf_all,wsigs_all,wsigh_all, format='I,D,D,D,D,D,D,D,D,D,D,D,D,D,D'
readcol, photcat1, id_all,ra_all,dec_all,netcnts_corr_all,netcnts_all,counts_all,sig_all,offaxis_all,src_flux_all,wmask_all,wsigf_all,wsigs_all,wsigh_all, format='I,D,D,D,D,D,D,D,D,D,D,D,D'

; Fluxes for sources 30 and 40 are overestimated.  Not sure by how much, so lets just bring it down a little.
; src_flux_all[71] = src_flux_all[71]*0.9
; src_flux_all[87] = src_flux_all[87]*0.9

src_flux_all = src_flux_all*k/k2
g = where(sig_all gt sigma)
ra = ra_all[g]
dec = dec_all[g]
sig = sig_all[g]
src_flux = src_flux_all[g]
netcnts = netcnts_all[g]  

src_sky_cov = interp1(farr*k,sky_cov,src_flux)
src_sky_cov_inv = 1.0/src_sky_cov 

N = make_array(n_elements(src_flux))
Nerr = make_array(n_elements(src_flux))
src_flux_sort = src_flux[reverse(sort(src_flux))]
src_sky_cov_inv_sort = src_sky_cov_inv[reverse(sort(src_flux))] 

for i=0L, n_elements(src_flux_sort)-1 do begin  &$
    g = where(src_flux_sort ge src_flux_sort[i],count) &$
    if (count gt 0) then N[i] = total(src_sky_cov_inv_sort[g]) &$
    if (count gt 0) then Nerr[i] = sqrt(total(((src_sky_cov_inv_sort[g])^2.0))) &$
;    if (count eq 0) then N[i] = 0 &$
endfor

; Plot logN-logS
; window, 1
;plot, src_flux_sort, N,  psym=7,xrange=[6E-16,2E-14],yrange=[50,2000]
oplot, src_flux_sort, N,  psym=5,color=100,SYMSIZE=1,THICK=2


;; Set counts to flux conversion
k = 0.0000000000277963945676
k2 = 0.0000000000221796960286

;; Set sigma above background to use in constructing logN-logS
sigma = 3.0


;; First get amount of sky covered at a given flux (6932)

rdfloat, "/scratch/rumbaugh/ciaotesting/RXJ1757/master/RXJ1757.img.2000-8000.nops.bin64.dat", x, y, counts
rdfloat, "/scratch/rumbaugh/ciaotesting/RXJ1757/master/RXJ1757.bin64.offaxis_angle.dat", x_theta, y_theta, theta

rdfloat, "/scratch/rumbaugh/Chandra_ORELSE_Notes/psfsize_4.51_90perc.dat", arcsec_offset, perc95_radius
r95a = interpol(perc95_radius, arcsec_offset, theta)
d95a = 2*r95a

rdfloat, "/scratch/rumbaugh/ciaotesting/RXJ1757/master/RXJ1757.expmap_hard.bin64.dat", x_exp, y_exp, exp_map
EA = exp_map         ; cm^2 * sec
V = max(exp_map) / exp_map
g1a = where(EA gt 0)
g2a = where(finite(V))

; imhead -v LIVETME < acisf06932_img.500-2000.fits
t = 46451.792387024  ; seconds
pix_area = 31.488^2.0      ; arcsec^2

flux = sigma * (1.0+SQRT(0.75 + ((counts/pix_area)*(!PI*r95a^2.0) ))) * V/t     ; / EA
flux_finite = flux(where(finite(flux)))

sky_cov = make_array(10001)
farr = make_array(10001)
farr[0] = 0.00001
fmax =  0.004   ; 
df = (fmax-farr[0])/double(n_elements(sky_cov))
for i=1L, n_elements(sky_cov)-1 do begin  &$
    farr[i] = farr[i-1] + df  &$
    Nf = n_elements(where(flux_finite le farr[i]))  &$
    sky_cov[i] = Nf * pix_area / (3600.0^2.0)  &$     ; N pixels * pixel area in degrees
endfor

i = n_elements(sky_cov)-1 
while sky_cov[i] GT 0.2*max(sky_cov) do begin &$
    i-- &$
endwhile
inds = indgen(n_elements(sky_cov))
i_lim = interpol(sky_cov, inds, i + 0.5)
j_lim = interpol(farr, inds, i + 0.5)
;print, j_lim
;j_lim = farr[i]
limitingX = dindgen(4)
limitingX[0] = j_lim*k
limitingX[1] = j_lim*k
limitingX[2] = j_lim*k
limitingX[3] = j_lim*k
limitingY = dindgen(4)
limitingY[0] = 205
limitingY[1] = 500
limitingY[2] = 1000
limitingY[3] = 2000
; Plot sky coverage vs flux
;plot, farr*k, sky_cov, xrange=[1e-16,5.5e-15],yrange=[0.001,0.5],/xstyle,/ystyle



;; Now construct logN-logS 

; Read in photometery
photcat1 = '/scratch/rumbaugh/ciaotesting/RXJ1757/master/CALDB_PHOT/RXJ1757_caldb_phot/hard/stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat'
readcol, photcat1, id_all,ra_all,dec_all,netcnts_corr_all,netcnts_all,counts_all,sig_all,offaxis_all,src_flux_all,wmask_all,wflag_all,wsigf_all,wsigs_all,wsigh_all, format='I,D,D,D,D,D,D,D,D,D,D,D,D,D,D'

; Fluxes for sources 30 and 40 are overestimated.  Not sure by how much, so lets just bring it down a little.
; src_flux_all[71] = src_flux_all[71]*0.9
; src_flux_all[87] = src_flux_all[87]*0.9

src_flux_all = src_flux_all*k/k2
g = where(sig_all gt sigma)
ra = ra_all[g]
dec = dec_all[g]
sig = sig_all[g]
src_flux = src_flux_all[g]
netcnts = netcnts_all[g]  

src_sky_cov = interp1(farr*k,sky_cov,src_flux)
src_sky_cov_inv = 1.0/src_sky_cov 

N = make_array(n_elements(src_flux))
Nerr = make_array(n_elements(src_flux))
src_flux_sort = src_flux[reverse(sort(src_flux))]
src_sky_cov_inv_sort = src_sky_cov_inv[reverse(sort(src_flux))] 

for i=0L, n_elements(src_flux_sort)-1 do begin  &$
    g = where(src_flux_sort ge src_flux_sort[i],count) &$
    if (count gt 0) then N[i] = total(src_sky_cov_inv_sort[g]) &$
    if (count gt 0) then Nerr[i] = sqrt(total(((src_sky_cov_inv_sort[g])^2.0))) &$
;    if (count eq 0) then N[i] = 0 &$
endfor

; Plot logN-logS
; window, 1
;plot, src_flux_sort, N,  psym=7,xrange=[6E-16,2E-14],yrange=[50,2000]
oplot, src_flux_sort, N,  psym=6,color=160,SYMSIZE=1,THICK=2

;for q=0L,n_elements(N)-1 do print,N[q],src_flux_sort[q]

rdfloat,"/home/rumbaugh/CDF/src_flux_sort.N_sort.Nerr.2232_582.hard.lst",CDFflux,CDFN,CDFNerr

oplot,limitingX,limitingY,linestyle=1
oplot,CDFflux,CDFN,linestyle=2,THICK=3

legend,['Cl0023','Cl1604','Cl1324','NEP200','NEP5281'],PSYM=[7,4,2,6,5],color=[0,255,60,160,100],SYMSIZE=[1.8,1.8,1.8,1.8,1.8],THICK=[2.2,2.2,2.2,2.2,2.2],CHARSIZE=1.6,CHARTHICK=2,/bottom,box=0

end
