import numpy as np
import math as m
import sys

minsrchrad = 5

try:
    testRA
except NameError:
    sys.exit("Must pick a test RA")
try:
    testDec
except NameError:
    sys.exit("Must pick a test Dec")

def SphDist(RAi,Deci,Raf,Decf):
	#Distance in arcminutes
	dist = 2.0*m.asin(m.sqrt((m.sin(0.5*m.pi*(Decf-Deci)/180))**2+m.cos(m.pi*Decf/180.0)*m.cos(m.pi*Deci/180.0)*(m.sin(0.5*m.pi*(Raf-RAi)/180))**2))
	dist *= 180.0*60/m.pi
	return dist

def WindingNum(RA,Dec,boundRAs,boundDecs):
	#Computes winding number by counting number of quadrants moved through counterclockwise
	NumCCW = 0
	for i in range(0,len(boundRAs)):
		if boundRAs[i] > RA:
			if boundDecs[i] > Dec:
				CQ = 1
			else: 
				CQ = 4
		else:
			if boundDecs[i] > Dec:
				CQ = 2
			else:
				CQ = 3
		if i != 0:
			DelQ = CQ-PQ
			if m.fabs((m.fabs(DelQ)-2)) < 0.1:
				testDec = (boundDecs[i]-boundDecs[i-1])*(RA-boundRAs[i-1])/(boundRAs[i]-boundRAs[i-1])+boundDecs[i-1]
				if testDec < Dec:
					if ((PQ == 2) or (PQ == 3)):
						NumCCW += 2
					else: 
						NumCCW -= 2
				else: 
					if ((PQ == 4) or (PQ == 1)):
						NumCCW += 2
					else:
						NumCCW -= 2
			else:
				if (m.fabs(DelQ)) > 2.9: DelQ /= -3
				NumCCW += DelQ
		PQ = CQ
	return NumCCW

def FindCloseSources(ra,dec,tol,ra_opt,dec_opt,usemin):
	if ((tol < minsrchrad) & (usemin != 0)): tol = minsrchrad
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
				if len(inside_tol_ind) > 0:
					return ra_box_temp_ind1[[dec_box_temp_ind2[inside_tol_ind]]]
				else:
					return np.zeros(0)
			else:
				return np.zeros(0)
		else:
			return np.zeros(0)
	else:
		return np.zeros(0)

cr = read_file("/home/rumbaugh/finoguenov.COSMOS.cluster.table.dat")
ras = get_colvals(cr,'col2')
decs = get_colvals(cr,'col3')
srch = 0.0
nummatch = 0
while nummatch < 0.1:
    srch += 60
    closeids = FindCloseSources(testRA,testDec,srch,ras,decs,0)
    nummatch = len(closeids)
dists = np.zeros(len(closeids))
for i in range(0,len(closeids)):
    dists[i] = SphDist(testRA,testDec,ras[closeids[i]],decs[closeids[i]])
    print "One of the nearest clusters is " + str(dists[i]) + "arcminutes away."
