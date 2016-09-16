import os
import sys
import numpy as np
import random as rand
import math as m
import time

start_time = time.time()

try:
	skip_setup
except NameError:
	skip_setup = 0
try:
	write_setup
except NameError:
	write_setup = 0

try:
	reps
except NameError:
	reps = 10

try: 
	Ra_aim
except NameError:
	Ra_aim = 137.66683284689
try:
	Dec_aim
except NameError:
	Dec_aim = 54.332598333638


try:
	ra_opt_cen
except NameError:
	ra_opt_cen = Ra_aim
try:
	dec_opt_cen
except NameError:
	dec_opt_cen = Dec_aim

try:
	optical_cat
except NameError:
	optical_cat = "/mnt/data2/rumbaugh/dump/ORELSE/opt_cats/cl0910.LFC.IDradecnmags.cat"

radio_cat = ""
try:
	xray_cat
except NameError:
	xray_cat = "/mnt/data2/rumbaugh/dump/ChandraData/0910/master/photometry/2227+2452.xray_phot.soft_hard_full.dat"

try:
	matching_dir
except NameError:
	matching_dir = "/mnt/data2/rumbaugh/dump/ChandraData/0910/master/opt_match"
try:
	reg_dir
except NameError:
	reg_dir = matching_dir + "/regions"

try:
	ra_opt_cen
except NameError:
	ra_opt_cen = Ra_aim
try:
	dec_opt_cen
except NameError:
	dec_opt_cen = Dec_aim
try:
	radius_opt_cen
except NameError:
	radius_opt_cen = 0.2*3600
area_opt_cen = m.pi*(radius_opt_cen**2)

try:
	output_file
except NameError:
	output_file = matching_dir + "/opt_Xray_matched_catalog_3high.twk.dat"
try:
	out_reg
except NameError:
	out_reg = reg_dir + "/matched_3high.twk.reg"

try:
	prob_thresh
except NameError:
	prob_thresh = 0.15

try: 
	minsrchrad
except NameError:
	minsrchrad = 5.0

def SphDist(RAi,Deci,Raf,Decf):
	#Distance in arcminutes
	dist = 2.0*m.asin(m.sqrt((m.sin(0.5*m.pi*(Decf-Deci)/180))**2+m.cos(m.pi*Decf/180.0)*m.cos(m.pi*Deci/180.0)*(m.sin(0.5*m.pi*(Raf-RAi)/180))**2))
	dist *= 180.0*60/m.pi
	return dist

def OffAxis1324(ra,dec):
	#Determines if source is in North or South pointing in 1324 and finds off axis angle
	if dec > 30.67:
		dist = SphDist(ra,dec,201.20389190325,30.86373172217)
	else:
		dist = SphDist(ra,dec,201.17495829431,30.279328719557)
	return dist

def FindCloseSources(ra,dec,tol,ra_opt,dec_opt,usemin):
	if (tol < 1.5): tol = 1.5
	if ((tol < minsrchrad) & (usemin > 0.1)): tol = minsrchrad
	tolx = tol/m.cos(dec*m.pi/180.0)
	ra_box_temp_ind1 = np.where((ra_opt >= ra-tolx/3600.0) & (ra_opt <= ra+tolx/3600.0))
	if len(ra_box_temp_ind1) > 0: 
		ra_box_temp_ind1 = ra_box_temp_ind1[0]
		ra_box_temp1 = ra_opt[ra_box_temp_ind1]
		dec_box_temp1 = dec_opt[ra_box_temp_ind1]
		dec_box_temp_ind2 = np.where((dec_box_temp1 >= dec-tol/3600.0) & (dec_box_temp1 <= dec+tol/3600.0))
		if len(dec_box_temp_ind2) > 0:
			dec_box_temp_ind2 = dec_box_temp_ind2[0]
			dec_box_temp3 = dec_box_temp1[dec_box_temp_ind2]
			ra_box_temp3 = ra_box_temp1[dec_box_temp_ind2]
			temp_dist_ar = np.zeros(len(dec_box_temp3))
			for i in range(0L,len(temp_dist_ar)):
				temp_dist_ar[i] = SphDist(ra_box_temp3[i],dec_box_temp3[i],ra,dec)
			inside_tol_ind = np.where(temp_dist_ar*60.0 <= tol)
			if len(inside_tol_ind) > 0: 
				inside_tol_ind = inside_tol_ind[0]
				return ra_box_temp_ind1[[dec_box_temp_ind2[inside_tol_ind]]]
			else:
				return np.zeros(0)
		else:
			return np.zeros(0)
	else:
		return np.zeros(0)

