execfile("/home/rumbaugh/FindPeaks.py")
execfile("/home/rumbaugh/FindCloseSources.py")
import sys

cr = read_file("/home/rumbaugh/COSMOS/conv.centers.12.28.11.dat")
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
FILE = open("/home/rumbaugh/COSMOS/lens.flux.analysis.1.28.11.dat","w")
avglum = 0.0
avglumcut = 0.0
for i in range(0,len(ID)):
    texp += exps[i]
    load_data('/scratch/rumbaugh/ciaotesting/' + str(int(ID[i])) + '/acis' + str(int(ID[i])) + '.img.500-2000.S07.nops.norand.fits')
    set_coord("physical")
    cnts_inner = calc_data_sum2d('circle(%f,%f,80)'%(cenX[i],cenY[i]))
    cnts_bg = calc_data_sum2d('circle(%f,%f,110)-circle(%f,%f,100)'%(cenX[i],cenY[i],cenX[i],cenY[i]))
    ncnts = cnts_inner - cnts_bg*(80*80)/(110*110-1.0*100*100)
    cntrt = ncnts/exps[i]
    flux = cntrt*c2f[i]*10**(-11)
    lum = fourpiDl2[i]*flux
    avglum += lum
    if z[i] > 0.411: avglumcut += lum
    print str(int(ID[i])) + " " + str(lum)
    FILE.write('%12s %6.4f %E %E %E %f %f %f %5.2f %4.2f %i %f %E\n'%(str(int(ID[i])),z[i],lum,flux,cntrt,ncnts,cnts_inner,cnts_bg,exps[i],c2f[i],isnotcut[i],DLs[i],fourpiDl2[i]))
FILE.close()
#sys.exit("g")

#avglum=5.40522375607e+44
#avglumcut=4.32022806755e+44

zg = np.where(z > 0.411)

#avglum2 = avglum + 1.28713416173e+41 + 9.01651153226e+41
#avglum2 /= 25
avglum /= 27
avglumcut /= len(zg[0])

print 'Average Luminosity: ' + str(avglum)
print 'Average Mass: ' + str(10**14*(avglum/(12.6*10**42))**(1/1.65))
#print 'Average Luminosity2: ' + str(avglum2)
#print 'Average Mass2: ' + str(10**14*(avglum2/(12.6*10**42))**(1/1.65))
print 'Average Luminosity - cut: ' + str(avglumcut)
print 'Average Mass - cut: ' + str(10**14*(avglumcut/(12.6*10**42))**(1/1.65))
