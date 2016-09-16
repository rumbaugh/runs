execfile("/home/rumbaugh/FindCloseSources.py")
import matplotlib
import matplotlib.pylab as pylab
#Contains the boundary points of the polygon containing the ADS field
crWN = read_file("/home/rumbaugh/LFC/ACSboundaries.dat")
boundRAs = get_colvals(crWN,'col1')
boundDecs = get_colvals(crWN,'col2')
boundRAs = np.append(boundRAs,boundRAs[0])
boundDecs = np.append(boundDecs,boundDecs[0])
#Contains the boundary points of the polygon containing the LFC field
#crWNLFC = read_file("/home/rumbaugh/LFC/LFCboundaries1604.dat")#
#LFCboundRAs = get_colvals(crWNLFC,'col1')
#LFCboundDecs = get_colvals(crWNLFC,'col2')
#LFCboundRAs = np.append(LFCboundRAs,LFCboundRAs[0])
#LFCboundDecs = np.append(LFCboundDecs,LFCboundDecs[0])

chipbndNra = np.array([241.10226,240.76077,240.96136,241.30362,241.10226])
chipbndNdec = np.array([43.57945,43.434249,43.186224,43.33387,43.57945])
chipbndSra = np.array([241.14989,240.80454,240.99266,241.33869,241.14989])
chipbndSdec = np.array([43.361082,43.219552,42.967248,43.105167,43.361082]) 

sinThetaN = (chipbndNdec[3]-chipbndNdec[2])/m.sqrt((chipbndNra[3]-chipbndNra[2])**2+(chipbndNdec[3]-chipbndNdec[2])**2)
cosThetaN = (chipbndNra[3]-chipbndNra[2])/m.sqrt((chipbndNra[3]-chipbndNra[2])**2+(chipbndNdec[3]-chipbndNdec[2])**2)
sinThetaS = (chipbndSdec[3]-chipbndSdec[2])/m.sqrt((chipbndSra[3]-chipbndSra[2])**2+(chipbndSdec[3]-chipbndSdec[2])**2)
cosThetaS = (chipbndSra[3]-chipbndSra[2])/m.sqrt((chipbndSra[3]-chipbndSra[2])**2+(chipbndSdec[3]-chipbndSdec[2])**2)
xmaxN = (chipbndNdec[0]-chipbndNdec[2])*sinThetaN+(chipbndNra[0]-chipbndNra[2])*cosThetaN
ymaxN = (chipbndNdec[0]-chipbndNdec[2])*cosThetaN-(chipbndNra[0]-chipbndNra[2])*sinThetaN
xmaxS = (chipbndSdec[0]-chipbndSdec[2])*sinThetaS+(chipbndSra[0]-chipbndSra[2])*cosThetaS
ymaxS = (chipbndSdec[0]-chipbndSdec[2])*cosThetaS-(chipbndSra[0]-chipbndSra[2])*sinThetaS

ACStopPerc = (14600.267*5319.7733)/((14600.267*5319.7733)+4800.2978*10601.818)


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


def OffAxis1324(ra,dec):
	#Determines if source is in North or South pointing in 1324 and finds off axis angle
	if dec > 30.67:
		dist = SphDist(ra,dec,201.20389190325,30.86373172217)
	else:
		dist = SphDist(ra,dec,201.17495829431,30.279328719557)
	return dist

def OffAxis1604(ra,dec):
	#Determines if source is in North or South pointing in 1324 and finds off axis angle
	inNorth = WindingNum(ra,dec,chipbndNra,chipbndNdec)
	inSouth = WindingNum(ra,dec,chipbndSra,chipbndSdec)
	distS,distN = 0.0,0.0
	if inSouth != 0:
		distS = SphDist(ra,dec,241.08194403527,43.170689962746)
	if inNorth != 0:
		distN = SphDist(ra,dec,241.04370182276,43.375900326239)
		if inSouth != 0:
			if distN > distS:
				return distS,0
			else:
				return distN,1
		else:
			return distN,1
	if ((inNorth == 0) & (inSouth == 0)): sys.exit("Winding Error")
	if distN == 0:
		return distS,0
	else:
		return 999,999