def OptMatch(raX,decX,d_xerr,ra_opt,dec_opt,usemin):
	close_ind = FindCloseSources(raX,decX,d_xerr,ra_opt,dec_opt,usemin)
	if len(close_ind) > 0:
		ra_close = ra_opt[close_ind]
		dec_close = dec_opt[close_ind]
		magI_close = magI_opt[close_ind]
		numdens_close = loc_num_dens_gtMag[close_ind]
		close_likelihoods = np.zeros(len(close_ind))
		close_dist = np.zeros(len(close_ind))
		for j in range(0L,len(close_ind)):
			close_dist[j] = 60*SphDist(raX,decX,ra_close[j],dec_close[j])
			close_likelihoods[j] = m.exp(-0.5*(close_dist[j]**2)/(d_xerr**2))/(d_xerr**2.0*m.sqrt(numdens_close[j]))
#			print close_dist,d_xerr,numdens_close,close_likelihoods
#		print close_likelihoods
		return close_likelihoods,close_ind
	else:	
		return np.zeros(0),np.zeros(0)
	
def MonteCarlo(reps,ra_UB,ra_LB,dec_UB,dec_LB,err,ra_opt,dec_opt,usemin):
	rand.seed()
	output = np.zeros(0)
	for i in range(0L,reps):
		rand.seed()
		rand1 = rand.random()
		rand2 = rand.random()
		ra_rand = (ra_UB-ra_LB)*rand1 + ra_LB
		dec_rand = (dec_UB-dec_LB)*rand2 + dec_LB
		likelihoods,like_inds = OptMatch(ra_rand,dec_rand,err,ra_opt,dec_opt,usemin)
		output = np.append(output,likelihoods)
	return output

#X-Ray
cr_xray = np.loadtxt(xray_cat)
# openw, 1, 'Cl0023.xray_phot.soft_hard_full.dat'
# for i=0, n_elements(ra)-1 do printf,1, ra[i], dec[i], flux_softz[i], flux_hardz[i], flux_fullz[i],  netcnts_corr_softz[i], netcnts_corr_hardz[i], netcnts_corr_fullz[i], sig_soft[i], sig_hard[i], sig_full[i], wsig_soft[i], wsig_hard[i], wsig_full[i], wmask[i], wflag[i],format='(1(G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",I," ",I," "))'
# close, 1
raX = cr_xray[:,0]
decX = cr_xray[:,1]

netcnts_corrX_soft = cr_xray[:,5]
netcnts_corrX_hard = cr_xray[:,6]
netcnts_corrX_full = cr_xray[:,7]
wflagX = cr_xray[:,15]

ncnts_corrX = np.zeros((3,len(raX)))
ncnts_corrX[0][:] = netcnts_corrX_soft[:]
ncnts_corrX[1][:] = netcnts_corrX_hard[:]
ncnts_corrX[2][:] = netcnts_corrX_full[:]

off_axisX = np.zeros(len(raX))

if skip_setup == 0:
	xwnetcnts = np.zeros(len(raX))
	for i in range(0L,len(raX)):
#	off_axisX[i] = SphDist(Ra_aim,Dec_aim,raX[i],decX[i])
		off_axisX[i] = SphDist(raX[i],decX[i],Ra_aim,Dec_aim)
		xwnetcnts[i] = ncnts_corrX[int(wflagX[i])][i]
		#if xwnetcnts[i] <= 0: print ncnts_corrX[:,i]
		if ((xwnetcnts[i] <= 0) & (ncnts_corrX[2][i] > 0)): 
			xwnetcnts[i] = ncnts_corrX[2][i]

