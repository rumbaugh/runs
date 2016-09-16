; IDL script to construct the logN-logS plot for Cl0023

mkct

;; Set counts to flux conversion
;k = 0.0000000000278179021615
k = 0.0000000000278875534235
k2 = 0.0000000000222524348045

;; Set sigma above background to use in constructing logN-logS
sigma = 1.0


;; First get amount of sky covered at a given flux (6932)

rdfloat, "acis7914.img.2000-8000.nops.bin64.dat", x, y, counts
rdfloat, "acis7914.bin64.offaxis_angle.dat", x_theta, y_theta, theta

rdfloat, "/scratch/rumbaugh/Chandra_ORELSE_Notes/psfsize_4.51_90perc.dat", arcsec_offset, perc95_radius
r95a = interpol(perc95_radius, arcsec_offset, theta)
d95a = 2*r95a

rdfloat, "acis7914.expmap_hard.bin64.dat", x_exp, y_exp, exp_map
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
fluxl = 10^(41.7-57)*1.627*0.7^(-2)
flag1 = 0
for i=1L, n_elements(sky_cov)-1 do begin  &$
    farr[i] = farr[i-1] + df  &$
    Nf = n_elements(where(flux_finite le farr[i]))  &$
    if ((flag1 eq 0) and (farr[i] ge fluxl)) then flag1++ &$
    if flag1 eq 1 then skycovt = Nf * pix_area / (3600.0^2.0)  &$ 
    if ((flag1 eq 1)) then flag1++ &$
    sky_cov[i] = Nf * pix_area / (3600.0^2.0)  &$     ; N pixels * pixel area in degrees
endfor

print,skycovt/max(sky_cov)

i = n_elements(sky_cov)-1 
while sky_cov[i] GT 0.1*max(sky_cov) do begin &$
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

;fluxt = j_lim*k
tts = sort(flux_finite)
fluxt = flux_finite[tts[round(n_elements(tts)/2)]]*k
lnlum = alog10(fluxt)+57+alog10(1.627)-2*alog10(0.7)
lum = (lnlum-42)
print,"Limiting Luminosity: " + string(lnlum)

; Plot sky coverage vs flux
;plot, farr*k, sky_cov, /xlog, /ylog,xrange=[3E-15,5E-14],yrange=[0.001,0.5],/xstyle,/ystyle



;; Now construct logN-logS 

; Read in photometery
photcat1 = 'stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat'
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
ploterror, src_flux_sort, N,Nerr, /xlog, /ylog, psym=7,xrange=[3E-15,5E-14],yrange=[30,2000],XTITLE="S (erg s!E-1!N cm!E-2!N)", YTITLE = "N(>S) (deg!E-2!N)", TITLE = "Cl0023 - Hard Band (2-10 keV)",/ysty,/xsty

;; Optional Output
;openw, 1, "src_flux_sort.N_sort.Nerr.Cl0023.hard.lst"
;for i=0, n_elements(N)-1 do printf, 1, src_flux_sort[i], N[i],Nerr[i]
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

oplot, COSMOS_S2, COSMOS_N, PSYM=0,LINESTYLE=5

oplot, limitingX, limitingY, PSYM=0, LINESTYLE=2


end