names = np.array(['RXJ1821','RXJ1757','Cl0023','Cl1604','Cl1324'])
names2 = np.array(['NEP5281','RXJ1757','Cl0023','Cl1604','Cl1324'])
RA_aims = np.array([275.30591870821,269.33149632001,5.9623443182206,0,0])
Dec_aims = np.array([68.463372070651,66.489756575514,4.3820249449499,0,0])
offax = np.zeros(0)
allfluxes = np.zeros(0)
for i in range(0,len(names)):
    crx = read_file("/home/rumbaugh/%s.xray_phot.soft_hard_full.dat"%(names2[i]))
    raXtemp = copy_colvals(crx,'col1')
    decXtemp = copy_colvals(crx,'col2')
    fluxX_softtemp = copy_colvals(crx,'col3')
    fluxX_hardtemp = copy_colvals(crx,'col4')
    fluxX_fulltemp = copy_colvals(crx,'col5')
    netcnts_corrX_softtemp = copy_colvals(crx,'col6')
    netcnts_corrX_hardtemp = copy_colvals(crx,'col7')
    netcnts_corrX_fulltemp = copy_colvals(crx,'col8')
    sigX_softtemp = copy_colvals(crx,'col9')
    sigX_hardtemp = copy_colvals(crx,'col10')
    sigX_fulltemp = copy_colvals(crx,'col11')
    B = (netcnts_corrX_fulltemp/sigX_fulltemp-1)**2-0.75
    offax_tmp = np.zeros(len(raXtemp))
    for j in range(0,len(raXtemp)):
        if i < 3:
            offax_tmp[j] = SphDist(raXtemp[j],decXtemp[j],RA_aims[i],Dec_aims[i])
        elif i == 3:
            offax_tmp[j],tmp = OffAxis1604(raXtemp[j],decXtemp[j])
        else:
            offax_tmp[j] = OffAxis1324(raXtemp[j],decXtemp[j])
    gs = np.where((sigX_fulltemp >= 3))
    gs = gs[0]
    offax = np.append(offax,offax_tmp[gs])
    allfluxes = np.append(allfluxes,fluxX_fulltemp[gs])
offax_dens = np.zeros(20)
offax_num = np.zeros(len(offax_dens))
x1 = (np.arange(len(offax_dens))+0.5)*np.max(offax)/len(offax_dens)
offax_dens_err = np.zeros(len(offax_dens))
offax_num_err = np.zeros(len(offax_dens))
prev = 0.0
step = np.max(offax)/len(offax_dens)
for i in range(0,len(offax_dens)):
    gt = np.where((offax > prev) & (offax <= prev + step))
    offax_dens[i] = len(gt[0])/7.0/(m.pi*((prev+step)**2-prev**2))
    offax_num[i] = len(gt[0])/7.0
    offax_dens_err[i] = m.sqrt(len(gt[0]))/7.0/(m.pi*((prev+step)**2-prev**2))
    offax_num_err[i] = m.sqrt(len(gt[0]))/7.0
    prev += step
RA_aim = 163.43679730653
Dec_aim = 57.574581662708
crx = read_file("/home/rumbaugh/4936.xray_phot.soft_hard_full.dat")
raXtemp = copy_colvals(crx,'col1')
decXtemp = copy_colvals(crx,'col2')
fluxX_fulltemp = copy_colvals(crx,'col5')
sigX_fulltemp = copy_colvals(crx,'col11')
netcnts_corrX_fulltemp = copy_colvals(crx,'col8')
B = np.zeros(len(raXtemp))
newsig = np.zeros(len(B))
for i in range(0,len(B)): 
    if sigX_fulltemp[i] > 0:
        B[i] = (netcnts_corrX_fulltemp[i]/sigX_fulltemp[i]-1)**2-0.75
        newsig[i] = netcnts_corrX_fulltemp[i]*5/9.2/(1.0+m.sqrt(0.75+B[i]*5/9.2))
    else:
        B[i] = 999999999.0
        newsig[i] = 0.0