cr_opt = np.loadtxt(optical_cat)
ra_opt = cr_opt[:,1]
dec_opt = cr_opt[:,2]
magI_opt = cr_opt[:,4]
newid_opt = cr_opt[:,0]

# Calculate errors

#Get source densities
if skip_setup == 0:
	d_xerr = np.zeros(len(raX))
	for i in range(0L,len(raX)):
		if xwnetcnts[i] > 0.0:
			if xwnetcnts[i] <= 137.816: d_xerr[i] = 10**(0.1145*off_axisX[i] - 0.4958*m.log10(xwnetcnts[i])+0.1932)
			if xwnetcnts[i] > 137.816: d_xerr[i] = 10**(((0.0968*off_axisX[i] - 0.2064*m.log10(xwnetcnts[i])-0.4260)))
			if off_axisX[i] >= 15.0: d_xerr[i] = 60.0   # Upper limit is 1'
		else:
			print xwnetcnts[i]
			d_xerr[i] = 60.0
		if d_xerr[i] < 1.5: d_xerr[i] = 1.5
	d_fromoptcen = np.zeros(len(ra_opt))
	for i in range(0L,len(ra_opt)):
		d_fromoptcen[i] = 60*SphDist(ra_opt[i],dec_opt[i],ra_opt_cen,dec_opt_cen)

	loc_num_dens_gtMag = np.zeros(len(ra_opt))
	for i in range(0L,len(ra_opt)):
		ind_local = np.where(d_fromoptcen <= radius_opt_cen)
		ind_local = ind_local[0]
		magI_loc = magI_opt[ind_local]
		ind_lemagI = np.where(magI_loc <= magI_opt[i])
		ind_lemagI = ind_lemagI[0]
		num_gt_limit = len(ind_lemagI)
		loc_num_dens_gtMag[i] = num_gt_limit/area_opt_cen

#Optical Matching

matched_raX = np.zeros(len(raX))
matched_decX = np.zeros(len(raX))
matched_errX = np.zeros(len(raX))
matched_indX = np.zeros(len(raX))
matched_num_matches = np.zeros(len(raX))
matched_dec_opt1 = np.zeros(len(raX))
matched_dec_opt2 = np.zeros(len(raX))
matched_dec_opt3 = np.zeros(len(raX))
matched_ra_opt1 = np.zeros(len(raX))
matched_ra_opt2 = np.zeros(len(raX))
matched_ra_opt3 = np.zeros(len(raX))
matched_ind_opt1 = np.zeros(len(raX))
matched_ind_opt2 = np.zeros(len(raX))
matched_ind_opt3 = np.zeros(len(raX))
matched_prob_opt1 = np.zeros(len(raX))
matched_prob_opt2 = np.zeros(len(raX))
matched_prob_opt3 = np.zeros(len(raX))
matched_like_opt1 = np.zeros(len(raX))
matched_like_opt2 = np.zeros(len(raX))
matched_like_opt3 = np.zeros(len(raX))
matched_like_opt1.fill(-1)
matched_like_opt2.fill(-1)
matched_like_opt3.fill(-1)
matched_dec_opt1.fill(-1)
matched_dec_opt2.fill(-1)
matched_dec_opt3.fill(-1)
matched_ra_opt1.fill(-1)
matched_ra_opt2.fill(-1)
matched_ra_opt3.fill(-1)
matched_ind_opt1.fill(-1)
matched_ind_opt2.fill(-1)
matched_ind_opt3.fill(-1)
matched_prob_opt1.fill(-1)
matched_prob_opt2.fill(-1)
matched_prob_opt3.fill(-1)
matched_prob_none = np.zeros(len(raX))
unmatched_raX = np.zeros(0)
unmatched_decX = np.zeros(0)
unmatched_errX = np.zeros(0)
unmatched_indX = np.zeros(0)
unmatched_prob = np.zeros(0)

