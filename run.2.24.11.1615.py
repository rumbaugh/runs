execfile("/home/rumbaugh/FindPeaks.py")
execfile("/home/rumbaugh/FindCloseSources.py")
import sys

try:
    loadsetup
except NameError:
    loadsetup = 1
try:
    omega_m
except NameError:
    omega_m = 0.3
try:
    omega_lamda
except NameError:
    omega_lamda = 0.7
try:
    h
except NameError:
    h = 0.7
M0 = 10**13.7/h
Lx0 = 10**42.7/h
A = 10**0.068
alpha = 0.66
dA = A*m.log(10)*0.063
dalpha = 0.14

cr = read_file("/home/rumbaugh/COSMOS/conv.centers.2.24.11.dat")
DLs = get_colvals(cr,'col8')
fourpiDl2 = get_colvals(cr,'col9')
DLs = DLs/0.7
fourpiDl2 = fourpiDl2/(0.7*0.7)
ID = get_colvals(cr,'col1')
z = get_colvals(cr,'col4')
exps = get_colvals(cr,'col5')
exps *= 1000
c2f = get_colvals(cr,'col6')
isnotcut = get_colvals(cr,'col7')
cenX = get_colvals(cr,'col2')
cenY = get_colvals(cr,'col3')
texp= 0.0
FILE = open("/home/rumbaugh/COSMOS/full.spat.anal.2.24.11.dat","w")
avglum = 0.0
avglumcut = 0.0
cnterrsum = 0.0
cnterrsumcut = 0.0
merrsum = 0.0
msum = 0.0
merrsumcut = 0.0
msumcut = 0.0
Ez = np.zeros(len(z))
if loadsetup == 0: 
    FILEt = open("/scratch/rumbaugh/ciaotesting/analysis/cnts.ref.record.setup.1.31.11.dat","w")
else:
    crl = read_file("/scratch/rumbaugh/ciaotesting/analysis/cnts.ref.record.setup.1.31.11.dat")
    cntsinnerarr = get_colvals(crl,'col1')
    cntsbgarr = get_colvals(crl,'col2')
