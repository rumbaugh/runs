import sys
import os
import numpy as np
import math as m

Beta = 2.064

def BetaFunc( Amp, R, Rcore, Beta, bkg, dvnum):
    #Evaluates beta function a r=R if dvnum = 0. Otherwise, evaluates 
    #the derivate of the beta function with respect to parameter
    #number dvnum (1=Amp,2=Rcore,3=beta,4=bkg)
    if dvnum == 0: BetaFuncValue = (Rcore**2)*(-Amp/(Beta-1))/(1+(R/Rcore)**2)**(Beta-1) + bkg*R**2
    if dvnum == 1: BetaFuncValue = (Rcore**2)*(-1.0/(Beta-1))/(1+(R/Rcore)**2)**(Beta-1)
    if dvnum == 2: BetaFuncValue = 2*Beta*Amp*((R**2)/(Rcore**3))/(1+(R/Rcore)**2)**(Beta+1)
    if dvnum == 3: BetaFuncValue = -m.log(1+(R/Rcore)**2)*Amp/(1+(R/Rcore)**2)**(Beta)
    if dvnum == 4: BetaFuncValue = R**2
    if dvnum != 0 and dvnum != 1 and dvnum != 2 and dvnum != 3 and dvnum != 4:
        print "Improper calling of BetaFunc: dvnum = " + str(dvnum)
        BetaFuncValue = -1.0/0.0
    return BetaFuncValue

step = 0.251
def IntegrateSurBr( floata, floatb, ParamVec ):
    #Integrates beta model from point a to b to 
    #find average surface brightness
    pos = floata
    RManSum = 0.0
    while pos < floatb:
        if step + pos > floatb:
            laststep = floatb - pos
            RManSum += laststep*2*(pos+laststep/2)*BetaFunc(ParamVec[0],pos+laststep/2,ParamVec[1],ParamVec[2],ParamVec[3])
        else:
            RManSum += step*2*(pos+step/2)*BetaFunc(ParamVec[0],pos+step/2,ParamVec[1],ParamVec[2],ParamVec[3])
        pos += step
    Ar = (floatb**2-floata**2)
    return RManSum/Ar

def IntegrateSurBrSimp( floata, floatb, ParamVec, dvnum ):
    #Integrates beta model from point a to b to 
    #find average surface brightness
    #This function uses Simpon's Rule isntead of rectangles
    pos = floata
    Sum = 0.0
    if dvnum == 3 or dvnum == 2:
        while pos < floatb:
            if step + pos > floatb:
                laststep = floatb - pos
                Sum += (laststep/6)*2*(pos*BetaFunc(ParamVec[0],pos,ParamVec[1],ParamVec[2],ParamVec[3],dvnum) + 4*(pos+laststep/2)*BetaFunc(ParamVec[0],pos+laststep/2,ParamVec[1],ParamVec[2],ParamVec[3],dvnum)+ (floatb)*BetaFunc(ParamVec[0],floatb,ParamVec[1],ParamVec[2],ParamVec[3],dvnum))
            else:
                Sum += (step/6)*2*(pos*BetaFunc(ParamVec[0],pos,ParamVec[1],ParamVec[2],ParamVec[3],dvnum) + 4*(pos+step/2)*BetaFunc(ParamVec[0],pos+step/2,ParamVec[1],ParamVec[2],ParamVec[3],dvnum)+ (pos+step)*BetaFunc(ParamVec[0],pos+step,ParamVec[1],ParamVec[2],ParamVec[3],dvnum))
            pos += step
    else:
        Sum = BetaFunc(ParamVec[0],floatb,ParamVec[1],ParamVec[2],ParamVec[3],dvnum) - BetaFunc(ParamVec[0],floata,ParamVec[1],ParamVec[2],ParamVec[3],dvnum)
    Ar = (floatb**2-floata**2)
    return Sum/Ar

conv = np.array(['1.24.11.7757+363','9515+10576.12.9.10','1.24.11.427+3461','1.24.11.419+1629','423+424.12.9.10'])

Rcore = np.array([36.45,28.32,19.55,16.62,15.44])
names = np.array(['7757+363','9515+10576','427+3461','419+1629','423+424'])

FILE=open("/scratch/rumbaugh/ciaotesting/analysis/lens.analysis.Amp.1.25.11.dat","w")
for i in range(0,len(names)):
    load_data('/scratch/rumbaugh/ciaotesting/merged/%s.fits'%(names[i]))
    set_coord("physical")
    ostemp = os.system('dmstat /scratch/rumbaugh/ciaotesting/merged/conv.beta.%s.fits verbose=0'%(conv[i]))
    ostemp = os.system('pget dmstat out_max_loc | tee dmstat.temp.txt')
    crcen = read_file("dmstat.temp.txt")
    centemp = get_colvals(crcen,'col1')
    centemp = centemp[0]
    bgtemp = calc_data_sum2d('circle(%s,90)-circle(%s,80)'%(centemp,centemp))
    bkg = bgtemp/(m.pi*(90**2-80**2))
    DataCen = calc_data_sum2d('circle(%s,15)'%(centemp))
    a = np.array([1,Rcore[i],Beta,bkg])
    tInt = IntegrateSurBrSimp(0, 15, a, 0 )
    Amp = DataCen/(m.pi*(15*15)*tInt)
    FILE.write('%12s %5.2f %9.7f %9.7f %9.7f\n'%(names[i],Rcore[i],bkg,Amp,Amp/bkg)) 
FILE.close()