if skip_setup != 0:
	cr_info = np.loadtxt(matching_dir + "/temp/info.txt")
	info_col = cr_info[:,0]
	ttcnt = int(info_col[0])
	cr_xraysetup = read_file(matching_dir + "/temp/xray_setup.txt")
	off_axisX = cr_xraysetup[:,0]
	xwnetcnts = cr_xraysetup[:,1]
	d_xerr = cr_xraysetup[:,2]
	d_fromoptcen = np.zeros(0)
	loc_num_dens_gtMag = np.zeros(0)
	for i in range(0,ttcnt):
		cr_optsetup = np.loadtxt(matching_dir + "/temp/opt_setup." + str(i+1) + "0000.txt")
		d_fromoptcen_temp = cr_optsetup[:,0]
		loc_num_dens_gtMag_temp = cr_optsetup[:,1]
		d_fromoptcen = np.append(d_fromoptcen,d_fromoptcen_temp)
		loc_num_dens_gtMag = np.append(loc_num_dens_gtMag,loc_num_dens_gtMag_temp)

if write_setup != 0:
	wcnt = 0L
	ttcnt = 0
	while wcnt < len(ra_opt):
		ttcnt += 1
		FILE = open(matching_dir + "/temp/opt_setup." + str(ttcnt) + "0000.txt","w")
		n = 0
		while ((wcnt < len(ra_opt)) and (n < 10000)):
			FILE.write(str(d_fromoptcen[wcnt]) + " " + str(loc_num_dens_gtMag[wcnt]) + "\n")
			n += 1
			wcnt += 1
		FILE.close()
	FILE = open(matching_dir + "/temp/info.txt","w")
	FILE.write(str(ttcnt))
	FILE.close()
	FILE = open(matching_dir + "/temp/xray_setup.txt","w")
	for i in range(0L,len(raX)):
		FILE.write(str(off_axisX[i]) + " " + str(xwnetcnts[i]) + " " + str(d_xerr[i]) + "\n")
	FILE.close()

ra_UB = np.max(raX)
ra_LB = np.min(raX)
dec_UB = np.max(decX)
dec_LB = np.min(decX)