for i in range(0,len(ID)):
    if loadsetup != 0: cnts_inner,cnts_bg = cntsinnerarr[i],cntsbgarr[i]
    Ez[i] = m.sqrt(omega_m*(1+z[i])**3+omega_lamda)
    texp += exps[i]
    if loadsetup == 0: 
        load_data('/scratch/rumbaugh/ciaotesting/' + str(int(ID[i])) + '/acis' + str(int(ID[i])) + '.img.500-2000.S07.nops.norand.fits')
        set_coord("physical")
        cnts_inner = calc_data_sum2d('circle(%f,%f,80)'%(cenX[i],cenY[i]))
    if i != len(ID)-2:
        if loadsetup == 0: cnts_bg = calc_data_sum2d('circle(%f,%f,110)-circle(%f,%f,90)'%(cenX[i],cenY[i],cenX[i],cenY[i]))
        ncnts = cnts_inner - cnts_bg*(80*80)/(110*110-1.0*90*90)
        cestemp = (cnts_inner**2+cnts_bg**2*(80*80)**2/(110*110-1.0*90*90)**2)/(exps[i]**2)
    else:
        if loadsetup == 0: cnts_bg = calc_data_sum2d('circle(%f,%f,110)-circle(%f,%f,100)'%(cenX[i],cenY[i],cenX[i],cenY[i]))
        ncnts = cnts_inner - cnts_bg*(80*80)/(110*110-1.0*100*100)
        cestemp = (cnts_inner**2+cnts_bg**2*(80*80)**2/(110*110-1.0*90*90)**2)/(exps[i]**2)
    if i == 3:
        if loadsetup == 0: cnts_inner = calc_data_sum2d('circle(%f,%f,60)'%(cenX[i],cenY[i]))
        if loadsetup == 0: cnts_bg = calc_data_sum2d('circle(4388.7144,4462.0777,60)')
        ncnts = cnts_inner - cnts_bg
        cestemp = (cnts_inner**2+cnts_bg**2)/(exps[i]**2)
    if i == 7:
        if loadsetup == 0: cnts_inner = calc_data_sum2d('circle(%f,%f,60)'%(cenX[i],cenY[i]))
        if loadsetup == 0: cnts_bg = calc_data_sum2d('circle(4469.7732,4309.7301,60)')
        ncnts = cnts_inner - cnts_bg*(60*60)/(60*60)
        cestemp = (cnts_inner**2+cnts_bg**2)/(exps[i]**2)
    if i == len(ID)-4:
        if loadsetup == 0: cnts_inner = calc_data_sum2d('circle(%f,%f,120)'%(cenX[i],cenY[i]))
        if loadsetup == 0: cnts_bg = calc_data_sum2d('circle(%f,%f,150)-circle(%f,%f,140)'%(cenX[i],cenY[i],cenX[i],cenY[i]))
        ncnts = cnts_inner - cnts_bg*(120*120)/(150*150-1.0*140*140)
        cestemp = (cnts_inner**2+cnts_bg**2*(120*120)**2/(150*150-1.0*140*140)**2)/(exps[i]**2)
    if loadsetup == 0: FILEt.write('%f %f\n'%(cnts_inner,cnts_bg))
    cntrt = ncnts/exps[i]
    flux = cntrt*c2f[i]*10**(-11)
    lum = m.exp(m.log(fourpiDl2[i])+56*m.log(10)+m.log(flux))
    cnterrsum += cestemp*(lum/ncnts)**2
    avglum += lum
    mass = M0*A*(lum/Lx0)**alpha/(Ez[i]**(alpha+1))
    msum += mass
    merrsum += (M0/(Lx0**alpha*Ez[i]**(1+alpha)))**2*((dA*lum**alpha)**2 + cestemp*((lum/ncnts)*A*alpha*lum**(alpha-1))**2+(A*dalpha*lum**(alpha)*m.log(lum/(Lx0*Ez[i])))**2)
    if z[i] > 0.411: 
        avglumcut += lum
        cnterrsumcut += cestemp*(lum/ncnts)**2
        merrsumcut += (M0/((Lx0**alpha)*Ez[i]**(1+alpha)))**2*((dA*lum**alpha)**2 + cestemp*((lum/ncnts)*A*alpha*lum**(alpha-1))**2+(A*dalpha*lum**(alpha)*m.log(lum/(Lx0*Ez[i])))**2)
        msumcut += mass
    print str(int(ID[i])) + " " + str(mass) + " " + str(cestemp)
    FILE.write('%12s %6.4f %E %E %E %f %f %f %5.2f %4.2f %i %f %E\n'%(str(int(ID[i])),z[i],lum,flux,cntrt,ncnts,cnts_inner,cnts_bg,exps[i],c2f[i],isnotcut[i],DLs[i],fourpiDl2[i]))
FILE.close()
#sys.exit("g")
if loadsetup == 1: FILEt.close()
cnterr = m.sqrt(cnterrsum)
cnterrcut = m.sqrt(cnterrsumcut)

#avglum=5.40522375607e+44
#avglumcut=4.32022806755e+44

zg = np.where(z > 0.411)

#avglum2 = avglum + 1.28713416173e+41 + 9.01651153226e+41
#avglum2 /= 25
avglum /= 1.0*len(ID)
avglumcut /= 1.0*len(zg[0])
avgM = msum/len(ID)
avgMcut = msumcut/len(zg[0])
avgMerr = m.sqrt(merrsum)/len(ID)
avgMcuterr = m.sqrt(merrsumcut)/len(ID)


#print 'Average Luminosity: ' + str(avglum)
#print 'Average Mass: ' + str(10**14*(avglum/(12.6*10**42))**(1/1.65))
print 'Average Mass: ' + str(avgM) + ' +/- ' + str(avgMerr)
#print 'Average Luminosity2: ' + str(avglum2)
#print 'Average Mass2: ' + str(10**14*(avglum2/(12.6*10**42))**(1/1.65))
#print 'Average Luminosity - cut: ' + str(avglumcut)
print 'Average Mass - cut: ' + str(avgMcut) + ' +/- ' + str(avgMcuterr)