offax_tmp = np.zeros(len(raXtemp))
for j in range(0,len(raXtemp)): offax_tmp[j] = SphDist(raXtemp[j],decXtemp[j],RA_aim,Dec_aim)
gso = np.where((sigX_fulltemp >= 3) & (fluxX_fulltemp > 0.1E-13))
gso = gso[0]
gs= np.where((newsig >= 3))
gs = gs[0]
offax_tmp = offax_tmp[gs]
offax_dens2 = np.zeros(10)
offax_num2 = np.zeros(len(offax_dens2))
x2 = (np.arange(len(offax_dens2))+0.5)*np.max(offax_tmp)/len(offax_dens2)
offax_dens2_err = np.zeros(len(offax_dens2))
offax_num2_err = np.zeros(len(offax_dens2))
prev = 0.0
step = np.max(offax_tmp)/len(offax_dens2)
for i in range(0,len(offax_dens2)):
    gt = np.where((offax_tmp > prev) & (offax_tmp <= prev + step))
    offax_dens2[i] = len(gt[0])/(m.pi*((prev+step)**2-prev**2))
    offax_dens2_err[i] = m.sqrt(len(gt[0]))/(m.pi*((prev+step)**2-prev**2))
    offax_num2[i] = len(gt[0])
    offax_num2_err[i] = m.sqrt(len(gt[0]))
    prev += step
pylab.xlim(0,np.max(offax))
pylab.ylim(0,np.max(np.append(offax_num,offax_num2))*1.1)
pylab.xlabel('Off-Axis Angle (arcminutes)')
pylab.ylabel('N(Sources)')
pylab.errorbar(x1,offax_num,yerr=offax_num_err,color='red',fmt='ro',lw=1,capsize=3,mew=1,label='_nolegend_')
pylab.errorbar(x2,offax_num2,yerr=offax_num2_err,marker='d',fmt='ro',color='blue',lw=1,capsize=3,mew=1,ms=8)
pylab.savefig('/home/rumbaugh/offaxis_analysis_num_scalesig.3.7.12.png')
pylab.close('all')
pylab.xlim(0,np.max(offax))
pylab.ylim(0,np.max(np.append(offax_dens,offax_dens2))*1.1)
pylab.xlabel('Off-Axis Angle (arcminutes)')
pylab.ylabel('N(Sources)/Area of Annulus')
pylab.scatter([0,0],[99,99],color='red')
pylab.scatter([0,0],[99,99],color='blue',marker='d')
pylab.legend(('Rumbaugh et al. (2012) Sample','RXJ1053'))
pylab.errorbar(x1,offax_dens,yerr=offax_dens_err,color='red',fmt='ro',lw=1,capsize=3,mew=1)
pylab.errorbar(x2,offax_dens2,yerr=offax_dens2_err,marker='d',fmt='ro',color='blue',lw=1,capsize=3,mew=1,ms=8)
pylab.savefig('/home/rumbaugh/offaxis_analysis_scalesig.3.7.12.png')
pylab.close('all')
pylab.xlim(0,np.max(offax))
pylab.ylim(0,0.81)
pylab.xlabel('Off-Axis Angle (arcminutes)')
pylab.ylabel('N(Sources)/Area of Annulus')
pylab.scatter([0,0],[99,99],color='red')
pylab.scatter([0,0],[99,99],color='blue',marker='d')
pylab.legend(('Rumbaugh et al. (2012) Sample','RXJ1053'))
pylab.errorbar(x1,offax_dens,yerr=offax_dens_err,color='red',fmt='ro',lw=1,capsize=3,mew=1)
pylab.errorbar(x2,offax_dens2,yerr=offax_dens2_err,marker='d',fmt='ro',color='blue',lw=1,capsize=3,mew=1,ms=8)
pylab.savefig('/home/rumbaugh/offaxis_analysis_scalesig_smaller.3.7.12.png')
pylab.close('all')
pylab.hist(allfluxes,bins=20,range=[0,0.2E-13])
pylab.savefig('/home/rumbaugh/fluxtest1.png')
pylab.close('all')
pylab.hist(fluxX_fulltemp[gs],bins=20,range=[0,0.2E-13])
pylab.savefig('/home/rumbaugh/fluxtest2.png')
pylab.close('all')