setup_time = time.time()-start_time
print "Setup took " + str(setup_time) + " seconds."
for usemin in range(0,2):
	for i in range(0L,len(raX)):
		if i == 1:
			MC_time = time.time()-start_time-setup_time
			print "One source with MC run took " + str(MC_time) + " seconds."
			print str(int(len(raX))) + " sources to match. ETA: " + str(int(MC_time*(len(raX) - 1))) + " seconds."
		if i == int(len(raX)/4.0):
			quarter_time = time.time()-start_time-setup_time
			print "25% done - ETA: " + str(int(3*quarter_time)) + " seconds."
		if i == int(len(raX)/2.0):
		       	half_time = time.time()-start_time-setup_time
			print "50% done - ETA: " + str(int(half_time)) + " seconds."
		if i == int(3*len(raX)/4.0):
			quarter_time = time.time()-start_time-setup_time
			print "75% done - ETA: " + str(int(quarter_time/3.0)) + " seconds."
		likelihoods,like_inds = OptMatch(raX[i],decX[i],d_xerr[i],ra_opt,dec_opt,usemin)
		num_matches = len(likelihoods)
		reliability_ij = np.zeros(len(likelihoods))
		if ((len(likelihoods) > 0)):
			rel_ref = MonteCarlo(reps,ra_UB,ra_LB,dec_UB,dec_LB,d_xerr[i],ra_opt,dec_opt,usemin)
		else:
			rel_ref = np.zeros(0)
		for j in range(0L,len(likelihoods)):
			MC_temp = np.where(rel_ref >= likelihoods[j])
			if len(MC_temp) > 0: MC_temp = MC_temp[0]
			rel_cnt = len(MC_temp)
			reliability_ij[j] = 1.0 - (rel_cnt*1.0)/reps
			if reliability_ij[j] < 0: reliability_ij[j] = 0.0
	#print reliability_ij
		probability_ij = np.zeros(len(likelihoods))
		for j in range(0L,len(likelihoods)):
			probability_ij[j] = reliability_ij[j]
			for k in range(0L,len(likelihoods)):
				if k != j: probability_ij[j] *= (1-reliability_ij[k])
		probability_nonej = 1.0
		for j in range(0L,len(likelihoods)): probability_nonej *= (1-reliability_ij[j])
		prob_sum = probability_nonej + np.sum(probability_ij)
		if prob_sum >= 0: 
			probability_ij /= prob_sum
			probability_nonej /= prob_sum
		else:
			probability_nonej = 1.0
	#print probability_ij, probability_nonej
		matched_raX[i] = raX[i]
		matched_decX[i] = decX[i]
		matched_errX[i] = d_xerr[i]
		matched_indX[i] = i
		matched_prob_none[i] = probability_nonej
		if num_matches == 1:
			matched_ra_opt1[i] = ra_opt[like_inds[0]]
			matched_dec_opt1[i] = dec_opt[like_inds[0]]
			matched_prob_opt1[i] = 1-probability_nonej
			matched_ind_opt1[i] = like_inds[0]
			matched_like_opt1[i] = likelihoods[0]
			if probability_nonej <= prob_thresh: 
				matched_num_matches[i] = 1
			else:
				unmatched_raX = np.append(unmatched_raX,raX[i])
				unmatched_decX = np.append(unmatched_decX,decX[i])
				unmatched_errX = np.append(unmatched_errX,d_xerr[i])
				unmatched_indX = np.append(unmatched_indX,i)
				unmatched_prob = np.append(unmatched_prob,probability_nonej)
				matched_num_matches[i] = 0
		if num_matches > 1:
			opt_matched_temp_ind = np.argsort(-1*likelihoods)
		#print likelihoods
		#print opt_matched_temp_ind
			q = 0
			opt_matched_ra_temp = np.array([-1.0,-1.0,-1.0])
			opt_matched_dec_temp = np.array([-1.0,-1.0,-1.0])
			opt_matched_prob_temp = np.array([-1.0,-1.0,-1.0])
			opt_matched_ind_temp = np.array([-1.0,-1.0,-1.0])
			opt_matched_like_temp = np.array([-1.0,-1.0,-1.0])
			while ((q < 3) and (q < len(opt_matched_temp_ind))):
				opt_matched_ra_temp[q] = ra_opt[like_inds[opt_matched_temp_ind[q]]]
				opt_matched_dec_temp[q] = dec_opt[like_inds[opt_matched_temp_ind[q]]]
				opt_matched_ind_temp[q] = like_inds[opt_matched_temp_ind[q]]
				opt_matched_prob_temp[q] = probability_ij[opt_matched_temp_ind[q]]
				opt_matched_like_temp[q] = likelihoods[opt_matched_temp_ind[q]]
				q += 1
			matched_ra_opt1[i] = opt_matched_ra_temp[0]
			matched_dec_opt1[i] = opt_matched_dec_temp[0]	
			matched_prob_opt1[i] = opt_matched_prob_temp[0]
			matched_ind_opt1[i] = opt_matched_ind_temp[0]
			matched_like_opt1[i] = opt_matched_like_temp[0]
			matched_ra_opt2[i] = opt_matched_ra_temp[1]
			matched_dec_opt2[i] = opt_matched_dec_temp[1]	
			matched_prob_opt2[i] = opt_matched_prob_temp[1]
			matched_ind_opt2[i] = opt_matched_ind_temp[1]
			matched_like_opt2[i] = opt_matched_like_temp[1]
			matched_ra_opt3[i] = opt_matched_ra_temp[2]
			matched_dec_opt3[i] = opt_matched_dec_temp[2]	
			matched_prob_opt3[i] = opt_matched_prob_temp[2]
			matched_ind_opt3[i] = opt_matched_ind_temp[2]
			matched_like_opt3[i] = opt_matched_like_temp[2]
			if probability_nonej <= prob_thresh:
				prob_probe_temp = np.zeros(num_matches)
				for k in range(0L,num_matches):
					prob_probe_temp = probability_ij[k]/(1 - probability_nonej - probability_ij[k])
				cand_temp_ind = np.where(prob_probe_temp >= 4.0)
				if len(cand_temp_ind) > 0: cand_temp_ind = cand_temp_ind[0]
				if len(cand_temp_ind) > 1: sys.exit("Probabilities don't sum to 1")
				if len(cand_temp_ind) == 1:
					matched_num_matches[i] = 1
				if len(cand_temp_ind) == 0:
					if num_matches < 1: sys.exit("Inconsistency: 001")
					test_sig_cands_ind = np.where(probability_ij >= 0.2)
					if len(test_sig_cands_ind) > 0: test_sig_cands_ind = test_sig_cands_ind[0]
					if len(test_sig_cands_ind) > 3: 
                                            test_sig_cands_ind = test_sig_cands_ind[np.argsort(probability_ij[test_sig_cands_ind])[len(test_sig_cands_ind)-3:]]
                                            #sys.exit("More than 3 matches")
					if len(test_sig_cands_ind) > 0:
						if len(test_sig_cands_ind) == 1:
							matched_num_matches[i] = 1
						if len(test_sig_cands_ind) == 2:
							matched_num_matches[i] = 2
						if len(test_sig_cands_ind) == 3:
							matched_num_matches[i] = 3
					else:
						unmatched_raX = np.append(unmatched_raX,raX[i])
						unmatched_decX = np.append(unmatched_decX,decX[i])
						unmatched_errX = np.append(unmatched_errX,d_xerr[i])
						unmatched_indX = np.append(unmatched_indX,i)
						unmatched_prob = np.append(unmatched_prob,probability_nonej)
						matched_num_matches[i] = 0
			else:
				unmatched_raX = np.append(unmatched_raX,raX[i])
				unmatched_decX = np.append(unmatched_decX,decX[i])
				unmatched_errX = np.append(unmatched_errX,d_xerr[i])
				unmatched_indX = np.append(unmatched_indX,i)
				unmatched_prob = np.append(unmatched_prob,probability_nonej)
				matched_num_matches[i] = 0
	endMCtime = time.time()-start_time-setup_time
	print "Matching Done - Writing to files...Matching took " + str(endMCtime) + " seconds"
	if usemin < 0.1:
		FILE = open(output_file,"w")
		FILE2 = open(out_reg,"w")
	else:
		FILE = open(output_file + ".minsrch.dat","w")
		FILE2 = open(out_reg + ".minsrch.reg","w")
	temp_ra_opts = np.zeros(3)
	temp_dec_opts = np.zeros(3)
	temp_ind_opts = np.zeros(3)
	temp_new_inds = np.array(['-000001','-000001','-000001'])
	FILE2.write("# Region file format: DS9 version 4.1\n")
	FILE2.write('global color=green dashlist=8 3 width=1 font="helvetica 10 normal" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\n')
	#ci = 0
        matched_num_matches[matched_errX > 59.999] = 0
	for i in range(0L,len(matched_num_matches)):
		#citemp = 1
		#if sigmax[i] >= 3: 
		#	citemp = ci
		#	ci += 1
		temp_new_inds.fill(str(-1))
		temp_ind_opts[0] = int(matched_ind_opt1[i])
		temp_ind_opts[1] = int(matched_ind_opt2[i])
		temp_ind_opts[2] = int(matched_ind_opt3[i])
		for k in range(0L,3):
			if ((temp_ind_opts[k] != -1) and(temp_ind_opts[k] != "-1")):
				temp_new_inds[k] = newid_opt[int(temp_ind_opts[k])]
               # FILE.write('%3i %9.5f %9.5f %8.5f %2i %9.5f %9.5f %15s %6.3f %7.1f %9.5f %9.5f %15s %6.3f %7.1f %9.5f %9.5f %15s %6.3f %7.1f %6.3f %3i %3.1f\n'
		FILE.write('%3i %9.5f %9.5f %8.5f %2i %9.5f %9.5f %15s %6.3f %7.1f %9.5f %9.5f %15s %6.3f %7.1f %9.5f %9.5f %15s %6.3f %7.1f %6.3f\n'%(matched_indX[i],matched_raX[i],matched_decX[i],matched_errX[i],matched_num_matches[i],matched_ra_opt1[i],matched_dec_opt1[i],temp_new_inds[0],matched_prob_opt1[i],matched_like_opt1[i],matched_ra_opt2[i],matched_dec_opt2[i],temp_new_inds[1],matched_prob_opt2[i],matched_like_opt2[i],matched_ra_opt3[i],matched_dec_opt3[i],temp_new_inds[2],matched_prob_opt3[i],matched_like_opt3[i],matched_prob_none[i]))#,citemp,sigmax[i]))
		temp_ra_opts[0] = matched_ra_opt1[i]
		temp_ra_opts[1] = matched_ra_opt2[i]
		temp_ra_opts[2] = matched_ra_opt3[i]
		temp_dec_opts[0] = matched_dec_opt1[i]
		temp_dec_opts[1] = matched_dec_opt2[i]
		temp_dec_opts[2] = matched_dec_opt3[i]
		for j in range(0L,int(matched_num_matches[i])):
			if j == 0: FILE2.write("circle(" + str(matched_raX[i]) + "," + str(matched_decX[i]) + "," + str(matched_errX[i]) + '")\n')
			FILE2.write("circle(" + str(temp_ra_opts[j]) + "," + str(temp_dec_opts[j]) + "," + str(matched_errX[i]/5) + '")\n')
	FILE.close()
	FILE2.close()
	setup_time = time.time()-start_time
	matched_raX = np.zeros(len(raX))
	matched_decX = np.zeros(len(raX))
	matched_errX = np.zeros(len(raX))
	matched_indX = np.zeros(len(raX))
	matched_num_matches = np.zeros(len(raX))
	matched_dec_opt1 = np.zeros(len(raX))
	matched_dec_opt2 = np.zeros(len(raX))
	matched_dec_opt3 = np.zeros(len(raX))
	matched_ra_opt1 = np.zeros(len(raX))
	matched_ra_opt2 = np.zeros(len(raX))
	matched_ra_opt3 = np.zeros(len(raX))
	matched_ind_opt1 = np.zeros(len(raX))
	matched_ind_opt2 = np.zeros(len(raX))
	matched_ind_opt3 = np.zeros(len(raX))
	matched_prob_opt1 = np.zeros(len(raX))
	matched_prob_opt2 = np.zeros(len(raX))
	matched_prob_opt3 = np.zeros(len(raX))
	matched_like_opt1 = np.zeros(len(raX))
	matched_like_opt2 = np.zeros(len(raX))
	matched_like_opt3 = np.zeros(len(raX))
	matched_like_opt1.fill(-1)
	matched_like_opt2.fill(-1)
	matched_like_opt3.fill(-1)
	matched_dec_opt1.fill(-1)
	matched_dec_opt2.fill(-1)
	matched_dec_opt3.fill(-1)
	matched_ra_opt1.fill(-1)
	matched_ra_opt2.fill(-1)
	matched_ra_opt3.fill(-1)
	matched_ind_opt1.fill(-1)
	matched_ind_opt2.fill(-1)
	matched_ind_opt3.fill(-1)
	matched_prob_opt1.fill(-1)
	matched_prob_opt2.fill(-1)
	matched_prob_opt3.fill(-1)
	matched_prob_none = np.zeros(len(raX))
	unmatched_raX = np.zeros(0)
	unmatched_decX = np.zeros(0)
	unmatched_errX = np.zeros(0)
	unmatched_indX = np.zeros(0)
	unmatched_prob = np.zeros(0)
endtime = time.time()-start_time
print "Total Elapsed time: " + str(endtime) + " seconds."
